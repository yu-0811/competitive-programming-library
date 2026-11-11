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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u5168\u65B9\u4F4D\u6728DP\u3002\u5404\u64CD\u4F5C\u304C O(1) \u306A\u3089\
    \u6642\u9593\u30FB\u7A7A\u9593 O(N)\u3001\u518D\u5E30\u306A\u3057\u3002\ndef rerooting(g,\
    \ e, merge, add_vertex, add_edge=lambda x, w: x):\n    \"\"\"\n    \u5168\u65B9\
    \u4F4D\u6728DP\uFF1A\u3059\u3079\u3066\u306E\u9802\u70B9 r \u306B\u3064\u3044\u3066\
    \u300Cr \u3092\u6839\u3068\u3057\u305F\u3068\u304D\u306E\u6728DP\u306E\u5024\u300D\
    \u3092\u6C42\u3081\u308B\n\n    g[v] = [(\u96A3\u63A5\u9802\u70B9, \u8FBA\u306E\
    \u60C5\u5831), ...]\uFF1A0-indexed \u306E\u7121\u5411\u6728\u3002\n    e\uFF1A\
    merge \u306E\u5358\u4F4D\u5143\u3002merge \u306F\u7D50\u5408\u7684\u3067\u3001\
    g[v] \u306E\u9806\u306B\u9069\u7528\u3059\u308B\u3002\n    merge(a, b)\uFF1A\u540C\
    \u3058\u9802\u70B9\u304B\u3089\u898B\u305F\u3001\u5225\u3005\u306E\u65B9\u5411\
    \u306E\u60C5\u5831\u3092\u307E\u3068\u3081\u308B\u3002\n    add_vertex(x, v)\uFF1A\
    v \u304B\u3089\u898B\u305F\u5468\u56F2\u306E\u60C5\u5831 x \u306B\u3001v \u81EA\
    \u8EAB\u3092\u52A0\u3048\u308B\u3002\n    add_edge(x, w)\uFF1A\n        \u72B6\
    \u614B x \u306B\u8FBA w \u3092\u8FFD\u52A0\u3057\u305F\u3068\u304D\u306E\u72B6\
    \u614B\u3092\u8FFD\u52A0\u3059\u308B\n        w \u306F g \u306B\u5165\u308C\u305F\
    \u7B2C\u4E8C\u8981\u7D20\u306E\u8FBA\u306E\u60C5\u5831\n    \u5404\u95A2\u6570\
    \u306F\u5165\u529B\u3092\u5909\u66F4\u305B\u305A\u3001\u65B0\u3057\u3044\u5024\
    \u3092\u8FD4\u3059\u3002\n    \u623B\u308A\u5024\uFF1Aans[r] = r \u3092\u6839\u3068\
    \u3057\u305F\u3068\u304D\u306E dp \u306E\u72B6\u614B\n    \"\"\"\n    n = len(g)\n\
    \    parent = [-1] * n\n    order = [0]\n    for v in order:\n        for u, w\
    \ in g[v]:\n            if u != parent[v]:\n                parent[u] = v\n  \
    \              order.append(u)\n\n    # down[v]\uFF1Av \u5074\u304B\u3089\u89AA\
    \u3078\u5C4A\u304F\u60C5\u5831\u3002\u3059\u3067\u306B\u89AA\u304B\u3089\u898B\
    \u305F\u72B6\u614B\u3002\n    down = [e] * n\n    for v in order[:0:-1]:\n   \
    \     x = e\n        for u, w in g[v]:\n            if u == parent[v]:\n     \
    \           parent_edge = w\n            else:\n                x = merge(x, down[u])\n\
    \        down[v] = add_edge(add_vertex(x, v), parent_edge)\n\n    # up[v]\uFF1A\
    \u89AA\u5074\u304B\u3089 v \u3078\u5C4A\u304F\u60C5\u5831\u3002\u3059\u3067\u306B\
    \ v \u304B\u3089\u898B\u305F\u72B6\u614B\u3002\n    up = [e] * n\n    ans = [e]\
    \ * n\n    for v in order:\n        p = parent[v]\n        vals = [up[v] if u\
    \ == p else down[u] for u, _ in g[v]]\n        right = [e] * (len(vals) + 1)\n\
    \        for i in range(len(vals) - 1, -1, -1):\n            right[i] = merge(vals[i],\
    \ right[i + 1])\n        ans[v] = add_vertex(right[0], v)\n        left = e\n\
    \        for i, (u, w) in enumerate(g[v]):\n            if u != p:\n         \
    \       # u \u4EE5\u5916\u306E\u5168\u65B9\u5411\u3092\u307E\u3068\u3081\u3001\
    v \u3092\u52A0\u3048\u3066\u304B\u3089\u8FBA\u3092\u6E21\u308B\u3002\n       \
    \         up[u] = add_edge(add_vertex(merge(left, right[i + 1]), v), w)\n    \
    \        left = merge(left, vals[i])\n    return ans\n\n\n# \u4F8B\uFF1A\u5404\
    \u9802\u70B9\u304B\u3089\u306E\u8DDD\u96E2\u306E\u7DCF\u548C\u3002g[v] = [(\u96A3\
    \u63A5\u9802\u70B9, \u8FBA\u306E\u9577\u3055), ...]\n# \u72B6\u614B\u306F (\u8DDD\
    \u96E2\u306E\u7DCF\u548C, \u9802\u70B9\u6570)\u3002\n# def merge(a, b):\n#   \
    \  return (a[0] + b[0], a[1] + b[1])\n# def add_vertex(x, v):\n#     return (x[0],\
    \ x[1] + 1)\n# def add_edge(x, w):\n#     return (x[0] + w * x[1], x[1])\n# dp\
    \ = rerooting(g, (0, 0), merge, add_vertex, add_edge)\n# ans = [x[0] for x in\
    \ dp]\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/Rerooting.py
  requiredBy: []
  timestamp: '2026-11-11 22:38:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/Rerooting.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/Rerooting.py
- /library/algorithm_library/python/graph/Rerooting.py.html
title: algorithm_library/python/graph/Rerooting.py
---
