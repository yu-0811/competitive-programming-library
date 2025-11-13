# 組合せ総数ライブラリ
mod = 998244353

MAX = pow(10,6) # n の最大値
fact = [1, 1] 
factinv = [1, 1]  
inv = [0, 1] 
for i in range(2, MAX+1):
    fact.append((fact[i-1] * i) % mod)
    inv.append((mod-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[i-1] * inv[i]) % mod)
    
def modComb(n,k): # nCk % modを返す
  if (k < 0 or n<0) or (n < k):return 0
  if k==1: return n
  k = min(k,n-k)
  return fact[n]*factinv[k]%mod*factinv[n-k]%mod

# 重複組合せ nHr % modを返す
def modH(n,r):
    return modComb(n+r-1,r)