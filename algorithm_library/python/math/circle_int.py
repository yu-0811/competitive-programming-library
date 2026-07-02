Point = tuple[int, int]
Line = tuple[Point, Point]
Circle = tuple[Point, int]


# 符号を返す。正: 1, 負: -1, 0: 0
def sgn(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


# 2点・2ベクトルが等しいか
def point_eq(p: Point, q: Point) -> bool:
    return p[0] == q[0] and p[1] == q[1]


# set/sort 用の辞書順比較
def point_lt(p: Point, q: Point) -> bool:
    if p[0] != q[0]:
        return p[0] < q[0]
    return p[1] < q[1]


# ベクトル p + q
def add(p: Point, q: Point) -> Point:
    return p[0] + q[0], p[1] + q[1]


# ベクトル p - q
def sub(p: Point, q: Point) -> Point:
    return p[0] - q[0], p[1] - q[1]


# ベクトル p の整数 k 倍
def mul(p: Point, k: int) -> Point:
    return p[0] * k, p[1] * k


# 直線・線分 l の方向ベクトル B - A
def vec(l: Line) -> Point:
    return sub(l[1], l[0])


# 内積
def dot(p: Point, q: Point) -> int:
    return p[0] * q[0] + p[1] * q[1]


# 外積
def cross(p: Point, q: Point) -> int:
    return p[0] * q[1] - p[1] * q[0]


# ベクトルの長さの 2 乗
def norm(p: Point) -> int:
    return dot(p, p)


# 2点間距離の 2 乗
def dist2(p: Point, q: Point) -> int:
    return norm(sub(p, q))


# 反時計回りに 90 度回転
def rotate90(p: Point) -> Point:
    return -p[1], p[0]


# 点 c が有向線分 ab に対してどの位置にあるか
# 1: 反時計回り, -1: 時計回り, 2: a-b-c, -2: c-a-b, 0: a-c-b
def ccw(a: Point, b: Point, c: Point) -> int:
    ab = sub(b, a)
    ac = sub(c, a)
    cr = cross(ab, ac)
    if cr > 0:
        return 1
    if cr < 0:
        return -1
    if dot(ab, ac) < 0:
        return 2
    if norm(ab) < norm(ac):
        return -2
    return 0


# 点 p が直線 l 上にあるか
def point_on_line(p: Point, l: Line) -> bool:
    return cross(sub(p, l[0]), vec(l)) == 0


# 点 p が線分 l 上にあるか
def point_on_segment(p: Point, l: Line) -> bool:
    return point_on_line(p, l) and dot(sub(p, l[0]), sub(p, l[1])) <= 0


# 2直線が平行か
def is_parallel(l1: Line, l2: Line) -> bool:
    return cross(vec(l1), vec(l2)) == 0


# 2直線が直交するか
def is_orthogonal(l1: Line, l2: Line) -> bool:
    return dot(vec(l1), vec(l2)) == 0


# 2線分が交差するか。端点で接する場合も True
def segment_intersect(l1: Line, l2: Line) -> bool:
    return (
        ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) <= 0
        and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) <= 0
    )


def radius2(c: Circle) -> int:
    assert c[1] >= 0
    return c[1] * c[1]


# 点 p と円 c の位置関係。-1: 内部, 0: 円周上, 1: 外部
def point_circle_relation(p: Point, c: Circle) -> int:
    return sgn(dist2(p, c[0]) - radius2(c))


# 点 p が円 c の円周上にあるか
def point_on_circle(p: Point, c: Circle) -> bool:
    return point_circle_relation(p, c) == 0


# 点 p が円 c の内部または円周上にあるか
def point_in_circle(p: Point, c: Circle) -> bool:
    return point_circle_relation(p, c) <= 0


# 直線 l と円 c の交点数。ゼロ長直線の場合は assert で落とす
def line_circle_intersection_count(l: Line, c: Circle) -> int:
    v2 = norm(vec(l))
    assert v2 > 0
    cr = cross(sub(c[0], l[0]), vec(l))
    x = cr * cr - radius2(c) * v2
    if x > 0:
        return 0
    return 1 if x == 0 else 2


# 直線 l と円 c が交わるか。接する場合も True
def line_circle_intersect(l: Line, c: Circle) -> bool:
    return line_circle_intersection_count(l, c) > 0


# 線分 l と円 c の円周が交わるか。端点で接する場合も True
def segment_circle_intersect(l: Line, c: Circle) -> bool:
    r2 = radius2(c)
    d0 = dist2(l[0], c[0])
    d1 = dist2(l[1], c[0])
    if l[0] == l[1]:
        return d0 == r2
    if d0 == r2 or d1 == r2:
        return True
    if d0 < r2 and d1 < r2:
        return False
    if (d0 < r2) != (d1 < r2):
        return True

    v = vec(l)
    v2 = norm(v)
    assert v2 > 0
    if dot(sub(c[0], l[0]), v) < 0 or dot(sub(c[0], l[1]), mul(v, -1)) < 0:
        return False
    cr = cross(sub(c[0], l[0]), v)
    return cr * cr <= r2 * v2


# 2円 c1, c2 の交点数。完全に一致する場合は -1 を返す
def circle_intersection_count(c1: Circle, c2: Circle) -> int:
    center1, radius1 = c1
    center2, radius2_ = c2
    assert radius1 >= 0 and radius2_ >= 0
    d2 = dist2(center1, center2)
    if d2 == 0:
        return -1 if radius1 == radius2_ else 0

    diff2 = abs(radius1 - radius2_) ** 2
    sum2 = (radius1 + radius2_) ** 2
    if d2 < diff2 or sum2 < d2:
        return 0
    if d2 == diff2 or d2 == sum2:
        return 1
    return 2


# 2円 c1, c2 の円周が交わるか。完全に一致する場合も True
def circle_intersect(c1: Circle, c2: Circle) -> bool:
    return circle_intersection_count(c1, c2) != 0


# 2円 c1, c2 の共通接線の本数。完全に一致する場合は -1 を返す
def common_tangent_count(c1: Circle, c2: Circle) -> int:
    center1, radius1 = c1
    center2, radius2_ = c2
    assert radius1 >= 0 and radius2_ >= 0
    d2 = dist2(center1, center2)
    if d2 == 0 and radius1 == radius2_:
        return -1

    diff2 = abs(radius1 - radius2_) ** 2
    sum2 = (radius1 + radius2_) ** 2
    if d2 < diff2:
        return 0
    if d2 == diff2:
        return 1
    if d2 < sum2:
        return 2
    if d2 == sum2:
        return 3
    return 4
