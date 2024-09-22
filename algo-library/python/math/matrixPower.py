# 行列累乗
mod = 998244353

# 行列 A と 行列 B の積を返す
# mod がいらない時は消して
def mat_mul(A: list[list[int]], B: list[list[int]]):
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
def mat_pow(M: list[list[int]], K: int):
  res = [[0]*len(M) for _ in range(len(M))]
  # 単位行列で初期化する
  for i in range(len(M)): res[i][i] = 1
  
  while (K>0):
    if (K&1==1): res = mat_mul(M,res)
    M = mat_mul(M,M)
    K >>= 1
  return res

# 使用例////////////////////

# 遷移行列
M = [[0]*52 for _ in range(52)]
# M^K
M_K = mat_pow(M,K)

# 初期ベクトル(初期状態)
V = [0]*52
# 初期化 ex. V[0] = 1

# K 回の移動後の状態
# M_K * V
result = [0]*52
for i in range(52):
  for j in range(52):
    result[i] += M_K[i][j]*V[j]
    result[i] %= mod