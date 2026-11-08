# problem: https://judge.yosupo.jp/problem/bitwise_and_convolution
# include: algorithm_library/python/math/mobius.py


def main():
    N = int(readline())
    arrays = [list(map(int, readline().split())) for _ in range(2)]
    for data in arrays:
        for i in range(N):
            bit = 1 << i
            for start in range(0, 1 << N, 2 * bit):
                for mask in range(start, start + bit):
                    data[mask] += data[mask + bit]
    result = [(a % mod) * (b % mod) % mod for a, b in zip(*arrays)]
    mobius(result)
    print(*(x % mod for x in result))


if __name__ == "__main__":
    main()
