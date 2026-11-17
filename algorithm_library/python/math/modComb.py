# 二項係数ライブラリ

# 前計算 O(n + log mod)
# O(1) で nCk, nHk を返す
class Comb:
    def __init__(self, n, mod):
        self.mod = mod
        fact = self.fact = [1] * (n + 1)
        factinv = self.factinv = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % mod
        factinv[n] = pow(fact[n], -1, mod)
        for i in range(n, 0, -1):
            factinv[i - 1] = factinv[i] * i % mod

    def C(self, n, k):  # nCk % modを返す（n <= 前計算の上限）
        if not 0 <= k <= n:
            return 0
        mod = self.mod
        return self.fact[n] * self.factinv[k] % mod * self.factinv[n - k] % mod

    # 重複組合せ nHr % modを返す
    def H(self, n, r):
        return self.C(n + r - 1, r) if n else int(r == 0)


# O(k + log mod) 前計算
# O(min(k, n-k)) で nCk を計算（n が大きいときでも使える）
class Comb:
    def __init__(self, k, mod):
        self.mod = mod
        f = self.fact_inv = [1] * (k + 1)
        for i in range(2, k + 1):
            f[i] = f[i - 1] * i % mod
        f[k] = pow(f[k], -1, mod)
        for i in range(k, 0, -1):
            f[i - 1] = f[i] * i % mod

    def nCk(self, n, k):  # min(k, n-k) <= 前計算の上限
        if not 0 <= k <= n:
            return 0
        k = min(k, n - k)
        mod = self.mod
        ans = self.fact_inv[k]
        n %= mod
        if n < k:
            return 0
        for i in range(k):
            ans = ans * (n - i) % mod
        return ans


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
