# edges は (始点, 終点) のリスト
# 返り値: groups, dag
# groups[i] は成分 i の頂点リスト、dag[i] は成分 i から出る辺の行き先。
def scc_dag(n, edges):
    start = [0] * (n + 1)
    for u, _ in edges:
        start[u] += 1
    for u in range(n):
        start[u + 1] += start[u]
    to = [0] * len(edges)
    # 各頂点の辺を後ろから格納すると start が開始位置になる。
    for u, v in reversed(edges):
        start[u] -= 1
        to[start[u]] = v

    pos = [-1] * n  # 未訪問は -1、探索中は active 内の位置、確定済みは n 以上
    # roots には成分の根候補の active 内の位置を積む。
    active, roots, groups = [], [], []
    k = n
    for r in range(n):
        if pos[r] >= 0:
            continue
        if start[r] == start[r + 1]:
            pos[r] = k
            k += 1
            groups.append([r])
            continue
        st = [r]
        while st:
            v = st.pop()
            if v < 0:  # ~v は帰りがけ
                v = ~v
                if roots[-1] == pos[v]:
                    i = roots.pop()
                    group = active[i:]
                    del active[i:]
                    for u in group:
                        pos[u] = k
                    k += 1
                    groups.append(group)
            elif pos[v] == -1:
                p = pos[v] = len(active)
                active.append(v)
                roots.append(p)
                st.append(~v)
                st.extend(to[start[v]:start[v + 1]])
            else:
                p = pos[v]
                while roots[-1] > p:
                    roots.pop()
    groups.reverse()
    dag = [[] for _ in range(k - n)]
    # 確定順の番号を反転し、groups と同じトポロジカル順にする。
    last = k - 1
    if len(dag) > 1:
        for u, v in edges:
            a, b = pos[u], pos[v]
            if a != b:
                dag[last - a].append(last - b)
    return groups, dag
