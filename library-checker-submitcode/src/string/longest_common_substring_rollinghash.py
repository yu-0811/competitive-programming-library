# problem: https://judge.yosupo.jp/problem/longest_common_substring
# include: algorithm_library/python/string/RollingHash.py


def main():
    S = readline().decode().strip()
    T = readline().decode().strip()
    left, right = RollingHash(S), RollingHash(T)
    n, m = len(S), len(T)

    def find(length):
        positions = {left.get_hash(i, i + length): i for i in range(n - length + 1)}
        for j in range(m - length + 1):
            key = right.get_hash(j, j + length)
            if key in positions:
                return positions[key], j
        return None

    lo, hi = 0, min(n, m) + 1
    a = b = 0
    while hi - lo > 1:
        length = (lo + hi) // 2
        match = find(length)
        if match is None:
            hi = length
        else:
            lo = length
            a, b = match
    print(a, a + lo, b, b + lo)


if __name__ == "__main__":
    main()
