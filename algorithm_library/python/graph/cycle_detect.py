def cycle_detect(n, edges):
    """無向グラフの閉路を (頂点列, 辺 ID 列) で返す。なければ ([], [])。

    頂点は 0-indexed、辺 ID は edges 内の位置。自己ループ・多重辺に対応。
    時間・空間計算量 O(n + m)。
    """
    g = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i))
        g[v].append((u, i))
    pos = [-1] * n
    for r in range(n):
        if pos[r] != -1:
            continue
        vs, es = [r], [-1]
        pos[r] = 0
        while vs:
            v = vs[-1]
            if not g[v]:
                pos[v] = -2
                vs.pop()
                es.pop()
                continue
            u, i = g[v].pop()
            if i == es[-1]:
                continue
            if pos[u] >= 0:
                return vs[pos[u]:], es[pos[u] + 1:] + [i]
            if pos[u] == -1:
                pos[u] = len(vs)
                vs.append(u)
                es.append(i)
    return [], []
