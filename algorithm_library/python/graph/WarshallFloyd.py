# タイプ数削減、余計なことを考えなくていいように、inf,N,G はグローバル変数
# グラフは 1-index

def WarshallFloyd():
  dist = [[inf]*(N+1) for _ in range(N+1)]
  for i in range(1,N+1): dist[i][i] = 0
  for i in range(1,N+1):
    for c,j in G[i]:
      if dist[i][j]>c: dist[i][j] = c
      if dist[j][i]>c: dist[i][j] = c
  
  for k in range(1,N+1):
    for i in range(1,N+1):
      for j in range(1,N+1):
        if i==j: continue
        if dist[i][j]>dist[i][k]+dist[k][j]:
          dist[i][j] = dist[i][k]+dist[k][j]
  
  return dist