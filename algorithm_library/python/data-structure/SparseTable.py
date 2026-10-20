class SparseTable:
    def __init__(self, arr, op):
        """
        arr: 配列
        op: 演算 (結合則、冪等則を満たすこと)
        時間計算量: O(n log n) 構築, O(1) クエリ
        空間計算量: O(n log n)
        """
        self.op = op
        self.n = n = len(arr)
        mk = n.bit_length()
        # table[k][i] = i から長さ 2^k の区間に対する演算結果
        self.table = table = [arr[:]] if n else []

        for k in range(1, mk):
            half_len = 1 << (k - 1)
            prev = table[-1]
            table.append(
                [op(prev[i], prev[i + half_len]) for i in range(n - (1 << k) + 1)]
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
