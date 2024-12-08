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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind():\n  # O(\u03B1(N)) \u306F\u307B\u307C\u5B9A\u6570\u6642\
    \u9593\n  def __init__(self, n):\n    self.n = n\n    # \u5404\u9802\u70B9\u306E\
    \u89AA(1\u500B\u4E0A\u306E\u8981\u7D20)\u3092\u8A18\u5165\n    # \u305D\u306E\u9802\
    \u70B9\u304C\u6839\u306A\u3089 -1 \u4EE5\u4E0B\u306E\u5024\n    # parents*-1 \u304C\
    \u305D\u306E\u6728\u306E\u30B5\u30A4\u30BA(\u8981\u7D20\u6570)\n    self.parents\
    \ = [-1] * (n+1)  \n\n  # \u9802\u70B9x\u306E\u6839\u3092\u8FD4\u3059\u95A2\u6570\
    \n  # \u6839\u307E\u3067\u4E0A\u306B\u305F\u3069\u308B\n  # \u7D4C\u8DEF\u5727\
    \u7E2E\u3067 x \u304B\u3089\u6839\u307E\u3067\u306B\u901A\u308B\u9802\u70B9\u3092\
    \u3059\u3079\u3066\u6839\u306B\u3064\u306A\u304E\u306A\u304A\u3059\n  # \u7D4C\
    \u8DEF\u5727\u7E2E\u306B\u3088\u3063\u3066\u3053\u306E\u95A2\u6570\u304C\u8FD4\
    \u3059\u5024\u306F\u5909\u308F\u3089\u306A\u3044(\u6839\u3092\u8FD4\u3059\u304B\
    \u3089)\n  # O(\u03B1(N))\n  def root(self, x):\n    if self.parents[x] < 0: return\
    \ x # x\u304C\u6839\u306A\u3089x\u3092\u8FD4\u3059\n    else:\n      self.parents[x]\
    \ = self.root(self.parents[x]) # \u7D4C\u8DEF\u5727\u7E2E\n      return self.parents[x]\n\
    \n  # O(\u03B1(N))\n  # \u30DE\u30FC\u30B8\u5F8C\u306E\u6839\u3092\u8FD4\u3059\
    \n  def union(self, x, y):\n    x = self.root(x); y = self.root(y)\n    if x ==\
    \ y: return # x,y \u304C\u540C\u3058\u30B0\u30EB\u30FC\u30D7\u306A\u3089\u306A\
    \u306B\u3082\u3057\u306A\u3044\n    # x,y \u306F\u6839\u3067\u3042\u308A\u3001\
    parents \u306E\u5024*-1 \u304C\u305D\u306E\u6728\u306E\u30B5\u30A4\u30BA(\u8981\
    \u7D20\u6570)\n    # \u30B5\u30A4\u30BA\u304C\u5C0F\u3055\u3044\u65B9\u306B\u3064\
    \u306A\u3052\u308B (union by size)\n    if self.parents[x] > self.parents[y]:\
    \ x, y = y, x # x \u304C\u5C0F\u3055\u3044\u65B9\u306B\u306A\u308B\u3088\u3046\
    \u306B\u3059\u308B\n    self.parents[x] += self.parents[y] # \u30B5\u30A4\u30BA\
    \u3092\u66F4\u65B0\n    self.parents[y] = x\n    return x\n\n  # \u8981\u7D20\
    x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\u8981\u7D20\u6570\u3092\
    \u8FD4\u3059\n  # O(\u03B1(N))\n  def size(self, x): return -self.parents[self.root(x)]\n\
    \n  # x,y\u304C\u540C\u3058\u30B0\u30EB\u30FC\u30D7\u304B(\u9023\u7D50\u304B)\u3092\
    \u8FD4\u3059\u95A2\u6570\n  # O(\u03B1(N))\n  def isSame(self, x, y): return self.root(x)\
    \ == self.root(y)\n\n  # x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\
    \u8981\u7D20\u3092\u30EA\u30B9\u30C8\u3067\u8FD4\u3059\n  # O(N)\n  def members(self,\
    \ x):\n      root = self.root(x)\n      return [i for i in range(self.n) if self.root(i)\
    \ == root]\n\n  # \u3059\u3079\u3066\u306E\u6839\u306E\u8981\u7D20\u3092\u30EA\
    \u30B9\u30C8\u3067\u8FD4\u3059\n  # O(N)\n  def roots(self): return [i for i,\
    \ x in enumerate(self.parents) if x < 0]\n\n  # \u30B0\u30EB\u30FC\u30D7\u306E\
    \u6570\u3092\u8FD4\u3059\n  # O(N)\n  def group_count(self): return len(self.roots())"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/UnionFind.py
  requiredBy: []
  timestamp: '2024-12-08 12:18:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/UnionFind.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/UnionFind.py
- /library/algorithm_library/python/graph/UnionFind.py.html
title: algorithm_library/python/graph/UnionFind.py
---
