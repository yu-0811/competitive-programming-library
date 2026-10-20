# problem: https://judge.yosupo.jp/problem/static_range_sum
# include: algorithm_library/python/data-structure/DisjointSparseTable.py


def main():
    N, Q = map(int, readline().split())
    table = DisjointSparseTable(list(map(int, readline().split())), lambda a, b: a + b)
    ans = []
    for _ in range(Q):
        l, r = map(int, readline().split())
        ans.append(str(table.query(l, r) if l < r else 0))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
