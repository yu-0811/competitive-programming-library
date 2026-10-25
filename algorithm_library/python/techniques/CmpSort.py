def cmp_sort(a: list, cmp) -> list:
    """比較関数 cmp に従ってリスト a を破壊的に安定ソートする。

    cmp(x, y) は x が先なら負、同順位なら 0、後なら正を返す。
    比較結果は一貫した順序を定めること。並べ替えた同じリスト a を返す。
    時間 O(n log n)、追加領域 O(n)。整列済み・狭義逆順なら O(n)。
    PyPy 向けに比較関数を直接呼び出す、非再帰の自然マージソート。
    """
    n = len(a)
    if n < 2:
        return a

    # 単調な区間 (run) を見つけ、短い run は二分挿入で長さ 16 まで延ばす。
    ends = []
    start = 0
    while start < n:
        end = start + 1
        if end < n:
            if cmp(a[end], a[start]) < 0:
                end += 1
                while end < n and cmp(a[end], a[end - 1]) < 0:
                    end += 1
                # 同順位を含む区間は反転しない (安定性を保つ)。
                left, right = start, end - 1
                while left < right:
                    a[left], a[right] = a[right], a[left]
                    left += 1
                    right -= 1
            else:
                end += 1
                while end < n and cmp(a[end], a[end - 1]) >= 0:
                    end += 1

        stop = min(n, start + 16)
        for i in range(end, stop):
            value = a[i]
            lo, hi = start, i
            while lo < hi:
                mid = (lo + hi) // 2
                if cmp(value, a[mid]) < 0:
                    hi = mid
                else:
                    lo = mid + 1
            j = i
            while j > lo:
                a[j] = a[j - 1]
                j -= 1
            a[lo] = value
        end = max(end, stop)
        ends.append(end)
        start = end

    # 隣接する run を組にしてマージ。左側だけ退避し、右側の残りは動かさない。
    while len(ends) > 1:
        new_ends = []
        start = 0
        for r in range(0, len(ends) - 1, 2):
            mid, end = ends[r], ends[r + 1]
            if cmp(a[mid - 1], a[mid]) > 0:
                left = a[start:mid]
                size = len(left)
                i, j, k = 0, mid, start
                while i < size and j < end:
                    if cmp(left[i], a[j]) <= 0:
                        a[k] = left[i]
                        i += 1
                    else:
                        a[k] = a[j]
                        j += 1
                    k += 1
                if i < size:
                    a[k:j] = left[i:]
            new_ends.append(end)
            start = end
        if len(ends) & 1:
            new_ends.append(n)
        ends = new_ends
    return a
