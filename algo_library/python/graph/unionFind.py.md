---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/union_find_yosupo.test.py
    title: tests/union_find_yosupo.test.py
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
    \n  # O(\u03B1(N))\n  def union(self, x, y):\n    x = self.root(x); y = self.root(y)\n\
    \    if x == y: return # x,y \u304C\u540C\u3058\u30B0\u30EB\u30FC\u30D7\u306A\u3089\
    \u306A\u306B\u3082\u3057\u306A\u3044\n    # x,y \u306F\u6839\u3067\u3042\u308A\
    \u3001parents \u306E\u5024*-1 \u304C\u305D\u306E\u6728\u306E\u30B5\u30A4\u30BA\
    (\u8981\u7D20\u6570)\n    # \u30B5\u30A4\u30BA\u304C\u5C0F\u3055\u3044\u65B9\u306B\
    \u3064\u306A\u3052\u308B (union by size)\n    if self.parents[x] > self.parents[y]:\
    \ x, y = y, x # x \u304C\u5C0F\u3055\u3044\u65B9\u306B\u306A\u308B\u3088\u3046\
    \u306B\u3059\u308B\n    self.parents[x] += self.parents[y] # \u30B5\u30A4\u30BA\
    \u3092\u66F4\u65B0\n    self.parents[y] = x\n\n  # \u8981\u7D20x\u304C\u5C5E\u3059\
    \u308B\u30B0\u30EB\u30FC\u30D7\u306E\u8981\u7D20\u6570\u3092\u8FD4\u3059\n  #\
    \ O(\u03B1(N))\n  def size(self, x): return -self.parents[self.root(x)]\n\n  #\
    \ x,y\u304C\u540C\u3058\u30B0\u30EB\u30FC\u30D7\u304B(\u9023\u7D50\u304B)\u3092\
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
  path: algo_library/python/graph/unionFind.py
  requiredBy: []
  timestamp: '2024-09-24 23:23:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/union_find_yosupo.test.py
documentation_of: algo_library/python/graph/unionFind.py
layout: document
title: Union find (dsu)
---

N 頂点無向グラフに対して以下の操作を $O(\alpha(N))$ で処理できる
* 辺の追加
* 2 頂点が連結かの判定

経路圧縮と union by size を採用している。  
根の親の値 (parents) に連結成分のサイズの情報を持たせる実装をしている。

### 初期化
```
uf = UnionFind(N)
```
- 時間計算量：$O(\alpha(N))$

### union
```
uf.union(u,v)
```
頂点 $u$ と頂点 $v$ を結ぶ無向辺を追加する。  
返り値はない。  
union by size で結合している  
つまり、連結成分の要素数が少ない方に結合している。
- 時間計算量：$O(\alpha(N))$

### root
```
uf.root(v)
```
頂点 $v$ が属する連結成分の代表元 (内部的には根) を返す。  
処理過程で経路圧縮している。
- 時間計算量：$O(\alpha(N))$

### size
```
uf.size(v)
```
頂点 $v$ が属する連結成分のサイズ (要素数) を返す。  
$root()$ を呼び出している。
- 時間計算量：$O(\alpha(N))$

### isSame
```
uf.isSame(u,v)
```
頂点 $u$ と頂点 $v$ が同じ連結成分に含まれるかを返す。
- 時間計算量：$O(\alpha(N))$

### members
```
uf.members(v)
```
頂点 $v$ が属する連結成分に含まれる頂点を配列で返す。
- 時間計算量：$O(N)$

### roots
```
uf.roots(v)
```
すべての根の要素をリストで返す。
- 時間計算量：$O(N)$

### group_count
```
uf.group_count()
```
連結成分の個数を返す。
- 時間計算量：$O(N)$