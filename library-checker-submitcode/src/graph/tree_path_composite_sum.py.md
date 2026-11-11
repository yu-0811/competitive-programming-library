---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/problem/tree_path_composite_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/tree_path_composite_sum\n# include:\
    \ algorithm_library/python/graph/Rerooting.py\n\n\ndef main():\n    N = int(readline())\n\
    \    values = list(map(int, readline().split()))\n    g = [[] for _ in range(N)]\n\
    \    for _ in range(N - 1):\n        u, v, b, c = map(int, readline().split())\n\
    \        g[u].append((v, (b, c)))\n        g[v].append((u, (b, c)))\n\n    # \u72B6\
    \u614B\u306F (\u5024\u306E\u7DCF\u548C, \u9802\u70B9\u6570)\u3002\n    def merge(a,\
    \ b):\n        return ((a[0] + b[0]) % mod, a[1] + b[1])\n\n    def add_vertex(x,\
    \ v):\n        return ((x[0] + values[v]) % mod, x[1] + 1)\n\n    def add_edge(x,\
    \ w):\n        b, c = w\n        return ((b * x[0] + c * x[1]) % mod, x[1])\n\n\
    \    dp = rerooting(g, (0, 0), merge, add_vertex, add_edge)\n    print(*(x[0]\
    \ for x in dp))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/tree_path_composite_sum.py
  requiredBy: []
  timestamp: '2026-11-11 22:38:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/tree_path_composite_sum.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/tree_path_composite_sum.py
- /library/library-checker-submitcode/src/graph/tree_path_composite_sum.py.html
title: library-checker-submitcode/src/graph/tree_path_composite_sum.py
---
