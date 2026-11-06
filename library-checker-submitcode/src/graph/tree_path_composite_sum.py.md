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
    \    values = list(map(int, readline().split()))\n    edges = []\n    coefficients\
    \ = []\n    # \u8FBA\u3092\u4E2D\u7D99\u9802\u70B9\u306B\u7F6E\u304D\u63DB\u3048\
    \u3001\u65E2\u5B58\u306E\u9802\u70B9\u5909\u63DB API \u3067\u4E00\u6B21\u95A2\u6570\
    \u3092\u9069\u7528\u3059\u308B\u3002\n    for i in range(N - 1):\n        u, v,\
    \ b, c = map(int, readline().split())\n        middle = N + i\n        edges.append((u,\
    \ middle))\n        edges.append((middle, v))\n        coefficients.append((b,\
    \ c))\n\n    # \u72B6\u614B\u306F (\u5024\u306E\u7DCF\u548C, \u5143\u306E\u6728\
    \u306E\u9802\u70B9\u6570)\u3002\u4E2D\u7D99\u9802\u70B9\u306F\u6570\u3048\u306A\
    \u3044\u3002\n    def merge(a, b):\n        return ((a[0] + b[0]) % mod, a[1]\
    \ + b[1])\n\n    def node_value(a, v):\n        if v < N:\n            return\
    \ ((a[0] + values[v]) % mod, a[1] + 1)\n        b, c = coefficients[v - N]\n \
    \       return ((b * a[0] + c * a[1]) % mod, a[1])\n\n    def answer(a, v):\n\
    \        return node_value(a, v)[0]\n\n    tree = rerooting(2 * N - 1, edges,\
    \ (0, 0), merge, node_value, answer)\n    print(*tree.run(0)[:N])\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/tree_path_composite_sum.py
  requiredBy: []
  timestamp: '2026-10-29 14:17:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/tree_path_composite_sum.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/tree_path_composite_sum.py
- /library/library-checker-submitcode/src/graph/tree_path_composite_sum.py.html
title: library-checker-submitcode/src/graph/tree_path_composite_sum.py
---
