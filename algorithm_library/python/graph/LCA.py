from collections import deque


class LCA:
    def __init__(self, N, G, root):
        # 根からの距離と親を求める
        self.N = N
        self.bit = N.bit_length()
        parent = self.parent = [[-1] * (N + 1) for _ in range(self.bit)]
        depth = self.depth = [-1] * (N + 1)  # 根からの距離
        depth[root] = 0
        first = parent[0]
        que = deque([root])
        while que:
            v = que.popleft()
            d = depth[v] + 1
            for v2 in G[v]:
                if depth[v2] == -1:
                    depth[v2] = d
                    first[v2] = v
                    que.append(v2)

        # ダブリングする
        for i in range(1, self.bit):
            prev, cur = parent[i - 1], parent[i]
            for j in range(N + 1):
                if prev[j] != -1:
                    cur[j] = prev[prev[j]]

    # u と v の LCA を返す
    # O(log N)
    def lca(self, u, v):
        parent, depth = self.parent, self.depth
        # 深さを同じにする
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        while diff:
            k = diff.bit_length() - 1
            u = parent[k][u]
            diff ^= 1 << k
        # 二分探索する
        if u == v:
            return u
        for row in reversed(parent):
            pu, pv = row[u], row[v]
            if pu != pv:
                u, v = pu, pv
        return parent[0][u]

    # u と v の距離を返す
    def get_distance(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    # u-v のパス上に a が存在するか
    def is_on_path(self, u, v, a):
        return self.get_distance(u, a) + self.get_distance(a, v) == self.get_distance(
            u, v
        )
