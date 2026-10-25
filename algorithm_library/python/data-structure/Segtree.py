from warnings import warn


class segtree:  # すべて 0-index
    def __init__(s, v, op, e):
        s.n = len(v)
        s.op = op
        s.e = e
        s.z = 1 << (s.n - 1).bit_length()
        d = s.d = [e] * (2 * s.z)
        d[s.z : s.z + s.n] = v
        for i in range(s.z - 1, 0, -1):
            d[i] = op(d[2 * i], d[2 * i + 1])

    # 1 点更新
    def set(s, p, x):
        assert 0 <= p and p < s.n
        d, op = s.d, s.op
        p += s.z
        d[p] = x
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    # 1 点加算
    def add(s, p, x):
        assert 0 <= p and p < s.n
        d, op = s.d, s.op
        p += s.z
        d[p] += x
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    # 元の配列の p 番目の要素を取得
    def get(s, p):
        assert 0 <= p and p < s.n
        return s.d[p + s.z]

    # [l,r) の演算結果を返す
    def prod(s, l, r):
        assert 0 <= l and l <= r and r <= s.n
        if l == r:
            warn("l=r in prod(l,r)")
            return s.e
        d, op = s.d, s.op
        sml = smr = s.e
        l += s.z
        r += s.z
        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)

    # 全区間の演算結果を返す
    def all_prod(s):
        return s.d[1]

    # check(operate(data[l],data[l+1],...,data[r-1])) = True
    # を満たす最大の r を返す
    def max_right(s, l, check):
        assert 0 <= l and l <= s.n
        assert check(s.e)
        if l == s.n:
            return s.n
        l += s.z
        sm = s.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not (check(s.op(sm, s.d[l]))):
                while l < s.z:
                    l = 2 * l
                    if check(s.op(sm, s.d[l])):
                        sm = s.op(sm, s.d[l])
                        l += 1
                return l - s.z
            sm = s.op(sm, s.d[l])
            l += 1
            if (l & -l) == l:
                break
        return s.n

    # check(operate(data[l],data[l+1],...,data[r-1])) = True
    # を満たす最小の l を返す
    def min_left(s, r, check):
        assert 0 <= r and r <= s.n
        assert check(s.e)
        if r == 0:
            return 0
        r += s.z
        sm = s.e
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (check(s.op(s.d[r], sm))):
                while r < s.z:
                    r = 2 * r + 1
                    if check(s.op(s.d[r], sm)):
                        sm = s.op(s.d[r], sm)
                        r -= 1
                return r + 1 - s.z
            sm = s.op(s.d[r], sm)
            if (r & -r) == r:
                break
        return 0

    # print(seg) で葉の値（元の配列）を表示する
    def __str__(s):
        return str([s.get(i) for i in range(s.n)])
