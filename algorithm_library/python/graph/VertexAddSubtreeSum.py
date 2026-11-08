class VertexAddSubtreeSum:
    """親番号が子番号より小さい根付き木の頂点加算・部分木和。

    parents[0] = -1, 0 <= parents[v] < v とする。
    構築 O(N)、空間 O(N)。高さが 2 * N.bit_length() 以下なら祖先の和を直接更新し、
    それ以外は帰りがけ順の部分木区間と Fenwick Tree を使う。
    """

    def __init__(s, parents, values):
        n = s.n = len(parents)
        s.parents = parents
        sums = s.sums = list(values)
        depth = [0] * n
        for v in range(1, n):
            depth[v] = depth[parents[v]] + 1
        s.shallow = max(depth) <= 2 * n.bit_length()
        if s.shallow:
            for v in range(n - 1, 0, -1):
                sums[parents[v]] += sums[v]
        else:
            size = s.size = [1] * n
            for v in range(n - 1, 0, -1):
                p = parents[v]
                sums[p] += sums[v]
                size[p] += size[v]
            # end[v] は帰りがけ順での v の位置 + 1。
            # 子の区間を親の手前に置く。隣接リストや DFS は不要。
            end = s.end = [1] * n
            for v in range(1, n):
                p = parents[v]
                end[v] = end[p]
                end[p] += size[v]
            # 初期値は sums に持ち、BIT には構築後の加算だけを載せる。
            s.bit = [0] * (n + 1)

    def add(s, v, x):
        """頂点 v に x を加算。O(log N)。"""
        if s.shallow:
            sums = s.sums
            parents = s.parents
            while v >= 0:
                sums[v] += x
                v = parents[v]
        else:
            bit = s.bit
            n = s.n
            v = s.end[v]
            while v <= n:
                bit[v] += x
                v += v & -v

    def subtree_sum(s, v):
        """v を根とする部分木の和。O(1)、深い木では O(log N)。"""
        total = s.sums[v]
        if not s.shallow:
            bit = s.bit
            r = s.end[v]
            l = r - s.size[v]
            # 共通する累積和の項は相殺されるので読まない。
            while l != r:
                if l < r:
                    total += bit[r]
                    r &= r - 1
                else:
                    total -= bit[l]
                    l &= l - 1
        return total
