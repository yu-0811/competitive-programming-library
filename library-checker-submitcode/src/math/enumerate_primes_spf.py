# problem: https://judge.yosupo.jp/problem/enumerate_primes
# include: algorithm_library/python/math/factorization.py


def main():
    N, A, B = map(int, readline().split())
    # 最小素因数表は N 以下の整数をすべて持つ。大きいケースは奇数だけの篩を使う。
    if N <= 1_000_000:
        factors = init_factorization(N)
        primes = [i for i in range(2, N + 1) if factors[i] == i]
    else:
        primes = res_primeList(N)
    selected = primes[B::A]
    print(len(primes), len(selected))
    print(*selected)


if __name__ == "__main__":
    main()
