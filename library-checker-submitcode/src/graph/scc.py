# problem: https://judge.yosupo.jp/problem/scc
# include: algorithm_library/python/graph/SCC.py


def main():
    N, M = map(int, readline().split())
    graph = SCC(N)
    for _ in range(M):
        u, v = map(int, readline().split())
        graph.addEdge(u, v)
    groups = graph.build_scc()
    ans = [str(len(groups))]
    ans.extend(f"{len(group)} " + " ".join(map(str, group)) for group in groups)
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
