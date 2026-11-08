# problem: https://judge.yosupo.jp/problem/pow_of_matrix
# include: algorithm_library/python/math/MatrixPower.py


def main():
    N, K = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(N)]
    result = [[int(i == j) for j in range(N)] for i in range(N)]
    while K:
        if K & 1:
            result = [vec_mul(row, A, mod) for row in result]
        K >>= 1
        if K:
            A = [vec_mul(row, A, mod) for row in A]
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()
