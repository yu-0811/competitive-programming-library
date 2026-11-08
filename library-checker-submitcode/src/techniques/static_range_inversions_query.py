# problem: https://judge.yosupo.jp/problem/static_range_inversions_query
# include: algorithm_library/python/data_structure/BIT.py
# include: algorithm_library/python/techniques/Compression.py


def mos_inversions(data, que):
    """Mos_algorithm.py のテンプレートを区間転倒数用に具体化する。"""
    from math import ceil, sqrt

    n = len(data)
    q = len(que)
    if q == 0:
        return []
    B = max(1, ceil(sqrt(1.5) * n / sqrt(q)))

    data = compression(data)
    bit = fenwick_tree(max(data) + 1 if data else 0)
    add = bit.add
    prefix = bit.sum0
    inversions = size = 0

    # 左端では自分より小さい要素、右端では自分より大きい要素を数える。
    def add_left(left, right):
        nonlocal inversions, size
        for i in range(right - 1, left - 1, -1):
            x = data[i]
            inversions += prefix(x)
            add(x, 1)
            size += 1

    def add_right(left, right):
        nonlocal inversions, size
        for i in range(left, right):
            x = data[i]
            inversions += size - prefix(x + 1)
            add(x, 1)
            size += 1

    def del_left(left, right):
        nonlocal inversions, size
        for i in range(left, right):
            x = data[i]
            inversions -= prefix(x)
            add(x, -1)
            size -= 1

    def del_right(left, right):
        nonlocal inversions, size
        for i in range(right - 1, left - 1, -1):
            x = data[i]
            inversions -= size - prefix(x + 1)
            add(x, -1)
            size -= 1

    # ライブラリのテンプレートと同じブロック幅・整数パック・蛇行順。
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
            add_left(l, L)
        if R < r:
            add_right(R, r)
        if L < l:
            del_left(L, l)
        if R > r:
            del_right(r, R)
        L, R = l, r
        ret[i] = inversions
    return ret


def main():
    N, Q = map(int, readline().split())
    data = list(map(int, readline().split()))
    que = [tuple(map(int, readline().split())) for _ in range(Q)]
    ans = mos_inversions(data, que)
    sys.stdout.write("\n".join(map(str, ans)) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
