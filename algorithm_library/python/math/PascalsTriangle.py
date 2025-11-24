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
                self.binom[i][j] = (self.binom[i - 1][j - 1] + self.binom[i - 1][j]) % mod

    def C(self, n, k):
        assert 0 <= k <= n
        return self.binom[n][k]

    def H(self, n, k):
        """ 重複組合せ nHk """
        assert n >= 0 and k >= 0
        return self.C(n + k - 1, k)