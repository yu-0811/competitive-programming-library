# 切り上げ除算
def ceilDiv(p: int, q: int) -> int:
    return (p + q - 1) // q


def max_leq_congruent(R: int, r: int, m: int) -> int:
    """R 以下で r ≡ x (mod m) を満たす最大の整数 x を求める"""
    r %= m
    return R - ((R - r) % m)


def min_geq_congruent(L: int, r: int, m: int) -> int:
    """L 以上で r ≡ x (mod m) を満たす最小の整数 x を求める"""
    if m <= 0:
        raise ValueError("m must be positive")
    r %= m
    return L + ((r - L) % m)
