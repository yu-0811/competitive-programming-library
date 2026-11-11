def euler_tour(G, r=0):
    """木の隣接リスト G -> (tin, tout, od)
    時間・空間 O(N)
    tin: 各頂点を訪れた時刻
    tout: 各頂点から帰る時刻
    od: 行きがけ順に頂点を並べた列
    部分木 v = od[tin[v]:tout[v]]（v 自身を含む）
    """
    tin = [-1] * len(G)
    tout = [-1] * len(G)
    od = []
    st = [r]
    while st:
        v = st.pop()
        if v < 0:  # 退出の印を元の頂点に戻す
            tout[~v] = len(od)
        else:
            tin[v] = len(od)
            od.append(v)
            st.append(~v)
            for u in reversed(G[v]):
                if tin[u] < 0:
                    st.append(u)
    return tin, tout, od
