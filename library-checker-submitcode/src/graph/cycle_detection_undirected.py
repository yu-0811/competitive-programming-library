# problem: https://judge.yosupo.jp/problem/cycle_detection_undirected
# include: algorithm_library/python/graph/cycle_detect.py


def main():
    N, M = map(int, readline().split())
    edges = [tuple(map(int, readline().split())) for _ in range(M)]
    vertices, edge_ids = cycle_detect(N, edges)
    if not vertices:
        print(-1)
        return
    print(len(vertices))
    print(*vertices)
    print(*edge_ids)


if __name__ == "__main__":
    main()
