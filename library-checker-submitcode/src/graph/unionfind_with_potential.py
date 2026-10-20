# problem: https://judge.yosupo.jp/problem/unionfind_with_potential
# include: algorithm_library/python/graph/PotentialUnionFind.py


def main():
    N, Q = map(int, readline().split())
    uf = PotentialUnionFind(N)
    ans = []
    for _ in range(Q):
        t, u, v, *rest = map(int, readline().split())
        # Library Checker asks for a[u] - a[v]; dist(x, y) returns a[y] - a[x].
        distance = uf.dist(v, u)
        if t == 0:
            x = rest[0]
            if distance == uf.inf:
                uf.union(v, u, x)
                ans.append("1")
            else:
                ans.append("1" if distance % mod == x else "0")
        else:
            ans.append(str(-1 if distance == uf.inf else distance % mod))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
