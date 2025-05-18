class PotentialUnionFind():
  def __init__(self,N) -> None:
    self.N = N
    self.parents = [-1]*(N+1)
    # 各要素の根からの距離
    # 相対的な重さを表す
    # 経路圧縮前は親ノードとの差分
    self.potential = [0]*(N+1)
    self.inf = pow(10,18)
    self.inconsistent = [False]*(N+1) # 連結成分に負閉路があるか（矛盾があるか）
  
  # 頂点xの根を返す関数
  # O(α(N))
  def root(self,x):
    if self.parents[x]<0: return x
    else:
      # 経路圧縮
      r = self.root(self.parents[x]) # 先に経路圧縮してポテンシャルを更新する
      self.potential[x] += self.potential[self.parents[x]] # ポテンシャルは根までの合計(根につないだ時につじつま合うように)
      self.parents[x] = r
      return self.parents[x]
  
  # potential[y] - potential[x]
  # y が x よりどれだけ重いか
  # 連結でないなら inf を返す
  # O(α(N))
  def dist(self,x,y):
    rx = self.root(x); ry = self.root(y)
    if rx==ry: # 同じ連結成分に属するなら
      return self.potential[y] - self.potential[x]
    else: return self.inf

  # x と y を距離 distance でつなぐ
  # 正確には potential[y] = potential[x] + distance になるようにつなぐ
  # x の下に y をつなぐ
  # y は x より w 重い
  # x -> y の重み distance の有向辺
  # 返り値は矛盾がなければ true
  # O(α(N))
  def union(self,x,y,w):
    rx = self.root(x); ry = self.root(y)
    if rx==ry: # 既に連結なら
      if self.potential[y] - self.potential[x] != w:
        self.inconsistent[rx] = True
      return self.potential[y] - self.potential[x] == w
    # ややこしいが、x-y をつなぐが、経路圧縮の都合で実装では rx-ry をつなぐことになる
    # union by size でつなげる
    if self.parents[ry] > self.parents[rx]:
      # rx の下に ry をつなぐ
      self.parents[rx] += self.parents[ry]
      self.potential[ry] = self.potential[x] + w - self.potential[y]
      self.parents[ry] = rx
    else:
      # ry の下に rx をつなぐ
      self.parents[ry] += self.parents[rx]
      self.potential[rx] = self.potential[y] - w - self.potential[x]
      self.parents[rx] = ry
    return True

  # 要素xが属するグループの要素数を返す
  # O(α(N))
  def size(self,x): return -self.parents[self.root(x)]

  # x,yが同じグループか(連結か)を返す関数
  # O(α(N))
  def isSame(self,x,y): return self.root(x)==self.root(y)
  
  # xが属するグループの要素をリストで返す
  # O(N)
  def members(self, x):
      root = self.root(x)
      return [i for i in range(1,self.N+1) if self.root(i) == root]

  # すべての根の要素をリストで返す
  # O(N × α(N))
  def roots(self): return [i for i, x in enumerate(self.parents) if x < 0]

  # グループの数を返す
  # O(N × α(N))
  def group_count(self): return len(self.roots())