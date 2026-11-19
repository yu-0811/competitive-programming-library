class RangeAddBIT:
    def __init__(s, n):
        s.n = n
        s.bit = [[0] * s.n for _ in range(2)]

    # 初期配列 a から O(n) で構築する場合は __init__ をこちらに差し替える。
    # def __init__(s, a):
    #     n = s.n = len(a)
    #     b0, b1 = s.bit = [[0] * n, [0] * n]
    #     p = 0
    #     for i, x in enumerate(a):
    #         d = x - p
    #         p = x
    #         b0[i] -= i * d
    #         b1[i] += d
    #         j = i | (i + 1)
    #         if j < n:
    #             b0[j] += b0[i]
    #             b1[j] += b1[i]

    def add(s, l, r, x):  # [l,r)にxを加算
        b0, b1 = s.bit
        n = s.n
        c = -x * l
        while l < n:
            b0[l] += c
            b1[l] += x
            l |= l + 1
        c = x * r
        while r < n:
            b0[r] += c
            b1[r] -= x
            r |= r + 1

    # 区間 [0, i) の和を取得
    def _sum(s, i):
        b0, b1 = s.bit
        s0 = s1 = 0
        idx = i - 1
        while idx >= 0:
            s0 += b0[idx]
            s1 += b1[idx]
            idx = (idx & (idx + 1)) - 1
        return s0 + s1 * i

    # 区間 [l, r) の和を取得
    def sum(s, l, r):
        return s._sum(r) - s._sum(l)

    # a[0] + ... + a[x] >= w となる最小の x を O(log n) で求める
    # 各要素は非負であること。w <= 0 なら 0、見つからなければ n
    def lower_bound(s, w):
        if w <= 0:
            return 0

        b0, b1 = s.bit
        n = s.n
        x = -1
        s0 = s1 = 0
        step = 1 << n.bit_length()
        while step:
            nxt = x + step
            if nxt < n:
                t0 = s0 + b0[nxt]
                t1 = s1 + b1[nxt]
                # _sum(nxt + 1) を2本のBITの累積値から復元する
                if t0 + t1 * (nxt + 1) < w:
                    x, s0, s1 = nxt, t0, t1
            step >>= 1
        return x + 1


class BIT:
    def __init__(s, a):
        d = s.d = a
        n = s.n = len(d)
        for i in range(n):
            j = i | (i + 1)
            if j < n:
                d[j] += d[i]

    def add(s, p, x):
        assert 0 <= p < s.n
        d = s.d
        while p < s.n:
            d[p] += x
            p |= p + 1

    def sum0(s, r):
        res = 0
        while r:
            res += s.d[r - 1]
            r &= r - 1
        return res

    def sum(s, l, r):
        assert 0 <= l <= r <= s.n
        return s.sum0(r) - s.sum0(l)
