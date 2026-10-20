# problem: https://judge.yosupo.jp/problem/lca
# include: algorithm_library/python/graph/LCA.py


def main():
    N, Q = map(int, readline().split())
    graph = [[] for _ in range(N)]
    for v, parent in enumerate(map(int, readline().split()), 1):
        graph[parent].append(v)
    tree = LCA(N, graph, 0)
    ans = []
    for _ in range(Q):
        u, v = map(int, readline().split())
        ans.append(str(tree.lca(u, v)))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
