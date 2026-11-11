# problem: https://judge.yosupo.jp/problem/tree_path_composite_sum
# include: algorithm_library/python/graph/Rerooting.py


def main():
    N = int(readline())
    values = list(map(int, readline().split()))
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, b, c = map(int, readline().split())
        g[u].append((v, (b, c)))
        g[v].append((u, (b, c)))

    # 状態は (値の総和, 頂点数)。
    def merge(a, b):
        return ((a[0] + b[0]) % mod, a[1] + b[1])

    def add_vertex(x, v):
        return ((x[0] + values[v]) % mod, x[1] + 1)

    def add_edge(x, w):
        b, c = w
        return ((b * x[0] + c * x[1]) % mod, x[1])

    dp = rerooting(g, (0, 0), merge, add_vertex, add_edge)
    print(*(x[0] for x in dp))


if __name__ == "__main__":
    main()
