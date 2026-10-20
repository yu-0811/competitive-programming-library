# Dinic法 O(V^2 E)
class maxflow_edge:
    def __init__(self, to, cap, rev_idx):
        self.to = to  # 行き先
        self.cap = cap  # 容量
        self.rev_idx = rev_idx  # 逆向きの辺のインデックス


class maximum_flow:
    def __init__(self, N):
        self.G = [[] for _ in range(N + 1)]
        self.N = N

    def add_edge(self, a, b, c):
        self.G[a].append(maxflow_edge(b, c, len(self.G[b])))
        self.G[b].append(maxflow_edge(a, 0, len(self.G[a]) - 1))  # 逆向き

    def dfs(self, v, goal, f):
        graph, level, it = self.G, self.level, self.it
        vertices = [v]
        path = []
        limits = [f]
        while vertices:
            v = vertices[-1]
            if v == goal:
                flow = limits[-1]
                for edge in path:
                    edge.cap -= flow
                    graph[edge.to][edge.rev_idx].cap += flow
                return flow

            row = graph[v]
            i = it[v]
            while i < len(row):
                edge = row[i]
                if edge.cap > 0 and level[edge.to] == level[v] + 1:
                    it[v] = i
                    vertices.append(edge.to)
                    path.append(edge)
                    limits.append(min(limits[-1], edge.cap))
                    break
                i += 1
            else:
                it[v] = i
                level[v] = -1  # この頂点からはこれ以上流せない
                vertices.pop()
                limits.pop()
                if path:
                    path.pop()
                    it[vertices[-1]] += 1
        return 0

    def maxflow(self, start, goal):
        assert start != goal
        graph = self.G
        total_flow = 0
        inf = sum(edge.cap for edge in graph[start])
        while True:
            level = self.level = [-1] * (self.N + 1)
            level[start] = 0
            que = [start]
            for v in que:
                for edge in graph[v]:
                    if edge.cap > 0 and level[edge.to] == -1:
                        level[edge.to] = level[v] + 1
                        que.append(edge.to)
            if level[goal] == -1:
                return total_flow

            self.it = [0] * (self.N + 1)
            while True:
                res = self.dfs(start, goal, inf)
                if res == 0:
                    break
                total_flow += res
