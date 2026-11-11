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
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n# include:\
    \ algorithm_library/python/graph/EulerTourOrder.py\n# include: algorithm_library/python/data_structure/BIT.py\n\
    \n\ndef main():\n    n, q = map(int, readline().split())\n    values = list(map(int,\
    \ readline().split()))\n    G = [[] for _ in range(n)]\n    # \u756A\u53F7\u3092\
    \u53CD\u8EE2\u3057\u3001\u89AA\u756A\u53F7\u306E\u5927\u5C0F\u3084\u6839\u304C\
    \ 0 \u3067\u3042\u308B\u3053\u3068\u306B\u4F9D\u5B58\u305B\u305A\u4F7F\u3046\u3002\
    \n    for child, parent in enumerate(map(int, readline().split()), 1):\n     \
    \   u, v = n - 1 - parent, n - 1 - child\n        G[u].append(v)\n        G[v].append(u)\n\
    \    tin, tout, order = euler_tour(G, n - 1)\n    bit = fenwick_tree(n)\n    data\
    \ = bit.data = [values[n - 1 - v] for v in order]\n    for i in range(n):\n  \
    \      j = i | (i + 1)\n        if j < n:\n            data[j] += data[i]\n  \
    \  ans = []\n    for _ in range(q):\n        query = list(map(int, readline().split()))\n\
    \        v = n - 1 - query[1]\n        if query[0] == 0:\n            bit.add(tin[v],\
    \ query[2])\n        else:\n            ans.append(bit.sum(tin[v], tout[v]))\n\
    \    for i in range(0, len(ans), 8192):\n        sys.stdout.write(\"\\n\".join(map(str,\
    \ ans[i:i + 8192])) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/vertex_add_subtree_sum_euler_tour.py
  requiredBy: []
  timestamp: '2026-11-11 22:38:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/vertex_add_subtree_sum_euler_tour.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/vertex_add_subtree_sum_euler_tour.py
- /library/library-checker-submitcode/src/graph/vertex_add_subtree_sum_euler_tour.py.html
title: library-checker-submitcode/src/graph/vertex_add_subtree_sum_euler_tour.py
---
