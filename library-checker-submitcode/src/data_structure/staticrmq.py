# problem: https://judge.yosupo.jp/problem/staticrmq
# include: algorithm_library/python/data-structure/SparseTable.py


def main():
    N, Q = map(int, readline().split())
    table = SparseTable(list(map(int, readline().split())), min)
    ans = []
    for _ in range(Q):
        l, r = map(int, readline().split())
        ans.append(str(table.query(l, r)))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
