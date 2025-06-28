from collections import defaultdict,deque

# 二部グラフなら True と色分けを返す
def is_bipartite_graph(G : list[list[int]], N : int) -> tuple[bool, list[int]]:
  col = [-1]*(N+1)
  def dfs(v):
    que = deque()
    que.append(v)
    while que:
      v = que.pop()
      for v2 in G[v]:
        if col[v2]!=-1:
          if col[v]==col[v2]:
            return False
          continue
        col[v2] = 1-col[v]
        que.append(v2)
    return True

  for v in range(1,N+1):
    if col[v]!=-1: continue
    col[v] = 1
    if dfs(v) == False:
      return False, []
  
  return True, col