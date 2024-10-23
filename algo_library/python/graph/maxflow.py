class maxflow_edge:
  def __init__(self, to, cap, rev_idx):
    self.to = to # 行き先
    self.cap = cap # 容量
    self.rev_idx = rev_idx # 逆向きの辺のインデックス

class maximum_flow():
  def __init__(self,N):
    self.G = [[] for _ in range(N+1)]
    self.N = N
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')
    sys.setrecursionlimit(10**7)
  
  def add_edge(self,a,b,c):
    self.G[a].append(maxflow_edge(b,c,len(self.G[b])))
    self.G[b].append(maxflow_edge(a,0,len(self.G[a])-1)) # 逆向き
  
  def dfs(self,v,goal,f):
    if v==goal: return f
    self.vis[v] = True
    for edge in self.G[v]:
      if edge.cap > 0 and self.vis[edge.to] == False:
        flow = self.dfs(edge.to, goal, min(f, edge.cap))
        # フローを流せるなら、残余グラフの容量を flow 増減させる
        if flow >= 1:
          edge.cap -= flow
          self.G[edge.to][edge.rev_idx].cap += flow
          return flow
    # 流せないなら
    return 0

  def maxflow(self,start,goal):
    total_flow = 0
    inf = pow(10,18)
    while True:
      self.vis = [False]*(self.N+1)
      res = self.dfs(start, goal, inf)
      if res > 0: total_flow += res
      else: break
    return total_flow