from random import randint
class MultisetHash:
  # 比較したい配列を引数に渡す
  def __init__(self,A: list, B: list) -> None:
    self.mod = (1<<61)-1
    self.hash = dict()
    for a in A: self.hash[a] = randint(1,self.mod-1)
    for b in B: self.hash[b] = randint(1,self.mod-1)
    # ハッシュを取る
    self.hashA,self.hashB = [0],[0]
    for a in A: 
      self.hashA.append((self.hashA[-1] + self.hash[a]) %self.mod)
    for b in B: 
      self.hashB.append((self.hashB[-1] + self.hash[b]) %self.mod)
    
  # 1-index(A_1, A_2, ...)
  # A[al:ar+1)==B[bl:br+1) を返す
  def isEqual(self,al,ar,bl,br):
    return (self.hashA[ar] - self.hashA[al-1])%self.mod == (self.hashB[br] - self.hashB[bl-1])%self.mod