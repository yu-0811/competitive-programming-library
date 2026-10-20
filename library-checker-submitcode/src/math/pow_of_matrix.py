# problem: https://judge.yosupo.jp/problem/pow_of_matrix
# include: algorithm_library/python/math/MatrixPower.py


def main():
    N, K = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(N)]
    result = mat_pow(A, K, mod)
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()
