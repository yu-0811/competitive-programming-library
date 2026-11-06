---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/data_structure/BIT.py
    title: algorithm_library/python/data_structure/BIT.py
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
  code: "from algorithm_library.python.data_structure.BIT import fenwick_tree\n\n\n\
    class EulerTour:\n    # \u4EFB\u610F\u306E\u9802\u70B9\u756A\u53F7\u30FB\u6839\
    \u30FB\u8FBA\u91CD\u307F\u3002\u9802\u70B9\u306F 0..N-1 \u307E\u305F\u306F 1..N\u3002\
    \n    def __init__(s, N):\n        s.N = N\n        s.G = [[] for _ in range(N\
    \ + 1)]\n        s._in = [-1] * (N + 1)\n        s._out = [-1] * (N + 1)\n   \
    \     s.m = 0\n        s.vs, s.ws, s.es, s.depth = [], [], [], []\n        s.base\
    \ = 1 << N.bit_length()\n        s.mask = s.base - 1\n\n    def add_edge(s, u,\
    \ v, w):\n        s.m += 1\n        s.G[u].append((v, w, s.m))\n        s.G[v].append((u,\
    \ w, s.m))\n\n    def _build_fentree(s):\n        n = len(s.ws)\n        s.fen\
    \ = fenwick_tree(n)\n        d = s.fen.data = s.ws[:]\n        for i in range(n):\n\
    \            j = i | (i + 1)\n            if j < n:\n                d[j] += d[i]\n\
    \n    def _build_lca(s):\n        order = s.order = [v for v, e in zip(s.vs, s.es)\
    \ if e >= 0]\n        rank = s.rank = [0] * (s.N + 1)\n        for i, v in enumerate(order):\n\
    \            rank[v] = i\n        # \u884C\u304D\u304C\u3051\u9806\u3067 u<v \u306A\
    \u3089\u3001\u533A\u9593 (u,v] \u306E\u89AA\u306E\u6700\u5C0F\u9806\u4F4D\u304C\
    \ LCA\u3002\n        a = [rank[abs(s.vs[s._in[v] - 1])] for v in order[1:]]\n\
    \        tab = s.lca_tab = [a]\n        for k in range(len(a).bit_length() - 1):\n\
    \            prev = tab[-1]\n            row = prev[1 << k :]\n            for\
    \ i in range(len(row)):\n                if prev[i] < row[i]:\n              \
    \      row[i] = prev[i]\n            tab.append(row)\n\n    # vs/ws/es/depth \u3068\
    \ _in/_out\uFF08\u7D42\u4E86\u4F4D\u7F6E\u3092\u542B\u3080\uFF09\u3092\u69CB\u7BC9\
    \n    def build(s, root, *, lca=True, path_sum=True):\n        s.root = root\n\
    \        s.fen = s.lca_tab = None\n        s._in[:] = s._out[:] = [-1] * (s.N\
    \ + 1)\n        tin, tout = s._in, s._out\n        n = sum(map(len, s.G)) + 1\n\
    \        s.vs, s.ws, s.es, s.depth = ([0] * n for _ in range(4))\n        vs,\
    \ ws, es, depth = s.vs, s.ws, s.es, s.depth\n        parent = [-1] * (s.N + 1)\n\
    \        stack = [root]\n        t, d = 0, -1\n        while stack:\n        \
    \    v = stack.pop()\n            if v >= 0:\n                tin[v] = tout[v]\
    \ = t\n                vs[t] = v\n                d += 1\n                for\
    \ u, w, i in s.G[v]:\n                    if u == parent[v]:\n               \
    \         ws[t], es[t] = w, i\n                    else:\n                   \
    \     parent[u] = v\n                        stack.extend((~u, u))\n         \
    \   else:\n                child = ~v\n                v = parent[child]\n   \
    \             tout[v] = t\n                vs[t] = -v\n                ws[t],\
    \ es[t] = -ws[tin[child]], -es[tin[child]]\n                d -= 1\n         \
    \   depth[t] = d\n            t += 1\n        for a in (vs, ws, es, depth):\n\
    \            del a[t:]\n        if path_sum:\n            s._build_fentree()\n\
    \        if lca:\n            s._build_lca()\n\n    def path_sum(s, u):\n    \
    \    if s.fen is None:\n            s._build_fentree()\n        return s.fen.sum0(s._in[u]\
    \ + 1)\n\n    def lca(s, u, v):\n        if s._in[u] > s._in[v]:\n           \
    \ u, v = v, u\n        if s._in[v] <= s._out[u]:\n            return u\n     \
    \   if s.lca_tab is None:\n            s._build_lca()\n        l, r = s.rank[u],\
    \ s.rank[v]\n        k = (r - l).bit_length() - 1\n        row = s.lca_tab[k]\n\
    \        return s.order[min(row[l], row[r - (1 << k)])]\n\n    def get_distance(s,\
    \ u, v):\n        a = s.lca(u, v)\n        return s.path_sum(u) + s.path_sum(v)\
    \ - 2 * s.path_sum(a)\n"
  dependsOn:
  - algorithm_library/python/data_structure/BIT.py
  isVerificationFile: false
  path: algorithm_library/python/graph/EulerTour.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/EulerTour.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/EulerTour.py
- /library/algorithm_library/python/graph/EulerTour.py.html
title: algorithm_library/python/graph/EulerTour.py
---
