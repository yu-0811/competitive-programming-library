# 約数系包除に使うやつ系

class eratosthenes:
    def __init__(self, MAX: int):
        """
        初期化 : O(MAX loglog MAX)
        """
        self.MAX = MAX
        self.isprime = [True] * (MAX + 1)
        self.mebius = [1] * (MAX + 1) # メビウス関数
        self.min_factor = [-1] * (MAX + 1) # 最小の素因数

        self.isprime[0] = self.isprime[1] = False
        self.min_factor[0], self.min_factor[1] = 0, 1

        for i in range(2, MAX + 1):
            if not self.isprime[i]:
                continue
            self.mebius[i] = -1
            self.min_factor[i] = i

            for j in range(2 * i, MAX + 1, i):
                self.isprime[j] = False
                if (j // i) % i == 0:
                    self.mebius[j] = 0
                else:
                    self.mebius[j] *= -1
                if self.min_factor[j] == -1:
                    self.min_factor[j] = i

    def prime_factors(self, n: int) -> list[tuple[int, int]]:
        """
        素因数分解: (素因数, 指数) のリストを返す
        O(log n)
        """
        res = []
        while n != 1:
            prime = self.min_factor[n]
            exp = 0
            while self.min_factor[n] == prime:
                exp += 1
                n //= prime
            res.append((prime, exp))
        return res

    def divisors(self, n: int) -> list[int]:
        """
        約数列挙: n の約数をすべてリストで返す
        O(d(n)) (d(n): n の約数の個数, d(n) < O(n^(1/3)))
        """
        res = [1]
        for prime, exp in self.prime_factors(n):
            current_size = len(res)
            for i in range(current_size):
                value = 1
                for _ in range(exp):
                    value *= prime
                    res.append(res[i] * value)
        return res