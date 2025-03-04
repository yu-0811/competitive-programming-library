class UnionFind():
  # O(α(N)) はほぼ定数時間
  def __init__(self, n):
    self.n = n
    # 各頂点の親(1個上の要素)を記入
    # その頂点が根なら -1 以下の値
    # parents*-1 がその木のサイズ(要素数)
    self.parents = [-1] * (n+1)  

  # 頂点xの根を返す関数
  # 根まで上にたどる
  # 経路圧縮で x から根までに通る頂点をすべて根につなぎなおす
  # 経路圧縮によってこの関数が返す値は変わらない(根を返すから)
  # O(α(N))
  def root(self, x):
    if self.parents[x] < 0: return x # xが根ならxを返す
    else:
      self.parents[x] = self.root(self.parents[x]) # 経路圧縮
      return self.parents[x]

  # O(α(N))
  # マージ後の根を返す
  def union(self, x, y):
    x = self.root(x); y = self.root(y)
    if x == y: return x # x,y が同じグループならなにもしない
    # x,y は根であり、parents の値*-1 がその木のサイズ(要素数)
    # サイズが小さい方につなげる (union by size)
    if self.parents[x] > self.parents[y]: x, y = y, x # x が小さい方になるようにする
    self.parents[x] += self.parents[y] # サイズを更新
    self.parents[y] = x
    return x

  # 要素xが属するグループの要素数を返す
  # O(α(N))
  def size(self, x): return -self.parents[self.root(x)]

  # x,yが同じグループか(連結か)を返す関数
  # O(α(N))
  def isSame(self, x, y): return self.root(x) == self.root(y)

  # xが属するグループの要素をリストで返す
  # O(N)
  def members(self, x):
      root = self.root(x)
      return [i for i in range(self.n) if self.root(i) == root]

  # すべての根の要素をリストで返す
  # O(N)
  def get_roots(self): return [i for i, x in enumerate(self.parents) if x < 0]

  # グループの数を返す
  # O(N)
  def group_count(self): return len(self.roots())