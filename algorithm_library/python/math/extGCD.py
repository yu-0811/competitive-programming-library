# 拡張ユークリッドの互除法, 一次合同式

# ax + by = gcd(a,b) を満たす (x,y) を求める
# 返り値：gcd(a,b), x, y
def extGCD(a,b) -> tuple[int,int,int]:
    if b == 0:
        return a, 1, 0
    g,s,t = extGCD(b, a%b)
    # g = b * s + (a%b) * t
    #   = b * s + (a - a//b * b) * t
    #   = a * t + b * s + (-a//b * b * t)
    #   = a * t + b * (s - a//b * t)
    x = t
    y = s - a//b * t
    return g, x, y

# ax ≡ 1 (mod m) を満たす x (a^-1) を求める
def modinv(a,m) -> int:
    g,x,y = extGCD(a,m)
    assert g == 1, "a と m が互いに素でない"
    return x % m

# ax ≡ b (mod m) を満たす x を求める
def modlin(a,b,m) -> int:
    g,x,y = extGCD(a,m)
    if b % g != 0:
        return None # 解なし
    a //= g; b //= g; m //= g
    inv_a = modinv(a,m)
    return (inv_a * b) % m

# 中国剰余定理
# x ≡ B[i] (mod M[i]) を満たす x ≡ r (mod lcm(M)) を求める
# 返り値：解 r, lcm(M)
def chineseRem(B : list[int], M : list[int]) -> tuple[int,int]:
    assert len(B) == len(M)
    n = len(B)
    r = 0; m = 1
    for i in range(n):
        d, p, q = extGCD(m, M[i])
        if (B[i] - r) % d != 0:
            return None, None # 解なし
        tmp = (B[i] - r) // d * p % (M[i] // d)
        r += m * tmp
        m *= M[i] // d
    return r % m, m