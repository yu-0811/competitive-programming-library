import math

eps = 1e-10
INF = 10**18

Point3D = tuple[float, float, float]
Line3D = tuple[Point3D, Point3D]
Plane3D = tuple[Point3D, Point3D]  # (平面上の点, 法線ベクトル)
Sphere3D = tuple[Point3D, float]
Circle3D = tuple[Point3D, Point3D, float]  # (中心, 円を含む平面の法線, 半径)


# 誤差付きで符号を返す。正: 1, 負: -1, ほぼ 0: 0
def sgn(x: float) -> int:
    if x > eps:
        return 1
    if x < -eps:
        return -1
    return 0


# [0, 1] に丸める
def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


# acos などに渡す値を [-1, 1] に丸める
def clamp_unit(x: float) -> float:
    return max(-1.0, min(1.0, x))


# 2点・2ベクトルが誤差付きで等しいか
def point_eq(p: Point3D, q: Point3D) -> bool:
    return abs(p[0] - q[0]) < eps and abs(p[1] - q[1]) < eps and abs(p[2] - q[2]) < eps


# set/sort 用の辞書順比較。誤差付きなので厳密な全順序が必要な用途には注意
def point_lt(p: Point3D, q: Point3D) -> bool:
    if abs(p[0] - q[0]) >= eps:
        return p[0] < q[0]
    if abs(p[1] - q[1]) >= eps:
        return p[1] < q[1]
    return p[2] < q[2] - eps


# ベクトル p + q
def add(p: Point3D, q: Point3D) -> Point3D:
    return p[0] + q[0], p[1] + q[1], p[2] + q[2]


# ベクトル p - q
def sub(p: Point3D, q: Point3D) -> Point3D:
    return p[0] - q[0], p[1] - q[1], p[2] - q[2]


# ベクトル p の k 倍
def mul(p: Point3D, k: float) -> Point3D:
    return p[0] * k, p[1] * k, p[2] * k


# ベクトル p を k で割る
def div(p: Point3D, k: float) -> Point3D:
    return p[0] / k, p[1] / k, p[2] / k


# 3点 a, b, c を通る平面を作る。3点が一直線上の場合は法線がゼロになる
def make_plane(a: Point3D, b: Point3D, c: Point3D) -> Plane3D:
    return a, cross(sub(b, a), sub(c, a))


# 直線・線分 l の方向ベクトル B - A
def vec(l: Line3D) -> Point3D:
    return sub(l[1], l[0])


# 内積
def dot(p: Point3D, q: Point3D) -> float:
    return p[0] * q[0] + p[1] * q[1] + p[2] * q[2]


# 外積
def cross(p: Point3D, q: Point3D) -> Point3D:
    return (
        p[1] * q[2] - p[2] * q[1],
        p[2] * q[0] - p[0] * q[2],
        p[0] * q[1] - p[1] * q[0],
    )


# スカラー三重積。符号付き平行六面体体積
def triple(a: Point3D, b: Point3D, c: Point3D) -> float:
    return dot(a, cross(b, c))


# ベクトルの長さの 2 乗
def norm(p: Point3D) -> float:
    return dot(p, p)


# ベクトルの長さ
def length(p: Point3D) -> float:
    return math.sqrt(norm(p))


# 2点間距離
def dist(p: Point3D, q: Point3D) -> float:
    return length(sub(p, q))


# 単位ベクトル。ゼロベクトルの場合は assert で落とす
def unit(p: Point3D) -> Point3D:
    l = length(p)
    assert l > eps
    return div(p, l)


# 2ベクトルのなす角 [0, pi]
def angle(p: Point3D, q: Point3D) -> float:
    assert length(p) > eps and length(q) > eps
    return math.acos(clamp_unit(dot(p, q) / length(p) / length(q)))


# 原点を通る axis を軸として p を theta ラジアン回転
def rotate_around_axis(p: Point3D, axis: Point3D, theta: float) -> Point3D:
    u = unit(axis)
    c = math.cos(theta)
    s = math.sin(theta)
    return add(add(mul(p, c), mul(cross(u, p), s)), mul(u, dot(u, p) * (1 - c)))


