from array import array
def doubling(nxt: list[int], max_steps: int) -> list[array]:
    """
    nxt: 状態iから1回遷移した後の状態nxt[i]
    max_steps: 最大遷移回数
    return dp[i][v] := v から 2**i 回遷移した先
    """
    assert all(0 <= v < len(nxt) for v in nxt)
    dp = [array('I', nxt)]
    for _ in range(1, max_steps.bit_length()):
        prev = dp[-1]
        cur = array('I', [0]) * len(prev)
        for v in range(len(prev)): cur[v] = prev[prev[v]]
        dp.append(cur)
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
