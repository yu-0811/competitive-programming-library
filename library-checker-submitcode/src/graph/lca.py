# problem: https://judge.yosupo.jp/problem/lca
# include: algorithm_library/python/graph/LCA.py


def main():
    readline = sys.stdin.buffer.readline
    N, Q = map(int, readline().split())
    edges = ((p, v) for v, p in enumerate(map(int, readline().split()), 1))
    tree = LCA(N, edges)
    ans = [0] * Q
    for i in range(Q):
        u, v = map(int, readline().split())
        ans[i] = tree.lca(u, v)
    sys.stdout.write("\n".join(map(str, ans)) + "\n")


if __name__ == "__main__":
    main()
