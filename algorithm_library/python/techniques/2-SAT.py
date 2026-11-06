# n: 変数数
# clause: 要素 (i, f, j, g) は (x[i] == f) or (x[j] == g) 0-indexed
# 満たすT/Fの組があればそれを、なければNoneを返す
def two_sat(n: int, clause: list[tuple[int, bool, int, bool]]) -> list[bool]:
    N = 2 * n
    s = [0] * (N + 1)
    e = []  # 含意の始点を節ごとに2つずつ保存。対の他方を反転すると終点。
    for i, f, j, g in clause:
        a, b = 2 * i + (not f), 2 * j + (not g)
        e.extend((a, b))
        s[a] += 1
        s[b] += 1
    for i in range(N):
        s[i + 1] += s[i]
    to = [0] * len(e)
    for i, v in enumerate(e):
        s[v] -= 1
        to[s[v]] = e[i ^ 1] ^ 1
    d = [-1] * N  # 未訪問: -1、探索中: S 内の位置、確定済み: N 以上
    S, P = [], []  # S: 未確定の頂点、P: 成分の根候補の位置
    k = N
    for r in range(N):
        if d[r] != -1:
            continue
        st = [r]
        while st:
            v = st.pop()
            if v < 0:  # ~v は帰りがけ
                if P[-1] == d[~v]:
                    b = P.pop()
                    while len(S) > b:
                        u = S.pop()
                        d[u] = k
                        if d[u ^ 1] == k:
                            return None
                    k += 1
            elif d[v] == -1:
                d[v] = len(S)
                S.append(v)
                P.append(d[v])
                st.append(~v)
                st.extend(to[s[v]:s[v + 1]])
            else:
                while P[-1] > d[v]:
                    P.pop()
    return [d[2 * i] > d[2 * i + 1] for i in range(n)]