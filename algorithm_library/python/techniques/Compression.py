# 座標圧縮
# ex. A=[2,9,9,7,9,2,4] -> 返り値=[1,4,4,3,4,1,2]
def compression(A):
  B = [0]*len(A)
  Adic = {x:i for i,x in enumerate(sorted(list(set(A))))}
  for i in range(len(A)):
    B[i] = Adic[A[i]]
  return B