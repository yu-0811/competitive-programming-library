# 無向グラフの場合は graphEdges にいつも通り u -> v と v -> u の両方を加える
# 重み付きグラフの場合は endList に格納する値を (終点, 重み) にすればよい

# 有向グラフのとき

# N := 頂点数
# graphEdges[i] := [辺 i の始点, 辺 i の終点]
def csr(N: int, graphEdges: list[list[int]]):
  start = [0]*(N+1)
  # endList := 辺を始点の昇順にソートした時の終点のリスト
  endList = [0]*len(graphEdges)

  # start[i+1] := 頂点 i を始点とする辺の数 となるように構築
  for u,v in graphEdges: # u -> v への辺
    start[u+1] += 1
  # start[i] := 始点の頂点番号が i 未満である辺の数 になるように累積和を取る
  # このとき、start[i] = endList で頂点 i が始点となる最小の index (0-index)
  for i in range(1,N+1):
    start[i] += start[i-1]

  # pointer[i] := 始点を i とする辺の endList への挿入位置
  pointer = start[:]
  for u,v in graphEdges:
    endList[pointer[u]] = v
    pointer[u] += 1
    
  return start, endList