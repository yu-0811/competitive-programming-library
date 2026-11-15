# LazySegtree.py を写経済みの場合の変更手順:
# 1. data と lazy に使う成分数の Columns クラスを追加する（同じなら1つでよい）。
# 2. __init__ と _push 全体を、下のものに差し替える。
# 3. apply 内の「変更」と付けた行を反映する。
# ほかのメソッドはそのまま使える。
# 呼び出し: lazy_segtree(v, op, e, mp, comp, ide, Columns2, Columns2)
# Columns は取得のたびにタプルを作るため、ide との is 比較は使わず pend で管理する。


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


class TupleLazySegtree:
    # 変更: __init__ 全体を差し替える。
    # columns は data 用、lazy_columns は lazy 用のクラスを直接指定する。
    def __init__(s, v, op, e, mp, comp, ide, columns, lazy_columns):
        s.n = len(v)
        s.log = (max(1, s.n) - 1).bit_length()
        z = s.z = 1 << s.log
        s.e = e = tuple(e)
        s.ide = ide = tuple(ide)
        s.op = op
        s.mp = mp
        s.comp = comp
        d = s.d = columns(2 * z, e)  # data のリストを Columns に置き換える
        s.lz = lazy_columns(z, ide)  # lazy のリストを Columns に置き換える
        s.pend = [False] * z  # 各内部ノードに未伝播のタグがあるか
        for i, value in enumerate(v, z):  # Columns はスライス代入できないので1点ずつ
            d[i] = value
        for i in range(z - 1, 0, -1):
            d[i] = op(d[2 * i], d[2 * i + 1])

    # 変更: _push 全体を差し替える。タグの有無は pend で判定する。
    def _push(s, k):
        pend = s.pend
        if not pend[k]:
            return
        d, lz, mp, comp = s.d, s.lz, s.mp, s.comp
        f = lz[k]
        c = 2 * k
        d[c] = mp(f, d[c])
        d[c + 1] = mp(f, d[c + 1])
        if c < s.z:
            lz[c] = comp(f, lz[c]) if pend[c] else f
            lz[c + 1] = comp(f, lz[c + 1]) if pend[c + 1] else f
            pend[c] = pend[c + 1] = True
        pend[k] = False

    def set(s, p, x):
        """p 番目の値をタプル x に更新する。"""
        assert 0 <= p < s.n
        d, op, push = s.d, s.op, s._push
        p += s.z
        for i in range(s.log, 0, -1):
            push(p >> i)
        d[p] = x
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    def get(s, p):
        assert 0 <= p < s.n
        push = s._push
        p += s.z
        for i in range(s.log, 0, -1):
            push(p >> i)
        return s.d[p]

    def prod(s, l, r):
        assert 0 <= l <= r <= s.n
        if l == r:
            return s.e
        d, op, push = s.d, s.op, s._push
        l += s.z
        r += s.z
        left = (l & -l).bit_length()
        right = (r & -r).bit_length()
        for i in range(s.log, 0, -1):
            if i >= left:
                push(l >> i)
            if i >= right:
                push(r >> i)
        sml = smr = s.e
        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)

    def all_prod(s):
        return s.d[1]

    def apply_point(s, p, f):
        assert 0 <= p < s.n
        d, op, push = s.d, s.op, s._push
        p += s.z
        for i in range(s.log, 0, -1):
            push(p >> i)
        d[p] = s.mp(f, d[p])
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    def apply(s, l, r, f):
        assert 0 <= l <= r <= s.n
        if l == r:
            return
        d, lz, pend = s.d, s.lz, s.pend  # 変更: pend を追加
        op, mp, comp = s.op, s.mp, s.comp
        push, z = s._push, s.z
        l += z
        r += z
        left = (l & -l).bit_length()
        right = (r & -r).bit_length()
        for i in range(s.log, 0, -1):
            if i >= left:
                push(l >> i)
            if i >= right:
                push(r >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                d[l] = mp(f, d[l])
                if l < z:
                    lz[l] = comp(f, lz[l]) if pend[l] else f  # 変更: タグがなければ f を代入
                    pend[l] = True  # 変更: この行を追加
                l += 1
            if r & 1:
                r -= 1
                d[r] = mp(f, d[r])
                if r < z:
                    lz[r] = comp(f, lz[r]) if pend[r] else f  # 変更: タグがなければ f を代入
                    pend[r] = True  # 変更: この行を追加
            l >>= 1
            r >>= 1
        for i in range(1, s.log + 1):
            if i >= left:
                k = l2 >> i
                d[k] = op(d[2 * k], d[2 * k + 1])
            if i >= right:
                k = r2 >> i
                d[k] = op(d[2 * k], d[2 * k + 1])

    def max_right(s, l, check):
        """check(prod(l, r)) を満たす最大の r。check(e) が真で単調であること。"""
        assert 0 <= l <= s.n
        assert check(s.e)
        if l == s.n:
            return s.n
        d, op, push = s.d, s.op, s._push
        z = s.z
        l += z
        for i in range(s.log, 0, -1):
            push(l >> i)
        sm = s.e
        while True:
            while l % 2 == 0:
                l >>= 1
            nxt = op(sm, d[l])
            if not check(nxt):
                while l < z:
                    push(l)
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
        d, op, push = s.d, s.op, s._push
        z = s.z
        r += z
        for i in range(s.log, 0, -1):
            push((r - 1) >> i)
        sm = s.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            nxt = op(d[r], sm)
            if not check(nxt):
                while r < z:
                    push(r)
                    r = 2 * r + 1
                    nxt = op(d[r], sm)
                    if check(nxt):
                        sm = nxt
                        r -= 1
                return r + 1 - z
            sm = nxt
            if (r & -r) == r:
                return 0

    def __str__(s):
        return str([s.get(i) for i in range(s.n)])
