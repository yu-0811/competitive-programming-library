"""pypy3 -B tests/math/benchmark_cmp_sort.py [--fresh-process]"""

import argparse
import gc
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
from functools import cmp_to_key
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
compare = runpy.run_path(str(ROOT / "algorithm_library/python/math/AngularSort.py"))[
    "compare"
]
cmp_sort = runpy.run_path(str(ROOT / "algorithm_library/python/techniques/CmpSort.py"))[
    "cmp_sort"
]
CASES = ["random", "sorted", "reversed", "equal", "few_angles", "nearly_sorted", "runs"]


def builtin_sort(values, cmp):
    values.sort(key=cmp_to_key(cmp))


METHODS = {"cmp_to_key": builtin_sort, "cmp_sort": cmp_sort}


def make_cases(n, seed, selected):
    rng = random.Random(seed + n)
    values = []
    for _ in range(n):
        x, y = rng.randint(-(10**9), 10**9), rng.randint(-(10**9), 10**9)
        values.append((x, y) if x or y else (1, 0))
    ordered = sorted(values, key=cmp_to_key(compare))
    for case in selected:
        if case == "random":
            yield case, values
        elif case == "sorted":
            yield case, ordered
        elif case == "reversed":
            yield case, ordered[::-1]
        elif case == "equal":
            yield (
                case,
                [(7 * k, 3 * k) for k in (rng.randint(1, 10**6) for _ in range(n))],
            )
        elif case == "few_angles":
            directions = [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ]
            points = []
            for _ in range(n):
                x, y = rng.choice(directions)
                k = rng.randint(1, 10**6)
                points.append((x * k, y * k))
            yield case, points
        elif case == "nearly_sorted":
            points = ordered[:]
            # n/100 回のランダムな交換。
            for _ in range(n // 100):
                i, j = rng.randrange(n), rng.randrange(n)
                points[i], points[j] = points[j], points[i]
            yield case, points
        else:
            # 約 64 本の整列済み run の順序をシャッフル。
            width = max(16, n // 64)
            runs = [ordered[i : i + width] for i in range(0, n, width)]
            rng.shuffle(runs)
            yield case, [point for run in runs for point in run]


def measure(values, expected, repeat, warmup):
    for _ in range(warmup):
        for method in METHODS.values():
            actual = values[:]
            method(actual, compare)
            assert actual == expected
    samples = {name: [] for name in METHODS}
    for i in range(repeat):
        # 実行順の偏りを避ける。コピー・GC・正しさ検証は計測区間の外。
        for name in list(METHODS)[:: 1 if i & 1 else -1]:
            actual = values[:]
            gc.collect()
            start = time.perf_counter()
            METHODS[name](actual, compare)
            elapsed = time.perf_counter() - start
            assert actual == expected
            samples[name].append(elapsed)
    return samples


def measure_processes(values, expected, repeat, warmup, fresh):
    samples = {name: [] for name in METHODS}
    with tempfile.TemporaryDirectory(prefix="benchmark-cmp-sort-") as directory:
        data_path = Path(directory) / "input.pickle"
        with data_path.open("wb") as stream:
            pickle.dump((values, expected), stream, protocol=4)
        command = [sys.executable, "-B", str(Path(__file__).resolve())]
        if not fresh:
            # 他のサイズ・入力分布による JIT の履歴を持ち越さない。
            result = subprocess.run(
                command
                + [
                    "--worker",
                    "warm",
                    str(data_path),
                    "--repeat",
                    str(repeat),
                    "--warmup",
                    str(warmup),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            return json.loads(result.stdout)
        for i in range(repeat):
            for name in list(METHODS)[:: 1 if i & 1 else -1]:
                result = subprocess.run(
                    command + ["--worker", name, str(data_path)],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                samples[name].append(float(result.stdout))
    return samples


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sizes", nargs="+", type=int, default=[1000, 10000, 100000, 200000]
    )
    parser.add_argument("--cases", nargs="+", choices=CASES, default=CASES)
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument("--warmup", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20261025)
    parser.add_argument(
        "--fresh-process",
        action="store_true",
        help="毎回新しいプロセスで最初のソートを測定 (起動・入力読込時間は除く)",
    )
    parser.add_argument(
        "--worker", nargs=2, metavar=("METHOD", "DATA"), help=argparse.SUPPRESS
    )
    args = parser.parse_args()
    if args.worker:
        name, data_path = args.worker
        with Path(data_path).open("rb") as stream:
            actual, expected = pickle.load(stream)
        if name == "warm":
            print(json.dumps(measure(actual, expected, args.repeat, args.warmup)))
            return
        gc.collect()
        start = time.perf_counter()
        METHODS[name](actual, compare)
        elapsed = time.perf_counter() - start
        assert actual == expected
        print(elapsed)
        return
    if min(args.sizes) < 1 or args.repeat < 1 or args.warmup < 0:
        parser.error("sizes/repeat must be positive; warmup must be nonnegative")
    print(
        f"# {platform.python_implementation()} {platform.python_version()}; {sys.version.splitlines()[-1]}"
    )
    mode = (
        "fresh-process"
        if args.fresh_process
        else f"isolated workload; warmup={args.warmup}"
    )
    print(f"# {mode}; repeat={args.repeat}; seed={args.seed}; sort only; median")
    print("case,n,cmp_to_key_ms,cmp_sort_ms,speedup", flush=True)
    for n in args.sizes:
        for case, values in make_cases(n, args.seed, args.cases):
            expected = sorted(values, key=cmp_to_key(compare))
            samples = measure_processes(
                values, expected, args.repeat, args.warmup, args.fresh_process
            )
            medians = {
                name: statistics.median(times) for name, times in samples.items()
            }
            old, new = medians["cmp_to_key"], medians["cmp_sort"]
            print(
                f"{case},{n},{old * 1000:.3f},{new * 1000:.3f},{old / new:.2f}x",
                flush=True,
            )


if __name__ == "__main__":
    main()
