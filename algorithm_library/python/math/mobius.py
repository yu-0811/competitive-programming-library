def mobius(A):
    """
    高速メビウス変換
    N = log_2 |A| として O(N 2^N)
    Args:
        A: サイズが 2^N のリスト
           A[mask] には「条件 mask を少なくとも満たす組合せの総和」が入っている
    Returns:
        A: 変換後のリスト (破壊的変更)
           A[mask] には「ちょうど条件 mask だけを満たす組合せ」が入る
    """
    n = len(A).bit_length() - 1
    assert len(A) == (1 << n), "配列の長さは 2^N である必要があります"

    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if not (mask & bit):
                A[mask] -= A[mask | bit]
    return A
