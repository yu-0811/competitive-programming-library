# Euler Tour 順による部分木の区間化

`algorithm_library/python/graph/EulerTourOrder.py` の `euler_tour(G, root=0)` は、
木を DFS の行きがけ順に並べ、`tin, tout, order` を返します。
構築時間・空間は O(N)。反復 DFS なので深い木でも再帰上限の変更は不要です。

- `G[v]`: 頂点 v の隣接頂点。無向木でも、親から子への辺だけでも使えます。
- `root`: 根。頂点番号は `0 <= v < len(G)`。1-indexed の場合は `G[0]` を空にします。
- `order[i]`: i 番目に訪問した頂点。各頂点は1回だけ現れ、子は隣接リストの順に訪問します。
- `tin[v]`: 頂点 v の位置。`order[tin[v]] == v`。
- `tout[v]`: 部分木の右端（含まない）。葉なら `tout[v] == tin[v] + 1`。

空でない木を渡してください。根から到達しない頂点の `tin`, `tout` は -1 です。

```python
tin, tout, order = euler_tour(G, root)
a = [values[v] for v in order]  # この順で BIT / セグ木を構築

# 頂点 v の値を更新する位置
p = tin[v]

# 頂点 v 自身を含む部分木に対応する半開区間
l, r = tin[v], tout[v]

# 部分木サイズ
size = tout[v] - tin[v]

# 頂点 u が v の部分木に含まれるか
inside = tin[v] <= tin[u] < tout[v]
```

辺の値を子の `tin` に置けば、部分木の内部の辺は `[tin[v] + 1, tout[v])` です。
頂点 v 自身を除いた子孫の区間も同じです。
配列のスライスは部分木サイズに比例するコピーが生じるので、区間クエリでは添字を渡します。

既存の `EulerTour.py` が持つ往復の巡回列、LCA、パス和は計算しません。
任意の2頂点間のパスは、この順序では一般に1つの区間になりません。

提出・検証コード: `library-checker-submitcode/graph/vertex_add_subtree_sum_euler_tour.test.py`
