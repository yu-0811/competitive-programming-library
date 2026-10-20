# contains の返り値
# _OUT: 外部, _ON: 辺上, _IN: 内部
_OUT = 0
_ON = 1
_IN = 2

Point = tuple[int, int]
Polygon = list[Point]


# ベクトル p - q
def sub(p: Point, q: Point) -> Point:
    return p[0] - q[0], p[1] - q[1]


# 内積
def dot(p: Point, q: Point) -> int:
    return p[0] * q[0] + p[1] * q[1]


# 外積
def cross(p: Point, q: Point) -> int:
    return p[0] * q[1] - p[1] * q[0]


# 多角形 q と点 p の包含判定
# _OUT: 外部, _ON: 辺上, _IN: 内部
def contains(q: Polygon, p: Point) -> int:
    if not q:
        return _OUT
    inside = False
    px, py = p
    prev = q[-1]
    for cur in q:
        ax, ay = prev[0] - px, prev[1] - py
        bx, by = cur[0] - px, cur[1] - py
        prev = cur
        if ay > by:
            ax, bx = bx, ax
            ay, by = by, ay
        cr = ax * by - ay * bx
        if ay <= 0 < by and cr < 0:
            inside = not inside
        if cr == 0 and ax * bx + ay * by <= 0:
            return _ON
    return _IN if inside else _OUT
