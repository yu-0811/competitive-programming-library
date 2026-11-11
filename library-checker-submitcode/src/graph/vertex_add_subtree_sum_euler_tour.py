# problem: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
# include: algorithm_library/python/graph/EulerTourOrder.py
# include: algorithm_library/python/data_structure/BIT.py


def main():
    n, q = map(int, readline().split())
    values = list(map(int, readline().split()))
    G = [[] for _ in range(n)]
    # 番号を反転し、親番号の大小や根が 0 であることに依存せず使う。
    for child, parent in enumerate(map(int, readline().split()), 1):
        u, v = n - 1 - parent, n - 1 - child
        G[u].append(v)
        G[v].append(u)
    tin, tout, order = euler_tour(G, n - 1)
    bit = fenwick_tree(n)
    data = bit.data = [values[n - 1 - v] for v in order]
    for i in range(n):
        j = i | (i + 1)
        if j < n:
            data[j] += data[i]
    ans = []
    for _ in range(q):
        query = list(map(int, readline().split()))
        v = n - 1 - query[1]
        if query[0] == 0:
            bit.add(tin[v], query[2])
        else:
            ans.append(bit.sum(tin[v], tout[v]))
    for i in range(0, len(ans), 8192):
        sys.stdout.write("\n".join(map(str, ans[i:i + 8192])) + "\n")


if __name__ == "__main__":
    main()
