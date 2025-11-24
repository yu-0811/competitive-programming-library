class SumTopK:
  # 長さ N の配列 A の大きい方からK個の和を高速に管理する
  def __init__(self,N,A,K):
    self.A = A
    self.ok = SortedMultiset([0]*K) # 使うやつ
    self.ng = SortedMultiset([0]*(N-K)) # 使わないやつ
    self.ans = 0 # 大きい方からK個の和
  
  def add(self,y): # どこかの値がyに変わる
    self.ok.add(y)
    self.ans += y
    yy = self.ok[0]
    self.ans -= yy
    self.ok.discard(yy)
    self.ng.add(yy)
    
  def DEL(self,y): # yを削除する
    if y>=self.ok[0]:
      self.ok.discard(y)
      self.ans -= y
      yy = self.ng[-1]
      self.ng.discard(yy)
      self.ok.add(yy)
      self.ans += yy
    else:
      self.ng.discard(y)
  
  def update(self,x,y): # A[x]をyに更新し、K個の和を返す
    self.add(y)
    self.DEL(self.A[x])
    self.A[x] = y
    return self.ans