from algorithm_library.python.math.line import add, sub, mul, div, vec, dot, cross, norm, length, dist, rotate90

import math

eps = 1e-10
INF = 10**18

Point = tuple[float, float]
Line = tuple[Point, Point]
Circle = tuple[Point, float]


# 直線 l と円 c の交点。交点がない場合は assert で落とす
def line_circle_intersection(l: Line, c: Circle) -> tuple[Point, Point]:
    center, radius = c
    v = vec(l)
    v_len = length(v)
    assert v_len > eps
    rel = sub(center, l[0])
    p = add(l[0], mul(v, dot(rel, v) / norm(v)))
    d = abs(cross(rel, v)) / v_len
    assert d <= radius + eps
    h = math.sqrt(max(0.0, radius * radius - d * d))
    u = div(v, v_len)
    return add(p, mul(u, h)), sub(p, mul(u, h))


# 2円 c1, c2 の交点。交点がない場合や同心円の場合は assert で落とす
def circle_intersection(c1: Circle, c2: Circle) -> tuple[Point, Point]:
    center1, radius1 = c1
    center2, radius2 = c2
    d = dist(center1, center2)
    assert d > eps
    assert abs(radius1 - radius2) <= d + eps and d <= radius1 + radius2 + eps
    m = (radius1 * radius1 - radius2 * radius2 + d * d) / (d * 2)
    midpoint = add(center1, mul(div(sub(center2, center1), d), m))
    h = math.sqrt(max(0.0, radius1 * radius1 - m * m))
    normal = mul(div(rotate90(sub(center2, center1)), d), h)
    return sub(midpoint, normal), add(midpoint, normal)


# 点 p から円 c へ引いた 2 本の接線の接点。p が円の内側にある場合は assert で落とす
def circle_tangent(p: Point, c: Circle) -> tuple[Point, Point]:
    center, radius = c
    d = dist(p, center)
    assert radius <= d + eps
    tangent_radius = math.sqrt(max(0.0, d * d - radius * radius))
    return circle_intersection(c, (p, tangent_radius))


# 2円 c1, c2 の共通接線。無限にある場合は assert で落とす
def common_tangent(c1: Circle, c2: Circle) -> list[Line]:
    center1, radius1 = c1
    center2, radius2 = c2
    if radius1 < radius2:
        center1, center2 = center2, center1
        radius1, radius2 = radius2, radius1
    d = dist(center1, center2)
    lines = []
    if radius1 - radius2 <= d + eps:
        if radius1 - radius2 <= eps:
            assert d > eps
            offset = mul(div(rotate90(sub(center2, center1)), d), radius1)
            lines.append((add(center1, offset), add(center2, offset)))
            lines.append((sub(center1, offset), sub(center2, offset)))
        else:
            m = (radius1 - radius2) * (radius1 - radius2) / d
            midpoint = add(center1, mul(div(sub(center2, center1), d), m))
            h = math.sqrt(max(0.0, (radius1 - radius2) * (radius1 - radius2) - m * m))
            base = div(rotate90(sub(center2, center1)), d)

            h1 = add(midpoint, mul(base, h))
            d1 = mul(div(sub(h1, center1), dist(h1, center1)), radius2)
            lines.append((add(h1, d1), add(center2, d1)))

            h2 = sub(midpoint, mul(base, h))
            d2 = mul(div(sub(h2, center1), dist(h2, center1)), radius2)
            lines.append((add(h2, d2), add(center2, d2)))

    if radius1 + radius2 <= d + eps:
        assert d > eps
        m = (radius1 + radius2) * (radius1 + radius2) / d
        midpoint = add(center1, mul(div(sub(center2, center1), d), m))
        h = math.sqrt(max(0.0, (radius1 + radius2) * (radius1 + radius2) - m * m))
        base = div(rotate90(sub(center2, center1)), d)

        h1 = add(midpoint, mul(base, h))
        d1 = mul(div(sub(h1, center1), dist(h1, center1)), radius2)
        lines.append((sub(h1, d1), sub(center2, d1)))

        h2 = sub(midpoint, mul(base, h))
        d2 = mul(div(sub(h2, center1), dist(h2, center1)), radius2)
        lines.append((sub(h2, d2), sub(center2, d2)))

    return lines
