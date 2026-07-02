Point = tuple[int, int]
Line = tuple[Point, Point]


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
