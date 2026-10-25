"""2 要素タプル用ヒープ。説明: documents/algo_library/data_structure/TupleHeap.md"""

from heapq import heapify, heappop, heappush, heappushpop, heapreplace


class TupleHeap:
    """成分を別々のリストに保存する。成分は全順序を持つ値を使う。"""

    __slots__ = ("_a", "_b")

    def __init__(self, values=()):
        a, b = self._a, self._b = [], []
        for x, y in values:
            a.append(x)
            b.append(y)
        for pos in range(len(a) // 2 - 1, -1, -1):
            self._sift_down(pos, a[pos], b[pos])

    def __len__(self):
        return len(self._a)

    def peek(self):
        return self._a[0], self._b[0]

    def push(self, item):
        x, y = item
        a, b = self._a, self._b
        pos = len(a)
        a.append(x)
        b.append(y)
        while pos:
            parent = (pos - 1) >> 1
            u, v = a[parent], b[parent]
            if not (x < u or (x == u and y < v)):
                break
            a[pos], b[pos] = u, v
            pos = parent
        a[pos], b[pos] = x, y

    def pop(self):
        a, b = self._a, self._b
        result = a[0], b[0]
        x, y = a.pop(), b.pop()
        if a:
            self._sift_down(0, x, y)
        return result

    def replace(self, item):
        """最小値を取り出して item を挿入する。空なら IndexError。"""
        x, y = item
        result = self.peek()
        self._sift_down(0, x, y)
        return result

    def pushpop(self, item):
        """挿入して最小値を取り出す。空なら item の値を返す。"""
        x, y = item
        a, b = self._a, self._b
        if a and (a[0] < x or (a[0] == x and b[0] < y)):
            result = a[0], b[0]
            self._sift_down(0, x, y)
            return result
        return x, y

    def _sift_down(self, pos, x, y):
        a, b = self._a, self._b
        n = len(a)
        start = pos
        child = 2 * pos + 1
        # 小さい方の子を葉まで引き上げ、空いた位置から x, y を戻す。
        while child < n:
            right = child + 1
            u, v = a[child], b[child]
            if right < n:
                r, s = a[right], b[right]
                if r < u or (r == u and s < v):
                    child = right
                    u, v = r, s
            a[pos], b[pos] = u, v
            pos = child
            child = 2 * pos + 1
        while pos > start:
            parent = (pos - 1) >> 1
            u, v = a[parent], b[parent]
            if not (x < u or (x == u and y < v)):
                break
            a[pos], b[pos] = u, v
            pos = parent
        a[pos], b[pos] = x, y


class PackedTupleHeap:
    """(整数 key, 0 <= value < 2**bits の整数) を 1 整数に符号化する。"""

    __slots__ = ("_heap", "_bits", "_mask")

    def __init__(self, values=(), bits=20):
        if not isinstance(bits, int) or bits < 0:
            raise ValueError("bits must be a nonnegative integer")
        self._bits = bits
        self._mask = (1 << bits) - 1
        self._heap = [self._pack(item) for item in values]
        heapify(self._heap)

    def _pack(self, item):
        x, y = item
        if not 0 <= y <= self._mask:
            raise ValueError("second component must satisfy 0 <= value < 2**bits")
        return (x << self._bits) | y

    def _unpack(self, value):
        return value >> self._bits, value & self._mask

    def __len__(self):
        return len(self._heap)

    def peek(self):
        return self._unpack(self._heap[0])

    def push(self, item):
        heappush(self._heap, self._pack(item))

    def pop(self):
        return self._unpack(heappop(self._heap))

    def replace(self, item):
        return self._unpack(heapreplace(self._heap, self._pack(item)))

    def pushpop(self, item):
        return self._unpack(heappushpop(self._heap, self._pack(item)))
