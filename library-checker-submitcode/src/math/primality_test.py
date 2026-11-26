# problem: https://judge.yosupo.jp/problem/primality_test
# include: algorithm_library/python/math/factorization.py


def main():
    for _ in range(int(readline())):
        n = int(readline())
        prime = is_prime(n) if n < 1024 else is_prime64(n)
        print("Yes" if prime else "No")


if __name__ == "__main__":
    main()
