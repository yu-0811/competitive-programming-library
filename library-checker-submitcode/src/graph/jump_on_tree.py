# problem: https://judge.yosupo.jp/problem/jump_on_tree
# include: algorithm_library/python/graph/LCA.py
# include: algorithm_library/python/techniques/Doubling.py


def main():
    N, Q = map(int, readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, readline().split())
        graph[u].append(v)
        graph[v].append(u)
    tree = LCA(N, graph, 0)
    # Build the jump table through Doubling.py as well as testing LCA.py.
    dp = [[0] * N for _ in range(N.bit_length())]
    dp[0] = [max(0, parent) for parent in tree.parent[0][:N]]
    doubling(dp, N, len(dp))
    ans = []
    for _ in range(Q):
        u, v, k = map(int, readline().split())
        ancestor = tree.lca(u, v)
        up = tree.depth[u] - tree.depth[ancestor]
        distance = up + tree.depth[v] - tree.depth[ancestor]
        if k > distance:
            ans.append("-1")
        elif k <= up:
            ans.append(str(query(dp, u, k)))
        else:
            ans.append(str(query(dp, v, distance - k)))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
