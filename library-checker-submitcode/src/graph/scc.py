# problem: https://judge.yosupo.jp/problem/scc
# include: algorithm_library/python/graph/SCC.py


def main():
    N, M = map(int, readline().split())
    edges = []
    for _ in range(M):
        u, v = map(int, readline().split())
        edges.append((u, v))
    groups, _ = scc_dag(N, edges)
    ans = [str(len(groups))]
    ans.extend(f"{len(group)} " + " ".join(map(str, group)) for group in groups)
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
