class PotentialUnionFind:
    def __init__(s, N) -> None:
        s.N = N
        s.p = [-1] * (N + 1)
        # 各要素の根からの距離
        # 相対的な重さを表す
        # 経路圧縮前は親ノードとの差分
        s.w = [0] * (N + 1)
        s.inf = pow(10, 18)
        s.inconsistent = [False] * (
            N + 1
        )  # 連結成分に負閉路があるか（矛盾があるか）

    # 頂点xの根を返す関数
    # O(α(N))
    def root(s, x):
        p, d = s.p, s.w
        path = []
        while p[x] >= 0:
            path.append(x)
            x = p[x]
        for v in reversed(path):
            d[v] += d[p[v]]
            p[v] = x
        return x

    # w[y] - w[x]
    # y が x よりどれだけ重いか
    # 連結でないなら inf を返す
    # O(α(N))
    def dist(s, x, y):
        rx = s.root(x)
        ry = s.root(y)
        if rx == ry:  # 同じ連結成分に属するなら
            return s.w[y] - s.w[x]
        else:
            return s.inf

    # x と y を距離 distance でつなぐ
    # 正確には w[y] = w[x] + distance になるようにつなぐ
    # x の下に y をつなぐ
    # y は x より w 重い
    # x -> y の重み distance の有向辺
    # 返り値は矛盾がなければ true
    # O(α(N))
    def union(s, x, y, w):
        rx = s.root(x)
        ry = s.root(y)
        if rx == ry:  # 既に連結なら
            if s.w[y] - s.w[x] != w:
                s.inconsistent[rx] = True
            return s.w[y] - s.w[x] == w
        p, d = s.p, s.w
        # 根どうしの差に直し、小さい木を大きい木につなぐ。
        if p[ry] > p[rx]:
            w = d[x] + w - d[y]
        else:
            rx, ry = ry, rx
            w = d[y] - w - d[x]
        p[rx] += p[ry]
        p[ry] = rx
        d[ry] = w
        return True

    # 要素xが属するグループの要素数を返す
    # O(α(N))
    def size(s, x):
        return -s.p[s.root(x)]

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
        return [i for i, x in enumerate(s.p) if x < 0]

    # グループの数を返す
    # O(N × α(N))
    def group_count(s):
        return len(s.roots())
