import math

def range_eratosthenes(L : int, R : int) -> list[bool]:
    """
    [L,R] の素数のリスト[bool]を返す
    O(sqrt(R) log log R + (R-L) log log R)
    """
    assert L <= R
    sqrtR = int(math.sqrt(R)) + 1
    # sqrtR 以下の素数リスト
    is_prime_base = [True] * (sqrtR + 1)
    # [L,R] の素数リスト
    is_prime = [True] * (R - L + 1)
    
    for p in range(2, sqrtR + 1):
        if not is_prime_base[p]:
            continue
        
        # 以下 p は素数
        # sqrtR 以下の素数リストを更新
        q = p * 2
        while q <= sqrtR:
            is_prime_base[q] = False
            q += p
        
        # L 以上の最小の p の倍数
        start = L + ((-L) % p)
        if start == p: start = p * 2
        
        # [L,R] の素数リストを更新
        q = start
        while q <= R:
            is_prime[q - L] = False
            q += p
            
    return is_prime