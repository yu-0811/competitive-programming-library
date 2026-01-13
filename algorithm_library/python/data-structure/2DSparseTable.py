# 未verified
# メモリ使用量に注意


class SparseTable2D:
    def __init__(self, grid, op):
        """
        grid: 2次元配列
        op: 演算 (結合則、冪等性が必要)
        O(H * W * logH * logW)
        """
        self.op = op
        self.H = len(grid)
        self.W = len(grid[0])
        self.K = self.H.bit_length()
        self.L = self.W.bit_length()

        # table[k][l][i][j]: 左上 (i, j)、高さ 2^k、幅 2^l の矩形に op を適用した結果
        self.table = [
            [[[0] * self.W for _ in range(self.H)] for _ in range(self.L)]
            for _ in range(self.K)
        ]

        for i in range(self.H):
            for j in range(self.W):
                self.table[0][0][i][j] = grid[i][j]

        # 行方向の構築 (高さ 1 固定で幅を拡大)
        for l in range(1, self.L):
            width = 1 << l
            half = width >> 1
            for i in range(self.H):
                # j から幅 2^l の区間が収まる範囲だけ計算
                for j in range(self.W - width + 1):
                    self.table[0][l][i][j] = op(
                        self.table[0][l - 1][i][j], self.table[0][l - 1][i][j + half]
                    )
        # 列方向の構築 (任意の幅 l に対して高さを拡大)
        for k in range(1, self.K):
            height = 1 << k
            half = height >> 1
            for l in range(self.L):
                width = 1 << l
                for i in range(self.H - height + 1):
                    for j in range(self.W - width + 1):
                        self.table[k][l][i][j] = op(
                            self.table[k - 1][l][i][j],
                            self.table[k - 1][l][i + half][j],
                        )

    def query(self, r1, c1, r2, c2):
        """
        (r1, c1) を左上, (r2, c2) を右下とする閉区間矩形の演算結果を返す
        0 <= r1 <= r2 < R, 0 <= c1 <= c2 < C
        """
        assert 0 <= r1 <= r2 < self.H
        assert 0 <= c1 <= c2 < self.W

        height = r2 - r1 + 1
        width = c2 - c1 + 1
        k = height.bit_length() - 1  # 2^k <= height を満たす最大の k
        l = width.bit_length() - 1  # 2^l <= width を満たす最大の l

        r2_start = r2 - (1 << k) + 1
        c2_start = c2 - (1 << l) + 1

        # 4つの長方形で (r1,c1)~(r2,c2) をカバーする
        tl = self.table[k][l][r1][c1]
        tr = self.table[k][l][r1][c2_start]
        bl = self.table[k][l][r2_start][c1]
        br = self.table[k][l][r2_start][c2_start]

        return self.op(self.op(tl, tr), self.op(bl, br))
