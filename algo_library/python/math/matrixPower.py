# 行列 A と 行列 B の積を返す
# mod がいらない時は消して
def mat_mul(A: list[list[int]], B: list[list[int]], mod):
  assert len(A[0])==len(B)
  res = [[0]*len(B[0]) for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        res[i][j] += A[i][k] * B[k][j]
        res[i][j] %= mod
  return res

# 行列累乗
# 行列 M^K
# ダブリングみたいにする(繰り返し二乗法)
def mat_pow(M: list[list[int]], K: int, mod: int):
  res = [[0]*len(M) for _ in range(len(M))]
  # 単位行列で初期化する
  for i in range(len(M)): res[i][i] = 1
  
  while (K>0):
    if (K&1==1): res = mat_mul(M,res,mod)
    M = mat_mul(M,M,mod)
    K >>= 1
  return res