# 直線 axis を軸として p を theta ラジアン回転
def rotate(p: Point3D, axis: Line3D, theta: float) -> Point3D:
    return add(axis[0], rotate_around_axis(sub(p, axis[0]), vec(axis), theta))


# 3点 a, b, c を頂点とする三角形の面積
def triangle_area(a: Point3D, b: Point3D, c: Point3D) -> float:
    return length(cross(sub(b, a), sub(c, a))) / 2


# 4点 a, b, c, d を頂点とする四面体の体積
def tetrahedron_volume(a: Point3D, b: Point3D, c: Point3D, d: Point3D) -> float:
    return abs(triple(sub(b, a), sub(c, a), sub(d, a))) / 6


# 点 p が直線 l 上にあるか
def point_on_line(p: Point3D, l: Line3D) -> bool:
    v = vec(l)
    assert length(v) > eps
    return length(cross(sub(p, l[0]), v)) <= eps * length(v)


# 点 p が線分 s 上にあるか
def point_on_segment(p: Point3D, s: Line3D) -> bool:
    return point_on_line(p, s) and dot(sub(p, s[0]), sub(p, s[1])) <= eps


# 点 p から直線 l へ下ろした垂線の足
def projection_on_line(p: Point3D, l: Line3D) -> Point3D:
    v = vec(l)
    assert length(v) > eps
    return add(l[0], mul(v, dot(sub(p, l[0]), v) / norm(v)))


# 点 p を直線 l に関して対称移動した点
def reflection_about_line(p: Point3D, l: Line3D) -> Point3D:
    return sub(mul(projection_on_line(p, l), 2), p)


# 線分 s 上で点 p に最も近い点
def closest_point_on_segment(p: Point3D, s: Line3D) -> Point3D:
    v = vec(s)
    if norm(v) < eps:
        return s[0]
    t = clamp01(dot(sub(p, s[0]), v) / norm(v))
    return add(s[0], mul(v, t))


# 点 p と直線 l の距離
def point_line_distance(p: Point3D, l: Line3D) -> float:
    v = vec(l)
    assert length(v) > eps
    return length(cross(sub(p, l[0]), v)) / length(v)


# 点 p と線分 s の距離
def point_segment_distance(p: Point3D, s: Line3D) -> float:
    return dist(p, closest_point_on_segment(p, s))


# 2直線が平行か
def is_parallel_lines(l1: Line3D, l2: Line3D) -> bool:
    assert length(vec(l1)) > eps and length(vec(l2)) > eps
    return length(cross(vec(l1), vec(l2))) < eps


# 2直線が直交するか
def is_orthogonal_lines(l1: Line3D, l2: Line3D) -> bool:
    assert length(vec(l1)) > eps and length(vec(l2)) > eps
    return abs(dot(vec(l1), vec(l2))) < eps


# 2直線が同一直線か
def same_line(l1: Line3D, l2: Line3D) -> bool:
    return is_parallel_lines(l1, l2) and point_on_line(l2[0], l1)


# 2直線間の距離。ねじれの位置にも対応
def line_line_distance(l1: Line3D, l2: Line3D) -> float:
    u = vec(l1)
    v = vec(l2)
    assert length(u) > eps and length(v) > eps
    w = cross(u, v)
    if length(w) < eps:
        return point_line_distance(l2[0], l1)
    return abs(triple(sub(l2[0], l1[0]), u, v)) / length(w)


# 2直線上の最近点の組。平行な場合は assert で落とす
def closest_points_between_lines(l1: Line3D, l2: Line3D) -> tuple[Point3D, Point3D]:
    u = vec(l1)
    v = vec(l2)
    w = sub(l1[0], l2[0])
    a = dot(u, u)
    b = dot(u, v)
    c = dot(v, v)
    d = dot(u, w)
    e = dot(v, w)
    den = a * c - b * b
    assert length(u) > eps and length(v) > eps and abs(den) > eps
    s = (b * e - c * d) / den
    t = (a * e - b * d) / den
    return add(l1[0], mul(u, s)), add(l2[0], mul(v, t))


# 2直線が交差するか
def line_intersect(l1: Line3D, l2: Line3D) -> bool:
    return line_line_distance(l1, l2) <= eps


