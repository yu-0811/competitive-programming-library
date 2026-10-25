"""pypy3 -B tests/data_structure/benchmark_tuple_heap.py [--fresh-process]"""

import argparse
import gc
import heapq
import json
import pickle
import platform
import random
import runpy
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = runpy.run_path(
    str(ROOT / "algorithm_library/python/data-structure/TupleHeap.py")
)
TupleHeap = MODULE["TupleHeap"]
PackedTupleHeap = runpy.run_path(
    str(ROOT / "algorithm_library/python/data-structure/PackedTupleHeap.py")
)["PackedTupleHeap"]
METHODS = ["heapq", "columns", "packed"]
CASES = ["random", "ties", "ascending", "descending", "wide"]
WORKLOADS = ["batch", "mixed", "dijkstra"]


def methods(name, bits, arity):
    if name == "heapq":

        def build(values):
            heap = list(values)
            heapq.heapify(heap)
            return heap

        return build, heapq.heappush, heapq.heappop
    if name == "columns":
        return (
            lambda values: TupleHeap(arity=arity, values=values),
            TupleHeap.push,
            TupleHeap.pop,
        )
    return (
        lambda values: PackedTupleHeap(arity=arity, bits=bits, values=values),
        PackedTupleHeap.push,
        PackedTupleHeap.pop,
    )


def batch(values, build, push, pop):
    heap = build(())
    for item in values:
        push(heap, item)
    checksum = 0
    for _ in values:
        checksum += sum(pop(heap))
    return checksum


