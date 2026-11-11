# HLD。参考: https://judge.yosupo.jp/submission/400748
class LCA:
    # n: 頂点数、E: 辺集合, r: 木の根
    def __init__(self, n, E, r=0):
        par = self.par = [0] * (n + 1)
        dep = self.dep = [-1] * (n + 1)
        siz = self.siz = [1] * (n + 1)
        jmp = self.jmp = [-1] * (n + 1)
        tin = self.tin = [0] * (n + 1)
        deg = [0] * (n + 1)

        for u, v in E:
            deg[u] += 1
            deg[v] += 1
            par[u] ^= v
            par[v] ^= u
        que = []
        for u in range(n + 1):
            if deg[u] == 1 and u != r:
                que.append(u)
            elif deg[u] == 0:
                par[u] = -1
        for u in que:
            v = par[u]
            siz[v] += siz[u]
            if siz[u] > tin[v]:
                tin[v] = siz[u]
                jmp[v] = u
            par[v] ^= u
            deg[v] -= 1
            if deg[v] == 1 and v != r:
                que.append(v)
        par[r] = -1

        if jmp[r] >= 0:
            siz[jmp[r]] = -siz[jmp[r]]
        jmp[r] = -1
        siz[r] = tin[r] + 1
        dep[r] = tin[r] = 0
        for u in reversed(que):
            v = par[u]
            dep[u] = dep[v] + 1
            h, b = jmp[u], tin[u] + 1
            if h >= 0:
                siz[h] = -siz[h]
            if siz[u] < 0:
                tin[u] = tin[v] + 1
                jmp[u] = jmp[v]
            else:
                tin[u] = tin[v] + siz[v]
                siz[v] += siz[u]
                jmp[u] = v
            siz[u] = b

    # u と v の LCA を返す O(log N)
    def lca(self, u, v):
        tin, jmp = self.tin, self.jmp
        l, r = tin[u], tin[v]
        if l > r:
            l, r = r, l
            u, v = v, u
        if r < l + self.siz[u]:
            return u
        v = jmp[v]
        while l < tin[v]:
            v = jmp[v]
        return v

    # 構築時の根を基準に、u の部分木に v が含まれるか O(1)
    def is_in_subtree(self, u, v):
        tin = self.tin
        return tin[u] <= tin[v] < tin[u] + self.siz[u]

    # u と v の距離を返す
    def get_distance(self, u, v):
        dep = self.dep
        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]

    # u-v のパスがviaを通るか（端点も含む）
    def is_on_path(self, u, v, via):
        anc_u = self.is_in_subtree(via, u)
        anc_v = self.is_in_subtree(via, v)
        return anc_u != anc_v or anc_u and self.lca(u, v) == via
