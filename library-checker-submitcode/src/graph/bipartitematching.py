# problem: https://judge.yosupo.jp/problem/bipartitematching
# include: algorithm_library/python/graph/maxflow.py


def main():
    L, R, M = map(int, readline().split())
    source, sink = L + R, L + R + 1
    flow = maximum_flow(L + R + 2)
    edges = []
    for _ in range(M):
        u, v = map(int, readline().split())
        flow.add_edge(u, L + v, 1)
        edges.append((u, v, flow.G[u][-1]))
    for u in range(L):
        flow.add_edge(source, u, 1)
    for v in range(R):
        flow.add_edge(L + v, sink, 1)
    ans = [str(flow.maxflow(source, sink))]
    ans.extend(f"{u} {v}" for u, v, edge in edges if edge.cap == 0)
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