# 2直線の交点。平行な場合やねじれの位置の場合は assert で落とす
def line_intersection(l1: Line3D, l2: Line3D) -> Point3D:
    assert line_intersect(l1, l2) and not is_parallel_lines(l1, l2)
    p, q = closest_points_between_lines(l1, l2)
    return div(add(p, q), 2)


# 2線分上の最近点の組。線分が退化して点になっている場合にも対応
def closest_points_between_segments(s1: Line3D, s2: Line3D) -> tuple[Point3D, Point3D]:
    u = vec(s1)
    v = vec(s2)
    w = sub(s1[0], s2[0])
    a = dot(u, u)
    b = dot(u, v)
    c = dot(v, v)
    d = dot(u, w)
    e = dot(v, w)
    den = a * c - b * b

    if a < eps and c < eps:
        return s1[0], s2[0]
    if a < eps:
        return s1[0], closest_point_on_segment(s1[0], s2)
    if c < eps:
        return closest_point_on_segment(s2[0], s1), s2[0]

    sd = den
    td = den
    if den < eps:
        sn = 0.0
        sd = 1.0
        tn = e
        td = c
    else:
        sn = b * e - c * d
        tn = a * e - b * d
        if sn < 0.0:
            sn = 0.0
            tn = e
            td = c
        elif sn > sd:
            sn = sd
            tn = e + b
            td = c

    if tn < 0.0:
        tn = 0.0
        if -d < 0.0:
            sn = 0.0
        elif -d > a:
            sn = sd
        else:
            sn = -d
            sd = a
    elif tn > td:
        tn = td
        if -d + b < 0.0:
            sn = 0.0
        elif -d + b > a:
            sn = sd
        else:
            sn = -d + b
            sd = a

    s = 0.0 if abs(sn) < eps else sn / sd
    t = 0.0 if abs(tn) < eps else tn / td
    return add(s1[0], mul(u, s)), add(s2[0], mul(v, t))


# 2線分間の距離。交差する場合は 0
def segment_distance(s1: Line3D, s2: Line3D) -> float:
    p, q = closest_points_between_segments(s1, s2)
    return dist(p, q)


# 2線分が交差するか。端点で接する場合も True
def segment_intersect(s1: Line3D, s2: Line3D) -> bool:
    return segment_distance(s1, s2) <= eps


# 点 p が平面 h 上にあるか
def point_on_plane(p: Point3D, h: Plane3D) -> bool:
    plane_point, normal = h
    assert length(normal) > eps
    return abs(dot(sub(p, plane_point), normal)) <= eps * length(normal)


# 点 p から平面 h へ下ろした垂線の足
def projection_on_plane(p: Point3D, h: Plane3D) -> Point3D:
    plane_point, normal = h
    assert length(normal) > eps
    return sub(p, mul(normal, dot(sub(p, plane_point), normal) / norm(normal)))


# 点 p を平面 h に関して対称移動した点
def reflection_about_plane(p: Point3D, h: Plane3D) -> Point3D:
    return sub(mul(projection_on_plane(p, h), 2), p)


# 点 p と平面 h の符号付き距離。法線方向が正
def signed_point_plane_distance(p: Point3D, h: Plane3D) -> float:
    plane_point, normal = h
    assert length(normal) > eps
    return dot(sub(p, plane_point), normal) / length(normal)


# 点 p と平面 h の距離
def point_plane_distance(p: Point3D, h: Plane3D) -> float:
    return abs(signed_point_plane_distance(p, h))


# 直線 l と平面 h が平行か
def is_parallel_line_plane(l: Line3D, h: Plane3D) -> bool:
    _, normal = h
    assert length(vec(l)) > eps and length(normal) > eps
    return abs(dot(vec(l), normal)) < eps


# 直線 l と平面 h が直交するか
def is_orthogonal_line_plane(l: Line3D, h: Plane3D) -> bool:
    _, normal = h
    assert length(vec(l)) > eps and length(normal) > eps
    return length(cross(vec(l), normal)) < eps


# 直線 l が平面 h 上にあるか
def line_on_plane(l: Line3D, h: Plane3D) -> bool:
    return point_on_plane(l[0], h) and point_on_plane(l[1], h)


