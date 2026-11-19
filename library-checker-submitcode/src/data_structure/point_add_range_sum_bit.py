# problem: https://judge.yosupo.jp/problem/point_add_range_sum
# include: algorithm_library/python/data_structure/BIT.py


def main():
    _, Q = map(int, readline().split())
    bit = BIT(map(int, readline().split()))
    ans = []
    for _ in range(Q):
        t, x, y = map(int, readline().split())
        if t == 0:
            bit.add(x, y)
        else:
            ans.append(str(bit.sum(x, y)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
