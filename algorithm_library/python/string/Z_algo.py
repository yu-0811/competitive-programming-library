# O(|S|)。Z[i] は S と S[i:] の最長共通接頭辞の長さ。
def z_algo(S):
    n = len(S)
    Z = [n] * n
    l = r = 0  # S[l:r] は接頭辞と一致する区間。r はここまでで最大
    for i in range(1, n):
        if i < r and Z[i - l] < r - i:
            Z[i] = Z[i - l]
            continue
        l, r = i, max(i, r)
        while r < n and S[r - l] == S[r]:
            r += 1
        Z[i] = r - l
    return Z
