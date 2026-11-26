# 任意の場所に挿入したり削除とかができる
import math


class BucketList:
    br = 16
    sr = 24

    def __init__(s, a=[]):
        a = list(a)
        n = s.size = len(a)
        k = math.ceil(math.sqrt(n / s.br))
        s.a = [
            a[n * i // k : n * (i + 1) // k]
            for i in range(k)
        ]

    def __iter__(s):
        for a in s.a:
            yield from a

    def __contains__(s, x):
        "x が含まれていれば True を返す。 / O(N)"
        for y in s:
            if x == y:
                return True
        return False

    # i 番目の要素を含むバケット、バケット番号、その中での添字
    def _locate(s, i):
        if i < 0:
            for b in range(len(s.a) - 1, -1, -1):
                a = s.a[b]
                i += len(a)
                if i >= 0:
                    return a, b, i
        else:
            for b, a in enumerate(s.a):
                if i < len(a):
                    return a, b, i
                i -= len(a)
        raise IndexError

    def insert(s, i, x):
        "i 番目の位置に x を挿入する。 / O(√N)"
        if i == s.size or (not s.size and i == -1):
            if not s.a:
                s.a.append([])
            b = len(s.a) - 1
            a = s.a[b]
            i = len(a)
        else:
            a, b, i = s._locate(i)
        a.insert(i, x)
        s.size += 1
        if len(a) > len(s.a) * s.sr:
            mid = len(a) >> 1
            s.a[b:b + 1] = [a[:mid], a[mid:]]

    def append(s, x):
        "末尾に x を追加する。 / 償却 O(1)"
        s.insert(s.size, x)

    def extend(s, a):
        for x in a:
            s.append(x)

    def __getitem__(s, i):
        a, _, i = s._locate(i)
        return a[i]

    def pop(s, i=-1):
        "i 番目の要素を削除して返す。 / O(√N) / i < 0 なら O(-i)"
        a, b, i = s._locate(i)
        ans = a.pop(i)
        s.size -= 1
        if not a:
            del s.a[b]
        return ans

    def count(s, x):
        "x の出現回数を返す。 / O(N)"
        return sum(1 for y in s if x == y)

    def index(s, x):
        "最初に現れる x の添字を返す。見つからなければ ValueError を送出する。 / O(N)"
        for i, y in enumerate(s):
            if x == y:
                return i
        raise ValueError

    def remove(s, x):
        "最初に現れる x を削除する。見つからなければ ValueError を送出する。 / O(N)"
        s.pop(s.index(x))

    def clear(s):
        s.a = []
        s.size = 0

    def reverse(s):
        s.a.reverse()
        for a in s.a:
            a.reverse()

    def copy(s):
        return BucketList(s)

    def __len__(s):
        return s.size

    def __str__(s):
        return str(list(s))
