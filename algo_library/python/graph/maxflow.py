import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)

class maxflow_edge:
  def __init__(self, to, cap, rev_idx):
    self.to = to # 行き先
    self.cap = cap # 容量
    self.rev_idx = rev_idx # 逆向きの辺のインデックス

def dfs(v,goal,f,G,vis):
  if v==goal: return f
  vis[v] = True
  for edge in G[v]:
    if edge.cap > 0 and vis[edge.to] == False:
      flow = dfs(edge.to, goal, min(f, edge.cap), G, vis)
      # フローを流せるなら、残余グラフの容量を flow 増減させる
      if flow >= 1:
        edge.cap -= flow
        G[edge.to][edge.rev_idx].cap += flow
        return flow
  # 流せないなら
  return 0

def maxflow(N,M,start,goal):
  G = [[] for _ in range(N+1)]
  for _ in range(M):
    a,b,c = ms()
    G[a].append(maxflow_edge(b,c,len(G[b])))
    G[b].append(maxflow_edge(a,0,len(G[a])-1)) # 逆向き
  total_flow = 0
  inf = pow(10,18)
  while True:
    vis = [False]*(N+1)
    res = dfs(start, goal, inf, G, vis)
    if res > 0: total_flow += res
    else: break
  return total_flow