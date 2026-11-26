# problem: https://judge.yosupo.jp/problem/static_range_frequency
# include: algorithm_library/python/data_structure/MargeSortTree.py


def main():
    _, q = map(int, readline().split())
    count = range_frequency(map(int, readline().split()))
    ans = []
    for _ in range(q):
        l, r, x = map(int, readline().split())
        ans.append(str(count(l, r, x)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
