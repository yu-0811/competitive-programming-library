def mos_algorithm(data, que):
    """
    data : list of int : 元の配列
    que : list of tuple : クエリのリスト
    クエリは 0-indexed で半開区間[l,r)
    更新関数には半開区間を渡し、回答の取得はクエリごとに1回だけ行う。
    左右の追加・削除を別々に定義し、各要素を端から順に処理する。
    """
    from math import sqrt, ceil

    n = len(data)
    q = len(que)
    if q == 0:
        return []
    B = max(1, ceil(sqrt(1.5) * n / sqrt(q)))

    # 状態を初期化する処理を書く
    # ans = ?

    def _add_left(left, right):
        # 左端に [left, right) を追加する（右から左の順）
        for i in range(right - 1, left - 1, -1):
            pass

    def _add_right(left, right):
        # 右端に [left, right) を追加する（左から右の順）
        for i in range(left, right):
            pass

    def _del_left(left, right):
        # 左端の [left, right) を削除する（左から右の順）
        for i in range(left, right):
            pass

    def _del_right(left, right):
        # 右端の [left, right) を削除する（右から左の順）
        for i in range(right - 1, left - 1, -1):
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
            _add_left(l, L)
        if R < r:
            _add_right(R, r)
        if L < l:
            _del_left(L, l)
        if R > r:
            _del_right(r, R)
        L, R = l, r

        # 更新された状態からクエリの答えを求める
        ret[i] = 

    return ret
