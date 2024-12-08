# クラスにしたいが、速度的に遅いので関数で
from itertools import accumulate

# 左上を(i0,j0), 右上を(i1,j1)とする長方形領域に d 加算する
# あえて返り値を None にしている(直接書き換えた方が速そう)
def applyRangeAddition(grid: list[list[int]], i0: int, j0: int, i1: int, j1: int, increment: int) -> None:
  assert i0<=i1 and j0<=j1
  grid[i0][j0] += increment
  if i1+1<len(grid): grid[i1+1][j0] -= increment
  if j1+1<len(grid[0]): grid[i0][j1+1] -= increment
  if i1+1<len(grid) and j1+1<len(grid[0]):
    grid[i1+1][j1+1] += increment
    
# 二次元累積和を取る
def crossAccumulate(grid: list[list[int]]) -> list[list[int]]:
  for i in range(len(grid)):
    grid[i] = list(accumulate(grid[i]))
  for j in range(len(grid[0])):
    for i in range(1,len(grid)):
      grid[i][j] += grid[i-1][j]
  return grid
    
# 左上を(i0,j0), 右上を(i1,j1)する長方形領域の合計を返す
def imos(grid: list[list[int]], i0: int, j0: int, i1: int, j1: int) -> int:
  res = 0
  if 0<=i0-1 and 0<=j0-1: res += grid[i0-1][j0-1]
  if 0<=i0-1: res -= grid[i0-1][j1]
  if 0<=j0-1: res -= grid[i1][j0-1]
  res += grid[i1][j1]
  return res