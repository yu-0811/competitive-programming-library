class lazy_segtree(): # すべて 0-index
  def _update(self,k):self.data[k]=self.op(self.data[2*k],self.data[2*k+1])
  def _all_apply(self,k,f):
      self.data[k]=self.mapping(f,self.data[k])
      if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])
  def _push(self,k):
      self._all_apply(2*k,self.lz[k])
      self._all_apply(2*k+1,self.lz[k])
      self.lz[k]=self.identity
  def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
      self.n=len(V)
      self.log=(self.n-1).bit_length()
      self.size=1<<self.log
      self.data=[E for i in range(2*self.size)]
      self.lz=[ID for i in range(self.size)]
      self.e=E
      self.op=OP
      self.mapping=MAPPING
      self.composition=COMPOSITION
      self.identity=ID
      for i in range(self.n):self.data[self.size+i]=V[i]
      for i in range(self.size-1,0,-1):self._update(i)
  
  # 一点更新
  def set(self,p,x):
      assert 0<=p and p<self.n
      p+=self.size
      for i in range(self.log,0,-1):self._push(p>>i)
      self.data[p]=x
      for i in range(1,self.log+1):self._update(p>>i)
      
  # data[p] を取得する
  def get(self,p):
      assert 0<=p and p<self.n
      p+=self.size
      for i in range(self.log,0,-1):self._push(p>>i)
      return self.data[p]
    
  # 区間 [l,r) の演算結果を返す
  def prod(self,l,r):
      assert 0<=l and l<=r and r<=self.n
      if l==r:return self.e
      l+=self.size
      r+=self.size
      for i in range(self.log,0,-1):
          if (((l>>i)<<i)!=l):self._push(l>>i)
          if (((r>>i)<<i)!=r):self._push(r>>i)
      sml,smr=self.e,self.e
      while(l<r):
          if l&1:
              sml=self.op(sml,self.data[l])
              l+=1
          if r&1:
              r-=1
              smr=self.op(self.data[r],smr)
          l>>=1
          r>>=1
      return self.op(sml,smr)
  
  # 全区間の演算結果を返す
  def all_prod(self):return self.data[1]

  # 一点に対して操作する
  # あんまわからん
  def apply_point(self,p,f):
      assert 0<=p and p<self.n
      p+=self.size
      for i in range(self.log,0,-1):self._push(p>>i)
      self.data[p]=self.mapping(f,self.data[p])
      for i in range(1,self.log+1):self._update(p>>i)

  # 区間操作
  # f は mapping に与える引数の f
  def apply(self,l,r,f):
      assert 0<=l and l<=r and r<=self.n
      if l==r:return
      l+=self.size
      r+=self.size
      for i in range(self.log,0,-1):
          if (((l>>i)<<i)!=l):self._push(l>>i)
          if (((r>>i)<<i)!=r):self._push((r-1)>>i)
      l2,r2=l,r
      while(l<r):
          if (l&1):
              self._all_apply(l,f)
              l+=1
          if (r&1):
              r-=1
              self._all_apply(r,f)
          l>>=1
          r>>=1
      l,r=l2,r2
      for i in range(1,self.log+1):
          if (((l>>i)<<i)!=l):self._update(l>>i)
          if (((r>>i)<<i)!=r):self._update((r-1)>>i)
          
  # check(operate(data[l],data[l+1],...,data[r-1])) = True
  # を満たす最大の r を返す
  def max_right(self,l,check):
      assert 0<=l and l<=self.n
      assert check(self.e)
      if l==self.n:return self.n
      l+=self.size
      for i in range(self.log,0,-1):self._push(l>>i)
      sm=self.e
      while(1):
          while(l%2==0):l>>=1
          if not(check(self.op(sm,self.data[l]))):
              while(l<self.size):
                  self._push(l)
                  l=(2*l)
                  if (check(self.op(sm,self.data[l]))):
                      sm=self.op(sm,self.data[l])
                      l+=1
              return l-self.size
          sm=self.op(sm,self.data[l])
          l+=1
          if (l&-l)==l:break
      return self.n
  
  # check(operate(data[l],data[l+1],...,data[r-1])) = True
  # を満たす最小の l を返す
  def min_left(self,r,check):
      assert (0<=r and r<=self.n)
      assert check(self.e)
      if r==0:return 0
      r+=self.size
      for i in range(self.log,0,-1):self._push((r-1)>>i)
      sm=self.e
      while(1):
          r-=1
          while(r>1 and (r%2)):r>>=1
          if not(check(self.op(self.data[r],sm))):
              while(r<self.size):
                  self._push(r)
                  r=(2*r+1)
                  if check(self.op(self.data[r],sm)):
                      sm=self.op(self.data[r],sm)
                      r-=1
              return r+1-self.size
          sm=self.op(self.data[r],sm)
          if (r&-r)==r:break
      return 0

# data の単位元
e = 0
# lazy の単位元
# 区間更新なら lazy としてとりえない値にする
ide = 0

# 区間に対して行いたい演算
def operate(a,b):
  return a+b

# 遅延させていた操作をdataに伝搬させる関数
# f が遅延させた操作、x がdata
# ex. 区間加算なら f+x
def mapping(f,x):
  # 区間更新なら
  # if f==ide: return x
  return f+x

# 既に遅延させていた操作にさらに操作を追加する関数
# f が追加する操作、g がいままでの操作
def composition(f,g): 
  # 区間更新なら
  # if f==ide: return g
  return f+g


