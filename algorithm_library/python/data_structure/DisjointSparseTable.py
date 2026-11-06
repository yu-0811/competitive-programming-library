class DisjointSparseTable:
    def __init__(self, arr, op):
        """
        arr: 配列
        op: 演算 (結合律を満たすこと)
        """
        self.n = len(arr)
        self.arr = arr[:]
        self.op = op

        self.max_k = self.n.bit_length()
        self.table = [[0] * self.n for _ in range(self.max_k)]

        for k in range(self.max_k):
            block_size = 1 << (k + 1)  # ブロック全体の長さ
            half = 1 << k  # 半分の長さ

            for start in range(0, self.n, block_size):
                mid = min(start + half, self.n)
                end = min(start + block_size, self.n)

                # 左側 [start, mid) の累積を計算
                if start < mid:
                    cur = arr[mid - 1]
                    self.table[k][mid - 1] = cur
                    for i in range(mid - 2, start - 1, -1):
                        cur = op(arr[i], cur)
                        self.table[k][i] = cur

                # 右側 [mid, end) の累積を計算
                if mid < end:
                    cur = arr[mid]
                    self.table[k][mid] = cur
                    for i in range(mid + 1, end):
                        cur = op(cur, arr[i])
                        self.table[k][i] = cur

    def query(self, l, r):
        assert 0 <= l < r <= self.n
        if r - l == 1:
            return self.arr[l]

        # クエリに答えるために使うレベル k を求める
        k = (l ^ (r - 1)).bit_length() - 1
        return self.op(self.table[k][l], self.table[k][r - 1])
