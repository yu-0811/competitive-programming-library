# 双方向連結リスト https://atcoder.jp/contests/abc344/editorial/9487
# 挿入・削除 O(1)
# 要素の重複不可


class TwoWayList:
    def __init__(self, L):
        self.head = -1
        self.tail = pow(10, 18)
        self.L = [self.head] + L + [self.tail]
        self.front, self.back = dict(), dict()
        for i in range(len(self.L) - 1):
            self.back[self.L[i]] = self.L[i + 1]  # xの後ろ
            self.front[self.L[i + 1]] = self.L[i]  # xの前

    def insert_front(self, x, y):  # xの前にyを挿入する
        # 現在 a -> x
        # a -> y -> x
        a = self.front[x]
        self.back[a] = y
        self.front[x] = y
        self.back[y] = x
        self.front[y] = a

    def insert_back(self, x, y):  # xの直後にyを挿入する
        # 現在 x -> b
        # x -> y -> b
        b = self.back[x]
        self.back[x] = y
        self.front[y] = x
        self.back[y] = b
        self.front[b] = y

    def del_x(self, x):  # xを削除する
        a = self.front[x]
        b = self.back[x]
        self.back[a] = b
        self.front[b] = a
        del self.front[x]
        del self.back[x]

    def res_LIST(self):  # リストを返す
        ans = list()
        crr = self.back[self.head]
        while crr != self.tail:
            ans.append(crr)
            crr = self.back[crr]
        return ans
