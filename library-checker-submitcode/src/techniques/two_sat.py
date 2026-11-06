# problem: https://judge.yosupo.jp/problem/two_sat
# include: algorithm_library/python/techniques/2-SAT.py


def main():
    _, _, n, m = readline().split()
    n, m = int(n), int(m)

    def clauses():
        for _ in range(m):
            a, b, _ = map(int, readline().split())
            yield abs(a) - 1, a > 0, abs(b) - 1, b > 0

    answer = two_sat(n, clauses())
    if answer is None:
        print("s UNSATISFIABLE")
    else:
        print("s SATISFIABLE")
        print("v", " ".join(str(i if x else -i) for i, x in enumerate(answer, 1)), 0)


if __name__ == "__main__":
    main()
