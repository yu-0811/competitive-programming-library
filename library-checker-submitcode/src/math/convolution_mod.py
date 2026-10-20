# problem: https://judge.yosupo.jp/problem/convolution_mod
# include: algorithm_library/python/math/FFT.py


def main():
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    print(*FFT(mod).convolution(A, B))


if __name__ == "__main__":
    main()
