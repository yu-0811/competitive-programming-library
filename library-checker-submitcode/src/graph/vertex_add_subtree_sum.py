# problem: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
# include: algorithm_library/python/graph/EulerTour.py


def main():
    N, Q = map(int, readline().split())
    values = list(map(int, readline().split()))
    tree = EulerTour(N)
    for v, parent in enumerate(map(int, readline().split()), 1):
        tree.add_edge(parent, v, 0)
    tree.build(0)
    bit = fenwick_tree(len(tree.vs))
    for v, value in enumerate(values):
        bit.add(tree._in[v], value)
    ans = []
    for _ in range(Q):
        query = list(map(int, readline().split()))
        v = query[1]
        if query[0] == 0:
            bit.add(tree._in[v], query[2])
        else:
            ans.append(str(bit.sum(tree._in[v], tree._out[v] + 1)))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
