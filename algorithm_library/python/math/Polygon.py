eps = 1e-10

# contains の返り値
# _OUT: 外部, _ON: 辺上, _IN: 内部
_OUT = 0
_ON = 1
_IN = 2

Point = tuple[float, float]
Polygon = list[Point]


# ベクトル p - q
def sub(p: Point, q: Point) -> Point:
    return p[0] - q[0], p[1] - q[1]


# 内積
def dot(p: Point, q: Point) -> float:
    return p[0] * q[0] + p[1] * q[1]


# 外積
def cross(p: Point, q: Point) -> float:
    return p[0] * q[1] - p[1] * q[0]


# 多角形 q と点 p の包含判定
# _OUT: 外部, _ON: 辺上, _IN: 内部
def contains(q: Polygon, p: Point) -> int:
    inside = False
    n = len(q)
    for i in range(n):
        a = sub(q[i], p)
        b = sub(q[(i + 1) % n], p)
        if a[1] > b[1]:
            a, b = b, a
        if a[1] <= eps and eps < b[1] and cross(a, b) < -eps:
            inside = not inside
        if abs(cross(a, b)) < eps and dot(a, b) <= eps:
            return _ON
    return _IN if inside else _OUT
