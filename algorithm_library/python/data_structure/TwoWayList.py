# 双方向連結リスト 
# 要素はハッシュ可能・重複不可。挿入・削除は平均 O(1)。


class TwoWayList:
    def __init__(self, L=()):
        self.head, self.tail = object(), object()
        self.front = {self.tail: self.head}
        self.back = {self.head: self.tail}
        for x in L:
            self.insert_front(self.tail, x)

    def insert_front(self, x, y):  # 値xの前にyを挿入する
        self.insert_back(self.front[x], y)

    def insert_back(self, x, y):  # 値xの直後にyを挿入する
        b = self.back[x]
        self.back[x] = self.front[b] = y
        self.front[y], self.back[y] = x, b

    def del_x(self, x):  # 値xを削除する
        a, b = self.front.pop(x), self.back.pop(x)
        self.back[a], self.front[b] = b, a

    def res_LIST(self):  # リストを返す
        ans = []
        x = self.back[self.head]
        while x is not self.tail:
            ans.append(x)
            x = self.back[x]
        return ans
