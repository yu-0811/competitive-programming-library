from itertools import accumulate

# 二次元のimos法
class imos:
  def __init__(self, H : int, W : int):
    self.grid = [[0]*W for _ in range(H)]
    
  def add(self, i0: int, j0: int, i1: int, j1: int, increment: int) -> None:
    """
    左上を(i0,j0), 右下を(i1,j1)とする長方形領域に increment 加算する
    
    grid[i0][j0], grid[i0][j0+1], ..., grid[i0][j1]
    grid[i0+1][j0], grid[i0+1][j0+1], ..., grid[i0+1][j1]
    ...
    grid[i1][j0], grid[i1][j0+1], ..., grid[i1][j1]
    """
    assert 0<=i0<=i1<len(self.grid) and 0<=j0<=j1<len(self.grid[0])
    
    self.grid[i0][j0] += increment
    if i1+1<len(self.grid): self.grid[i1+1][j0] -= increment
    if j1+1<len(self.grid[0]): self.grid[i0][j1+1] -= increment
    if i1+1<len(self.grid) and j1+1<len(self.grid[0]):
      self.grid[i1+1][j1+1] += increment
      
  # 二次元累積和を取る
  def cross_accumulate(self):
    self.flag = True
    for i in range(len(self.grid)):
      self.grid[i] = list(accumulate(self.grid[i]))
    for j in range(len(self.grid[0])):
      for i in range(1,len(self.grid)):
        self.grid[i][j] += self.grid[i-1][j]
    return self.grid