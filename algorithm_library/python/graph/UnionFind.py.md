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
  code: "from collections import defaultdict\n\n\nclass UnionFind:\n    def __init__(s,\
    \ n):\n        s.n = n\n        # \u5404\u9802\u70B9\u306E\u89AA(1\u500B\u4E0A\
    \u306E\u8981\u7D20)\u3092\u8A18\u5165\n        # \u305D\u306E\u9802\u70B9\u304C\
    \u6839\u306A\u3089 -1 \u4EE5\u4E0B\u306E\u5024\n        # parents*-1 \u304C\u305D\
    \u306E\u6728\u306E\u30B5\u30A4\u30BA(\u8981\u7D20\u6570)\n        s.parents =\
    \ [-1] * n\n\n    # \u9802\u70B9x\u306E\u6839\u3092\u8FD4\u3059\u95A2\u6570\n\
    \    # \u6839\u307E\u3067\u4E0A\u306B\u305F\u3069\u308B\n    # \u7D4C\u8DEF\u5727\
    \u7E2E\u3067 x \u304B\u3089\u6839\u307E\u3067\u306B\u901A\u308B\u9802\u70B9\u3092\
    \u3059\u3079\u3066\u6839\u306B\u3064\u306A\u304E\u306A\u304A\u3059\n    # \u7D4C\
    \u8DEF\u5727\u7E2E\u306B\u3088\u3063\u3066\u3053\u306E\u95A2\u6570\u304C\u8FD4\
    \u3059\u5024\u306F\u5909\u308F\u3089\u306A\u3044(\u6839\u3092\u8FD4\u3059\u304B\
    \u3089)\n    # O(\u03B1(N))\n    def root(s, x):\n        parents = s.parents\n\
    \        r = x\n        while parents[r] >= 0:\n            r = parents[r]\n \
    \       while x != r:\n            parents[x], x = r, parents[x]\n        return\
    \ r\n\n    # \u30DE\u30FC\u30B8\u5F8C\u306E\u6839\u3092\u8FD4\u3059 O(\u03B1(N))\n\
    \    def union(s, x, y):\n        x = s.root(x)\n        y = s.root(y)\n     \
    \   if x == y:\n            return x  # x,y \u304C\u540C\u3058\u30B0\u30EB\u30FC\
    \u30D7\u306A\u3089\u306A\u306B\u3082\u3057\u306A\u3044\n        # x,y \u306F\u6839\
    \u3067\u3042\u308A\u3001parents \u306E\u5024*-1 \u304C\u305D\u306E\u6728\u306E\
    \u30B5\u30A4\u30BA(\u8981\u7D20\u6570)\n        # \u30B5\u30A4\u30BA\u304C\u5C0F\
    \u3055\u3044\u65B9\u306B\u3064\u306A\u3052\u308B (union by size)\n        if s.parents[x]\
    \ > s.parents[y]:\n            x, y = y, x  # x \u304C\u5C0F\u3055\u3044\u65B9\
    \u306B\u306A\u308B\u3088\u3046\u306B\u3059\u308B\n        s.parents[x] += s.parents[y]\
    \  # \u30B5\u30A4\u30BA\u3092\u66F4\u65B0\n        s.parents[y] = x\n        return\
    \ x\n\n    # \u8981\u7D20x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\
    \u8981\u7D20\u6570\u3092\u8FD4\u3059 O(\u03B1(N))\n    def size(s, x):\n     \
    \   return -s.parents[s.root(x)]\n\n    # x,y\u304C\u540C\u3058\u30B0\u30EB\u30FC\
    \u30D7\u304B(\u9023\u7D50\u304B)\u3092\u8FD4\u3059\u95A2\u6570 O(\u03B1(N))\n\
    \    def isSame(s, x, y):\n        return s.root(x) == s.root(y)\n\n    # x\u304C\
    \u5C5E\u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\u8981\u7D20\u3092\u30EA\u30B9\
    \u30C8\u3067\u8FD4\u3059 O(N)\n    def members(s, x):\n        root = s.root(x)\n\
    \        return [i for i in range(s.n) if s.root(i) == root]\n\n    # \u3059\u3079\
    \u3066\u306E\u6839\u306E\u8981\u7D20\u3092\u30EA\u30B9\u30C8\u3067\u8FD4\u3059\
    \ O(N)\n    def roots(s):\n        return [i for i, x in enumerate(s.parents)\
    \ if x < 0]\n\n    # \u30B0\u30EB\u30FC\u30D7\u306E\u6570\u3092\u8FD4\u3059 O(N)\n\
    \    def group_count(s):\n        return len(s.roots())\n\n    # \u3059\u3079\u3066\
    \u306E\u30B0\u30EB\u30FC\u30D7\u3092\u30EA\u30B9\u30C8\u3067\u8FD4\u3059 O(N)\n\
    \    def all_group_members(s):\n        group_members = defaultdict(list)\n  \
    \      for i in range(s.n):\n            root = s.root(i)\n            group_members[root].append(i)\n\
    \        return list(group_members.values())\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/UnionFind.py
  requiredBy: []
  timestamp: '2026-11-08 11:01:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/UnionFind.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/UnionFind.py
- /library/algorithm_library/python/graph/UnionFind.py.html
title: algorithm_library/python/graph/UnionFind.py
---