# 直線 l と平面 h の交点。平行な場合は assert で落とす
def line_plane_intersection(l: Line3D, h: Plane3D) -> Point3D:
    plane_point, normal = h
    assert not is_parallel_line_plane(l, h)
    v = vec(l)
    t = dot(sub(plane_point, l[0]), normal) / dot(v, normal)
    return add(l[0], mul(v, t))


# 直線 l と平面 h の距離。交差する場合は 0
def line_plane_distance(l: Line3D, h: Plane3D) -> float:
    if not is_parallel_line_plane(l, h):
        return 0.0
    return point_plane_distance(l[0], h)


# 2平面が平行か
def is_parallel_planes(h1: Plane3D, h2: Plane3D) -> bool:
    assert length(h1[1]) > eps and length(h2[1]) > eps
    return length(cross(h1[1], h2[1])) < eps


# 2平面が直交するか
def is_orthogonal_planes(h1: Plane3D, h2: Plane3D) -> bool:
    assert length(h1[1]) > eps and length(h2[1]) > eps
    return abs(dot(h1[1], h2[1])) < eps


# 2平面が同一平面か
def same_plane(h1: Plane3D, h2: Plane3D) -> bool:
    return is_parallel_planes(h1, h2) and point_on_plane(h2[0], h1)


# 2平面の交線。平行な場合は assert で落とす
def plane_intersection(h1: Plane3D, h2: Plane3D) -> Line3D:
    assert not is_parallel_planes(h1, h2)
    p1, n1 = h1
    p2, n2 = h2
    direction = cross(n1, n2)
    d1 = dot(n1, p1)
    d2 = dot(n2, p2)
    point = div(cross(sub(mul(n2, d1), mul(n1, d2)), direction), norm(direction))
    return point, add(point, direction)


# 2平面間の距離。交差する場合は 0
def plane_plane_distance(h1: Plane3D, h2: Plane3D) -> float:
    if not is_parallel_planes(h1, h2):
        return 0.0
    return point_plane_distance(h2[0], h1)


# 点 p が球 s の内部または表面にあるか
def point_in_sphere(p: Point3D, s: Sphere3D) -> bool:
    center, radius = s
    return dist(p, center) <= radius + eps


# 点 p が球 s の表面にあるか
def point_on_sphere(p: Point3D, s: Sphere3D) -> bool:
    center, radius = s
    return abs(dist(p, center) - radius) <= eps


# 直線 l と球 s の交点。0個、接する場合は1個、通常は2個返す
def line_sphere_intersection(l: Line3D, s: Sphere3D) -> list[Point3D]:
    center, radius = s
    p = projection_on_line(center, l)
    d = point_line_distance(center, l)
    if d > radius + eps:
        return []
    u = unit(vec(l))
    h = math.sqrt(max(0.0, radius * radius - d * d))
    if h < eps:
        return [p]
    return [sub(p, mul(u, h)), add(p, mul(u, h))]


# 線分 seg と球 s の交点。0個、接する場合は1個、通常は2個返す
def segment_sphere_intersection(seg: Line3D, s: Sphere3D) -> list[Point3D]:
    return [p for p in line_sphere_intersection(seg, s) if point_on_segment(p, seg)]


# 平面 h と球 s の交円。交わらない場合は assert で落とす
def plane_sphere_intersection(h: Plane3D, s: Sphere3D) -> Circle3D:
    center, radius = s
    c = projection_on_plane(center, h)
    d = point_plane_distance(center, h)
    assert d <= radius + eps
    r = math.sqrt(max(0.0, radius * radius - d * d))
    return c, h[1], r


# 2球 s1, s2 の交円。交わらない場合や同心球の場合は assert で落とす
def sphere_sphere_intersection(s1: Sphere3D, s2: Sphere3D) -> Circle3D:
    center1, radius1 = s1
    center2, radius2 = s2
    d = dist(center1, center2)
    assert d > eps
    assert abs(radius1 - radius2) <= d + eps and d <= radius1 + radius2 + eps
    u = div(sub(center2, center1), d)
    x = (radius1 * radius1 - radius2 * radius2 + d * d) / (2 * d)
    c = add(center1, mul(u, x))
    r = math.sqrt(max(0.0, radius1 * radius1 - x * x))
    return c, u, r
