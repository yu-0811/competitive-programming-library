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
  code: "class PotentialUnionFind:\n    def __init__(s, N) -> None:\n        s.N =\
    \ N\n        s.parents = [-1] * (N + 1)\n        # \u5404\u8981\u7D20\u306E\u6839\
    \u304B\u3089\u306E\u8DDD\u96E2\n        # \u76F8\u5BFE\u7684\u306A\u91CD\u3055\
    \u3092\u8868\u3059\n        # \u7D4C\u8DEF\u5727\u7E2E\u524D\u306F\u89AA\u30CE\
    \u30FC\u30C9\u3068\u306E\u5DEE\u5206\n        s.potential = [0] * (N + 1)\n  \
    \      s.inf = pow(10, 18)\n        s.inconsistent = [False] * (\n           \
    \ N + 1\n        )  # \u9023\u7D50\u6210\u5206\u306B\u8CA0\u9589\u8DEF\u304C\u3042\
    \u308B\u304B\uFF08\u77DB\u76FE\u304C\u3042\u308B\u304B\uFF09\n\n    # \u9802\u70B9\
    x\u306E\u6839\u3092\u8FD4\u3059\u95A2\u6570\n    # O(\u03B1(N))\n    def root(s,\
    \ x):\n        parents, potential = s.parents, s.potential\n        path = []\n\
    \        while parents[x] >= 0:\n            path.append(x)\n            x = parents[x]\n\
    \        for v in reversed(path):\n            potential[v] += potential[parents[v]]\n\
    \            parents[v] = x\n        return x\n\n    # potential[y] - potential[x]\n\
    \    # y \u304C x \u3088\u308A\u3069\u308C\u3060\u3051\u91CD\u3044\u304B\n   \
    \ # \u9023\u7D50\u3067\u306A\u3044\u306A\u3089 inf \u3092\u8FD4\u3059\n    # O(\u03B1\
    (N))\n    def dist(s, x, y):\n        rx = s.root(x)\n        ry = s.root(y)\n\
    \        if rx == ry:  # \u540C\u3058\u9023\u7D50\u6210\u5206\u306B\u5C5E\u3059\
    \u308B\u306A\u3089\n            return s.potential[y] - s.potential[x]\n     \
    \   else:\n            return s.inf\n\n    # x \u3068 y \u3092\u8DDD\u96E2 distance\
    \ \u3067\u3064\u306A\u3050\n    # \u6B63\u78BA\u306B\u306F potential[y] = potential[x]\
    \ + distance \u306B\u306A\u308B\u3088\u3046\u306B\u3064\u306A\u3050\n    # x \u306E\
    \u4E0B\u306B y \u3092\u3064\u306A\u3050\n    # y \u306F x \u3088\u308A w \u91CD\
    \u3044\n    # x -> y \u306E\u91CD\u307F distance \u306E\u6709\u5411\u8FBA\n  \
    \  # \u8FD4\u308A\u5024\u306F\u77DB\u76FE\u304C\u306A\u3051\u308C\u3070 true\n\
    \    # O(\u03B1(N))\n    def union(s, x, y, w):\n        rx = s.root(x)\n    \
    \    ry = s.root(y)\n        if rx == ry:  # \u65E2\u306B\u9023\u7D50\u306A\u3089\
    \n            if s.potential[y] - s.potential[x] != w:\n                s.inconsistent[rx]\
    \ = True\n            return s.potential[y] - s.potential[x] == w\n        parents,\
    \ potential = s.parents, s.potential\n        # \u6839\u3069\u3046\u3057\u306E\
    \u5DEE\u306B\u76F4\u3057\u3001\u5C0F\u3055\u3044\u6728\u3092\u5927\u304D\u3044\
    \u6728\u306B\u3064\u306A\u3050\u3002\n        if parents[ry] > parents[rx]:\n\
    \            w = potential[x] + w - potential[y]\n        else:\n            rx,\
    \ ry = ry, rx\n            w = potential[y] - w - potential[x]\n        parents[rx]\
    \ += parents[ry]\n        parents[ry] = rx\n        potential[ry] = w\n      \
    \  return True\n\n    # \u8981\u7D20x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\
    \u30D7\u306E\u8981\u7D20\u6570\u3092\u8FD4\u3059\n    # O(\u03B1(N))\n    def\
    \ size(s, x):\n        return -s.parents[s.root(x)]\n\n    # x,y\u304C\u540C\u3058\
    \u30B0\u30EB\u30FC\u30D7\u304B(\u9023\u7D50\u304B)\u3092\u8FD4\u3059\u95A2\u6570\
    \n    # O(\u03B1(N))\n    def isSame(s, x, y):\n        return s.root(x) == s.root(y)\n\
    \n    # x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\u8981\u7D20\u3092\
    \u30EA\u30B9\u30C8\u3067\u8FD4\u3059\n    # O(N)\n    def members(s, x):\n   \
    \     root = s.root(x)\n        return [i for i in range(1, s.N + 1) if s.root(i)\
    \ == root]\n\n    # \u3059\u3079\u3066\u306E\u6839\u306E\u8981\u7D20\u3092\u30EA\
    \u30B9\u30C8\u3067\u8FD4\u3059\n    # O(N \xD7 \u03B1(N))\n    def roots(s):\n\
    \        return [i for i, x in enumerate(s.parents) if x < 0]\n\n    # \u30B0\u30EB\
    \u30FC\u30D7\u306E\u6570\u3092\u8FD4\u3059\n    # O(N \xD7 \u03B1(N))\n    def\
    \ group_count(s):\n        return len(s.roots())\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/PotentialUnionFind.py
  requiredBy: []
  timestamp: '2026-11-08 11:01:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/PotentialUnionFind.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/PotentialUnionFind.py
- /library/algorithm_library/python/graph/PotentialUnionFind.py.html
title: algorithm_library/python/graph/PotentialUnionFind.py
---
