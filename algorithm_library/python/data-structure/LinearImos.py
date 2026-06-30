# 区間 [l,r] に i \in [l,r] に一次関数 a*i + b を加算できるライブラリ
class LinearImos:
    def __init__(self, n, mod=None):
        self.n = n
        self.mod = mod
        self.coef = [0] * (n + 1)  # i の係数
        self.cons = [0] * (n + 1)  # 定数項

    def add_linear(self, l, r, a, b):
        """
        閉区間 [l, r] に a*i + b を加算する
        """
        if l > r:
            return

        if self.mod is None:
            self.coef[l] += a
            self.coef[r + 1] -= a
            self.cons[l] += b
            self.cons[r + 1] -= b
        else:
            mod = self.mod
            self.coef[l] = (self.coef[l] + a) % mod
            self.coef[r + 1] = (self.coef[r + 1] - a) % mod
            self.cons[l] = (self.cons[l] + b) % mod
            self.cons[r + 1] = (self.cons[r + 1] - b) % mod

    def add_arithmetic(self, l, r, start, diff):
        """
        初項 start 公差 diff の等差数列を [l,r] に足す
        閉区間 [l, r] に
        start, start+diff, start+2*diff, ...
        を加算する

        位置 i に足す値は
        start + diff*(i-l)
        = diff*i + (start - diff*l)
        """
        a = diff
        b = start - diff * l
        self.add_linear(l, r, a, b)

    def build(self):
        res = [0] * self.n
        c = 0
        s = 0

        if self.mod is None:
            for i in range(self.n):
                c += self.coef[i]
                s += self.cons[i]
                res[i] = c * i + s
        else:
            mod = self.mod
            for i in range(self.n):
                c = (c + self.coef[i]) % mod
                s = (s + self.cons[i]) % mod
                res[i] = (c * i + s) % mod

        return res