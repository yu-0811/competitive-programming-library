from itertools import accumulate

# 二次元配列の長方形領域の値の和を計算できる
class cross_accumulate:
  # 二次元配列を渡す
  def __init__(self, grid : list[list[int]]):
    self.grid = self._crossAccumulate(grid)

  # 二次元累積和を取る
  def _crossAccumulate(self, grid):
    for i in range(len(grid)):
      grid[i] = list(accumulate(grid[i]))
    for j in range(len(grid[0])):
      for i in range(1,len(grid)):
        grid[i][j] += grid[i-1][j]
    return grid
      
  def query(self, i0: int, j0: int, i1: int, j1: int) -> int:
    """
    左上を(i0,j0), 右下を(i1,j1)する長方形領域の合計を返す
    
    grid[i0][j0], grid[i0][j0+1], ..., grid[i0][j1]
    grid[i0+1][j0], grid[i0+1][j0+1], ..., grid[i0+1][j1]
    ...
    grid[i1][j0], grid[i1][j0+1], ..., grid[i1][j1]
    """
    assert 0<=i0<=i1<len(self.grid) and 0<=j0<=j1<len(self.grid[0])
  
    res = 0
    if 0<=i0-1 and 0<=j0-1: res += self.grid[i0-1][j0-1]
    if 0<=i0-1: res -= self.grid[i0-1][j1]
    if 0<=j0-1: res -= self.grid[i1][j0-1]
    res += self.grid[i1][j1]
    return res