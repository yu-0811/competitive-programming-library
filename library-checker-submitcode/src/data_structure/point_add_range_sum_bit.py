# problem: https://judge.yosupo.jp/problem/point_add_range_sum
# include: algorithm_library/python/data_structure/BIT.py


def main():
    N, Q = map(int, readline().split())
    bit = BIT(N)
    for i, value in enumerate(map(int, readline().split())):
        bit.add(i, i + 1, value)
    ans = []
    for _ in range(Q):
        t, x, y = map(int, readline().split())
        if t == 0:
            bit.add(x, x + 1, y)
        else:
            ans.append(str(bit.range_sum(x, y)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
