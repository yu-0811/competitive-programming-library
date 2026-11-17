# 切り上げ除算
def ceilDiv(p: int, q: int) -> int:
    return (p + q - 1) // q


# 等差数列の和
# 初項 a1, 項数 n, 公差 d
def cal(a1, n, d):
    return (n * (2 * a1 + (n - 1) * d)) // 2
