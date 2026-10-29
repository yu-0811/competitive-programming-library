# 任意の場所に挿入したり削除とかができる
import math


class BucketList:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a=[]):
        a = list(a)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self):
        for a in self.a:
            yield from a

    def __contains__(self, x):
        "x が含まれていれば True を返す。 / O(N)"
        for y in self:
            if x == y:
                return True
        return False

    def _insert(self, a, b, i, x):
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def insert(self, i, x):
        "i 番目の位置に x を挿入する。 / O(√N)"
        if self.size == 0:
            if i != 0 and i != -1:
                raise IndexError
            self.a = [[x]]
            self.size = 1
            return
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._insert(a, len(self.a) + ~b, i, x)
        else:
            for b, a in enumerate(self.a):
                if i <= len(a):
                    return self._insert(a, b, i, x)
                i -= len(a)
        raise IndexError

    def append(self, x):
        "末尾に x を追加する。 / 償却 O(1)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self.a[-1]
        return self._insert(a, len(self.a) - 1, len(a), x)

    def extend(self, a):
        for x in a:
            self.append(x)

    def __getitem__(self, i):
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def _pop(self, a, b, i):
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def pop(self, i=-1):
        "i 番目の要素を削除して返す。 / O(√N) / i < 0 なら O(-i)"
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def count(self, x):
        "x の出現回数を返す。 / O(N)"
        return sum(1 for y in self if x == y)

    def index(self, x):
        "最初に現れる x の添字を返す。見つからなければ ValueError を送出する。 / O(N)"
        for i, y in enumerate(self):
            if x == y:
                return i
        raise ValueError

    def remove(self, x):
        "最初に現れる x を削除する。見つからなければ ValueError を送出する。 / O(N)"
        self.pop(self.index(x))

    def clear(self):
        self.a = []
        self.size = 0

    def reverse(self):
        self.a.reverse()
        for a in self.a:
            a.reverse()

    def copy(self):
        return BucketList(self)

    def __len__(self):
        return self.size

    def __str__(self):
        return str(list(self))
