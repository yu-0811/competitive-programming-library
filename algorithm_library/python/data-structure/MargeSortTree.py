from bisect import bisect_right, bisect_left


class MergeSortTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = size = 1 << max(0, self.n - 1).bit_length()
        self.tree = tree = [[] for _ in range(2 * size)]

        tree[size : size + self.n] = [[x] for x in data]
        # 子ノードの要素をソートしてすべて持つように構築
        for i in range(size - 1, 0, -1):
            tree[i] = sorted(tree[2 * i] + tree[2 * i + 1])

    # 区間 [l, r) で値が x 以下の要素数を求める
    def query_leq(self, l, r, x):
        l += self.size
        r += self.size
        res = 0
        while l < r:
            if l & 1:
                res += bisect_right(self.tree[l], x)
                l += 1
            if r & 1:
                res += bisect_right(self.tree[r - 1], x)
                r -= 1
            l >>= 1
            r >>= 1
        return res

    # 区間[l, r) で値が a 以上 b 未満の要素数を求める
    def query_range(self, l, r, a, b):
        l += self.size
        r += self.size
        res = 0
        while l < r:
            if l & 1:
                res += bisect_left(self.tree[l], b) - bisect_left(self.tree[l], a)
                l += 1
            if r & 1:
                res += bisect_left(self.tree[r - 1], b) - bisect_left(
                    self.tree[r - 1], a
                )
                r -= 1
            l >>= 1
            r >>= 1
        return res
