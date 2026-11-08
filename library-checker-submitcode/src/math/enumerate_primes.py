# problem: https://judge.yosupo.jp/problem/enumerate_primes
# include: algorithm_library/python/math/factorization.py


def main():
    N, A, B = map(int, readline().split())
    primes = res_primeList(N)
    selected = primes[B::A]
    print(len(primes), len(selected))
    print(*selected)


if __name__ == "__main__":
    main()
