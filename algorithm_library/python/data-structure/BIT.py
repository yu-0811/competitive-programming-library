class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [[0] * self.n for _ in range(2)]

    def add(self, l, r, x):  # [l,r)にxを加算
        bit0, bit1 = self.bit
        n = self.n
        c = -x * l
        while l < n:
            bit0[l] += c
            bit1[l] += x
            l |= l + 1
        c = x * r
        while r < n:
            bit0[r] += c
            bit1[r] -= x
            r |= r + 1

    # 区間 [0, i) の和を取得
    def SUM(self, i):
        bit0, bit1 = self.bit
        s0 = s1 = 0
        idx = i - 1
        while idx >= 0:
            s0 += bit0[idx]
            s1 += bit1[idx]
            idx = (idx & (idx + 1)) - 1
        return s0 + s1 * i

    # 区間 [l, r) の和を取得
    def range_sum(self, l, r):
        return self.SUM(r) - self.SUM(l)

    # a[0] + ... + a[x] >= w となる最小の x を O(log n) で求める
    # 各要素は非負であること。w <= 0 なら 0、見つからなければ n
    def lower_bound(self, w):
        if w <= 0:
            return 0

        bit0, bit1 = self.bit
        n = self.n
        x = -1
        s0 = s1 = 0
        step = 1 << n.bit_length()
        while step:
            nxt = x + step
            if nxt < n:
                t0 = s0 + bit0[nxt]
                t1 = s1 + bit1[nxt]
                # SUM(nxt + 1) を2本のBITの累積値から復元する
                if t0 + t1 * (nxt + 1) < w:
                    x, s0, s1 = nxt, t0, t1
            step >>= 1
        return x + 1
