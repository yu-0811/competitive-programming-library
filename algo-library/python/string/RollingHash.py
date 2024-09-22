class RollingHash:
  def __init__(self, S, base = 1237, mod = (1<<61)-1):
    N = len(S)
    ord_base = ord('a')
    self.base = base
    self.mod = mod 
    self.hash = [0] * (N + 1)
    self.base_pow = [1] * (N + 1)
    for i in range(N):
      self.base_pow[i+1] = self.base_pow[i] * base % mod
    for idx, s in enumerate(S):
      tmp = ord(s) - ord_base + 1 # 0 を割り当ててはいけない
      self.hash[idx+1] = (self.hash[idx] * self.base + tmp) % mod

  def get_hash(self, l, r): #[l, r)
    return (self.hash[r] - self.hash[l] * self.base_pow[r - l]) % self.mod