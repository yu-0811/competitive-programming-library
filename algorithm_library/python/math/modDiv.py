def modDiv(P, Q, mod):  # P/Q mod m
    return P * pow(Q, -1, mod) % mod  # Q が同じなら前計算したほうが速い


def max_leq_congruent(R: int, r: int, m: int) -> int:
    """R 以下で r ≡ x (mod m) を満たす最大の整数 x を求める"""
    return R - ((R - r) % m)


def min_geq_congruent(L: int, r: int, m: int) -> int:
    """L 以上で r ≡ x (mod m) を満たす最小の整数 x を求める"""
    if m <= 0:
        raise ValueError("m must be positive")
    return L + ((r - L) % m)
