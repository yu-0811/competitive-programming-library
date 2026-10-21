from array import array
from bisect import bisect_left, bisect_right


class MergeSortTree:
    """構築 O(n log n)、区間内の個数クエリ O(log n)。"""

    def __init__(self, data):
        self.n = len(data)
        self.size = size = 1 << max(0, self.n - 1).bit_length()
        self.tree = tree = [[]] * (2 * size)
        self._left_prefix = links = [None] * size

        tree[size : size + self.n] = [[x] for x in data]
        # 子ノードの要素をソートしてすべて持つように構築
        for i in range(size - 1, 0, -1):
            left = tree[2 * i]
            values = tree[i] = sorted(left + tree[2 * i + 1])
            left_size = len(left)
            # 親の先頭 k 要素に含まれる左の子の要素数を記録する。
            # 同値の要素は、安定ソートと同じく左の子を先に数える。
            prefix = array("I", [0])
            rank = 0
            for value in values:
                if rank < left_size and not value < left[rank]:
                    rank += 1
                prefix.append(rank)
            links[i] = prefix

    def _count(self, l, r, lo, hi, node, height):
        links = self._left_prefix
        width = 1 << height
        mask = width - 1
        # 両端の累積個数を同じループで求め、その差を取る。
        res = hi - lo if r & mask == 0 else 0
        for pos, sign in ((l & mask, -1), (r & mask, 1)):
            v, a, b, bit = node, lo, hi, width
            count = 0
            while pos and a != b:
                bit >>= 1
                link = links[v]
                x, y = link[a], link[b]
                v <<= 1
                if pos & bit:
                    count += y - x
                    a -= x
                    b -= y
                    v += 1
                    pos -= bit
                else:
                    a, b = x, y
            res += sign * count
        return res

    # 区間 [l, r) で値が x 以下の要素数を求める
    def query_leq(self, l, r, x):
        if l >= r:
            return 0
        # 両端の葉を含む最小ノードでだけ二分探索する。
        height = (l ^ (r - 1)).bit_length()
        node = (l + self.size) >> height
        values = self.tree[node]
        hi = bisect_right(values, x)
        if hi == len(values):
            return r - l
        return self._count(l, r, 0, hi, node, height)

    # 区間[l, r) で値が a 以上 b 未満の要素数を求める
    def query_range(self, l, r, a, b):
        if l >= r:
            return 0
        height = (l ^ (r - 1)).bit_length()
        node = (l + self.size) >> height
        values = self.tree[node]
        lo = bisect_left(values, a)
        hi = bisect_left(values, b)
        if not lo and hi == len(values):
            return r - l
        return self._count(l, r, lo, hi, node, height)
