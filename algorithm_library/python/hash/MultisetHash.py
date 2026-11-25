from random import randint


class MultisetHash:
    # 比較したい配列を引数に渡す
    def __init__(self, A: list, B: list) -> None:
        mod = self.mod = (1 << 61) - 1
        h = self.hash = {}
        self.hashA, self.hashB = [0], [0]
        for values, prefix in ((A, self.hashA), (B, self.hashB)):
            for x in values:
                v = h.get(x)
                if v is None:
                    v = h[x] = randint(1, mod - 1)
                prefix.append((prefix[-1] + v) % mod)

    # 0-index の半開区間 A[al:ar] と B[bl:br] の多重集合を比較する。
    def isEqual(self, al, ar, bl, br):
        diff = self.hashA[ar] - self.hashA[al] - self.hashB[br] + self.hashB[bl]
        return diff % self.mod == 0
