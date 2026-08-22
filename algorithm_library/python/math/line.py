import math

eps = 1e-10
INF = 10**18

Point = tuple[float, float]
Line = tuple[Point, Point]


# 補助関数
# 誤差付きで符号を返す。正: 1, 負: -1, ほぼ 0: 0
def sgn(x: float) -> int:
    if x > eps:
        return 1
    if x < -eps:
        return -1
    return 0


# 2点・2ベクトルが誤差付きで等しいか
def point_eq(p: Point, q: Point) -> bool:
    return abs(p[0] - q[0]) < eps and abs(p[1] - q[1]) < eps


# set/sort 用の辞書順比較。誤差付きなので厳密な全順序が必要な用途には注意
def point_lt(p: Point, q: Point) -> bool:
    if abs(p[0] - q[0]) >= eps:
        return p[0] < q[0]
    return p[1] < q[1] - eps


# ベクトル p + q
def add(p: Point, q: Point) -> Point:
    return p[0] + q[0], p[1] + q[1]


# ベクトル p - q
def sub(p: Point, q: Point) -> Point:
    return p[0] - q[0], p[1] - q[1]


# ベクトル p の k 倍
def mul(p: Point, k: float) -> Point:
    return p[0] * k, p[1] * k


# ベクトル p を k で割る
def div(p: Point, k: float) -> Point:
    return p[0] / k, p[1] / k


# 直線・線分 l の方向ベクトル B - A
def vec(l: Line) -> Point:
    return sub(l[1], l[0])


# 内積
def dot(p: Point, q: Point) -> float:
    return p[0] * q[0] + p[1] * q[1]


# 外積
def cross(p: Point, q: Point) -> float:
    return p[0] * q[1] - p[1] * q[0]


# ベクトルの長さの 2 乗
def norm(p: Point) -> float:
    return dot(p, p)


# ベクトルの長さ
def length(p: Point) -> float:
    return math.hypot(p[0], p[1])


# 2点間距離
def dist(p: Point, q: Point) -> float:
    return length(sub(p, q))


# 反時計回りに 90 度回転
def rotate90(p: Point) -> Point:
    return -p[1], p[0]


# 反時計回りに theta ラジアン回転
def rotate(p: Point, theta: float) -> Point:
    c = math.cos(theta)
    s = math.sin(theta)
    return c * p[0] - s * p[1], s * p[0] + c * p[1]


# 点 c が有向線分 ab に対してどの位置にあるか
# 1: 反時計回り, -1: 時計回り, 2: a-b-c, -2: c-a-b, 0: a-c-b
def ccw(a: Point, b: Point, c: Point) -> int:
    ab = sub(b, a)
    ac = sub(c, a)
    cr = cross(ab, ac)
    if cr > eps:
        return 1
    if cr < -eps:
        return -1
    if dot(ab, ac) < -eps:
        return 2
    if norm(ab) < norm(ac) - eps:
        return -2
    return 0


# /////////////////////////////////////////////


# 点 p が直線 l 上にあるか
def point_on_line(p: Point, l: Line) -> bool:
    return abs(cross(sub(p, l[0]), vec(l))) < eps


# 点 p が線分 l 上にあるか
def point_on_segment(p: Point, l: Line) -> bool:
    return point_on_line(p, l) and dot(sub(p, l[0]), sub(p, l[1])) < eps


# 点 p から直線 l へ下ろした垂線の足
def projection(p: Point, l: Line) -> Point:
    v = vec(l)
    return add(l[0], mul(v, dot(sub(p, l[0]), v) / norm(v)))


# 点 p を直線 l に関して対称移動した点
def reflection(p: Point, l: Line) -> Point:
    return sub(mul(projection(p, l), 2), p)


# 点 p と直線 l の距離
def point_line_distance(p: Point, l: Line) -> float:
    return abs(cross(sub(p, l[0]), vec(l))) / length(vec(l))


# 点 p と線分 l の距離
def point_segment_distance(p: Point, l: Line) -> float:
    v = vec(l)
    if dot(sub(p, l[0]), v) < 0:
        return dist(p, l[0])
    if dot(sub(p, l[1]), v) > 0:
        return dist(p, l[1])
    return point_line_distance(p, l)


# 2直線が平行か
def is_parallel(l1: Line, l2: Line) -> bool:
    return abs(cross(vec(l1), vec(l2))) < eps


# 2直線が直交するか
def is_orthogonal(l1: Line, l2: Line) -> bool:
    return abs(dot(vec(l1), vec(l2))) < eps


# 2直線の交点。平行な場合は assert で落とす
def line_intersection(l1: Line, l2: Line) -> Point:
    assert not is_parallel(l1, l2)
    v1 = vec(l1)
    v2 = vec(l2)
    return add(l1[0], mul(v1, cross(sub(l2[0], l1[0]), v2) / cross(v1, v2)))


# 2線分が交差するか。端点で接する場合も True
def segment_intersect(l1: Line, l2: Line) -> bool:
    return (
        ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) <= 0
        and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) <= 0
    )


# 2線分間の距離。交差する場合は 0
def segment_distance(l1: Line, l2: Line) -> float:
    if segment_intersect(l1, l2):
        return 0
    return min(
        point_segment_distance(l1[0], l2),
        point_segment_distance(l1[1], l2),
        point_segment_distance(l2[0], l1),
        point_segment_distance(l2[1], l1),
    )
