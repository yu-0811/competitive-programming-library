"""python3 tests/graph/benchmark_euler_tour.py --baseline /tmp/EulerTour.py"""

import argparse
import gc
import random
import runpy
import statistics
import time
from pathlib import Path


LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/graph/EulerTour.py"
)


def measure(cls, parents, queries):
    start = time.perf_counter()
    tree = cls(len(parents) + 1)
    for v, parent in enumerate(parents, 1):
        tree.add_edge(parent, v, v % 17 - 8)
    added = time.perf_counter()
    tree.build(0)
    built = time.perf_counter()
    lca_checksum = sum(tree.lca(u, v) for u, v in queries)
    queried = time.perf_counter()
    distance_checksum = sum(tree.get_distance(u, v) for u, v in queries)
    finished = time.perf_counter()
    return (
        (added - start, built - added, queried - built, finished - queried),
        (lca_checksum, distance_checksum),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--library", type=Path, default=LIBRARY)
    parser.add_argument("--n", type=int, default=100000)
    parser.add_argument("--q", type=int, default=100000)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument(
        "--shape", choices=["chain", "star", "random", "all"], default="all"
    )
    args = parser.parse_args()
    if min(args.n, args.q, args.repeat) < 1:
        parser.error("n, q, repeat must be positive")
    classes = [("current", runpy.run_path(str(args.library))["EulerTour"])]
    if args.baseline:
        classes.insert(0, ("baseline", runpy.run_path(str(args.baseline))["EulerTour"]))
    rng = random.Random(819)
    queries = [(rng.randrange(args.n), rng.randrange(args.n)) for _ in range(args.q)]
    shapes = ["chain", "star", "random"] if args.shape == "all" else [args.shape]
    for shape in shapes:
        parents = [
            v - 1 if shape == "chain" else 0 if shape == "star" else rng.randrange(v)
            for v in range(1, args.n)
        ]
        expected = measure(classes[0][1], parents, queries)[1]
        # PyPy の JIT をウォームアップしてから計測する。
        for _, cls in classes:
            for _ in range(2):
                assert measure(cls, parents, queries)[1] == expected
        samples = {name: [] for name, _ in classes}
        for repeat in range(args.repeat):
            for name, cls in classes[:: 1 if repeat & 1 else -1]:
                gc.collect()
                elapsed, checksum = measure(cls, parents, queries)
                assert checksum == expected
                samples[name].append(elapsed)
        print(f"{shape}: n={args.n}, q={args.q}")
        for name, results in samples.items():
            medians = [statistics.median(column) for column in zip(*results)]
            times = ", ".join(
                f"{phase}={elapsed:.4f}s"
                for phase, elapsed in zip(
                    ["edges", "build", "lca", "distance"], medians
                )
            )
            print(f"  {name}: {times}")
        print("  checksums match")


if __name__ == "__main__":
    main()
