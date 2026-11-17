# problem: https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
# include: algorithm_library/python/math/modComb.py:Comb:1


def main():
    T, mod = map(int, readline().split())
    queries = [tuple(map(int, readline().split())) for _ in range(T)]
    comb = Comb(max(n for n, _ in queries), mod)
    print("\n".join(str(comb.C(n, k)) for n, k in queries))


if __name__ == "__main__":
    main()
