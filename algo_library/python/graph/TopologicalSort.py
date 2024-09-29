from collections import deque

def TopologicalSort(N,G):
  sortedVertices = list()
  indegree = [0]*(N+1)
  for v in range(1,N+1):
    for v2 in G[v]:
      indegree[v2] += 1
  
  que = deque()
  for v in range(1,N+1):
    if indegree[v]==0: que.append(v)
    
  # 入次数 0 の頂点とその頂点から出る辺を削除する
  while que:
    v = que.popleft()
    sortedVertices.append(v)
    for v2 in G[v]:
      indegree[v2] -= 1
      if indegree[v2]==0: que.append(v2)
  
  # 閉路があるなら空の配列を返す
  if len(sortedVertices)!=N: return []
  else: return sortedVertices