# problem: https://judge.yosupo.jp/problem/lca
# include: algorithm_library/python/graph/EulerTour.py


def main():
    N, Q = map(int, readline().split())
    tree = EulerTour(N)
    for v, parent in enumerate(map(int, readline().split()), 1):
        tree.add_edge(parent, v, 1)
    tree.build(0)
    ans = []
    for _ in range(Q):
        u, v = map(int, readline().split())
        ans.append(str(tree.lca(u, v)))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
