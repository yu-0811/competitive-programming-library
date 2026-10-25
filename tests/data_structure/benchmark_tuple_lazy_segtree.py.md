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
  code: "\"\"\"pypy3 -B tests/data_structure/benchmark_tuple_lazy_segtree.py\"\"\"\
    \n\nimport argparse\nimport gc\nimport random\nimport runpy\nimport statistics\n\
    import time\nfrom pathlib import Path\n\n\nLIBRARY = (\n    Path(__file__).resolve().parents[2]\
    \ / \"algorithm_library/python/data-structure\"\n)\nLazySegtree = runpy.run_path(str(LIBRARY\
    \ / \"LazySegtree.py\"))[\"lazy_segtree\"]\nTupleLazySegtree = runpy.run_path(str(LIBRARY\
    \ / \"TupleLazySegtree.py\"))[\n    \"TupleLazySegtree\"\n]\nMOD = 998244353\n\
    \n\ndef op(x, y):\n    return (x[0] + y[0]) % MOD, x[1] + y[1]\n\n\ndef mp(f,\
    \ x):\n    return (f[0] * x[0] + f[1] * x[1]) % MOD, x[1]\n\n\ndef comp(f, g):\n\
    \    return f[0] * g[0] % MOD, (f[0] * g[1] + f[1]) % MOD\n\n\ndef main():\n \
    \   parser = argparse.ArgumentParser(description=__doc__)\n    parser.add_argument(\"\
    --n\", type=int, default=65536)\n    parser.add_argument(\"--q\", type=int, default=20000)\n\
    \    parser.add_argument(\"--repeat\", type=int, default=5)\n    args = parser.parse_args()\n\
    \    if args.n < 1 or args.q < 1 or args.repeat < 1:\n        parser.error(\"\
    n, q, repeat must be positive\")\n    rng = random.Random(20261020)\n    values\
    \ = [(rng.randrange(MOD), 1) for _ in range(args.n)]\n    operations = []\n  \
    \  for _ in range(args.q):\n        left = rng.randrange(args.n)\n        right\
    \ = rng.randrange(left + 1, args.n + 1)\n        operations.append((left, right,\
    \ rng.randrange(MOD), rng.randrange(MOD)))\n\n    def run(cls):\n        tree\
    \ = cls(values, op, (0, 0), mp, comp, (1, 0))\n        checksum = 0\n        for\
    \ i, (left, right, b, c) in enumerate(operations):\n            if i & 1:\n  \
    \              checksum += tree.prod(left, right)[0]\n            else:\n    \
    \            tree.apply(left, right, (b, c))\n        return checksum\n\n    classes\
    \ = [(\"tuple\", LazySegtree), (\"columns\", TupleLazySegtree)]\n    expected\
    \ = run(LazySegtree)\n    for _ in range(2):\n        for _, cls in classes:\n\
    \            assert run(cls) == expected\n    samples = {name: [] for name, _\
    \ in classes}\n    for repeat in range(args.repeat):\n        for name, cls in\
    \ classes[:: 1 if repeat & 1 else -1]:\n            gc.collect()\n           \
    \ start = time.perf_counter()\n            checksum = run(cls)\n            samples[name].append(time.perf_counter()\
    \ - start)\n            assert checksum == expected\n    medians = {name: statistics.median(times)\
    \ for name, times in samples.items()}\n    for name, elapsed in medians.items():\n\
    \        print(f\"{name}: {elapsed * 1000:.3f} ms\")\n    print(f\"speedup: {medians['tuple']\
    \ / medians['columns']:.2f}x\")\n    print(\"checksums match\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/benchmark_tuple_lazy_segtree.py
  requiredBy: []
  timestamp: '2026-10-20 12:59:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/benchmark_tuple_lazy_segtree.py
layout: document
redirect_from:
- /library/tests/data_structure/benchmark_tuple_lazy_segtree.py
- /library/tests/data_structure/benchmark_tuple_lazy_segtree.py.html
title: tests/data_structure/benchmark_tuple_lazy_segtree.py
---
