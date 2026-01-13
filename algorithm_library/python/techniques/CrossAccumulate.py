class CrossAccumulate:
    def __init__(self, grid: list[list[int]]):
        self.H = len(grid)
        self.W = len(grid[0])
        self.s = [[0] * (self.W + 1) for _ in range(self.H + 1)]

        for i in range(self.H):
            for j in range(self.W):
                self.s[i + 1][j + 1] = (
                    self.s[i][j + 1] + self.s[i + 1][j] - self.s[i][j] + grid[i][j]
                )

    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        左上(r1,c1), 右下(r2,c2) の閉区間矩形の和を返す
        """
        assert 0 <= r1 <= r2 < self.H and 0 <= c1 <= c2 < self.W
        return (
            self.s[r2 + 1][c2 + 1]
            - self.s[r1][c2 + 1]
            - self.s[r2 + 1][c1]
            + self.s[r1][c1]
        )
