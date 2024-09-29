---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/graph/PotentialUnionFind_yosupo.test.py
    title: tests/graph/PotentialUnionFind_yosupo.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PotentialUnionFind():\n  def __init__(self,N) -> None:\n    self.N\
    \ = N\n    self.parents = [-1]*(N+1)\n    # \u5404\u8981\u7D20\u306E\u6839\u304B\
    \u3089\u306E\u8DDD\u96E2\n    # \u76F8\u5BFE\u7684\u306A\u91CD\u3055\u3092\u8868\
    \u3059\n    # \u7D4C\u8DEF\u5727\u7E2E\u524D\u306F\u89AA\u30CE\u30FC\u30C9\u3068\
    \u306E\u5DEE\u5206\n    self.potential = [0]*(N+1)\n    self.inf = pow(10,18)\n\
    \  \n  # \u9802\u70B9x\u306E\u6839\u3092\u8FD4\u3059\u95A2\u6570\n  # O(\u03B1\
    (N))\n  def root(self,x):\n    if self.parents[x]<0: return x\n    else:\n   \
    \   # \u7D4C\u8DEF\u5727\u7E2E\n      r = self.root(self.parents[x]) # \u5148\u306B\
    \u7D4C\u8DEF\u5727\u7E2E\u3057\u3066\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u3092\
    \u66F4\u65B0\u3059\u308B\n      self.potential[x] += self.potential[self.parents[x]]\
    \ # \u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u306F\u6839\u307E\u3067\u306E\u5408\u8A08\
    (\u6839\u306B\u3064\u306A\u3044\u3060\u6642\u306B\u3064\u3058\u3064\u307E\u5408\
    \u3046\u3088\u3046\u306B)\n      self.parents[x] = r\n      return self.parents[x]\n\
    \  \n  # potential[y] - potential[x]\n  # y \u304C x \u3088\u308A\u3069\u308C\u3060\
    \u3051\u91CD\u3044\u304B\n  # \u9023\u7D50\u3067\u306A\u3044\u306A\u3089 inf \u3092\
    \u8FD4\u3059\n  # O(\u03B1(N))\n  def dist(self,x,y):\n    rx = self.root(x);\
    \ ry = self.root(y)\n    if rx==ry: # \u540C\u3058\u9023\u7D50\u6210\u5206\u306B\
    \u5C5E\u3059\u308B\u306A\u3089\n      return self.potential[y] - self.potential[x]\n\
    \    else: return self.inf\n\n  # x \u3068 y \u3092\u8DDD\u96E2 distance \u3067\
    \u3064\u306A\u3050\n  # \u6B63\u78BA\u306B\u306F potential[y] = potential[x] +\
    \ distance \u306B\u306A\u308B\u3088\u3046\u306B\u3064\u306A\u3050\n  # x \u306E\
    \u4E0B\u306B y \u3092\u3064\u306A\u3050\n  # y \u306F x \u3088\u308A w \u91CD\u3044\
    \n  # x -> y \u306E\u91CD\u307F distance \u306E\u6709\u5411\u8FBA\n  # \u8FD4\u308A\
    \u5024\u306F\u77DB\u76FE\u304C\u306A\u3051\u308C\u3070 true\n  # O(\u03B1(N))\n\
    \  def union(self,x,y,w):\n    rx = self.root(x); ry = self.root(y)\n    if rx==ry:\
    \ # \u65E2\u306B\u9023\u7D50\u306A\u3089\n      return self.potential[y] - self.potential[x]\
    \ == w\n    # \u3084\u3084\u3053\u3057\u3044\u304C\u3001x-y \u3092\u3064\u306A\
    \u3050\u304C\u3001\u7D4C\u8DEF\u5727\u7E2E\u306E\u90FD\u5408\u3067\u5B9F\u88C5\
    \u3067\u306F rx-ry \u3092\u3064\u306A\u3050\u3053\u3068\u306B\u306A\u308B\n  \
    \  # union by size \u3067\u3064\u306A\u3052\u308B\n    if self.parents[ry] > self.parents[rx]:\n\
    \      # rx \u306E\u4E0B\u306B ry \u3092\u3064\u306A\u3050\n      self.parents[rx]\
    \ += self.parents[ry]\n      self.potential[ry] = self.potential[x] + w - self.potential[y]\n\
    \      self.parents[ry] = rx\n    else:\n      # ry \u306E\u4E0B\u306B rx \u3092\
    \u3064\u306A\u3050\n      self.parents[ry] += self.parents[rx]\n      self.potential[rx]\
    \ = self.potential[y] - w - self.potential[x]\n      self.parents[rx] = ry\n \
    \   return True\n\n  # \u8981\u7D20x\u304C\u5C5E\u3059\u308B\u30B0\u30EB\u30FC\
    \u30D7\u306E\u8981\u7D20\u6570\u3092\u8FD4\u3059\n  # O(\u03B1(N))\n  def size(self,x):\
    \ return -self.parents[self.root(x)]\n\n  # x,y\u304C\u540C\u3058\u30B0\u30EB\u30FC\
    \u30D7\u304B(\u9023\u7D50\u304B)\u3092\u8FD4\u3059\u95A2\u6570\n  # O(\u03B1(N))\n\
    \  def isSame(self,x,y): return self.root(x)==self.root(y)\n  \n  # x\u304C\u5C5E\
    \u3059\u308B\u30B0\u30EB\u30FC\u30D7\u306E\u8981\u7D20\u3092\u30EA\u30B9\u30C8\
    \u3067\u8FD4\u3059\n  # O(N)\n  def members(self, x):\n      root = self.root(x)\n\
    \      return [i for i in range(1,self.N+1) if self.root(i) == root]\n\n  # \u3059\
    \u3079\u3066\u306E\u6839\u306E\u8981\u7D20\u3092\u30EA\u30B9\u30C8\u3067\u8FD4\
    \u3059\n  # O(N \xD7 \u03B1(N))\n  def roots(self): return [i for i, x in enumerate(self.parents)\
    \ if x < 0]\n\n  # \u30B0\u30EB\u30FC\u30D7\u306E\u6570\u3092\u8FD4\u3059\n  #\
    \ O(N \xD7 \u03B1(N))\n  def group_count(self): return len(self.roots())"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/graph/PotentialUnionFind.py
  requiredBy: []
  timestamp: '2024-09-29 14:24:30+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/PotentialUnionFind_yosupo.test.py
documentation_of: algo_library/python/graph/PotentialUnionFind.py
layout: document
redirect_from:
- /library/algo_library/python/graph/PotentialUnionFind.py
- /library/algo_library/python/graph/PotentialUnionFind.py.html
title: algo_library/python/graph/PotentialUnionFind.py
---
