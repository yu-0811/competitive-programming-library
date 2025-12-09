import math


# (x1,y1) - (x2,y2) の正規化ベクトルを返す
def normalize_vector(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
        dx = 0
        dy = 1
    elif dy == 0:
        dx = 1
        dy = 0
    else:
        if dx < 0:
            dx *= -1
            dy *= -1
        g = math.gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
    return dx, dy


# (x0,y0) - (x1,y1) を通る直線の上に (px,py) があるか
def on_line(x0, y0, x1, y1, px, py) -> bool:
    return (y1 - y0) * (px - x0) == (x1 - x0) * (py - y0)


# 2点 (x0, y0), (x1, y1) を通る直線 ax + by + c = 0 の (a, b, c) を返す
def get_line_abc(x0, y0, x1, y1):
    a = y1 - y0
    b = x0 - x1
    c = -(a * x0 + b * y0)
    return a, b, c
