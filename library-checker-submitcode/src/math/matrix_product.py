# problem: https://judge.yosupo.jp/problem/matrix_product
# include: algorithm_library/python/math/MatrixPower.py


def main():
    N, M, K = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(N)]
    B = [list(map(int, readline().split())) for _ in range(M)]
    result = mat_mul(A, B, mod)
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()
