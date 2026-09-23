class segtree:  # すべて 0-index
    def __init__(self, V, OP, E):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.data[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    # 1 点更新
    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.data[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    # 1 点加算(自分で書いた)
    def add(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.data[p] += x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    # data[p] を返す
    def get(self, p):
        assert 0 <= p and p < self.n
        return self.data[p + self.size]

    # [l,r) の演算結果を返す
    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                smr = self.op(self.data[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def _update(self, k):
        self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


class fenwick_tree:
    n = 1
    data = [0 for i in range(n)]

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l and l <= r and r <= self.n, "0<=l<=r<=n,l={0},r={1},n={2}".format(
            l, r, self.n
        )
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


class EulerTour:
    def __init__(self, N: int):
        self.N = N
        self.G = [[] for _ in range(N + 1)]
        self._in = [-1] * (N + 1)  # 各頂点の訪問開始時刻
        self._out = [-1] * (N + 1)  # 各頂点の訪問終了時刻
        self.edge_cnt = 0
        self.edge_cost = []
        # オイラーツアーでの訪問順
        self.vartex_order = []
        self.edge_order = []
        self.depth = [-1]

        self.shift = N.bit_length()
        self.base = 1 << self.shift
        self.mask = self.base - 1

    # 無向辺 u-v を重さ w で追加する
    def add_edge(self, u: int, v: int, w: int):
        self.edge_cnt += 1
        self.G[u].append((v, w, self.edge_cnt))
        self.G[v].append((u, w, self.edge_cnt))

    def _dfs(self, v: int):
        stack = []
        stack.append(("f", v, 0, 0))
        while stack:
            state, v, w, idx = stack.pop()
            if state == "f":  # 行きがけ
                if self.vis[v]:
                    stack.pop()
                    continue
                self.vis[v] = True
                self.depth.append(self.depth[-1] + 1)
                self.edge_order.append(idx)
                self.edge_cost.append(w)
                self._in[v] = len(self.edge_order) - 1
                self._out[v] = len(self.edge_order) - 1
                self.vartex_order.append(v)
                for u, w, edge_idx in self.G[v]:
                    if self.vis[u]:
                        continue
                    stack.append(("b", v, w, edge_idx))
                    stack.append(("f", u, w, edge_idx))
            else:  # 帰りがけ
                self.depth.append(self.depth[-1] - 1)
                self.vartex_order.append(-v)
                self.edge_order.append(-idx)
                self.edge_cost.append(-w)
                self._out[v] = len(self.edge_order) - 1

    def _euler_tour(self, root: int):
        # edge_cost 内で辺 i が何番目に登場するか(+と-でそれぞれ)
        self.edge_idx_plus = [-1] * (self.edge_cnt + 1)
        self.edge_idx_minus = [-1] * (self.edge_cnt + 1)
        self.vis = [False] * (self.N + 1)
        self.step = 0
        self._dfs(root)

    def _build_fentree(self):
        self.fen = fenwick_tree(len(self.edge_cost))
        for i in range(1, len(self.edge_cost)):
            self.fen.add(i, self.edge_cost[i])

    def _build_lca(self):
        # lca 用のセグ木の構築
        e = (self.N + 1) * self.base
        s = [
            self.depth[i] * self.base + abs(self.vartex_order[i])
            for i in range(len(self.vartex_order))
        ]
        self.lca_seg = segtree(s, min, e)

    def build(self, root: int):
        self.root = root
        self._euler_tour(root)
        self.depth.pop(0)
        self._build_fentree()
        self._build_lca()

    # 根から u へのパスのコストの和
    def path_sum(self, u: int):
        return self.fen.sum0(self._in[u] + 1)

    # lca(u, v)
    def lca(self, u: int, v: int):
        in_u, in_v = self._in[u], self._in[v]
        if in_u > in_v:
            in_u, in_v = in_v, in_u
        lca_idx = self.lca_seg.prod(in_u, in_v + 1) & self.mask
        return lca_idx

    # パス u - v のコストの和
    def get_distance(self, u: int, v: int):
        lca_idx = self.lca(u, v)
        return self.subtree_sum(u) + self.subtree_sum(v) - 2 * self.subtree_sum(lca_idx)
