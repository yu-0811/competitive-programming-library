from collections import deque

class LCA:
    def __init__(self, N, G, root):  
        # 根からの距離と親を求める
        self.N = N
        self.bit = N.bit_length() + 2
        self.parent = [[-1]*(N+1) for _ in range(self.bit)]
        self.parent[0][root] = -1
        self.depth = [-1]*(N+1) # 根からの距離
        self.depth[root] = 0
        que = deque()
        que.append(root)
        while que:
            v = que.popleft()
            for v2 in G[v]:
                if self.depth[v2]==-1:
                    self.depth[v2] = self.depth[v]+1
                    self.parent[0][v2] = v
                    que.append(v2)

        # ダブリングする
        for i in range(1,self.bit):
            for j in range(N+1):
                if self.parent[i-1][j]!=-1: 
                    self.parent[i][j] = self.parent[i-1][self.parent[i-1][j]]

    # u と v の LCA を返す
    # O(log N)
    def lca(self,u,v):
        # 深さを同じにする
        if self.depth[u]<self.depth[v]: u,v = v,u
        for k in range(self.bit):
            if ((self.depth[u]-self.depth[v]) >> k) & 1:
                u = self.parent[k][u]
        # 二分探索する
        if u==v: return u
        for k in reversed(range(self.bit)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    # u と v の距離を返す
    def get_distance(self,u,v):
        return self.depth[u] + self.depth[v] - 2*self.depth[self.lca(u,v)]
    
    # u-v のパス上に a が存在するか
    def is_on_path(self,u,v,a):
        return self.get_distance(u,a) + self.get_distance(v,u) == self.get_distance(u,v)