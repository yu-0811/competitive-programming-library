from collections import defaultdict

"""
高速素因数分解 https://atcoder.jp/contests/abc177/editorial/82
素因数分解をしたい最大の数を N として
構築 O(N log log N)
素因数分解 O(log N)
init_factorization の引数に最大の数 N を入れて初期化
"""
def init_factorization(N : int) -> list[int]:
  # N 以下の整数に対して最小の素因数を求める
  # D[i] = i の最小の素因数
  D = [1]*(N+1)
  for i in range(2,N+1):
    if D[i]!=1: continue
    for j in range(i,N+1,i):
      if D[j]==1: D[j] = i
  return D

D = init_factorization( ) 

# 素因数分解
def factorization(x : int) -> dict[int,int]: 
  res = defaultdict(int)
  while x!=1:
    res[D[x]] += 1
    x //= D[x]
  return res