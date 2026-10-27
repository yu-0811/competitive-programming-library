# HLD。参考: https://judge.yosupo.jp/submission/400748
class LCA:
    # O(N) 時間・空間。G を変更せず、0-index / 1-index の両方に対応。
    def __init__(s, N, G, root):
        p = s.p = [-1] * (N + 1)
        d = s.depth = [-1] * (N + 1)
        z = s.size = [1] * (N + 1)
        h = s.up = [-1] * (N + 1)
        t = s.tin = [-1] * (N + 1)
        heavy = [-1] * (N + 1)
        offset = [1] * (N + 1)
        q = [root]
        d[root] = t[root] = 0
        # BFSで親と深さを求める。
        for u in q:
            for v in G[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    p[v] = u
                    q.append(v)
        # 部分木サイズと、部分木が最大の子（heavy）を求める。
        for u in q[:0:-1]:
            v = p[u]
            z[v] += z[u]
            if heavy[v] < 0 or z[u] > z[heavy[v]]:
                heavy[v] = u
        # heavyの部分木を先に置くDFS順を割り当てる。
        # up[u] は u が属する重パスの先頭の親。
        for u in q[1:]:
            v = p[u]
            if heavy[v] == u:
                h[u] = h[v]
                t[u] = t[v] + 1
            else:
                h[u] = v
                t[u] = t[v] + z[heavy[v]] + offset[v]
                offset[v] += z[u]

    # u と v の LCA を返す O(log N)
    def lca(s, u, v):
        p = s.p
        if p[u] == p[v]:
            return u if u == v else p[u]
        t, h = s.tin, s.up
        a, b = t[u], t[v]
        if a > b:
            a, b = b, a
            u, v = v, u
        if b < a + s.size[u]:
            return u
        # DFS順が後ろの側だけを、重パス単位で上げる。
        while a < b:
            v = h[v]
            b = t[v]
        return v

    # 構築時の根を基準に、v が u の部分木に含まれるか（u 自身を含む）O(1)
    def is_in_subtree(s, u, v):
        t = s.tin
        return t[u] <= t[v] < t[u] + s.size[u]

    # u と v の距離を返す
    def get_distance(s, u, v):
        d = s.depth
        return d[u] + d[v] - 2 * d[s.lca(u, v)]

    # u-v のパス上に a が存在するか
    def is_on_path(s, u, v, a):
        x = s.is_in_subtree(a, u)
        y = s.is_in_subtree(a, v)
        return x != y or x and s.lca(u, v) == a
