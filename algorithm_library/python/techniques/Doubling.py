def doubling(dp, LEN, POW):
    for i in range(1, POW):
        prev, cur = dp[i - 1], dp[i]
        for j in range(LEN):
            cur[j] = prev[prev[j]]
    return dp


def query(dp, j, k):
    """
    j から始めて k 回移動する
    """
    tmp = j
    while k:
        i = k.bit_length() - 1
        tmp = dp[i][tmp]
        k ^= 1 << i
    return tmp
