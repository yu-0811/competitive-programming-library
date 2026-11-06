# 未verified
# メモリ使用量に注意


class SparseTable2D:
    def __init__(self, grid, op):
        """
        grid: 空でない2次元配列
        op: 演算 (結合則、可換性、冪等性が必要)
        構築・空間: O(H * W * logH * logW), クエリ: O(1)
        """
        self.op = op
        self.H = len(grid)
        self.W = len(grid[0])
        self.K = self.H.bit_length()
        self.L = self.W.bit_length()

        # table[k][l][i][j]: 左上 (i, j)、高さ 2^k、幅 2^l の矩形
        # 各段は矩形が収まる位置だけ保持する
        self.table = table = [[[row[:] for row in grid]]]

        for l in range(1, self.L):
            half = 1 << (l - 1)
            table[0].append([list(map(op, row, row[half:])) for row in table[0][-1]])
        for k in range(1, self.K):
            half = 1 << (k - 1)
            table.append(
                [
                    [list(map(op, top, bottom)) for top, bottom in zip(prev, prev[half:])]
                    for prev in table[-1]
                ]
            )

    def query(self, r1, c1, r2, c2):
        """
        (r1, c1) を左上, (r2, c2) を右下とする閉区間矩形の演算結果を返す
        0 <= r1 <= r2 < H, 0 <= c1 <= c2 < W
        """
        assert 0 <= r1 <= r2 < self.H
        assert 0 <= c1 <= c2 < self.W

        k = (r2 - r1 + 1).bit_length() - 1
        l = (c2 - c1 + 1).bit_length() - 1
        rows = self.table[k][l]
        top = rows[r1]
        bottom = rows[r2 - (1 << k) + 1]
        c2 = c2 - (1 << l) + 1
        op = self.op
        return op(op(top[c1], top[c2]), op(bottom[c1], bottom[c2]))
