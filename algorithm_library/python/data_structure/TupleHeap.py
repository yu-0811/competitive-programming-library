# 先頭 k 成分だけを辞書順で比較する最小ヒープ。k >= 1、各タプルの長さ >= k。
# h = TupleHeap(1, [(0, start)])  # (距離, 頂点) を距離だけで比較
# h.push((d, v)); d, v = h.pop(); h.top(); len(h)
# while h: d, v = h.pop()
# k=2 なら (優先度1, 優先度2, データ, ...) の先頭2成分で比較。
# 後続成分は比較しない。同じキーの取り出し順は不定。空の pop/top は IndexError。


class TupleHeap:
    def __init__(s, k=1, values=()):
        s.k = k
        s.q = list(values)
        s.keys = [x[0] if k == 1 else x[:k] for x in s.q]
        for i in range(len(s.q) // 2 - 1, -1, -1):
            s._down(i)

    def __len__(s):
        return len(s.q)

    def top(s):
        return s.q[0]

    def push(s, x):
        a, q = s.keys, s.q
        key = x[0] if s.k == 1 else x[:s.k]
        i = len(q)
        a.append(key)
        q.append(x)
        while i:
            p = (i - 1) // 2
            if not key < a[p]:
                break
            a[i], q[i] = a[p], q[p]
            i = p
        a[i], q[i] = key, x

    def _down(s, i):
        a, q = s.keys, s.q
        n = len(q)
        key, x = a[i], q[i]
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if j + 1 < n and a[j + 1] < a[j]:
                j += 1
            if not a[j] < key:
                break
            a[i], q[i] = a[j], q[j]
            i = j
        a[i], q[i] = key, x

    def pop(s):
        a, q = s.keys, s.q
        result = q[0]
        key, x = a.pop(), q.pop()
        if q:
            a[0], q[0] = key, x
            s._down(0)
        return result
