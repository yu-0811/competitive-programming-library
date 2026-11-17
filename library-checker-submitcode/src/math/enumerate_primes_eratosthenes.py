# problem: https://judge.yosupo.jp/problem/enumerate_primes
# include: algorithm_library/python/math/factorization.py


def main():
    N, A, B = map(int, readline().split())
    # bool の表を返す版は小さいケース、奇数だけの篩は大きいケースに使う。
    if N <= 1_000_000:
        primes, isprime = eratosthenes(N)
        count = sum(isprime)
    else:
        primes = res_primeList(N)
        count = len(primes)
    selected = primes[B::A]
    print(count, len(selected))
    print(*selected)


if __name__ == "__main__":
    main()
