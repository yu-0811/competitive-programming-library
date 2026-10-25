---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"pypy3 -B tests/math/benchmark_cmp_sort.py [--fresh-process]\"\"\"\n\
    \nimport argparse\nimport gc\nimport json\nimport pickle\nimport platform\nimport\
    \ random\nimport runpy\nimport statistics\nimport subprocess\nimport sys\nimport\
    \ tempfile\nimport time\nfrom functools import cmp_to_key\nfrom pathlib import\
    \ Path\n\nROOT = Path(__file__).resolve().parents[2]\ncompare = runpy.run_path(str(ROOT\
    \ / \"algorithm_library/python/math/AngularSort.py\"))[\n    \"compare\"\n]\n\
    cmp_sort = runpy.run_path(str(ROOT / \"algorithm_library/python/techniques/CmpSort.py\"\
    ))[\n    \"cmp_sort\"\n]\nCASES = [\"random\", \"sorted\", \"reversed\", \"equal\"\
    , \"few_angles\", \"nearly_sorted\", \"runs\"]\n\n\ndef builtin_sort(values, cmp):\n\
    \    values.sort(key=cmp_to_key(cmp))\n\n\nMETHODS = {\"cmp_to_key\": builtin_sort,\
    \ \"cmp_sort\": cmp_sort}\n\n\ndef make_cases(n, seed, selected):\n    rng = random.Random(seed\
    \ + n)\n    values = []\n    for _ in range(n):\n        x, y = rng.randint(-(10**9),\
    \ 10**9), rng.randint(-(10**9), 10**9)\n        values.append((x, y) if x or y\
    \ else (1, 0))\n    ordered = sorted(values, key=cmp_to_key(compare))\n    for\
    \ case in selected:\n        if case == \"random\":\n            yield case, values\n\
    \        elif case == \"sorted\":\n            yield case, ordered\n        elif\
    \ case == \"reversed\":\n            yield case, ordered[::-1]\n        elif case\
    \ == \"equal\":\n            yield (\n                case,\n                [(7\
    \ * k, 3 * k) for k in (rng.randint(1, 10**6) for _ in range(n))],\n         \
    \   )\n        elif case == \"few_angles\":\n            directions = [\n    \
    \            (1, 0),\n                (1, 1),\n                (0, 1),\n     \
    \           (-1, 1),\n                (-1, 0),\n                (-1, -1),\n  \
    \              (0, -1),\n                (1, -1),\n            ]\n           \
    \ points = []\n            for _ in range(n):\n                x, y = rng.choice(directions)\n\
    \                k = rng.randint(1, 10**6)\n                points.append((x *\
    \ k, y * k))\n            yield case, points\n        elif case == \"nearly_sorted\"\
    :\n            points = ordered[:]\n            # n/100 \u56DE\u306E\u30E9\u30F3\
    \u30C0\u30E0\u306A\u4EA4\u63DB\u3002\n            for _ in range(n // 100):\n\
    \                i, j = rng.randrange(n), rng.randrange(n)\n                points[i],\
    \ points[j] = points[j], points[i]\n            yield case, points\n        else:\n\
    \            # \u7D04 64 \u672C\u306E\u6574\u5217\u6E08\u307F run \u306E\u9806\
    \u5E8F\u3092\u30B7\u30E3\u30C3\u30D5\u30EB\u3002\n            width = max(16,\
    \ n // 64)\n            runs = [ordered[i : i + width] for i in range(0, n, width)]\n\
    \            rng.shuffle(runs)\n            yield case, [point for run in runs\
    \ for point in run]\n\n\ndef measure(values, expected, repeat, warmup):\n    for\
    \ _ in range(warmup):\n        for method in METHODS.values():\n            actual\
    \ = values[:]\n            method(actual, compare)\n            assert actual\
    \ == expected\n    samples = {name: [] for name in METHODS}\n    for i in range(repeat):\n\
    \        # \u5B9F\u884C\u9806\u306E\u504F\u308A\u3092\u907F\u3051\u308B\u3002\u30B3\
    \u30D4\u30FC\u30FBGC\u30FB\u6B63\u3057\u3055\u691C\u8A3C\u306F\u8A08\u6E2C\u533A\
    \u9593\u306E\u5916\u3002\n        for name in list(METHODS)[:: 1 if i & 1 else\
    \ -1]:\n            actual = values[:]\n            gc.collect()\n           \
    \ start = time.perf_counter()\n            METHODS[name](actual, compare)\n  \
    \          elapsed = time.perf_counter() - start\n            assert actual ==\
    \ expected\n            samples[name].append(elapsed)\n    return samples\n\n\n\
    def measure_processes(values, expected, repeat, warmup, fresh):\n    samples =\
    \ {name: [] for name in METHODS}\n    with tempfile.TemporaryDirectory(prefix=\"\
    benchmark-cmp-sort-\") as directory:\n        data_path = Path(directory) / \"\
    input.pickle\"\n        with data_path.open(\"wb\") as stream:\n            pickle.dump((values,\
    \ expected), stream, protocol=4)\n        command = [sys.executable, \"-B\", str(Path(__file__).resolve())]\n\
    \        if not fresh:\n            # \u4ED6\u306E\u30B5\u30A4\u30BA\u30FB\u5165\
    \u529B\u5206\u5E03\u306B\u3088\u308B JIT \u306E\u5C65\u6B74\u3092\u6301\u3061\u8D8A\
    \u3055\u306A\u3044\u3002\n            result = subprocess.run(\n             \
    \   command\n                + [\n                    \"--worker\",\n        \
    \            \"warm\",\n                    str(data_path),\n                \
    \    \"--repeat\",\n                    str(repeat),\n                    \"--warmup\"\
    ,\n                    str(warmup),\n                ],\n                check=True,\n\
    \                capture_output=True,\n                text=True,\n          \
    \  )\n            return json.loads(result.stdout)\n        for i in range(repeat):\n\
    \            for name in list(METHODS)[:: 1 if i & 1 else -1]:\n             \
    \   result = subprocess.run(\n                    command + [\"--worker\", name,\
    \ str(data_path)],\n                    check=True,\n                    capture_output=True,\n\
    \                    text=True,\n                )\n                samples[name].append(float(result.stdout))\n\
    \    return samples\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=__doc__)\n\
    \    parser.add_argument(\n        \"--sizes\", nargs=\"+\", type=int, default=[1000,\
    \ 10000, 100000, 200000]\n    )\n    parser.add_argument(\"--cases\", nargs=\"\
    +\", choices=CASES, default=CASES)\n    parser.add_argument(\"--repeat\", type=int,\
    \ default=5)\n    parser.add_argument(\"--warmup\", type=int, default=2)\n   \
    \ parser.add_argument(\"--seed\", type=int, default=20261025)\n    parser.add_argument(\n\
    \        \"--fresh-process\",\n        action=\"store_true\",\n        help=\"\
    \u6BCE\u56DE\u65B0\u3057\u3044\u30D7\u30ED\u30BB\u30B9\u3067\u6700\u521D\u306E\
    \u30BD\u30FC\u30C8\u3092\u6E2C\u5B9A (\u8D77\u52D5\u30FB\u5165\u529B\u8AAD\u8FBC\
    \u6642\u9593\u306F\u9664\u304F)\",\n    )\n    parser.add_argument(\n        \"\
    --worker\", nargs=2, metavar=(\"METHOD\", \"DATA\"), help=argparse.SUPPRESS\n\
    \    )\n    args = parser.parse_args()\n    if args.worker:\n        name, data_path\
    \ = args.worker\n        with Path(data_path).open(\"rb\") as stream:\n      \
    \      actual, expected = pickle.load(stream)\n        if name == \"warm\":\n\
    \            print(json.dumps(measure(actual, expected, args.repeat, args.warmup)))\n\
    \            return\n        gc.collect()\n        start = time.perf_counter()\n\
    \        METHODS[name](actual, compare)\n        elapsed = time.perf_counter()\
    \ - start\n        assert actual == expected\n        print(elapsed)\n       \
    \ return\n    if min(args.sizes) < 1 or args.repeat < 1 or args.warmup < 0:\n\
    \        parser.error(\"sizes/repeat must be positive; warmup must be nonnegative\"\
    )\n    print(\n        f\"# {platform.python_implementation()} {platform.python_version()};\
    \ {sys.version.splitlines()[-1]}\"\n    )\n    mode = (\n        \"fresh-process\"\
    \n        if args.fresh_process\n        else f\"isolated workload; warmup={args.warmup}\"\
    \n    )\n    print(f\"# {mode}; repeat={args.repeat}; seed={args.seed}; sort only;\
    \ median\")\n    print(\"case,n,cmp_to_key_ms,cmp_sort_ms,speedup\", flush=True)\n\
    \    for n in args.sizes:\n        for case, values in make_cases(n, args.seed,\
    \ args.cases):\n            expected = sorted(values, key=cmp_to_key(compare))\n\
    \            samples = measure_processes(\n                values, expected, args.repeat,\
    \ args.warmup, args.fresh_process\n            )\n            medians = {\n  \
    \              name: statistics.median(times) for name, times in samples.items()\n\
    \            }\n            old, new = medians[\"cmp_to_key\"], medians[\"cmp_sort\"\
    ]\n            print(\n                f\"{case},{n},{old * 1000:.3f},{new * 1000:.3f},{old\
    \ / new:.2f}x\",\n                flush=True,\n            )\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/math/benchmark_cmp_sort.py
  requiredBy: []
  timestamp: '2026-10-25 18:45:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/math/benchmark_cmp_sort.py
layout: document
redirect_from:
- /library/tests/math/benchmark_cmp_sort.py
- /library/tests/math/benchmark_cmp_sort.py.html
title: tests/math/benchmark_cmp_sort.py
---
