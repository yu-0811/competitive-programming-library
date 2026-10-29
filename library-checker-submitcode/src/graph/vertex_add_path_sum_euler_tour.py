# problem: https://judge.yosupo.jp/problem/vertex_add_path_sum
# include: algorithm_library/python/graph/EulerTour.py


def main():
    N, Q = map(int, readline().split())
    values = list(map(int, readline().split()))
    tree = EulerTour(N)
    for _ in range(N - 1):
        u, v = map(int, readline().split())
        tree.add_edge(u, v, -(values[u] + values[v]))
    # パス和は根によらないので、頂点 0 以外を根にしても同じように扱える。
    root = N - 1
    tree.build(root)
    bit = tree.fen
    ans = []
    for _ in range(Q):
        t, u, v = map(int, readline().split())
        if t == 0:
            values[u] += v
            if u == root:
                if N > 1:
                    bit.add(1, -v)
            else:
                # 根からの距離の増分は u で -v、真の子孫で -2v、部分木外で 0。
                l, r = tree._in[u], tree._out[u] + 1
                bit.add(l, -v)
                bit.add(l + 1, -v)
                bit.add(r, 2 * v)
        else:
            # 辺重み -(a[u]+a[v]) を使い、負の辺重みにも対応する。
            ans.append((-tree.get_distance(u, v) + values[u] + values[v]) // 2)
    for i in range(0, len(ans), 8192):
        sys.stdout.write("\n".join(map(str, ans[i:i + 8192])) + "\n")


if __name__ == "__main__":
    main()
