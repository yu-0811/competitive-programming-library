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
  code: "\"\"\"pypy3 -B tests/data_structure/benchmark_tuple_heap.py [--fresh-process]\"\
    \"\"\n\nimport argparse\nimport gc\nimport heapq\nimport json\nimport pickle\n\
    import platform\nimport random\nimport runpy\nimport statistics\nimport subprocess\n\
    import sys\nimport tempfile\nimport time\nfrom pathlib import Path\n\n\nROOT =\
    \ Path(__file__).resolve().parents[2]\nMODULE = runpy.run_path(\n    str(ROOT\
    \ / \"algorithm_library/python/data-structure/TupleHeap.py\")\n)\nTupleHeap =\
    \ MODULE[\"TupleHeap\"]\nPackedTupleHeap = MODULE[\"PackedTupleHeap\"]\nMETHODS\
    \ = [\"heapq\", \"columns\", \"packed\"]\nCASES = [\"random\", \"ties\", \"ascending\"\
    , \"descending\", \"wide\"]\nWORKLOADS = [\"batch\", \"mixed\", \"dijkstra\"]\n\
    \n\ndef methods(name, bits):\n    if name == \"heapq\":\n\n        def build(values):\n\
    \            heap = list(values)\n            heapq.heapify(heap)\n          \
    \  return heap\n\n        return build, heapq.heappush, heapq.heappop\n    if\
    \ name == \"columns\":\n        return TupleHeap, TupleHeap.push, TupleHeap.pop\n\
    \    return (\n        lambda values: PackedTupleHeap(values, bits=bits),\n  \
    \      PackedTupleHeap.push,\n        PackedTupleHeap.pop,\n    )\n\n\ndef batch(values,\
    \ build, push, pop):\n    heap = build(())\n    for item in values:\n        push(heap,\
    \ item)\n    checksum = 0\n    for _ in values:\n        x, y = pop(heap)\n  \
    \      checksum += x ^ y\n    return checksum\n\n\ndef mixed(values, build, push,\
    \ pop):\n    initial = max(1, len(values) // 4)\n    heap = build(values[:initial])\n\
    \    checksum = 0\n    for i in range(initial, len(values)):\n        x, y = pop(heap)\n\
    \        checksum += x ^ y\n        push(heap, values[i])\n    for _ in range(initial):\n\
    \        x, y = pop(heap)\n        checksum += x ^ y\n    return checksum\n\n\n\
    def dijkstra(graph, build, push, pop):\n    distances = [None] * len(graph)\n\
    \    distances[0] = 0\n    heap = build(((0, 0),))\n    while heap:\n        distance,\
    \ vertex = pop(heap)\n        if distances[vertex] != distance:\n            continue\n\
    \        for to, weight in graph[vertex]:\n            candidate = distance +\
    \ weight\n            old = distances[to]\n            if old is None or candidate\
    \ < old:\n                distances[to] = candidate\n                push(heap,\
    \ (candidate, to))\n    return distances\n\n\nRUNNERS = {\"batch\": batch, \"\
    mixed\": mixed, \"dijkstra\": dijkstra}\n\n\ndef make_data(workload, case, n,\
    \ seed):\n    rng = random.Random(seed + n)\n    limit = {\"ties\": 8, \"wide\"\
    : 1 << 90}.get(case, 10**9)\n    if workload == \"dijkstra\":\n        # \u6709\
    \u5411\u30B5\u30A4\u30AF\u30EB\u3067\u5168\u9802\u70B9\u306B\u5230\u9054\u53EF\
    \u80FD\u306B\u3057\u3001\u5404\u9802\u70B9\u306B\u8A08 8 \u8FBA\u3092\u5F35\u308B\
    \u3002\n        limit = {\"ties\": 3, \"wide\": 1 << 80}.get(case, 1000)\n   \
    \     graph = []\n        for vertex in range(n):\n            edges = [((vertex\
    \ + 1) % n, rng.randrange(1, limit + 1))]\n            edges.extend(\n       \
    \         (rng.randrange(n), rng.randrange(1, limit + 1)) for _ in range(7)\n\
    \            )\n            graph.append(edges)\n        return graph\n    values\
    \ = [(rng.randrange(limit), rng.randrange(n)) for _ in range(n)]\n    if case\
    \ == \"ascending\":\n        values.sort()\n    elif case == \"descending\":\n\
    \        values.sort(reverse=True)\n    return values\n\n\ndef verify_sequence(data,\
    \ runner, name, bits):\n    \"\"\"\u8A08\u6E2C\u5F8C\u306B\u3082\u3046\u4E00\u5EA6\
    \u5B9F\u884C\u3057\u3001\u5168 pop \u306E\u5024\u30FB\u9806\u5E8F\u3092 heapq\
    \ \u3068\u7167\u5408\u3059\u308B\u3002\"\"\"\n    reference = []\n    build, push,\
    \ pop = methods(name, bits)\n\n    def checked_build(values):\n        reference[:]\
    \ = values\n        heapq.heapify(reference)\n        return build(values)\n\n\
    \    def checked_push(heap, item):\n        heapq.heappush(reference, item)\n\
    \        push(heap, item)\n\n    def checked_pop(heap):\n        item = pop(heap)\n\
    \        assert item == heapq.heappop(reference)\n        return item\n\n    runner(data,\
    \ checked_build, checked_push, checked_pop)\n    assert not reference\n\n\ndef\
    \ worker(args):\n    name, workload, data_path = args.worker\n    with Path(data_path).open(\"\
    rb\") as stream:\n        data, expected = pickle.load(stream)\n    runner = RUNNERS[workload]\n\
    \    operations = methods(name, args.bits)\n    for _ in range(args.warmup):\n\
    \        assert runner(data, *operations) == expected\n    samples = []\n    for\
    \ _ in range(args.repeat):\n        gc.collect()\n        start = time.perf_counter()\n\
    \        actual = runner(data, *operations)\n        elapsed = time.perf_counter()\
    \ - start\n        assert actual == expected\n        samples.append(elapsed)\n\
    \    verify_sequence(data, runner, name, args.bits)\n    print(json.dumps(samples))\n\
    \n\ndef measure(data, workload, args, index):\n    expected = RUNNERS[workload](data,\
    \ *methods(\"heapq\", args.bits))\n    samples = {name: [] for name in args.methods}\n\
    \    with tempfile.TemporaryDirectory(prefix=\"benchmark-tuple-heap-\") as directory:\n\
    \        path = Path(directory) / \"data.pickle\"\n        with path.open(\"wb\"\
    ) as stream:\n            pickle.dump((data, expected), stream, protocol=4)\n\
    \        count = args.repeat if args.fresh_process else 1\n        for repeat\
    \ in range(count):\n            order = args.methods[:: 1 if (index + repeat)\
    \ & 1 else -1]\n            for name in order:\n                command = [\n\
    \                    sys.executable,\n                    \"-B\",\n          \
    \          str(Path(__file__).resolve()),\n                    \"--worker\",\n\
    \                    name,\n                    workload,\n                  \
    \  str(path),\n                    \"--bits\",\n                    str(args.bits),\n\
    \                    \"--repeat\",\n                    str(1 if args.fresh_process\
    \ else args.repeat),\n                    \"--warmup\",\n                    str(0\
    \ if args.fresh_process else args.warmup),\n                ]\n              \
    \  result = subprocess.run(\n                    command, check=True, capture_output=True,\
    \ text=True\n                )\n                samples[name].extend(json.loads(result.stdout))\n\
    \    return samples\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=__doc__)\n\
    \    parser.add_argument(\"--sizes\", nargs=\"+\", type=int, default=[100000])\n\
    \    parser.add_argument(\n        \"--cases\", nargs=\"+\", choices=CASES, default=[\"\
    random\", \"ties\", \"wide\"]\n    )\n    parser.add_argument(\"--workloads\"\
    , nargs=\"+\", choices=WORKLOADS, default=WORKLOADS)\n    parser.add_argument(\"\
    --methods\", nargs=\"+\", choices=METHODS, default=METHODS)\n    parser.add_argument(\"\
    --bits\", type=int, default=20)\n    parser.add_argument(\"--repeat\", type=int,\
    \ default=5)\n    parser.add_argument(\"--warmup\", type=int, default=2)\n   \
    \ parser.add_argument(\"--seed\", type=int, default=20261025)\n    parser.add_argument(\"\
    --fresh-process\", action=\"store_true\")\n    parser.add_argument(\"--output\"\
    , type=Path, help=\"\u5168\u8A08\u6E2C\u5024\u3092 JSON \u3067\u4FDD\u5B58\")\n\
    \    parser.add_argument(\"--worker\", nargs=3, help=argparse.SUPPRESS)\n    args\
    \ = parser.parse_args()\n    if args.repeat < 1 or args.warmup < 0 or args.bits\
    \ < 0 or min(args.sizes) < 1:\n        parser.error(\"sizes/repeat must be positive;\
    \ warmup/bits must be nonnegative\")\n    if args.worker:\n        worker(args)\n\
    \        return\n    if \"packed\" in args.methods and max(args.sizes) > 1 <<\
    \ args.bits:\n        parser.error(\"sizes must not exceed 2**bits for the packed\
    \ heap\")\n    if \"dijkstra\" in args.workloads and any(\n        case in [\"\
    ascending\", \"descending\"] for case in args.cases\n    ):\n        parser.error(\"\
    ascending/descending are only defined for batch/mixed\")\n    metadata = {\n \
    \       \"implementation\": platform.python_implementation(),\n        \"version\"\
    : sys.version,\n        \"platform\": platform.platform(),\n        \"processor\"\
    : platform.processor(),\n        \"date\": time.strftime(\"%Y-%m-%d\"),\n    \
    \    \"mode\": \"fresh-process\" if args.fresh_process else \"warm\",\n      \
    \  \"warmup\": 0 if args.fresh_process else args.warmup,\n        \"repeat\":\
    \ args.repeat,\n        \"bits\": args.bits,\n        \"seed\": args.seed,\n \
    \   }\n    print(\"# \" + json.dumps(metadata), flush=True)\n    print(\"workload,case,n,method,median_ms,speedup\"\
    , flush=True)\n    results = []\n    for n in args.sizes:\n        for workload\
    \ in args.workloads:\n            for case in args.cases:\n                data\
    \ = make_data(workload, case, n, args.seed)\n                samples = measure(data,\
    \ workload, args, len(results))\n                medians = {\n               \
    \     name: statistics.median(times) for name, times in samples.items()\n    \
    \            }\n                results.append(\n                    {\n     \
    \                   \"n\": n,\n                        \"workload\": workload,\n\
    \                        \"case\": case,\n                        \"samples_seconds\"\
    : samples,\n                    }\n                )\n                for name,\
    \ elapsed in medians.items():\n                    speedup = medians.get(\"heapq\"\
    , elapsed) / elapsed\n                    print(\n                        f\"\
    {workload},{case},{n},{name},{elapsed * 1000:.3f},{speedup:.2f}\",\n         \
    \               flush=True,\n                    )\n    if args.output:\n    \
    \    args.output.write_text(\n            json.dumps({\"metadata\": metadata,\
    \ \"results\": results}, indent=2) + \"\\n\",\n            encoding=\"utf-8\"\
    ,\n        )\n    print(\"# all results and pop sequences match heapq\", flush=True)\n\
    \n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/benchmark_tuple_heap.py
  requiredBy: []
  timestamp: '2026-10-25 21:47:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/benchmark_tuple_heap.py
layout: document
redirect_from:
- /library/tests/data_structure/benchmark_tuple_heap.py
- /library/tests/data_structure/benchmark_tuple_heap.py.html
title: tests/data_structure/benchmark_tuple_heap.py
---
