# 行ベクトル v と行列 M の積。M は長方形でもよい。
def vec_mul(v: list[int], M: list[list[int]], mod: int):
    k = len(v)
    assert k == len(M)
    n = len(M[0]) if M else 0
    res = [0] * n
    rem = k % 4
    for x, row in zip(v[:rem], M):
        res = [(t + x*y) % mod for t, y in zip(res, row)]
    # 4 行ずつまとめ、各列の読み書きと剰余の回数を減らす。
    for i in range(rem, k, 4):
        a, b, c, d = v[i:i + 4]
        if a or b or c or d:
            A, B, C, D = M[i:i + 4]
            for j in range(n):
                res[j] = (res[j] + a*A[j] + b*B[j]
                          + c*C[j] + d*D[j]) % mod
    return res


# 行列 A と行列 B の積を返す
def mat_mul(A: list[list[int]], B: list[list[int]], mod):
    return [vec_mul(row, B, mod) for row in A]


# 行列累乗 M^K
def mat_pow(M: list[list[int]], K: int, mod: int):
    res = []
    while K > 0:
        if K & 1:
            if not res:
                # 最初の単位行列との積は、剰余を取ったコピーで置き換える
                res = [[x % mod for x in row] for row in M]
            else:
                res = mat_mul(M, res, mod)
        K >>= 1
        if K:
            M = mat_mul(M, M, mod)

    if not res:
        res = [[0] * len(M) for _ in range(len(M))]
        for i in range(len(M)):
            res[i][i] = 1
    return res
