"""pypy3 -B tests/graph/benchmark_lca.py --baseline /tmp/LCA-before.py"""

import argparse
import gc
import platform
import random
import runpy
import statistics
import time
from pathlib import Path


LIBRARY = Path(__file__).resolve().parents[2] / "algorithm_library/python/graph/LCA.py"
SHAPES = ["chain", "star", "balanced", "random", "broom"]
PHASES = ["build", "lca", "subtree", "distance", "is_on_path"]


def measure(cls, graph, queries):
    start = time.perf_counter()
    tree = cls(len(graph), graph, 0)
    built = time.perf_counter()
    lca_checksum = sum(tree.lca(u, v) for u, v, _ in queries)
    queried = time.perf_counter()
    is_in_subtree = getattr(tree, "is_in_subtree", lambda u, v: tree.lca(u, v) == u)
    subtree_checksum = sum(is_in_subtree(u, v) for u, v, _ in queries)
    subtrees = time.perf_counter()
    distance_checksum = sum(tree.get_distance(u, v) for u, v, _ in queries)
    distances = time.perf_counter()
    path_checksum = sum(tree.is_on_path(u, v, a) for u, v, a in queries)
    finished = time.perf_counter()
    return (
        (
            built - start,
            queried - built,
            subtrees - queried,
            distances - subtrees,
            finished - distances,
        ),
        (lca_checksum, subtree_checksum, distance_checksum, path_checksum),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--library", type=Path, default=LIBRARY)
    parser.add_argument("--n", type=int, default=100000)
    parser.add_argument("--q", type=int, default=100000)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--shape", choices=SHAPES + ["all"], default="all")
    args = parser.parse_args()
    if min(args.n, args.q, args.repeat) < 1:
        parser.error("n, q, repeat must be positive")
    classes = [("current", runpy.run_path(str(args.library))["LCA"])]
    if args.baseline:
        classes.insert(0, ("baseline", runpy.run_path(str(args.baseline))["LCA"]))
    rng = random.Random(819)
    queries = [
        (rng.randrange(args.n), rng.randrange(args.n), rng.randrange(args.n))
        for _ in range(args.q)
    ]
    shapes = SHAPES if args.shape == "all" else [args.shape]
    print(platform.python_implementation(), platform.python_version(), flush=True)
    for shape in shapes:
        graph = [[] for _ in range(args.n)]
        for v in range(1, args.n):
            p = (
                v - 1
                if shape == "chain"
                else 0
                if shape == "star"
                else (v - 1) // 2
                if shape == "balanced"
                else min(v - 1, args.n // 2)
                if shape == "broom"
                else rng.randrange(v)
            )
            graph[p].append(v)
            graph[v].append(p)
        expected = measure(classes[0][1], graph, queries)[1]
        # PyPy の JIT をウォームアップし、実行順も交互にする。
        for _, cls in classes:
            for _ in range(2):
                assert measure(cls, graph, queries)[1] == expected
        samples = {name: [] for name, _ in classes}
        for repeat in range(args.repeat):
            for name, cls in classes[:: 1 if repeat & 1 else -1]:
                gc.collect()
                elapsed, checksum = measure(cls, graph, queries)
                assert checksum == expected
                samples[name].append(elapsed)
        print(f"{shape}: n={args.n}, q={args.q}", flush=True)
        medians = {}
        for name, results in samples.items():
            medians[name] = [statistics.median(column) for column in zip(*results)]
            times = ", ".join(
                f"{phase}={elapsed:.4f}s"
                for phase, elapsed in zip(PHASES, medians[name])
            )
            print(f"  {name}: {times}", flush=True)
        if args.baseline:
            ratios = ", ".join(
                f"{phase}={old / new:.2f}x"
                for phase, old, new in zip(
                    PHASES, medians["baseline"], medians["current"]
                )
            )
            print(f"  speedup: {ratios}", flush=True)
        print("  checksums match", flush=True)


if __name__ == "__main__":
    main()
