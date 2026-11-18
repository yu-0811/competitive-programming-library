# problem: https://judge.yosupo.jp/problem/shortest_path
# include: algorithm_library/python/data_structure/TupleHeap.py


def main():
    N, M, start, goal = map(int, readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, readline().split())
        graph[u].append((v, w))

    dist = [inf] * N
    prev = [-1] * N
    dist[start] = 0
    heap = TupleHeap(1, [(0, start)])
    while heap:
        d, v = heap.pop()
        if d != dist[v]:
            continue
        if v == goal:
            break
        for u, w in graph[v]:
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                prev[u] = v
                heap.push((nd, u))

    if dist[goal] == inf:
        print(-1)
        return
    path = []
    v = goal
    while v != start:
        u = prev[v]
        path.append(f"{u} {v}")
        v = u
    print(dist[goal], len(path))
    sys.stdout.write("\n".join(reversed(path)) + "\n")


if __name__ == "__main__":
    main()
