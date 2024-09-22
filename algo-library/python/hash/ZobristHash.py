from random import randint
class ZobristHash:
  # 比較したい配列を引数に渡す
  def __init__(self,A: list, B: list) -> None:
    MAX = (1<<61)-1
    self.hash = dict()
    for a in A: self.hash[a] = randint(1,MAX)
    for b in B: self.hash[b] = randint(1,MAX)
    # ハッシュを取る
    self.hashA,self.hashB = [0],[0]
    setA,setB = set(),set()
    for a in A: 
      if a in setA:
        self.hashA.append(self.hashA[-1])
      else:
        self.hashA.append(self.hashA[-1] ^ self.hash[a])
        setA.add(a)
    for b in B: 
      if b in setB:
        self.hashB.append(self.hashB[-1])
      else:
        self.hashB.append(self.hashB[-1] ^ self.hash[b])
        setB.add(b)
    
  # 1-index(A_1, A_2, ...)
  # (A_al,A_{al+1},...,A_ar) == (B_al,B_{al+1},...,B_ar) を返す
  def isEqual(self,al,ar,bl,br):
    return (self.hashA[ar] - self.hashA[al-1]) == (self.hashB[br] - self.hashB[bl-1])