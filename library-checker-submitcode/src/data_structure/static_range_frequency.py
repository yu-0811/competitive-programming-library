# problem: https://judge.yosupo.jp/problem/static_range_frequency
# include: algorithm_library/python/data-structure/MargeSortTree.py


def main():
    N, Q = map(int, readline().split())
    tree = MergeSortTree(list(map(int, readline().split())))
    ans = []
    for _ in range(Q):
        l, r, x = map(int, readline().split())
        ans.append(str(tree.query_range(l, r, x, x + 1)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
