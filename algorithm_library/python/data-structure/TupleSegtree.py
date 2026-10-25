class Columns2:
    __slots__ = ("a", "b")

    def __init__(s, n, e):
        s.a = [e[0]] * n
        s.b = [e[1]] * n

    def __getitem__(s, i):
        return s.a[i], s.b[i]

    def __setitem__(s, i, x):
        s.a[i], s.b[i] = x


class Columns3:
    __slots__ = ("a", "b", "c")

    def __init__(s, n, e):
        s.a = [e[0]] * n
        s.b = [e[1]] * n
        s.c = [e[2]] * n

    def __getitem__(s, i):
        return s.a[i], s.b[i], s.c[i]

    def __setitem__(s, i, x):
        s.a[i], s.b[i], s.c[i] = x


# 4成分以上は同じ形のクラスを用意し、この辞書に追加する。
COLUMN_TYPES = {2: Columns2, 3: Columns3}


class TupleSegtree:  # すべて 0-index
    # タプルをそのまま載せるだけでいい
    def __init__(s, v, op, e):
        s.n = len(v)
        z = s.z = 1 << (max(1, s.n) - 1).bit_length()
        s.e = e = tuple(e)
        s.op = op
        assert len(e) in COLUMN_TYPES
        d = s.d = COLUMN_TYPES[len(e)](2 * z, e)
        for i, value in enumerate(v, z):
            d[i] = value
        for i in range(z - 1, 0, -1):
            d[i] = op(d[2 * i], d[2 * i + 1])

    # 1 点更新
    def set(s, p, x):
        assert 0 <= p < s.n
        d, op = s.d, s.op
        p += s.z
        d[p] = x
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    # 1 点加算（タプルの成分ごとに加算）
    def add(s, p, x):
        assert 0 <= p < s.n
        assert len(x) == len(s.e)
        d, op = s.d, s.op
        p += s.z
        d[p] = tuple(a + b for a, b in zip(d[p], x))
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    # 元の配列の p 番目の要素を取得
    def get(s, p):
        assert 0 <= p < s.n
        return s.d[p + s.z]

    # [l,r) の演算結果を返す
    def prod(s, l, r):
        assert 0 <= l <= r <= s.n
        if l == r:
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

    def max_right(s, l, check):
        """check(prod(l, r)) を満たす最大の r。check(e) が真で単調であること。"""
        assert 0 <= l <= s.n
        assert check(s.e)
        if l == s.n:
            return s.n
        d, op, z = s.d, s.op, s.z
        l += z
        sm = s.e
        while True:
            while l % 2 == 0:
                l >>= 1
            nxt = op(sm, d[l])
            if not check(nxt):
                while l < z:
                    l *= 2
                    nxt = op(sm, d[l])
                    if check(nxt):
                        sm = nxt
                        l += 1
                return l - z
            sm = nxt
            l += 1
            if (l & -l) == l:
                return s.n

    def min_left(s, r, check):
        """check(prod(l, r)) を満たす最小の l。check(e) が真で単調であること。"""
        assert 0 <= r <= s.n
        assert check(s.e)
        if r == 0:
            return 0
        d, op, z = s.d, s.op, s.z
        r += z
        sm = s.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            nxt = op(d[r], sm)
            if not check(nxt):
                while r < z:
                    r = 2 * r + 1
                    nxt = op(d[r], sm)
                    if check(nxt):
                        sm = nxt
                        r -= 1
                return r + 1 - z
            sm = nxt
            if (r & -r) == r:
                return 0

    # print(seg) で葉の値（元の配列）を表示する
    def __str__(s):
        return str([s.get(i) for i in range(s.n)])
