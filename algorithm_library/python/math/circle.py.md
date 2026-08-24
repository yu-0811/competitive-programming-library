---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\neps = 1e-10\nINF = 10**18\n\nPoint = tuple[float, float]\n\
    Line = tuple[Point, Point]\nCircle = tuple[Point, float]\n\n\n# \u88DC\u52A9\u95A2\
    \u6570\n# \u8AA4\u5DEE\u4ED8\u304D\u3067\u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63\
    : 1, \u8CA0: -1, \u307B\u307C 0: 0\ndef sgn(x: float) -> int:\n    if x > eps:\n\
    \        return 1\n    if x < -eps:\n        return -1\n    return 0\n\n\n# 2\u70B9\
    \u30FB2\u30D9\u30AF\u30C8\u30EB\u304C\u8AA4\u5DEE\u4ED8\u304D\u3067\u7B49\u3057\
    \u3044\u304B\ndef point_eq(p: Point, q: Point) -> bool:\n    return abs(p[0] -\
    \ q[0]) < eps and abs(p[1] - q[1]) < eps\n\n\n# set/sort \u7528\u306E\u8F9E\u66F8\
    \u9806\u6BD4\u8F03\u3002\u8AA4\u5DEE\u4ED8\u304D\u306A\u306E\u3067\u53B3\u5BC6\
    \u306A\u5168\u9806\u5E8F\u304C\u5FC5\u8981\u306A\u7528\u9014\u306B\u306F\u6CE8\
    \u610F\ndef point_lt(p: Point, q: Point) -> bool:\n    if abs(p[0] - q[0]) >=\
    \ eps:\n        return p[0] < q[0]\n    return p[1] < q[1] - eps\n\n\n# \u30D9\
    \u30AF\u30C8\u30EB p + q\ndef add(p: Point, q: Point) -> Point:\n    return p[0]\
    \ + q[0], p[1] + q[1]\n\n\n# \u30D9\u30AF\u30C8\u30EB p - q\ndef sub(p: Point,\
    \ q: Point) -> Point:\n    return p[0] - q[0], p[1] - q[1]\n\n\n# \u30D9\u30AF\
    \u30C8\u30EB p \u306E k \u500D\ndef mul(p: Point, k: float) -> Point:\n    return\
    \ p[0] * k, p[1] * k\n\n\n# \u30D9\u30AF\u30C8\u30EB p \u3092 k \u3067\u5272\u308B\
    \ndef div(p: Point, k: float) -> Point:\n    return p[0] / k, p[1] / k\n\n\n#\
    \ \u76F4\u7DDA\u30FB\u7DDA\u5206 l \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB\
    \ B - A\ndef vec(l: Line) -> Point:\n    return sub(l[1], l[0])\n\n\n# \u5185\u7A4D\
    \ndef dot(p: Point, q: Point) -> float:\n    return p[0] * q[0] + p[1] * q[1]\n\
    \n\n# \u5916\u7A4D\ndef cross(p: Point, q: Point) -> float:\n    return p[0] *\
    \ q[1] - p[1] * q[0]\n\n\n# \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\u306E 2\
    \ \u4E57\ndef norm(p: Point) -> float:\n    return dot(p, p)\n\n\n# \u30D9\u30AF\
    \u30C8\u30EB\u306E\u9577\u3055\ndef length(p: Point) -> float:\n    return math.hypot(p[0],\
    \ p[1])\n\n\n# 2\u70B9\u9593\u8DDD\u96E2\ndef dist(p: Point, q: Point) -> float:\n\
    \    return length(sub(p, q))\n\n\n# \u53CD\u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\
    \u56DE\u8EE2\ndef rotate90(p: Point) -> Point:\n    return -p[1], p[0]\n\n\n#\
    \ \u53CD\u6642\u8A08\u56DE\u308A\u306B theta \u30E9\u30B8\u30A2\u30F3\u56DE\u8EE2\
    \ndef rotate(p: Point, theta: float) -> Point:\n    c = math.cos(theta)\n    s\
    \ = math.sin(theta)\n    return c * p[0] - s * p[1], s * p[0] + c * p[1]\n\n\n\
    # \u70B9 c \u304C\u6709\u5411\u7DDA\u5206 ab \u306B\u5BFE\u3057\u3066\u3069\u306E\
    \u4F4D\u7F6E\u306B\u3042\u308B\u304B\n# 1: \u53CD\u6642\u8A08\u56DE\u308A, -1:\
    \ \u6642\u8A08\u56DE\u308A, 2: a-b-c, -2: c-a-b, 0: a-c-b\ndef ccw(a: Point, b:\
    \ Point, c: Point) -> int:\n    ab = sub(b, a)\n    ac = sub(c, a)\n    cr = cross(ab,\
    \ ac)\n    if cr > eps:\n        return 1\n    if cr < -eps:\n        return -1\n\
    \    if dot(ab, ac) < -eps:\n        return 2\n    if norm(ab) < norm(ac) - eps:\n\
    \        return -2\n    return 0\n\n\n# \u70B9 p \u304C\u76F4\u7DDA l \u4E0A\u306B\
    \u3042\u308B\u304B\ndef point_on_line(p: Point, l: Line) -> bool:\n    return\
    \ abs(cross(sub(p, l[0]), vec(l))) < eps\n\n\n# \u70B9 p \u304C\u7DDA\u5206 l\
    \ \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_segment(p: Point, l: Line) -> bool:\n\
    \    return point_on_line(p, l) and dot(sub(p, l[0]), sub(p, l[1])) < eps\n\n\n\
    # \u70B9 p \u304B\u3089\u76F4\u7DDA l \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\
    \u306E\u8DB3\ndef projection(p: Point, l: Line) -> Point:\n    v = vec(l)\n  \
    \  return add(l[0], mul(v, dot(sub(p, l[0]), v) / norm(v)))\n\n\n# \u70B9 p \u3092\
    \u76F4\u7DDA l \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\
    \ndef reflection(p: Point, l: Line) -> Point:\n    return sub(mul(projection(p,\
    \ l), 2), p)\n\n\n# \u70B9 p \u3068\u76F4\u7DDA l \u306E\u8DDD\u96E2\ndef point_line_distance(p:\
    \ Point, l: Line) -> float:\n    return abs(cross(sub(p, l[0]), vec(l))) / length(vec(l))\n\
    \n\n# \u70B9 p \u3068\u7DDA\u5206 l \u306E\u8DDD\u96E2\ndef point_segment_distance(p:\
    \ Point, l: Line) -> float:\n    v = vec(l)\n    if dot(sub(p, l[0]), v) < 0:\n\
    \        return dist(p, l[0])\n    if dot(sub(p, l[1]), v) > 0:\n        return\
    \ dist(p, l[1])\n    return point_line_distance(p, l)\n\n\n# 2\u76F4\u7DDA\u304C\
    \u5E73\u884C\u304B\ndef is_parallel(l1: Line, l2: Line) -> bool:\n    return abs(cross(vec(l1),\
    \ vec(l2))) < eps\n\n\n# 2\u76F4\u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\ndef\
    \ is_orthogonal(l1: Line, l2: Line) -> bool:\n    return abs(dot(vec(l1), vec(l2)))\
    \ < eps\n\n\n# 2\u76F4\u7DDA\u306E\u4EA4\u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\
    \u306F assert \u3067\u843D\u3068\u3059\ndef line_intersection(l1: Line, l2: Line)\
    \ -> Point:\n    assert not is_parallel(l1, l2)\n    v1 = vec(l1)\n    v2 = vec(l2)\n\
    \    return add(l1[0], mul(v1, cross(sub(l2[0], l1[0]), v2) / cross(v1, v2)))\n\
    \n\n# 2\u7DDA\u5206\u304C\u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\
    \u63A5\u3059\u308B\u5834\u5408\u3082 True\ndef segment_intersect(l1: Line, l2:\
    \ Line) -> bool:\n    return (\n        ccw(l1[0], l1[1], l2[0]) * ccw(l1[0],\
    \ l1[1], l2[1]) <= 0\n        and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1],\
    \ l1[1]) <= 0\n    )\n\n\n# 2\u7DDA\u5206\u9593\u306E\u8DDD\u96E2\u3002\u4EA4\u5DEE\
    \u3059\u308B\u5834\u5408\u306F 0\ndef segment_distance(l1: Line, l2: Line) ->\
    \ float:\n    if segment_intersect(l1, l2):\n        return 0\n    return min(\n\
    \        point_segment_distance(l1[0], l2),\n        point_segment_distance(l1[1],\
    \ l2),\n        point_segment_distance(l2[0], l1),\n        point_segment_distance(l2[1],\
    \ l1),\n    )\n\n\n# /////////////////////////////////////////////\n\n\n# \u76F4\
    \u7DDA l \u3068\u5186 c \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\
    \u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ndef line_circle_intersection(l:\
    \ Line, c: Circle) -> tuple[Point, Point]:\n    center, radius = c\n    assert\
    \ length(vec(l)) > eps\n    p = projection(center, l)\n    d = point_line_distance(center,\
    \ l)\n    assert d <= radius + eps\n    h = math.sqrt(max(0.0, radius * radius\
    \ - d * d))\n    u = div(vec(l), length(vec(l)))\n    return add(p, mul(u, h)),\
    \ sub(p, mul(u, h))\n\n\n# 2\u5186 c1, c2 \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\
    \u304C\u306A\u3044\u5834\u5408\u3084\u540C\u5FC3\u5186\u306E\u5834\u5408\u306F\
    \ assert \u3067\u843D\u3068\u3059\ndef circle_intersection(c1: Circle, c2: Circle)\
    \ -> tuple[Point, Point]:\n    center1, radius1 = c1\n    center2, radius2 = c2\n\
    \    d = dist(center1, center2)\n    assert d > eps\n    assert abs(radius1 -\
    \ radius2) <= d + eps and d <= radius1 + radius2 + eps\n    m = (radius1 * radius1\
    \ - radius2 * radius2 + d * d) / (d * 2)\n    midpoint = add(center1, mul(div(sub(center2,\
    \ center1), d), m))\n    h = math.sqrt(max(0.0, radius1 * radius1 - m * m))\n\
    \    normal = mul(div(rotate90(sub(center2, center1)), d), h)\n    return sub(midpoint,\
    \ normal), add(midpoint, normal)\n\n\n# \u70B9 p \u304B\u3089\u5186 c \u3078\u5F15\
    \u3044\u305F 2 \u672C\u306E\u63A5\u7DDA\u306E\u63A5\u70B9\u3002p \u304C\u5186\u306E\
    \u5185\u5074\u306B\u3042\u308B\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\
    \ndef circle_tangent(p: Point, c: Circle) -> tuple[Point, Point]:\n    center,\
    \ radius = c\n    d = dist(p, center)\n    assert radius <= d + eps\n    tangent_radius\
    \ = math.sqrt(max(0.0, d * d - radius * radius))\n    return circle_intersection(c,\
    \ (p, tangent_radius))\n\n\n# 2\u5186 c1, c2 \u306E\u5171\u901A\u63A5\u7DDA\u3002\
    \u7121\u9650\u306B\u3042\u308B\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\
    \ndef common_tangent(c1: Circle, c2: Circle) -> list[Line]:\n    center1, radius1\
    \ = c1\n    center2, radius2 = c2\n    if radius1 < radius2:\n        center1,\
    \ center2 = center2, center1\n        radius1, radius2 = radius2, radius1\n  \
    \  d = dist(center1, center2)\n    lines = []\n    if radius1 - radius2 <= d +\
    \ eps:\n        if radius1 - radius2 <= eps:\n            assert d > eps\n   \
    \         offset = mul(div(rotate90(sub(center2, center1)), d), radius1)\n   \
    \         lines.append((add(center1, offset), add(center2, offset)))\n       \
    \     lines.append((sub(center1, offset), sub(center2, offset)))\n        else:\n\
    \            m = (radius1 - radius2) * (radius1 - radius2) / d\n            midpoint\
    \ = add(center1, mul(div(sub(center2, center1), d), m))\n            h = math.sqrt(max(0.0,\
    \ (radius1 - radius2) * (radius1 - radius2) - m * m))\n            base = div(rotate90(sub(center2,\
    \ center1)), d)\n\n            h1 = add(midpoint, mul(base, h))\n            d1\
    \ = mul(div(sub(h1, center1), dist(h1, center1)), radius2)\n            lines.append((add(h1,\
    \ d1), add(center2, d1)))\n\n            h2 = sub(midpoint, mul(base, h))\n  \
    \          d2 = mul(div(sub(h2, center1), dist(h2, center1)), radius2)\n     \
    \       lines.append((add(h2, d2), add(center2, d2)))\n\n    if radius1 + radius2\
    \ <= d + eps:\n        assert d > eps\n        m = (radius1 + radius2) * (radius1\
    \ + radius2) / d\n        midpoint = add(center1, mul(div(sub(center2, center1),\
    \ d), m))\n        h = math.sqrt(max(0.0, (radius1 + radius2) * (radius1 + radius2)\
    \ - m * m))\n        base = div(rotate90(sub(center2, center1)), d)\n\n      \
    \  h1 = add(midpoint, mul(base, h))\n        d1 = mul(div(sub(h1, center1), dist(h1,\
    \ center1)), radius2)\n        lines.append((sub(h1, d1), sub(center2, d1)))\n\
    \n        h2 = sub(midpoint, mul(base, h))\n        d2 = mul(div(sub(h2, center1),\
    \ dist(h2, center1)), radius2)\n        lines.append((sub(h2, d2), sub(center2,\
    \ d2)))\n\n    return lines\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/circle.py
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/circle.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/circle.py
- /library/algorithm_library/python/math/circle.py.html
title: algorithm_library/python/math/circle.py
---
