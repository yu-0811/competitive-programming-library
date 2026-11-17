from collections import defaultdict


class UnionFind:
    def __init__(s, n):
        s.n = n
        # 各頂点の親(1個上の要素)を記入
        # その頂点が根なら -1 以下の値
        # p*-1 がその木のサイズ(要素数)
        s.p = [-1] * n

    # 頂点xの根を返す関数 O(α(N))  
    # 経路圧縮で x から根までに通る頂点をすべて根につなぎなおす
    def root(s, x):
        p = s.p
        r = x
        while p[r] >= 0:
            r = p[r]
        while x != r:
            p[x], x = r, p[x]
        return r

    # マージ後の根を返す O(α(N))
    def union(s, x, y):
        x = s.root(x)
        y = s.root(y)
        if x == y:
            return x  
        # x,y は根であり、p の値*-1 がその木のサイズ(要素数)
        # サイズが小さい方につなげる (union by size)
        if s.p[x] > s.p[y]:
            x, y = y, x  # x が小さい方になるようにする
        s.p[x] += s.p[y]  # サイズを更新
        s.p[y] = x
        return x

    # 要素xが属するグループの要素数を返す O(α(N))
    def size(s, x):
        return -s.p[s.root(x)]

    # x,yが同じグループか(連結か)を返す関数 O(α(N))
    def isSame(s, x, y):
        return s.root(x) == s.root(y)

    # xが属するグループの要素をリストで返す O(N)
    def members(s, x):
        root = s.root(x)
        return [i for i in range(s.n) if s.root(i) == root]

    # すべての根の要素をリストで返す O(N)
    def roots(s):
        return [i for i, x in enumerate(s.p) if x < 0]

    # グループの数を返す O(N)
    def group_count(s):
        return len(s.roots())

    # すべてのグループをリストで返す O(N)
    def all_group_members(s):
        group_members = defaultdict(list)
        for i in range(s.n):
            root = s.root(i)
            group_members[root].append(i)
        return list(group_members.values())
