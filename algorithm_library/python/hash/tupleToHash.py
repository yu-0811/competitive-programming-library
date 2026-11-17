# 10^6 くらいまでは 22 で大丈夫
# 22 で 3 つとかならいける
# タイプ数を減らすためにグローバル変数

SIZE = 3
LEN = 0
MASK = (1 << 22) - 1


def to_hash(x, y, z):
    return (x << 44) | (y << 22) | z


def rev(h):
    x = (h >> 44) & MASK
    y = (h >> 22) & MASK
    z = h & MASK
    return x, y, z
