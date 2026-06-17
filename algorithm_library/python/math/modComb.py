# 二項係数ライブラリ

# 前計算 O(n)
# O(1) で nCk, nHk を返す
class Comb:
  def __init__(self,n,mod):
    self.mod = mod
    self.n = n
    self.fact = [1, 1] 
    self.factinv = [1, 1]  
    self.inv = [0, 1] 
    for i in range(2,self.n+1):
        self.fact.append((self.fact[i-1] * i) % self.mod)
        self.inv.append((self.mod-self.inv[self.mod % i] * (self.mod // i)) % self.mod)
        self.factinv.append((self.factinv[i-1] * self.inv[i]) % self.mod)
        
  def C(self,n,k): # nCk % modを返す
    assert n <= self.n
    if (k < 0 or n < 0) or (n < k):return 0
    if k==1: return n
    k = min(k,n-k)
    return self.fact[n]*self.factinv[k]%self.mod*self.factinv[n-k]%self.mod

  # 重複組合せ nHr % modを返す
  def H(self,n,r):
      return self.C(n+r-1,r)

# O(k) 前計算
# O(k) で nCk を計算（n が大きいときでも使える）
class Comb:
    def __init__(self, k, mod):
        self.k = k
        self.mod = mod
        self.fact_inv = [0] * (k + 1)
        self.inv = [0] * (k + 1)
        self.fact_inv[0] = 1
        if k >= 1:
            self.fact_inv[1] = 1
            self.inv[1] = 1

        for i in range(2, k + 1):
            self.inv[i] = mod - self.inv[mod % i] * (mod // i) % mod
            self.fact_inv[i] = self.fact_inv[i - 1] * self.inv[i] % mod

    def nCk(self, n, k):
        if k < 0 or k > n:
            return 0
        if k > self.k:
            raise ValueError("precomputed k is too small")
        ans = 1
        for i in range(k):
            ans *= n - i
            ans %= self.mod
        return ans * self.fact_inv[k] % self.mod