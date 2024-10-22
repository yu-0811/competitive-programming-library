class segtree(): # すべて 0-index
  def __init__(self,V,OP,E):
      self.n=len(V)
      self.op=OP
      self.e=E
      self.log=(self.n-1).bit_length()
      self.size=1<<self.log
      self.data=[E for i in range(2*self.size)]
      for i in range(self.n):
          self.data[self.size+i]=V[i]
      for i in range(self.size-1,0,-1):
          self._update(i)
          
  # 1 点更新
  def set(self,p,x): 
      assert 0<=p and p<self.n
      p+=self.size
      self.data[p]=x
      for i in range(1,self.log+1):
          self._update(p>>i)
          
  # 1 点加算(自分で書いた)
  def add(self,p,x): 
      assert 0<=p and p<self.n
      p+=self.size
      self.data[p] += x
      for i in range(1,self.log+1):
          self._update(p>>i)
          
  # data[p] を返す
  def get(self,p):
      assert 0<=p and p<self.n
      return self.data[p+self.size]
    
  # [l,r) の演算結果を返す
  def prod(self,l,r):
      assert 0<=l and l<=r and r<=self.n
      sml=self.e; smr=self.e
      l+=self.size; r+=self.size
      while(l<r):
          if (l&1):
              sml=self.op(sml,self.data[l])
              l+=1
          if (r&1):
              smr=self.op(self.data[r-1],smr)
              r-=1
          l>>=1
          r>>=1
      return self.op(sml,smr)
    
  # 全区間の演算結果を返す
  def all_prod(self):
      return self.data[1]
    
  # check(operate(data[l],data[l+1],...,data[r-1])) = True
  # を満たす最大の r を返す
  def max_right(self,l,check):
      assert 0<=l and l<=self.n
      assert check(self.e)
      if l==self.n: return self.n
      l+=self.size
      sm=self.e
      while True:
        while(l%2==0):
            l>>=1
        if not(check(self.op(sm,self.data[l]))):
            while(l<self.size):
                l=2*l
                if check(self.op(sm,self.data[l])):
                    sm=self.op(sm,self.data[l])
                    l+=1
            return l-self.size
        sm=self.op(sm,self.data[l])
        l+=1
        if (l&-l)==l: break
      return self.n
  
  # check(operate(data[l],data[l+1],...,data[r-1])) = True
  # を満たす最小の l を返す
  def min_left(self,r,check):
      assert 0<=r and r<=self.n
      assert check(self.e)
      if r==0: return 0
      r+=self.size
      sm=self.e
      while True:
        r-=1
        while(r>1 and (r%2)):
            r>>=1
        if not(check(self.op(self.data[r],sm))):
            while(r<self.size):
                r=(2*r+1)
                if check(self.op(self.data[r],sm)):
                    sm=self.op(self.data[r],sm)
                    r-=1
            return r+1-self.size
        sm=self.op(self.data[r],sm)
        if (r& -r)==r: break
      return 0
    
  def _update(self,k):
      self.data[k]=self.op(self.data[2*k],self.data[2*k+1])
      
  def __str__(self):
      return str([self.get(i) for i in range(self.n)])

class changeable_RollingHash:
  def __init__(self, S, base = 1237, mod = (1<<61)-1):
    N = len(S)
    self.ord_base = ord('a')
    self.base = base
    self.mod = mod 
    self.base_pow = [1] * (N + 1)
    self.base_inv = [1] * (N + 1)
    self.inv = pow(base,mod-2,mod)
    for i in range(N):
      self.base_pow[i+1] = (self.base_pow[i] * base) % mod
      self.base_inv[i+1] = (self.base_inv[i] * self.inv) % mod
    hash = [((ord(s)-self.ord_base+1)*self.base_pow[N-idx-1])%mod for idx,s in enumerate(S)]
    e = 0
    def operate(a,b): return (a+b)%mod
    self.seg = segtree(hash,operate,e)

  # インデックス x の要素を c に変える
  def change(self, x, c): 
    self.seg.set(x,((ord(c)-self.ord_base+1)*self.base_pow[self.N-x-1])%self.mod)
    
  def get_hash(self, l, r): #[l, r),0-index
    return (self.seg.prod(l,r) * self.base_inv[self.N-r]) % self.mod