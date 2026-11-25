# problem: https://judge.yosupo.jp/problem/bipartitematching
# include: algorithm_library/python/graph/hopcroft_karp.py


def main():
    n, m, e = map(int, readline().split())
    g = [[] for _ in range(n)]
    for _ in range(e):
        u, v = map(int, readline().split())
        g[u].append(v)
    p = hopcroft_karp(g, m)
    ans = [f"{u} {v}" for u, v in enumerate(p) if v >= 0]
    print(len(ans))
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
