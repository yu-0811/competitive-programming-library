from bisect import bisect_right

class MergeSortTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1 << self.n.bit_length()
        self.tree = [[] for _ in range(2 * self.size)]
        self._build(data)

    def _build(self, data):
        for i in range(self.n):
            self.tree[self.size + i] = [data[i]]
        # 子ノードの要素をソートしてすべて持つように構築
        for i in range(self.size - 1, 0, -1):
           # マージソートの要領でマージ
            left_child = self.tree[2 * i]
            right_child = self.tree[2 * i + 1]
            l,r = 0,0
            while l < len(left_child) and r < len(right_child):
                if left_child[l] < right_child[r]:
                    self.tree[i].append(left_child[l])
                    l += 1
                else:
                    self.tree[i].append(right_child[r])
                    r += 1
            while l < len(left_child):
                self.tree[i].append(left_child[l])
                l += 1
            while r < len(right_child):
                self.tree[i].append(right_child[r])
                r += 1
            
    # 区間 [l, r) で値が x 以下の要素数を求める
    def query(self, l, r, x):
        l += self.size 
        r += self.size 
        res = 0
        while l < r:
            if (l&1):
                res += self._count_less_equal(self.tree[l], x)
                l += 1
            if (r&1):
                res += self._count_less_equal(self.tree[r-1], x)
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def _count_less_equal(self,array, x):
        return bisect_right(array, x)