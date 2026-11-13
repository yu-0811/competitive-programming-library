# 約数系包除に使うやつ系


class PIE:
    def __init__(self, MAX):
        """
        初期化 : O(MAX)
        """
        self.MAX = MAX
        self.isprime = ip = [False] * (MAX + 1)
        self.mebius = mu = [0] * (MAX + 1)  # メビウス関数
        self.min_factor = f = [0] * (MAX + 1)  # 最小の素因数
        f[1] = mu[1] = 1
        primes = []
        for i in range(2, MAX + 1):
            if not f[i]:
                f[i] = i
                ip[i] = True
                mu[i] = -1
                primes.append(i)
            p, m = f[i], mu[i]
            for q in primes:
                j = i * q
                if j > MAX:
                    break
                f[j] = q
                if q == p:
                    break
                mu[j] = -m

    def prime_factors(self, n):
        """
        素因数分解: (素因数, 指数) のリストを返す
        O(log n)
        """
        f = self.min_factor
        res = []
        while n > 1:
            p, e = f[n], 0
            while f[n] == p:
                e += 1
                n //= p
            res.append((p, e))
        return res

    def divisors(self, n):
        """
        約数列挙: n の約数をすべてリストで返す
        O(d(n)) (d(n): n の約数の個数, d(n) < O(n^(1/3)))
        """
        res = [1]
        for p, e in self.prime_factors(n):
            for i in range(len(res) * e):
                res.append(res[i] * p)
        return res
