def mos_algorithm(data, que):
    """
    data : list of int : 元の配列
    que : list of tuple : クエリのリスト
    クエリは 0-indexed で半開区間[l,r)
    更新関数には半開区間を渡し、回答の取得はクエリごとに1回だけ行う。
    """
    from math import sqrt, ceil

    n = len(data)
    q = len(que)
    if q == 0:
        return []
    B = max(1, ceil(sqrt(1.5) * n / sqrt(q)))

    # 状態を初期化する処理を書く
    # ans = ?

    def _add(left, right):
        # 区間 [left, right) の要素を追加したときの状態に更新する
        # ans は更新しない
        for i in range(left, right):
            pass
            

    def _del(left, right):
        # [left, right) の要素を削除するしたときの状態に更新する
        for i in range(left, right):
            pass

    shift = q.bit_length()
    lshift = n.bit_length()
    mask = (1 << shift) - 1
    bucs = [[] for _ in range(n // B + 1)]
    for idx, (l, r) in enumerate(que):
        bucs[l // B].append((((r << lshift) | l) << shift) | idx)
    order = []
    for b, buc in enumerate(bucs):
        buc.sort(reverse=bool(b & 1))
        order.extend(buc)

    L = R = 0
    ret = [-1] * q
    for lri in order:
        i = lri & mask
        l, r = que[i]

        if L > l:
            _add(l, L)
        if R < r:
            _add(R, r)
        if L < l:
            _del(L, l)
        if R > r:
            _del(r, R)
        L, R = l, r

        # 更新された状態からクエリの答えを求める
        ret[i] = 

    return ret