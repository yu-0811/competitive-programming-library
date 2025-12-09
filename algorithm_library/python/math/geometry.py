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


def pos_after_t(sx, sy, gx, gy, t, v, dist=None):
    """
    始点(sx, sy) → 終点(gx, gy) を速さ v で動くとき、
    t 秒後の位置を返す（到達したらゴールにとどまる）。
    dist = 始点と終点の距離（前計算しといた方が速い）
    """
    # (dx,dy) = 方向ベクトル
    dx = gx - sx
    dy = gy - sy
    if dist is None:
        dist = math.sqrt(dx * dx + dy * dy)

    # 始点と終点が同じ
    if dist == 0 or v <= 0:
        return sx, sy

    # 進んだ距離
    move = v * t

    # すでに（またはちょうど）到達している
    if move >= dist:
        return gx, gy

    # 全体の何割進んだか
    u = move / dist

    # 方向ベクトルに進んだ距離をかける
    x = sx + dx * u
    y = sy + dy * u
    return x, y
