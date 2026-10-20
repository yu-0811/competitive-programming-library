# O(|S|)
# Z[i] := S[0:|S|) と S[i:|S|) の最長共通接頭辞の長さ
def z_algo(S):
    n = len(S)
    Z = [0] * n
    Z[0] = n
    i, j = 1, 0
    while i < n:
        # 一致する限り延長する
        while i + j < n and S[j] == S[i + j]:
            j += 1
        Z[i] = j

        # 一文字も一致しないならコピーできないので次に進む
        if j == 0:
            i += 1
            continue

        k = 1
        # k+Z[k]>j なら1回目の登場の際にはみ出してしまっている
        # k+Z[k]=j なら2回目の登場の際にはみ出す可能性がある
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        # まだ未確定なところまで i を進める
        i += k
        # j を i に合わせる
        j -= k

    return Z
