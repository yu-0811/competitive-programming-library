class LCA:
    def __init__(s, N, G, root):
        s.N = N
        s.bit = N.bit_length()
        p = s.parent = [[-1] * (N + 1) for _ in range(s.bit)]
        d = s.depth = [-1] * (N + 1)  # 根からの距離
        d[root] = 0
        q = [root]
        for u in q:
            for v in G[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    p[0][v] = u
                    q.append(v)

        for k in range(1, d[q[-1]].bit_length()):
            a, b = p[k - 1], p[k]
            for v in range(N + 1):
                if a[v] >= 0:
                    b[v] = a[a[v]]

    # u と v の LCA を返す O(log N)
    def lca(s, u, v):
        p, d = s.parent, s.depth
        if d[u] < d[v]:  # 深さを同じにする
            u, v = v, u
        x = d[u] - d[v]
        while x:
            k = x.bit_length() - 1
            u = p[k][u]
            x ^= 1 << k
        if u == v:
            return u
        a = p[0]
        if a[u] == a[v]:
            return a[u]
        for k in range((d[u] - 1).bit_length() - 1, -1, -1):
            b = p[k]
            x, y = b[u], b[v]
            if x != y:
                u, v = x, y
        return a[u]

    # 構築時の根を基準に、v が u の部分木に含まれるか O(log N)
    def is_in_subtree(s, u, v):
        return s.lca(u, v) == u

    # u と v の距離を返す
    def get_distance(s, u, v):
        d = s.depth
        return d[u] + d[v] - 2 * d[s.lca(u, v)]

    # u-v のパス上に a が存在するか
    def is_on_path(s, u, v, a):
        x = s.lca(u, a) == a
        y = s.lca(v, a) == a
        return x != y or x and s.lca(u, v) == a
