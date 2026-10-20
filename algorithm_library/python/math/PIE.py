# 約数系包除に使うやつ系


class eratosthenes:
    def __init__(self, MAX: int):
        """
        初期化 : O(MAX)
        """
        self.MAX = MAX
        isprime = self.isprime = [False] * (MAX + 1)
        mebius = self.mebius = [1] * (MAX + 1)  # メビウス関数
        min_factor = self.min_factor = [0] * (MAX + 1)  # 最小の素因数
        min_factor[1] = 1
        primes = []

        for i in range(2, MAX + 1):
            if min_factor[i] == 0:
                min_factor[i] = i
                isprime[i] = True
                mebius[i] = -1
                primes.append(i)

            smallest, mu = min_factor[i], mebius[i]
            for prime in primes:
                j = i * prime
                if j > MAX:
                    break
                min_factor[j] = prime
                if prime == smallest:
                    mebius[j] = 0
                    break
                mebius[j] = -mu

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
