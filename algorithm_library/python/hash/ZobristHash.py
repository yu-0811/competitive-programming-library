from random import getrandbits


# 接頭辞版。N = len(A) + len(B) として、前処理は期待 O(N) 時間・O(N) 領域、クエリは O(1)。
# 異なる集合が一致する確率は 1 クエリあたり 2^-61。
class ZobristHash:
    def __init__(self, A, B):
        h, a, b = {}, [0], [0]
        for x in A:
            v = 0
            if x not in h:
                h[x] = v = getrandbits(61)
            a.append(a[-1] ^ v)
        for x in B:
            v = h.get(x)
            if v is None:
                v = getrandbits(61)
            h[x] = 0  # B で 2 回目以降に現れたら XOR しない
            b.append(b[-1] ^ v)
        self.a, self.b = a, b

    # [0, ar) と [0, br) の集合を比較する。
    def isEqual(self, ar, br):
        return self.a[ar] == self.b[br]


from bisect import bisect_left


# 任意区間版（厳密）。N = len(A) + len(B)、K = 異なる値の数、W = 2 区間の長さの和。
# 前処理は期待 O(N) 時間・O(N) 領域、クエリは期待 O(1 + min(W, K log(N + 2)))。
class ZobristHash:
    def __init__(self, A, B):
        self.A, self.B = list(A), list(B)
        self.log = (len(self.A) + len(self.B)).bit_length() + 1
        pos = {}
        for side, S in enumerate((self.A, self.B)):
            for i, x in enumerate(S):
                pos.setdefault(x, ([-1], [-1]))[side].append(i)
        self.pos = list(pos.values())

    # 0-index の半開区間 [al, ar), [bl, br) の集合を比較する。
    def isEqual(self, al, ar, bl, br):
        if al == ar or bl == br:
            return al == ar and bl == br

        def has(p, l, r, n):
            # 出現が多い値は、区間中央付近に当たる添字を見積もって先に試す。
            if len(p) > 64 and l <= p[(l + r) * len(p) // (2 * n + 1)] < r:
                return True
            return p[bisect_left(p, r) - 1] >= l

        n, m = len(self.A), len(self.B)
        budget = (ar - al + br - bl) // self.log
        for a, b in self.pos:
            if budget == 0:
                return set(self.A[al:ar]) == set(self.B[bl:br])
            budget -= 1
            if has(a, al, ar, n) != has(b, bl, br, m):
                return False
        return True
