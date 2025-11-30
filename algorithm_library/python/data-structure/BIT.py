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
        self._add_sub(0, l, -x * (l - 1))
        self._add_sub(0, r, x * (r - 1))
        self._add_sub(1, l, x)
        self._add_sub(1, r, -x)

    def _sum_sub(self, p, i):
        s = 0
        idx = i
        while idx > 0:
            s += self.bit[p][idx]
            idx -= idx & -idx
        return s

    def SUM(self, i):
        return self._sum_sub(0, i) + self._sum_sub(1, i) * i

    # 任意の区間[l,r)の区間をを取得
    def range_sum(self, l, r):
        return self.SUM(r - 1) - self.SUM(l - 1)

    # 二分探索
    ## a_1 + a_2 + ... + a_x >= w となる最小の x を求める
    def lower_bound(self, w):
        if w <= 0:
            return 0
        else:
            x, LEN = 0, 1
            # 最大の区間長を LEN に入れる
            while LEN < self.size:
                LEN <<= 1
            while LEN > 0:
                # 区間[x+1,x+LEN]が w 以下のとき = 採用する時
                if x + LEN < self.size and self.tree[x + LEN] < w:
                    w -= self.tree[x + LEN]
                    x += LEN
                LEN >>= 1

        return x + 1
