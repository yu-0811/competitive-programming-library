from array import array


def hopcroft_karp(g, m):
    # g[u] は左頂点 u の隣接先。右頂点は 0 以上 m 未満。
    # 左頂点ごとの相手を返す。未マッチは -1。
    n = len(g)
    neg, zero = array("i", [-1]), array("i", [0])
    left, right = neg * n, neg * m
    end = zero * (m + 1)
    for row in g:
        for v in row:
            end[v] += 1
    size = 0
    for v in range(m):
        end[v], size = size, size + end[v]
    rev = zero * size
    for u, row in enumerate(g):
        for v in row:
            rev[end[v]] = u
            end[v] += 1
    free = [u for u in range(n) if g[u]]
    src = [v for v in range(m) if end[v - 1] < end[v]]

    def augment(s):
        stack = [(s, iter(g[s]))]
        while stack:
            u, it = stack[-1]
            d = dist[u] - 1
            for v in it:
                w = right[v]
                if dist[w] != d:
                    continue
                if w == -1:
                    for x, _ in reversed(stack):
                        right[v], left[x], v = x, v, left[x]
                    return True
                stack.append((w, iter(g[w])))
                break
            else:
                dist[u] = -1
                stack.pop()
        return False

    while free:
        dist = neg * n + zero
        src = [v for v in src if right[v] < 0]
        que = src
        d = 1
        while que:
            nxt = []
            for v in que:
                for k in range(end[v - 1], end[v]):
                    u = rev[k]
                    if dist[u] < 0:
                        dist[u] = d
                        w = left[u]
                        if w >= 0:
                            nxt.append(w)
            que = nxt
            d += 1
        free = [u for u in free if dist[u] > 0 and not augment(u)]
    return list(left)
