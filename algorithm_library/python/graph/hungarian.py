def hungarian(a):
    """
    二部グラフの最小重み完全マッチング O(n^3) 時間
    正方整数行列 a[i][j] = 左頂点 i と右頂点 j を結ぶ辺の重み, 辺がなければ inf
    完全マッチングなので左頂点と右頂点の数は同じでないといけない
    (最小費用, P) を返す。P[i] = 左頂点 i とマッチした右頂点の番号
    """
    n = len(a)
    v, p = list(map(min, zip(*a))), [-1] * n
    for s in range(n):
        dist = [x - y for x, y in zip(a[s], v)]
        prev = [-1] * n
        rest = list(range(n))
        j = min(rest, key=dist.__getitem__)
        while p[j] >= 0:
            rest.remove(j)
            row = a[p[j]]
            shift = dist[j] - row[j] + v[j]
            last, j = j, rest[0]
            best = dist[j]
            for k in rest:
                d = dist[k]
                x = row[k] - v[k] + shift
                if x < d:
                    dist[k] = d = x
                    prev[k] = last
                if d < best or (d == best and p[k] < 0):
                    best, j = d, k
        end = dist[j]
        for k, d in enumerate(dist):
            if d < end:
                v[k] += d - end
        while prev[j] >= 0:
            k = prev[j]
            p[j], j = p[k], k
        p[j] = s
    ans = [0] * n
    for j, i in enumerate(p):
        ans[i] = j
    return sum(row[j] for row, j in zip(a, ans)), ans
