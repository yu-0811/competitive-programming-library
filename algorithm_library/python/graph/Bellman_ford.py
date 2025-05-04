inf = pow(10,18)

def bellman_ford(Edges : list[tuple[int,int,int]], N : int, s : int) -> tuple[list[int], bool]:
  """
  Edges : 有向辺(無向のときは両方入れる)
  N : 頂点数
  s : 始点 
  返り値 : (最短距離配列, 負閉路の有無)
  """
  dist = [inf] * (N+1)
  dist[s] = 0
  cnt = 0
  while (cnt < N):
    end = True
    for fro, to, cost in Edges:
      if dist[to] > dist[fro] + cost:
        dist[to] = dist[fro] + cost
        end = False
    if end: break
    cnt += 1
  
  return dist, cnt == N