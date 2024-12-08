from collections import deque

class SCC:
  def __init__(self, N: int):
    self.N = N # 頂点数
    self.graphEdges = list() # 辺
    self.inf = pow(10,9)
    
  def addEdge(self, frm: int, to: int):
    assert 0<=frm<=self.N
    assert 0<=to<=self.N
    self.graphEdges.append([frm,to])
  
  # 辺を CSR 形式にする
  # 高速化のため、python ではあんま意味ない？
  def _toCSR(self,N: int, graphEdges: list[list]):
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
  
  # 強連結成分分解をする
  def _decomposeToSCC(self):
    start, endList = self._toCSR(self.N, self.graphEdges)
    nowOrder = 0 # 訪れた頂点数
    groupNum = 0 # 見つかった強連結成分の数
    pendingStack = deque() # 探索済みかつ sccId が未確定の頂点を管理する stack
    lowlink = [0]*self.N
    order = [-1]*self.N # 頂点の行きがけ順
    groupId = [0]*self.N
    
    def dfs(v):
      nonlocal nowOrder, groupNum, pendingStack, lowlink, order, groupId
      dfsStack = deque()
      dfsStack.append(-(v+1))
      dfsStack.append(v)
      while dfsStack:
        v = dfsStack.pop()
        if v<0: # 帰りがけ
          # lowlink を更新する必要があるなら
          v *= -1
          v -= 1
          if v>=self.inf:
            frm = v//self.inf - 1
            to =  v%self.inf
            # lowlink[frm] = min(lowlink[frm], lowlink[to])
            if lowlink[frm]>lowlink[to]:
              lowlink[frm] = lowlink[to]
            v %= self.inf
            
          # scc_roote なら
          if lowlink[v] == order[v]:
            while True:
              u = pendingStack.pop()
              order[u] = self.inf # lowlink の計算に使われないように order を更新
              groupId[u] = groupNum # groupId を確定
              if u==v: break
            groupNum += 1
            
        else: # 行きがけ
          if order[v]!=-1: continue
          lowlink[v] = order[v] = nowOrder
          nowOrder += 1
          pendingStack.append(v)
          for i in range(start[v], start[v+1]):
            to = endList[i] # v -> to の辺
            if order[to]==-1: # 未探索なら
              dfsStack.append(-((to+1) + (v+1)*self.inf)) # 0-index で壊れないように v+1 に
              dfsStack.append(to)
            # 探索済みなら back edge か cross edge
            else:
              # lowlink[v] = min(lowlink[v], order[to])
              if lowlink[v]>order[to]:
                lowlink[v] = order[to]
          
    for v in range(self.N):
      if order[v]==-1: dfs(v)
    # 縮約後のグラフで groupId をトポロジカルソート順にする
    for v in range(self.N):
      groupId[v] = groupNum-1-groupId[v]
      
    return groupNum, groupId
  
  # groups[i] = グループID i に属する頂点の集合を 返す
  def doSCC(self):
    groupNum, groupId = self._decomposeToSCC()
    groups = [[] for _ in range(groupNum)]
    for v in range(self.N):
      groups[groupId[v]].append(v)
    return groups
