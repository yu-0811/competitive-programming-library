# 座標圧縮
# ex. A=[2,9,9,7,9,2,4] -> 返り値=[0,3,3,2,3,0,1]
def compression(A):
    Adic = {x: i for i, x in enumerate(sorted(set(A)))}
    return [Adic[A[i]] for i in range(len(A))]
