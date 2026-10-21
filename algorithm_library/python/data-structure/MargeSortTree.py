from array import array
from bisect import bisect_left, bisect_right


class MergeSortTree:
    """構築 O(n log n)、区間内の個数クエリ O(log n)。"""

    def __init__(self, data):
        self.n = len(data)
        self.size = size = 1 << max(0, self.n - 1).bit_length()
        self.tree = tree = [[] for _ in range(2 * size)]
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
        result = hi - lo
        if not result:
            return 0
        links = self._left_prefix
        mask = (1 << height) - 1
        prefix = l & mask
        suffix = -r & mask

        # ノード全体の個数から [l, r) の外側を引く。
        # 子での探索位置は prefix[lo], prefix[hi] から得られる。
        if prefix:
            v, low, high = node, lo, hi
            bit = 1 << (height - 1)
            while prefix:
                link = links[v]
                left_low, left_high = link[low], link[high]
                v <<= 1
                if prefix & bit:
                    result -= left_high - left_low
                    low -= left_low
                    high -= left_high
                    v += 1
                    prefix -= bit
                else:
                    low, high = left_low, left_high
                if low == high:
                    break
                bit >>= 1
        if suffix:
            bit = 1 << (height - 1)
            while suffix:
                link = links[node]
                left_low, left_high = link[lo], link[hi]
                node <<= 1
                if suffix & bit:
                    result -= (hi - lo) - (left_high - left_low)
                    lo, hi = left_low, left_high
                    suffix -= bit
                else:
                    lo -= left_low
                    hi -= left_high
                    node += 1
                if lo == hi:
                    break
                bit >>= 1
        return result

    # 区間 [l, r) で値が x 以下の要素数を求める
    def query_leq(self, l, r, x):
        if l >= r:
            return 0
        # 両端の葉を含む最小ノードでだけ二分探索する。
        height = (l ^ (r - 1)).bit_length()
        node = (l + self.size) >> height
        hi = bisect_right(self.tree[node], x)
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
        return self._count(l, r, lo, hi, node, height)
