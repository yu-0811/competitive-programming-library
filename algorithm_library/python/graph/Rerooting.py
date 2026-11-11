# 全方位木DP。各操作が O(1) なら時間・空間 O(N)、再帰なし。
def rerooting(g, e, merge, add_vertex, add_edge=lambda x, w: x):
    """
    全方位木DP：すべての頂点 r について「r を根としたときの木DPの値」を求める

    g[v] = [(隣接頂点, 辺の情報), ...]：0-indexed の無向木。
    e：merge の単位元。merge は結合的で、g[v] の順に適用する。
    merge(a, b)：同じ頂点から見た、別々の方向の情報をまとめる。
    add_vertex(x, v)：v から見た周囲の情報 x に、v 自身を加える。
    add_edge(x, w)：
        状態 x に辺 w を追加したときの状態を追加する
        w は g に入れた第二要素の辺の情報
    各関数は入力を変更せず、新しい値を返す。
    戻り値：ans[r] = r を根としたときの dp の状態
    """
    n = len(g)
    parent = [-1] * n
    order = [0]
    for v in order:
        for u, w in g[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    # down[v]：v 側から親へ届く情報。すでに親から見た状態。
    down = [e] * n
    for v in order[:0:-1]:
        x = e
        for u, w in g[v]:
            if u == parent[v]:
                parent_edge = w
            else:
                x = merge(x, down[u])
        down[v] = add_edge(add_vertex(x, v), parent_edge)

    # up[v]：親側から v へ届く情報。すでに v から見た状態。
    up = [e] * n
    ans = [e] * n
    for v in order:
        p = parent[v]
        vals = [up[v] if u == p else down[u] for u, _ in g[v]]
        right = [e] * (len(vals) + 1)
        for i in range(len(vals) - 1, -1, -1):
            right[i] = merge(vals[i], right[i + 1])
        ans[v] = add_vertex(right[0], v)
        left = e
        for i, (u, w) in enumerate(g[v]):
            if u != p:
                # u 以外の全方向をまとめ、v を加えてから辺を渡る。
                up[u] = add_edge(add_vertex(merge(left, right[i + 1]), v), w)
            left = merge(left, vals[i])
    return ans


# 例：各頂点からの距離の総和。g[v] = [(隣接頂点, 辺の長さ), ...]
# 状態は (距離の総和, 頂点数)。
# def merge(a, b):
#     return (a[0] + b[0], a[1] + b[1])
# def add_vertex(x, v):
#     return (x[0], x[1] + 1)
# def add_edge(x, w):
#     return (x[0] + w * x[1], x[1])
# dp = rerooting(g, (0, 0), merge, add_vertex, add_edge)
# ans = [x[0] for x in dp]
