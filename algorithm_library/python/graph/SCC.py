class SCC:
    def __init__(self, N: int):
        self.N = N  # 頂点数
        self.edges = []  # 辺

    def addEdge(self, frm: int, to: int):
        assert 0 <= frm <= self.N
        assert 0 <= to <= self.N
        self.edges.append((frm, to))

    # 辺を CSR 形式にする
    def _csr(self, N: int, edges: list[tuple]):
        start = [0] * (N + 1)
        # dst := 辺を始点の昇順にソートした時の終点のリスト
        dst = [0] * len(edges)

        # start[i+1] := 頂点 i を始点とする辺の数 となるように構築
        for u, _ in edges:  # u を始点とする辺
            start[u + 1] += 1
        for i in range(1, N + 1):
            start[i] += start[i - 1]

        # pos[i] := 始点を i とする辺の dst への挿入位置
        pos = start[:]
        for u, v in edges:
            dst[pos[u]] = v
            pos[u] += 1

        return start, dst

    # ids=True なら成分ID、False なら成分ごとの頂点リストを計算する
    def _scc(self, ids=False):
        N = self.N
        start, dst = self._csr(N, self.edges)
        order = [-1] * N  # 未訪問: -1、探索中: active 内の位置、確定済み: N
        result = [0] * N if ids else []
        active = []  # 探索済みかつ所属成分が未確定の頂点
        roots = []  # 強連結成分の根候補の active 内の位置
        count = 0
        for root in range(N):
            if order[root] != -1:
                continue
            stack = [root]
            while stack:
                v = stack.pop()
                if v < 0:  # ~v は帰りがけの処理
                    v = ~v
                    if roots[-1] == order[v]:
                        begin = roots.pop()
                        group = active[begin:]
                        del active[begin:]
                        for u in group:
                            order[u] = N
                            if ids:
                                result[u] = count
                        if not ids:
                            result.append(group)
                        count += 1
                elif order[v] == -1:
                    order[v] = len(active)
                    active.append(v)
                    roots.append(order[v])
                    stack.append(~v)
                    stack.extend(dst[start[v]:start[v + 1]])
                else:
                    while roots[-1] > order[v]:
                        roots.pop()
        return count, result

    # groups[i] = グループID i に属する頂点の集合を 返す
    def build_scc(self) -> list[list[int]]:
        return self._scc()[1][::-1]

    # 強連結成分分解後のグラフを構築する(同一の強連結成分内の頂点は縮約)
    def build_dag(self) -> list[list[int]]:
        # comp[i] = 頂点 i が属する強連結成分の ID
        count, comp = self._scc(True)
        comp = [count - 1 - c for c in comp]
        # dag[i] = 強連結成分 i から出る辺の行き先の強連結成分の ID
        dag = [[] for _ in range(count)]
        for u, v in self.edges:
            if comp[u] != comp[v]:
                dag[comp[u]].append(comp[v])
        return dag
