# problem: https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
# include: algorithm_library/python/math/modComb.py:Comb:1

CombTable = Comb

# include: algorithm_library/python/math/modComb.py:Comb:2


def main():
    T, mod = map(int, readline().split())
    queries = [tuple(map(int, readline().split())) for _ in range(T)]
    N = max(n for n, _ in queries)
    limit = min(N, 64)
    small = Comb(limit, mod)
    table = CombTable(N, mod)
    answers = []
    for n, k in queries:
        # 小さい k の版は O(k)。大きい k の公式ケースには階乗表を使う。
        if not 0 <= k <= n or min(k, n - k) <= limit:
            answer = small.nCk(n, k)
        else:
            answer = table.H(n - k + 1, k)
        answers.append(str(answer))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
