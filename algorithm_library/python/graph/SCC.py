class SCC:
    def __init__(self, N: int):
        self.N = N  # 頂点数
        self.graphEdges = list()  # 辺
        self.inf = pow(10, 9)

    def addEdge(self, frm: int, to: int):
        assert 0 <= frm <= self.N
        assert 0 <= to <= self.N
        self.graphEdges.append([frm, to])

    # 辺を CSR 形式にする(別にCSRじゃなくてもできるが高速化のため)
    def _toCSR(self, N: int, graphEdges: list[list]):
        start = [0] * (N + 1)
        # endList := 辺を始点の昇順にソートした時の終点のリスト
        endList = [0] * len(graphEdges)

        # start[i+1] := 頂点 i を始点とする辺の数 となるように構築
        for u, v in graphEdges:  # u -> v への辺
            start[u + 1] += 1
        # start[i] := 始点の頂点番号が i 未満である辺の数 になるように累積和を取る
        # このとき、start[i] = endList で頂点 i が始点となる最小の index (0-index)
        for i in range(1, N + 1):
            start[i] += start[i - 1]

        # pointer[i] := 始点を i とする辺の endList への挿入位置
        pointer = start[:]
        for u, v in graphEdges:
            endList[pointer[u]] = v
            pointer[u] += 1

        return start, endList

    # 強連結成分分解をする
    def _decomposeToSCC(self):
        N = self.N
        start, endList = self._toCSR(N, self.graphEdges)
        cursor = start[:-1]  # 各頂点で次に調べる辺の位置
        nowOrder = 0  # 訪れた頂点数
        groupNum = 0  # 見つかった強連結成分の数
        pendingStack = []  # 探索済みかつ sccId が未確定の頂点
        lowlink = [0] * N
        order = [-1] * N  # 頂点の行きがけ順
        parent = [-1] * N
        groupId = [0] * N

        for root in range(N):
            if order[root] != -1:
                continue
            dfsStack = [root]
            lowlink[root] = order[root] = nowOrder
            nowOrder += 1
            pendingStack.append(root)
            while dfsStack:
                v = dfsStack[-1]
                i = cursor[v]
                if i < start[v + 1]:
                    cursor[v] = i + 1
                    to = endList[i]
                    if order[to] == -1:
                        parent[to] = v
                        lowlink[to] = order[to] = nowOrder
                        nowOrder += 1
                        pendingStack.append(to)
                        dfsStack.append(to)
                    elif lowlink[v] > order[to]:
                        lowlink[v] = order[to]
                else:  # 帰りがけ
                    dfsStack.pop()
                    if lowlink[v] == order[v]:
                        while True:
                            u = pendingStack.pop()
                            order[u] = N  # 確定した成分を lowlink の計算から除く
                            groupId[u] = groupNum
                            if u == v:
                                break
                        groupNum += 1
                    pv = parent[v]
                    if pv != -1 and lowlink[pv] > lowlink[v]:
                        lowlink[pv] = lowlink[v]
        # 縮約後のグラフで groupId をトポロジカルソート順にする
        for v in range(N):
            groupId[v] = groupNum - 1 - groupId[v]

        return groupNum, groupId

    # groups[i] = グループID i に属する頂点の集合を 返す
    def build_scc(self) -> list[list[int]]:
        groupNum, groupId = self._decomposeToSCC()
        groups = [[] for _ in range(groupNum)]
        for v in range(self.N):
            groups[groupId[v]].append(v)
        return groups

    # 強連結成分分解後のグラフを構築する(同一の強連結成分内の頂点は縮約)
    def build_dag(self) -> list[list[int]]:
        # groupId[i] = 頂点 i が属する強連結成分の ID
        groupNum, groupId = self._decomposeToSCC()
        # dag[i] = 強連結成分 i から出る辺の行き先の強連結成分の ID
        dag = [[] for _ in range(groupNum)]
        for u, v in self.graphEdges:
            if groupId[u] != groupId[v]:
                dag[groupId[u]].append(groupId[v])
        return dag