def mixed(values, build, push, pop):
    initial = max(1, len(values) // 4)
    heap = build(values[:initial])
    checksum = 0
    for i in range(initial, len(values)):
        checksum += sum(pop(heap))
        push(heap, values[i])
    for _ in range(initial):
        checksum += sum(pop(heap))
    return checksum


def dijkstra(graph, build, push, pop):
    distances = [None] * len(graph)
    distances[0] = 0
    heap = build(((0, 0),))
    while heap:
        distance, vertex = pop(heap)
        if distances[vertex] != distance:
            continue
        for to, weight in graph[vertex]:
            candidate = distance + weight
            old = distances[to]
            if old is None or candidate < old:
                distances[to] = candidate
                push(heap, (candidate, to))
    return distances


RUNNERS = {"batch": batch, "mixed": mixed, "dijkstra": dijkstra}


def make_data(workload, case, n, seed, arity):
    rng = random.Random(seed + n)
    limit = {"ties": 8, "wide": 1 << 90}.get(case, 10**9)
    if workload == "dijkstra":
        # 有向サイクルで全頂点に到達可能にし、各頂点に計 8 辺を張る。
        limit = {"ties": 3, "wide": 1 << 80}.get(case, 1000)
        graph = []
        for vertex in range(n):
            edges = [((vertex + 1) % n, rng.randrange(1, limit + 1))]
            edges.extend(
                (rng.randrange(n), rng.randrange(1, limit + 1)) for _ in range(7)
            )
            graph.append(edges)
        return graph
    values = [
        (rng.randrange(limit),) + tuple(rng.randrange(n) for _ in range(arity - 1))
        for _ in range(n)
    ]
    if case == "ascending":
        values.sort()
    elif case == "descending":
        values.sort(reverse=True)
    return values


def verify_sequence(data, runner, name, bits, arity):
    """計測後にもう一度実行し、全 pop の値・順序を heapq と照合する。"""
    reference = []
    build, push, pop = methods(name, bits, arity)

    def checked_build(values):
        reference[:] = values
        heapq.heapify(reference)
        return build(values)

    def checked_push(heap, item):
        heapq.heappush(reference, item)
        push(heap, item)

    def checked_pop(heap):
        item = pop(heap)
        assert item == heapq.heappop(reference)
        return item

    runner(data, checked_build, checked_push, checked_pop)
    assert not reference


def worker(args):
    name, workload, data_path = args.worker
    with Path(data_path).open("rb") as stream:
        data, expected = pickle.load(stream)
    runner = RUNNERS[workload]
    operations = methods(name, args.bits, args.arity)
    for _ in range(args.warmup):
        assert runner(data, *operations) == expected
    samples = []
    for _ in range(args.repeat):
        gc.collect()
        start = time.perf_counter()
        actual = runner(data, *operations)
        elapsed = time.perf_counter() - start
        assert actual == expected
        samples.append(elapsed)
    verify_sequence(data, runner, name, args.bits, args.arity)
    print(json.dumps(samples))


def measure(data, workload, args, index):
    expected = RUNNERS[workload](data, *methods("heapq", args.bits, args.arity))
    samples = {name: [] for name in args.methods}
    with tempfile.TemporaryDirectory(prefix="benchmark-tuple-heap-") as directory:
        path = Path(directory) / "data.pickle"
        with path.open("wb") as stream:
            pickle.dump((data, expected), stream, protocol=4)
        count = args.repeat if args.fresh_process else 1
        for repeat in range(count):
            order = args.methods[:: 1 if (index + repeat) & 1 else -1]
            for name in order:
                command = [
                    sys.executable,
                    "-B",
                    str(Path(__file__).resolve()),
                    "--worker",
                    name,
                    workload,
                    str(path),
                    "--bits",
                    str(args.bits),
                    "--arity",
                    str(args.arity),
                    "--repeat",
                    str(1 if args.fresh_process else args.repeat),
                    "--warmup",
                    str(0 if args.fresh_process else args.warmup),
                ]
                result = subprocess.run(
                    command, check=True, capture_output=True, text=True
                )
                samples[name].extend(json.loads(result.stdout))
    return samples


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", nargs="+", type=int, default=[100000])
    parser.add_argument(
        "--cases", nargs="+", choices=CASES, default=["random", "ties", "wide"]
    )
    parser.add_argument("--workloads", nargs="+", choices=WORKLOADS)
    parser.add_argument("--methods", nargs="+", choices=METHODS, default=METHODS)
    parser.add_argument("--bits", type=int, default=20)
    parser.add_argument("--arity", type=int, default=2)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20261025)
    parser.add_argument("--fresh-process", action="store_true")
    parser.add_argument("--output", type=Path, help="全計測値を JSON で保存")
    parser.add_argument("--worker", nargs=3, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if (
        args.repeat < 1
        or args.warmup < 0
        or args.bits < 0
        or args.arity < 1
        or min(args.sizes) < 1
    ):
        parser.error(
            "sizes/repeat/arity must be positive; warmup/bits must be nonnegative"
        )
    if args.workloads is None:
        args.workloads = WORKLOADS if args.arity == 2 else ["batch", "mixed"]
    if "dijkstra" in args.workloads and args.arity != 2:
        parser.error("dijkstra requires arity=2")
    if args.worker:
        worker(args)
        return
    if "packed" in args.methods and args.arity > 1 and max(args.sizes) > 1 << args.bits:
        parser.error("sizes must not exceed 2**bits for the packed heap")
    if "dijkstra" in args.workloads and any(
        case in ["ascending", "descending"] for case in args.cases
    ):
        parser.error("ascending/descending are only defined for batch/mixed")
    metadata = {
        "implementation": platform.python_implementation(),
        "version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "date": time.strftime("%Y-%m-%d"),
        "mode": "fresh-process" if args.fresh_process else "warm",
        "warmup": 0 if args.fresh_process else args.warmup,
        "repeat": args.repeat,
        "bits": args.bits,
        "arity": args.arity,
        "heap_implementation": "compact",
        "seed": args.seed,
    }
    print("# " + json.dumps(metadata), flush=True)
    print("workload,case,n,method,median_ms,speedup", flush=True)
    results = []
    for n in args.sizes:
        for workload in args.workloads:
            for case in args.cases:
                data = make_data(workload, case, n, args.seed, args.arity)
                samples = measure(data, workload, args, len(results))
                medians = {
                    name: statistics.median(times) for name, times in samples.items()
                }
                results.append(
                    {
                        "n": n,
                        "workload": workload,
                        "case": case,
                        "samples_seconds": samples,
                    }
                )
                for name, elapsed in medians.items():
                    speedup = medians.get("heapq", elapsed) / elapsed
                    print(
                        f"{workload},{case},{n},{name},{elapsed * 1000:.3f},{speedup:.2f}",
                        flush=True,
                    )
    if args.output:
        args.output.write_text(
            json.dumps({"metadata": metadata, "results": results}, indent=2) + "\n",
            encoding="utf-8",
        )
    print("# all results and pop sequences match heapq", flush=True)


if __name__ == "__main__":
    main()
