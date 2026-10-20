def TopologicalSort(N, G):
    indegree = [0] * (N + 1)
    for v in range(1, N + 1):
        for v2 in G[v]:
            indegree[v2] += 1

    que = [v for v in range(1, N + 1) if indegree[v] == 0]

    # 入次数 0 の頂点とその頂点から出る辺を削除する
    for v in que:
        for v2 in G[v]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                que.append(v2)

    # 閉路があるなら空の配列を返す
    if len(que) != N:
        return []
    else:
        return que
