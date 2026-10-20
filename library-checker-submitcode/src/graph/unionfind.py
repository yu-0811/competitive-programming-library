# problem: https://judge.yosupo.jp/problem/unionfind
# include: algorithm_library/python/graph/UnionFind.py


def main():
    N, Q = map(int, readline().split())
    uf = UnionFind(N)
    ans = []
    for _ in range(Q):
        t, u, v = map(int, readline().split())
        if t == 0:
            uf.union(u, v)
        else:
            ans.append("1" if uf.isSame(u, v) else "0")
    if ans:
        sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
