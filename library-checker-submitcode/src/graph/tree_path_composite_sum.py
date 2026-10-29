# problem: https://judge.yosupo.jp/problem/tree_path_composite_sum
# include: algorithm_library/python/graph/Rerooting.py


def main():
    N = int(readline())
    values = list(map(int, readline().split()))
    edges = []
    coefficients = []
    # 辺を中継頂点に置き換え、既存の頂点変換 API で一次関数を適用する。
    for i in range(N - 1):
        u, v, b, c = map(int, readline().split())
        middle = N + i
        edges.append((u, middle))
        edges.append((middle, v))
        coefficients.append((b, c))

    # 状態は (値の総和, 元の木の頂点数)。中継頂点は数えない。
    def merge(a, b):
        return ((a[0] + b[0]) % mod, a[1] + b[1])

    def node_value(a, v):
        if v < N:
            return ((a[0] + values[v]) % mod, a[1] + 1)
        b, c = coefficients[v - N]
        return ((b * a[0] + c * a[1]) % mod, a[1])

    def answer(a, v):
        return node_value(a, v)[0]

    tree = rerooting(2 * N - 1, edges, (0, 0), merge, node_value, answer)
    print(*tree.run(0)[:N])


if __name__ == "__main__":
    main()
