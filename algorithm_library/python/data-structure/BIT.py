class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.bit = [[0] * self.n for _ in range(2)]

    def _add_sub(self, p, i, x):
        idx = i
        while idx < self.n:
            self.bit[p][idx] += x
            idx += idx & -idx

    def add(self, l, r, x):  # [l,r)にxを加算
        bit0, bit1 = self.bit
        n = self.n
        c = -x * (l - 1)
        while l < n:
            bit0[l] += c
            bit1[l] += x
            l += l & -l
        c = x * (r - 1)
        while r < n:
            bit0[r] += c
            bit1[r] -= x
            r += r & -r

    def _sum_sub(self, p, i):
        s = 0
        idx = i
        while idx > 0:
            s += self.bit[p][idx]
            idx -= idx & -idx
        return s

    def SUM(self, i):
        bit0, bit1 = self.bit
        s0 = s1 = 0
        idx = i
        while idx > 0:
            s0 += bit0[idx]
            s1 += bit1[idx]
            idx -= idx & -idx
        return s0 + s1 * i

    # 任意の区間[l,r)の区間をを取得
    def range_sum(self, l, r):
        return self.SUM(r - 1) - self.SUM(l - 1)

    # a_1 + a_2 + ... + a_x >= w となる最小の x を O(log n) で求める
    # 各要素は非負であること。w <= 0 なら 0、見つからなければ要素数 + 1
    def lower_bound(self, w):
        if w <= 0:
            return 0

        bit0, bit1 = self.bit
        n = self.n
        x = s0 = s1 = 0
        step = 1 << (n.bit_length() - 1)
        while step:
            nxt = x + step
            if nxt < n:
                t0 = s0 + bit0[nxt]
                t1 = s1 + bit1[nxt]
                # SUM(nxt) を2本のBITの累積値から復元する
                if t0 + t1 * nxt < w:
                    x, s0, s1 = nxt, t0, t1
            step >>= 1
        return x + 1
