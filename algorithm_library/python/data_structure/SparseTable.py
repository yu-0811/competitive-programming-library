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
        # table[k][i] = i から長さ 2^k の区間に対する演算結果
        self.tab = tab = [list(arr)]

        for k in range(n.bit_length() - 1):
            prev = tab[-1]
            row = prev[1 << k :]
            for i in range(len(row)):
                row[i] = op(prev[i], row[i])
            tab.append(row)

    def query(self, l, r):
        """
        [l, r) の区間に対する演算結果を返す O(1)
        """
        assert 0 <= l < r <= self.n
        # 2^k <= r - l を満たす最大の k を求める
        k = (r - l).bit_length() - 1
        # [l, l + 2^k) と [r - 2^k, r) の区間に分割して計算
        return self.op(self.tab[k][l], self.tab[k][r - (1 << k)])
