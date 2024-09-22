# 10^6 くらいまでは 22 で大丈夫
# 22 で 3 つとかならいける
# タイプ数を減らすためにグローバル変数

SIZE = 3
LEN = 0
MASK = (1<<22)-1

def to_hash(x,y,z):
  res = 0
  res |= x<<44
  res |= y<<22
  res |= z
  return res

def rev(h):
  x = (h>>44) & mask
  y = (h>>22) & mask
  z = h & mask
  return x,y,z