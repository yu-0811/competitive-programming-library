---
title: Union find (dsu)
documentation_of: ../algo_library/python/graph/unionFind.py
---

N 頂点無向グラフに対して
* 辺の追加
* 2 頂点が連結かの判定

を $O(\alpha(N))$ で行える

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