# 全方位木DP
class rerooting:
  def __init__(self, n:int, edges:list[tuple[int,int]], identity:int, merge:callable, calc_node_value:callable, calc_ans:callable):
    self.n = n
    self.identity = identity
    self.merge = merge
    self.calc_node_value = calc_node_value
    self.calc_ans = calc_ans
    # adjacents[i] = i と隣接する頂点のリスト
    self.adjacents = [[] for _ in range(n+1)]
    # indexForAdjacents[i][j] = adjacents[i][j](iのj番目の隣接頂点)にとって、iが何番目の隣接頂点か
    # adjacents[adjacents[i][j]][indexForAdjacents[i][j]] == i である
    self.indexForAdjacents = [[] for _ in range(n+1)]
    for a, b in edges:
      self.indexForAdjacents[a].append(len(self.adjacents[b]))
      self.indexForAdjacents[b].append(len(self.adjacents[a]))
      self.adjacents[a].append(b)
      self.adjacents[b].append(a)
    # childSubTreeValue[i] = iの子の部分木の値
    # childSubTreeValue[i][j] = i を親とし、adjacents[i][j]を根とした部分木の値
    self.childSubTreeValue = [[self.identity] * len(self.adjacents[i]) for i in range(n+1)]
    # ans[i] = i を根としたときの求めたい値
    self.ans = [self.identity] * (n+1)
    
  # root から DFS して、子の部分木の値を計算
  def _dfs1(self, root):
    self.parent = [-1] * (self.n+1)
    self.order = [-1] * self.n # DFSでの訪問順
    stack = [root]
    idx = 0
    while stack:
      v = stack.pop()
      self.order[idx] = v
      idx += 1
      for u in self.adjacents[v]:
        if u == self.parent[v]:
          continue
        self.parent[u] = v
        stack.append(u)
    # 訪問順を逆順にして、子から値を計算していく
    for v in reversed(self.order[1:]):
      pv = self.parent[v]
      result = self.identity
      parentIndex = -1
      for i, u in enumerate(self.adjacents[v]):
        if u == pv:
          parentIndex = i
          continue
        result = self.merge(result, self.childSubTreeValue[v][i])
      # v を根とした部分木の値を親側に記録
      self.childSubTreeValue[pv][self.indexForAdjacents[v][parentIndex]] = self.calc_node_value(result, v)
  
  # 親の部分木の値を使って、自分を根とした部分木の値を計算
  def _dfs2(self):
    for v in self.order:
      # 子の部分木の値の左からの累積
      accFromLeft = self.identity
      # 子の部分木の値の右からの累積
      # accFromRight[i] = merge(childSubTreeValue[v][i+1], childSubTreeValue[v][i+2], ..., childSubTreeValue[v][len(adjacents[v])-1])
      accFromRight = [self.identity] * len(self.adjacents[v])
      for i in reversed(range(len(self.adjacents[v])-1)):
        accFromRight[i] = self.merge(self.childSubTreeValue[v][i+1], accFromRight[i+1])
      
      for j in range(len(self.adjacents[v])):
        u = self.adjacents[v][j]
        # u が親、v が根の部分木の値を計算(u を考慮しないときの値)
        # maerge(accFromLeft, accFromRight[j]) で u 以外の v の子の値を計算
        result = self.calc_node_value(self.merge(accFromLeft, accFromRight[j]), v)
        # いま親とした頂点の配列に記録
        self.childSubTreeValue[u][self.indexForAdjacents[v][j]] = result
        # accFromLeft を更新
        accFromLeft = self.merge(accFromLeft, self.childSubTreeValue[v][j])
      # v を根としたときの求めたい値を計算
      self.ans[v] = self.calc_ans(accFromLeft, v)
  
  def run(self, root=1):
    self._dfs1(root)
    self._dfs2()
    return self.ans

"""
identity = 頂点に持たせる値(関数のaに渡される)の単位元
merge(a, b) = 部分木の値 a, b をマージする関数
calc_node_value(a, v) = すべての子部分木の値をマージした値 a から頂点 v を根としたときの計算に使う値(DPの値)を計算する関数
calc_ans(a, v) = すべての子部分木の値をマージした値 a から頂点 v を根としたときの求めたいものを計算する関数
"""

# identity = 
# def merge(a,b):
#   return 
# def calc_node_value(a,v):
#   return 
# def calc_ans(a,v):
#     return 


# rr = rerooting(N, edges, identity, merge, calc_node_value, calc_ans)