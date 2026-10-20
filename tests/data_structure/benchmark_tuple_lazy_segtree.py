"""pypy3 -B tests/data_structure/benchmark_tuple_lazy_segtree.py"""

import argparse
import gc
import random
import runpy
import statistics
import time
from pathlib import Path


LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/data-structure"
)
LazySegtree = runpy.run_path(str(LIBRARY / "LazySegtree.py"))["lazy_segtree"]
TupleLazySegtree = runpy.run_path(str(LIBRARY / "TupleLazySegtree.py"))[
    "TupleLazySegtree"
]
MOD = 998244353


def op(x, y):
    return (x[0] + y[0]) % MOD, x[1] + y[1]


def mp(f, x):
    return (f[0] * x[0] + f[1] * x[1]) % MOD, x[1]


def comp(f, g):
    return f[0] * g[0] % MOD, (f[0] * g[1] + f[1]) % MOD


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=65536)
    parser.add_argument("--q", type=int, default=20000)
    parser.add_argument("--repeat", type=int, default=5)
    args = parser.parse_args()
    if args.n < 1 or args.q < 1 or args.repeat < 1:
        parser.error("n, q, repeat must be positive")
    rng = random.Random(20261020)
    values = [(rng.randrange(MOD), 1) for _ in range(args.n)]
    operations = []
    for _ in range(args.q):
        left = rng.randrange(args.n)
        right = rng.randrange(left + 1, args.n + 1)
        operations.append((left, right, rng.randrange(MOD), rng.randrange(MOD)))

    def run(cls):
        tree = cls(values, op, (0, 0), mp, comp, (1, 0))
        checksum = 0
        for i, (left, right, b, c) in enumerate(operations):
            if i & 1:
                checksum += tree.prod(left, right)[0]
            else:
                tree.apply(left, right, (b, c))
        return checksum

    classes = [("tuple", LazySegtree), ("columns", TupleLazySegtree)]
    expected = run(LazySegtree)
    for _ in range(2):
        for _, cls in classes:
            assert run(cls) == expected
    samples = {name: [] for name, _ in classes}
    for repeat in range(args.repeat):
        for name, cls in classes[:: 1 if repeat & 1 else -1]:
            gc.collect()
            start = time.perf_counter()
            checksum = run(cls)
            samples[name].append(time.perf_counter() - start)
            assert checksum == expected
    medians = {name: statistics.median(times) for name, times in samples.items()}
    for name, elapsed in medians.items():
        print(f"{name}: {elapsed * 1000:.3f} ms")
    print(f"speedup: {medians['tuple'] / medians['columns']:.2f}x")
    print("checksums match")


if __name__ == "__main__":
    main()
