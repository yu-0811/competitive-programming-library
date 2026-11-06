from algorithm_library.python.data_structure.Segtree import segtree


class changeable_RollingHash:
    def __init__(self, S, base=1237, mod=(1 << 61) - 1):
        N = len(S)
        self.N = N
        self.ord_base = ord("a")
        self.base = base
        self.mod = mod
        self.base_pow = [1] * (N + 1)
        self.base_inv = [1] * (N + 1)
        self.inv = pow(base, mod - 2, mod)
        for i in range(N):
            self.base_pow[i + 1] = (self.base_pow[i] * base) % mod
            self.base_inv[i + 1] = (self.base_inv[i] * self.inv) % mod
        hash = [
            ((ord(s) - self.ord_base + 1) * self.base_pow[N - idx - 1]) % mod
            for idx, s in enumerate(S)
        ]
        e = 0

        def operate(a, b):
            return (a + b) % mod

        self.seg = segtree(hash, operate, e)

    # インデックス x の要素を c に変える
    def change(self, x, c):
        self.seg.set(
            x, ((ord(c) - self.ord_base + 1) * self.base_pow[self.N - x - 1]) % self.mod
        )

    def get_hash(self, l, r):  # [l, r),0-index
        return (self.seg.prod(l, r) * self.base_inv[self.N - r]) % self.mod
