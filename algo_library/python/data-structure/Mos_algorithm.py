# 0-index で数列を扱うことに注意

class Mo:
    def __init__(self, data): # data は数列
        from math import sqrt, ceil
        self.data = data
        self.n = len(data)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数
        # [l,r)の半開区間で考える
        self.l = 0
        self.r = 0
        # queryを格納する用
        self.bucket = [list() for _ in range((self.b + 1))]

        ########################################
        # ここに管理したい状態を初期化する処理を書く
        self.cnt = [0]*(self.n+1)
        self.ans = 0
        ########################################

    def _add(self, i):
        # i番目の要素を含めて考えるときへstatesを更新
        ########################################
        if self.cnt[self.data[i]]==1:
            self.ans += 1
        self.cnt[self.data[i]] ^= 1
        ########################################

    def _delete(self, i):
        # i番目の要素を除いて考えるときへstatesを更新
        ########################################
        if self.cnt[self.data[i]]==0:
            self.ans -= 1
        self.cnt[self.data[i]] ^= 1
        ########################################

    def _one_process(self, l, r):
        # クエリ[l,r)に対してstatesを更新する
        while self.r < r:  # rまで伸長
            self._add(self.r)
            self.r += 1
        while self.r > r:  # rまで短縮
            self.r -= 1
            self._delete(self.r)
            
        while self.l < l:  # lまで短縮
            self._delete(self.l)
            self.l += 1
        while self.l > l:  # lまで伸長
            self.l -= 1
            self._add(self.l)

    def process(self, queries):
        upper = len(queries)
        upper_upper = upper * (self.n + 1)

        for idx, (l, r) in enumerate(queries):  # queryをbucketに格納
            self.bucket[l // self.b].append(idx + l*upper + r*upper_upper)

        for i in range(len(self.bucket)):
            self.bucket[i].sort()

        ret = [-1] * len(queries)
        for b in self.bucket:
            for lri in b:  # クエリに答えていく
                i = lri % upper
                r = lri // upper_upper
                l = (lri % upper_upper) // upper
               # クエリ[l,r)に対してstatesを更新する
                while self.r < r:  # rまで伸長
                    self._add(self.r)
                    self.r += 1
                while self.r > r:  # rまで短縮
                    self.r -= 1
                    self._delete(self.r)
                    
                while self.l < l:  # lまで短縮
                    self._delete(self.l)
                    self.l += 1
                while self.l > l:  # lまで伸長
                    self.l -= 1
                    self._add(self.l)
                
                ########################################
                # クエリに答える作業をここで書く
                # ret[i] に i 番目のクエリの答えを格納する
                ret[i] = self.ans
                ########################################
        return ret