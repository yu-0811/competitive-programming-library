class PotentialUnionFind:
    def __init__(s, N) -> None:
        s.N = N
        s.parents = [-1] * (N + 1)
        # 各要素の根からの距離
        # 相対的な重さを表す
        # 経路圧縮前は親ノードとの差分
        s.potential = [0] * (N + 1)
        s.inf = pow(10, 18)
        s.inconsistent = [False] * (
            N + 1
        )  # 連結成分に負閉路があるか（矛盾があるか）

    # 頂点xの根を返す関数
    # O(α(N))
    def root(s, x):
        parents, potential = s.parents, s.potential
        path = []
        while parents[x] >= 0:
            path.append(x)
            x = parents[x]
        for v in reversed(path):
            potential[v] += potential[parents[v]]
            parents[v] = x
        return x

    # potential[y] - potential[x]
    # y が x よりどれだけ重いか
    # 連結でないなら inf を返す
    # O(α(N))
    def dist(s, x, y):
        rx = s.root(x)
        ry = s.root(y)
        if rx == ry:  # 同じ連結成分に属するなら
            return s.potential[y] - s.potential[x]
        else:
            return s.inf

    # x と y を距離 distance でつなぐ
    # 正確には potential[y] = potential[x] + distance になるようにつなぐ
    # x の下に y をつなぐ
    # y は x より w 重い
    # x -> y の重み distance の有向辺
    # 返り値は矛盾がなければ true
    # O(α(N))
    def union(s, x, y, w):
        rx = s.root(x)
        ry = s.root(y)
        if rx == ry:  # 既に連結なら
            if s.potential[y] - s.potential[x] != w:
                s.inconsistent[rx] = True
            return s.potential[y] - s.potential[x] == w
        parents, potential = s.parents, s.potential
        # 根どうしの差に直し、小さい木を大きい木につなぐ。
        if parents[ry] > parents[rx]:
            w = potential[x] + w - potential[y]
        else:
            rx, ry = ry, rx
            w = potential[y] - w - potential[x]
        parents[rx] += parents[ry]
        parents[ry] = rx
        potential[ry] = w
        return True

    # 要素xが属するグループの要素数を返す
    # O(α(N))
    def size(s, x):
        return -s.parents[s.root(x)]

    # x,yが同じグループか(連結か)を返す関数
    # O(α(N))
    def isSame(s, x, y):
        return s.root(x) == s.root(y)

    # xが属するグループの要素をリストで返す
    # O(N)
    def members(s, x):
        root = s.root(x)
        return [i for i in range(1, s.N + 1) if s.root(i) == root]

    # すべての根の要素をリストで返す
    # O(N × α(N))
    def roots(s):
        return [i for i, x in enumerate(s.parents) if x < 0]

    # グループの数を返す
    # O(N × α(N))
    def group_count(s):
        return len(s.roots())
