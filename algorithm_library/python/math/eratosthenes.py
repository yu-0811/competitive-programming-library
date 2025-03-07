# エラトステネスの篩
# O (N log log N)
def eratosthenes(N: int): 
  prime_number = list() # 素数
  isprime = [True] * (N+1) # isprime[i]==True なら i は素数
  isprime[0], isprime[1] = False, False
  for p in range(2, N+1):
      if not isprime[p]: continue
      q = p * 2
      while q <= N:
          isprime[q] = False
          q += p
  for p in range(2,N+1):
      if isprime[p]: prime_number.append(p)
  return prime_number, isprime

# M 以下の素数リストを返す
# O(M log log M)
def res_primeList(M):
    isprime = [True] * (M+1)
    isprime[0], isprime[1] = False, False
    for i in range(2, M+1):
        if i*i > M: break
        if isprime[i]:
            for j in range(i*i, M+1, i):
                isprime[j] = False
    return [i for i in range(2, M+1) if isprime[i]]