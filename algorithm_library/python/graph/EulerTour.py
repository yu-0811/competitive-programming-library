from algorithm_library.python.data_structure.BIT import fenwick_tree


class EulerTour:
    # 任意の頂点番号・根・辺重み。頂点は 0..N-1 または 1..N。
    def __init__(s, N):
        s.N = N
        s.G = [[] for _ in range(N + 1)]
        s._in = [-1] * (N + 1)
        s._out = [-1] * (N + 1)
        s.m = 0
        s.vs, s.ws, s.es, s.depth = [], [], [], []
        s.base = 1 << N.bit_length()
        s.mask = s.base - 1

    def add_edge(s, u, v, w):
        s.m += 1
        s.G[u].append((v, w, s.m))
        s.G[v].append((u, w, s.m))

    def _build_fentree(s):
        n = len(s.ws)
        s.fen = fenwick_tree(n)
        d = s.fen.data = s.ws[:]
        for i in range(n):
            j = i | (i + 1)
            if j < n:
                d[j] += d[i]

    def _build_lca(s):
        order = s.order = [v for v, e in zip(s.vs, s.es) if e >= 0]
        rank = s.rank = [0] * (s.N + 1)
        for i, v in enumerate(order):
            rank[v] = i
        # 行きがけ順で u<v なら、区間 (u,v] の親の最小順位が LCA。
        a = [rank[abs(s.vs[s._in[v] - 1])] for v in order[1:]]
        tab = s.lca_tab = [a]
        for k in range(len(a).bit_length() - 1):
            prev = tab[-1]
            row = prev[1 << k :]
            for i in range(len(row)):
                if prev[i] < row[i]:
                    row[i] = prev[i]
            tab.append(row)

    # vs/ws/es/depth と _in/_out（終了位置を含む）を構築
    def build(s, root, *, lca=True, path_sum=True):
        s.root = root
        s.fen = s.lca_tab = None
        s._in[:] = s._out[:] = [-1] * (s.N + 1)
        tin, tout = s._in, s._out
        n = sum(map(len, s.G)) + 1
        s.vs, s.ws, s.es, s.depth = ([0] * n for _ in range(4))
        vs, ws, es, depth = s.vs, s.ws, s.es, s.depth
        parent = [-1] * (s.N + 1)
        stack = [root]
        t, d = 0, -1
        while stack:
            v = stack.pop()
            if v >= 0:
                tin[v] = tout[v] = t
                vs[t] = v
                d += 1
                for u, w, i in s.G[v]:
                    if u == parent[v]:
                        ws[t], es[t] = w, i
                    else:
                        parent[u] = v
                        stack.extend((~u, u))
            else:
                child = ~v
                v = parent[child]
                tout[v] = t
                vs[t] = -v
                ws[t], es[t] = -ws[tin[child]], -es[tin[child]]
                d -= 1
            depth[t] = d
            t += 1
        for a in (vs, ws, es, depth):
            del a[t:]
        if path_sum:
            s._build_fentree()
        if lca:
            s._build_lca()

    def path_sum(s, u):
        if s.fen is None:
            s._build_fentree()
        return s.fen.sum0(s._in[u] + 1)

    def lca(s, u, v):
        if s._in[u] > s._in[v]:
            u, v = v, u
        if s._in[v] <= s._out[u]:
            return u
        if s.lca_tab is None:
            s._build_lca()
        l, r = s.rank[u], s.rank[v]
        k = (r - l).bit_length() - 1
        row = s.lca_tab[k]
        return s.order[min(row[l], row[r - (1 << k)])]

    def get_distance(s, u, v):
        a = s.lca(u, v)
        return s.path_sum(u) + s.path_sum(v) - 2 * s.path_sum(a)
