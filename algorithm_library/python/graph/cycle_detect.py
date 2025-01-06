vis = [False]*(N+1)
fin = [False]*(N+1)
history = deque()

# 頂点 v の連結成分内の閉路を返す
def cycle_detect(v):
  sta = deque()
  sta.append((v,0))
  cycle_start = -1
  while sta and cycle_start == -1:
    v,prev = sta.pop()
    if prev == -1:
      history.pop()
      fin[v] = True
      continue
    if vis[v]: continue
    vis[v] = True
    history.append(v)
    for v2 in G[v]:
      if v2==prev: continue
      if fin[v2]: continue
      if vis[v2]: # 閉路検出
        cycle_start = v2
        break
      sta.append((v2,-1))
      sta.append((v2,v))
  
  cycle = list()
  if cycle_start == -1: return cycle
  while history:
    v = history.pop()
    cycle.append(v)
    if v == cycle_start: break
  return cycle