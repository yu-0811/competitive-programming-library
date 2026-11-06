def cmp_sort(a, cmp):
    """比較関数 cmp に従ってリスト a を破壊的に安定ソートする。
    時間 O(n log n)、追加領域 O(n)。整列済み・狭義逆順なら O(n)。
    """
    n = len(a)
    # 全体が昇順または狭義降順なら O(n) で終了する。
    if n > 1:
        d = cmp(a[0], a[1]) > 0
        r = 2
        while r < n and (cmp(a[r - 1], a[r]) > 0) == d:
            r += 1
        if r == n:
            if d:
                a.reverse()
            return a

    # 幅 w の整列済み区間を隣同士でマージする。
    w = 1
    while w < n:
        for l in range(0, n - w, 2 * w):
            m, r = l + w, min(l + 2 * w, n)
            if cmp(a[m - 1], a[m]) <= 0:
                continue
            b = a[l:m]  # 左側だけ退避する。長さは常に w。
            i, j, k = 0, m, l
            while i < w and j < r:
                if cmp(b[i], a[j]) <= 0:
                    a[k] = b[i]
                    i += 1
                else:
                    a[k] = a[j]
                    j += 1
                k += 1
            a[k:j] = b[i:]
        w *= 2
    return a
