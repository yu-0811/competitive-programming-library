# 有向グラフのハミルトン路を返す O(N^2)
def hamiltonian_path(G):
    N = len(G)
    G = [set(g) for g in G]
    path = []

    for v in range(N):
        # vを既存のハミルトン路に挿入する
        for i, u in enumerate(path):
            # v → u が存在する最初の頂点を探す
            if u in G[v]:
                path.insert(i, v)
                break
        else:
            # 見つからなければ末尾に追加
            path.append(v)

    return path