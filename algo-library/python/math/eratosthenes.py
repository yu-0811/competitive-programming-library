# エラトステネスの篩
# O (N log log N) (ほぼ線形)
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