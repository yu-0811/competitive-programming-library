# 二項係数ライブラリ

# 前計算 O(n + log mod)
# O(1) で nCk, nHk を返す
class Comb:
    def __init__(self, n, mod):
        self.mod = mod
        self.n = n
        size = max(2, n + 1)
        fact = self.fact = [1] * size
        factinv = self.factinv = [1] * size
        inv = self.inv = [0, 1] + [0] * (size - 2)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % mod
        factinv[n] = pow(fact[n], -1, mod)
        for i in range(n, 0, -1):
            factinv[i - 1] = factinv[i] * i % mod
        for i in range(2, n + 1):
            inv[i] = factinv[i] * fact[i - 1] % mod

    def C(self, n, k):  # nCk % modを返す
        assert n <= self.n
        if (k < 0 or n < 0) or (n < k):
            return 0
        if k == 1:
            return n
        k = min(k, n - k)
        return (
            self.fact[n] * self.factinv[k] % self.mod * self.factinv[n - k] % self.mod
        )

    # 重複組合せ nHr % modを返す
    def H(self, n, r):
        return self.C(n + r - 1, r)


# O(k) 前計算
# O(min(k, n-k)) で nCk を計算（n が大きいときでも使える）
class Comb:
    def __init__(self, k, mod):
        self.k = k
        self.mod = mod
        self.fact_inv = [0] * (k + 1)
        self.inv = [0] * (k + 1)
        self.fact_inv[0] = 1
        if k >= 1:
            self.fact_inv[1] = 1
            self.inv[1] = 1

        for i in range(2, k + 1):
            self.inv[i] = mod - self.inv[mod % i] * (mod // i) % mod
            self.fact_inv[i] = self.fact_inv[i - 1] * self.inv[i] % mod

    def nCk(self, n, k):
        if k < 0 or k > n:
            return 0
        k = min(k, n - k)
        if k > self.k:
            raise ValueError("precomputed k is too small")
        mod = self.mod
        ans = 1
        for i in range(k):
            ans = ans * (n - i) % mod
        return ans * self.fact_inv[k] % mod


class PascalsTriangle:
    """
    パスカルの三角形で nCk を求める
    計算量: O(N^2)
    mod が素数でなくても使用可能
    """

    def __init__(self, N, mod):
        self.mod = mod
        self.binom = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            self.binom[i][0] = 1
            for j in range(1, i + 1):
                self.binom[i][j] = (
                    self.binom[i - 1][j - 1] + self.binom[i - 1][j]
                ) % mod

    def C(self, n, k):
        assert 0 <= k <= n
        return self.binom[n][k]

    def H(self, n, k):
        """重複組合せ nHk"""
        assert n >= 0 and k >= 0
        return self.C(n + k - 1, k)
