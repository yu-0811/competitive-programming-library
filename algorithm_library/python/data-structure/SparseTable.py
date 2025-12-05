class SparseTable:
    def __init__(self, arr, op):
        """
        arr: 配列
        op: 演算 (結合則、冪等則を満たすこと)
        時間計算量: O(n log n) 構築, O(1) クエリ
        空間計算量: O(n log n)
        """
        self.op = op
        self.n = len(arr)
        self.max_k = (self.n - 1).bit_length()
        # table[k][i] = i から長さ 2^k の区間に対する演算結果
        self.table = [[0] * self.n for _ in range(self.max_k)]

        for i in range(self.n):
            self.table[0][i] = arr[i]
        for k in range(1, self.max_k):
            range_ = 1 << (k - 1)
            for i in range(self.n - (1 << k) + 1):
                self.table[k][i] = op(
                    self.table[k - 1][i], self.table[k - 1][i + range_]
                )

    def query(self, l, r):
        """
        [l, r) の区間に対する演算結果を返す O(1)
        """
        assert 0 <= l < r <= self.n
        # 2^k <= r - l を満たす最大の k を求める
        k = (r - l).bit_length() - 1
        # [l, l + 2^k) と [r - 2^k, r) の区間に分割して計算
        return self.op(self.table[k][l], self.table[k][r - (1 << k)])
