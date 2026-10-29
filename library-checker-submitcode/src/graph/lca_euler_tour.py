# problem: https://judge.yosupo.jp/problem/lca
# include: algorithm_library/python/graph/EulerTour.py


def main():
    N, Q = map(int, readline().split())
    tree = EulerTour(N)
    for v, parent in enumerate(map(int, readline().split()), 1):
        tree.add_edge(parent, v, 1)
    tree.build(0, path_sum=False)
    ans = [0] * Q
    for i in range(Q):
        u, v = map(int, readline().split())
        ans[i] = tree.lca(u, v)
    for i in range(0, Q, 8192):
        sys.stdout.write("\n".join(map(str, ans[i:i + 8192])) + "\n")


if __name__ == "__main__":
    main()
