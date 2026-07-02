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
  code: "import math\n\neps = 1e-10\nINF = 10**18\n\nPoint3D = tuple[float, float,\
    \ float]\nLine3D = tuple[Point3D, Point3D]\nPlane3D = tuple[Point3D, Point3D]\
    \  # (\u5E73\u9762\u4E0A\u306E\u70B9, \u6CD5\u7DDA\u30D9\u30AF\u30C8\u30EB)\n\
    Sphere3D = tuple[Point3D, float]\nCircle3D = tuple[Point3D, Point3D, float]  #\
    \ (\u4E2D\u5FC3, \u5186\u3092\u542B\u3080\u5E73\u9762\u306E\u6CD5\u7DDA, \u534A\
    \u5F84)\n\n\n# \u8AA4\u5DEE\u4ED8\u304D\u3067\u7B26\u53F7\u3092\u8FD4\u3059\u3002\
    \u6B63: 1, \u8CA0: -1, \u307B\u307C 0: 0\ndef sgn(x: float) -> int:\n    if x\
    \ > eps:\n        return 1\n    if x < -eps:\n        return -1\n    return 0\n\
    \n\n# [0, 1] \u306B\u4E38\u3081\u308B\ndef clamp01(x: float) -> float:\n    return\
    \ max(0.0, min(1.0, x))\n\n\n# acos \u306A\u3069\u306B\u6E21\u3059\u5024\u3092\
    \ [-1, 1] \u306B\u4E38\u3081\u308B\ndef clamp_unit(x: float) -> float:\n    return\
    \ max(-1.0, min(1.0, x))\n\n\n# 2\u70B9\u30FB2\u30D9\u30AF\u30C8\u30EB\u304C\u8AA4\
    \u5DEE\u4ED8\u304D\u3067\u7B49\u3057\u3044\u304B\ndef point_eq(p: Point3D, q:\
    \ Point3D) -> bool:\n    return abs(p[0] - q[0]) < eps and abs(p[1] - q[1]) <\
    \ eps and abs(p[2] - q[2]) < eps\n\n\n# set/sort \u7528\u306E\u8F9E\u66F8\u9806\
    \u6BD4\u8F03\u3002\u8AA4\u5DEE\u4ED8\u304D\u306A\u306E\u3067\u53B3\u5BC6\u306A\
    \u5168\u9806\u5E8F\u304C\u5FC5\u8981\u306A\u7528\u9014\u306B\u306F\u6CE8\u610F\
    \ndef point_lt(p: Point3D, q: Point3D) -> bool:\n    if abs(p[0] - q[0]) >= eps:\n\
    \        return p[0] < q[0]\n    if abs(p[1] - q[1]) >= eps:\n        return p[1]\
    \ < q[1]\n    return p[2] < q[2] - eps\n\n\n# \u30D9\u30AF\u30C8\u30EB p + q\n\
    def add(p: Point3D, q: Point3D) -> Point3D:\n    return p[0] + q[0], p[1] + q[1],\
    \ p[2] + q[2]\n\n\n# \u30D9\u30AF\u30C8\u30EB p - q\ndef sub(p: Point3D, q: Point3D)\
    \ -> Point3D:\n    return p[0] - q[0], p[1] - q[1], p[2] - q[2]\n\n\n# \u30D9\u30AF\
    \u30C8\u30EB p \u306E k \u500D\ndef mul(p: Point3D, k: float) -> Point3D:\n  \
    \  return p[0] * k, p[1] * k, p[2] * k\n\n\n# \u30D9\u30AF\u30C8\u30EB p \u3092\
    \ k \u3067\u5272\u308B\ndef div(p: Point3D, k: float) -> Point3D:\n    return\
    \ p[0] / k, p[1] / k, p[2] / k\n\n\n# 3\u70B9 a, b, c \u3092\u901A\u308B\u5E73\
    \u9762\u3092\u4F5C\u308B\u30023\u70B9\u304C\u4E00\u76F4\u7DDA\u4E0A\u306E\u5834\
    \u5408\u306F\u6CD5\u7DDA\u304C\u30BC\u30ED\u306B\u306A\u308B\ndef make_plane(a:\
    \ Point3D, b: Point3D, c: Point3D) -> Plane3D:\n    return a, cross(sub(b, a),\
    \ sub(c, a))\n\n\n# \u76F4\u7DDA\u30FB\u7DDA\u5206 l \u306E\u65B9\u5411\u30D9\u30AF\
    \u30C8\u30EB B - A\ndef vec(l: Line3D) -> Point3D:\n    return sub(l[1], l[0])\n\
    \n\n# \u5185\u7A4D\ndef dot(p: Point3D, q: Point3D) -> float:\n    return p[0]\
    \ * q[0] + p[1] * q[1] + p[2] * q[2]\n\n\n# \u5916\u7A4D\ndef cross(p: Point3D,\
    \ q: Point3D) -> Point3D:\n    return (\n        p[1] * q[2] - p[2] * q[1],\n\
    \        p[2] * q[0] - p[0] * q[2],\n        p[0] * q[1] - p[1] * q[0],\n    )\n\
    \n\n# \u30B9\u30AB\u30E9\u30FC\u4E09\u91CD\u7A4D\u3002\u7B26\u53F7\u4ED8\u304D\
    \u5E73\u884C\u516D\u9762\u4F53\u4F53\u7A4D\ndef triple(a: Point3D, b: Point3D,\
    \ c: Point3D) -> float:\n    return dot(a, cross(b, c))\n\n\n# \u30D9\u30AF\u30C8\
    \u30EB\u306E\u9577\u3055\u306E 2 \u4E57\ndef norm(p: Point3D) -> float:\n    return\
    \ dot(p, p)\n\n\n# \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\ndef length(p: Point3D)\
    \ -> float:\n    return math.sqrt(norm(p))\n\n\n# 2\u70B9\u9593\u8DDD\u96E2\n\
    def dist(p: Point3D, q: Point3D) -> float:\n    return length(sub(p, q))\n\n\n\
    # \u5358\u4F4D\u30D9\u30AF\u30C8\u30EB\u3002\u30BC\u30ED\u30D9\u30AF\u30C8\u30EB\
    \u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ndef unit(p: Point3D)\
    \ -> Point3D:\n    l = length(p)\n    assert l > eps\n    return div(p, l)\n\n\
    \n# 2\u30D9\u30AF\u30C8\u30EB\u306E\u306A\u3059\u89D2 [0, pi]\ndef angle(p: Point3D,\
    \ q: Point3D) -> float:\n    assert length(p) > eps and length(q) > eps\n    return\
    \ math.acos(clamp_unit(dot(p, q) / length(p) / length(q)))\n\n\n# \u539F\u70B9\
    \u3092\u901A\u308B axis \u3092\u8EF8\u3068\u3057\u3066 p \u3092 theta \u30E9\u30B8\
    \u30A2\u30F3\u56DE\u8EE2\ndef rotate_around_axis(p: Point3D, axis: Point3D, theta:\
    \ float) -> Point3D:\n    u = unit(axis)\n    c = math.cos(theta)\n    s = math.sin(theta)\n\
    \    return add(add(mul(p, c), mul(cross(u, p), s)), mul(u, dot(u, p) * (1 - c)))\n\
    \n\n# \u76F4\u7DDA axis \u3092\u8EF8\u3068\u3057\u3066 p \u3092 theta \u30E9\u30B8\
    \u30A2\u30F3\u56DE\u8EE2\ndef rotate(p: Point3D, axis: Line3D, theta: float) ->\
    \ Point3D:\n    return add(axis[0], rotate_around_axis(sub(p, axis[0]), vec(axis),\
    \ theta))\n\n\n# 3\u70B9 a, b, c \u3092\u9802\u70B9\u3068\u3059\u308B\u4E09\u89D2\
    \u5F62\u306E\u9762\u7A4D\ndef triangle_area(a: Point3D, b: Point3D, c: Point3D)\
    \ -> float:\n    return length(cross(sub(b, a), sub(c, a))) / 2\n\n\n# 4\u70B9\
    \ a, b, c, d \u3092\u9802\u70B9\u3068\u3059\u308B\u56DB\u9762\u4F53\u306E\u4F53\
    \u7A4D\ndef tetrahedron_volume(a: Point3D, b: Point3D, c: Point3D, d: Point3D)\
    \ -> float:\n    return abs(triple(sub(b, a), sub(c, a), sub(d, a))) / 6\n\n\n\
    # \u70B9 p \u304C\u76F4\u7DDA l \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_line(p:\
    \ Point3D, l: Line3D) -> bool:\n    v = vec(l)\n    assert length(v) > eps\n \
    \   return length(cross(sub(p, l[0]), v)) <= eps * length(v)\n\n\n# \u70B9 p \u304C\
    \u7DDA\u5206 s \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_segment(p: Point3D,\
    \ s: Line3D) -> bool:\n    return point_on_line(p, s) and dot(sub(p, s[0]), sub(p,\
    \ s[1])) <= eps\n\n\n# \u70B9 p \u304B\u3089\u76F4\u7DDA l \u3078\u4E0B\u308D\u3057\
    \u305F\u5782\u7DDA\u306E\u8DB3\ndef projection_on_line(p: Point3D, l: Line3D)\
    \ -> Point3D:\n    v = vec(l)\n    assert length(v) > eps\n    return add(l[0],\
    \ mul(v, dot(sub(p, l[0]), v) / norm(v)))\n\n\n# \u70B9 p \u3092\u76F4\u7DDA l\
    \ \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\ndef reflection_about_line(p:\
    \ Point3D, l: Line3D) -> Point3D:\n    return sub(mul(projection_on_line(p, l),\
    \ 2), p)\n\n\n# \u7DDA\u5206 s \u4E0A\u3067\u70B9 p \u306B\u6700\u3082\u8FD1\u3044\
    \u70B9\ndef closest_point_on_segment(p: Point3D, s: Line3D) -> Point3D:\n    v\
    \ = vec(s)\n    if norm(v) < eps:\n        return s[0]\n    t = clamp01(dot(sub(p,\
    \ s[0]), v) / norm(v))\n    return add(s[0], mul(v, t))\n\n\n# \u70B9 p \u3068\
    \u76F4\u7DDA l \u306E\u8DDD\u96E2\ndef point_line_distance(p: Point3D, l: Line3D)\
    \ -> float:\n    v = vec(l)\n    assert length(v) > eps\n    return length(cross(sub(p,\
    \ l[0]), v)) / length(v)\n\n\n# \u70B9 p \u3068\u7DDA\u5206 s \u306E\u8DDD\u96E2\
    \ndef point_segment_distance(p: Point3D, s: Line3D) -> float:\n    return dist(p,\
    \ closest_point_on_segment(p, s))\n\n\n# 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\
    \ndef is_parallel_lines(l1: Line3D, l2: Line3D) -> bool:\n    assert length(vec(l1))\
    \ > eps and length(vec(l2)) > eps\n    return length(cross(vec(l1), vec(l2)))\
    \ < eps\n\n\n# 2\u76F4\u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\ndef is_orthogonal_lines(l1:\
    \ Line3D, l2: Line3D) -> bool:\n    assert length(vec(l1)) > eps and length(vec(l2))\
    \ > eps\n    return abs(dot(vec(l1), vec(l2))) < eps\n\n\n# 2\u76F4\u7DDA\u304C\
    \u540C\u4E00\u76F4\u7DDA\u304B\ndef same_line(l1: Line3D, l2: Line3D) -> bool:\n\
    \    return is_parallel_lines(l1, l2) and point_on_line(l2[0], l1)\n\n\n# 2\u76F4\
    \u7DDA\u9593\u306E\u8DDD\u96E2\u3002\u306D\u3058\u308C\u306E\u4F4D\u7F6E\u306B\
    \u3082\u5BFE\u5FDC\ndef line_line_distance(l1: Line3D, l2: Line3D) -> float:\n\
    \    u = vec(l1)\n    v = vec(l2)\n    assert length(u) > eps and length(v) >\
    \ eps\n    w = cross(u, v)\n    if length(w) < eps:\n        return point_line_distance(l2[0],\
    \ l1)\n    return abs(triple(sub(l2[0], l1[0]), u, v)) / length(w)\n\n\n# 2\u76F4\
    \u7DDA\u4E0A\u306E\u6700\u8FD1\u70B9\u306E\u7D44\u3002\u5E73\u884C\u306A\u5834\
    \u5408\u306F assert \u3067\u843D\u3068\u3059\ndef closest_points_between_lines(l1:\
    \ Line3D, l2: Line3D) -> tuple[Point3D, Point3D]:\n    u = vec(l1)\n    v = vec(l2)\n\
    \    w = sub(l1[0], l2[0])\n    a = dot(u, u)\n    b = dot(u, v)\n    c = dot(v,\
    \ v)\n    d = dot(u, w)\n    e = dot(v, w)\n    den = a * c - b * b\n    assert\
    \ length(u) > eps and length(v) > eps and abs(den) > eps\n    s = (b * e - c *\
    \ d) / den\n    t = (a * e - b * d) / den\n    return add(l1[0], mul(u, s)), add(l2[0],\
    \ mul(v, t))\n\n\n# 2\u76F4\u7DDA\u304C\u4EA4\u5DEE\u3059\u308B\u304B\ndef line_intersect(l1:\
    \ Line3D, l2: Line3D) -> bool:\n    return line_line_distance(l1, l2) <= eps\n\
    \n\n# 2\u76F4\u7DDA\u306E\u4EA4\u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u3084\
    \u306D\u3058\u308C\u306E\u4F4D\u7F6E\u306E\u5834\u5408\u306F assert \u3067\u843D\
    \u3068\u3059\ndef line_intersection(l1: Line3D, l2: Line3D) -> Point3D:\n    assert\
    \ line_intersect(l1, l2) and not is_parallel_lines(l1, l2)\n    p, q = closest_points_between_lines(l1,\
    \ l2)\n    return div(add(p, q), 2)\n\n\n# 2\u7DDA\u5206\u4E0A\u306E\u6700\u8FD1\
    \u70B9\u306E\u7D44\u3002\u7DDA\u5206\u304C\u9000\u5316\u3057\u3066\u70B9\u306B\
    \u306A\u3063\u3066\u3044\u308B\u5834\u5408\u306B\u3082\u5BFE\u5FDC\ndef closest_points_between_segments(s1:\
    \ Line3D, s2: Line3D) -> tuple[Point3D, Point3D]:\n    u = vec(s1)\n    v = vec(s2)\n\
    \    w = sub(s1[0], s2[0])\n    a = dot(u, u)\n    b = dot(u, v)\n    c = dot(v,\
    \ v)\n    d = dot(u, w)\n    e = dot(v, w)\n    den = a * c - b * b\n\n    if\
    \ a < eps and c < eps:\n        return s1[0], s2[0]\n    if a < eps:\n       \
    \ return s1[0], closest_point_on_segment(s1[0], s2)\n    if c < eps:\n       \
    \ return closest_point_on_segment(s2[0], s1), s2[0]\n\n    sd = den\n    td =\
    \ den\n    if den < eps:\n        sn = 0.0\n        sd = 1.0\n        tn = e\n\
    \        td = c\n    else:\n        sn = b * e - c * d\n        tn = a * e - b\
    \ * d\n        if sn < 0.0:\n            sn = 0.0\n            tn = e\n      \
    \      td = c\n        elif sn > sd:\n            sn = sd\n            tn = e\
    \ + b\n            td = c\n\n    if tn < 0.0:\n        tn = 0.0\n        if -d\
    \ < 0.0:\n            sn = 0.0\n        elif -d > a:\n            sn = sd\n  \
    \      else:\n            sn = -d\n            sd = a\n    elif tn > td:\n   \
    \     tn = td\n        if -d + b < 0.0:\n            sn = 0.0\n        elif -d\
    \ + b > a:\n            sn = sd\n        else:\n            sn = -d + b\n    \
    \        sd = a\n\n    s = 0.0 if abs(sn) < eps else sn / sd\n    t = 0.0 if abs(tn)\
    \ < eps else tn / td\n    return add(s1[0], mul(u, s)), add(s2[0], mul(v, t))\n\
    \n\n# 2\u7DDA\u5206\u9593\u306E\u8DDD\u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\
    \u5408\u306F 0\ndef segment_distance(s1: Line3D, s2: Line3D) -> float:\n    p,\
    \ q = closest_points_between_segments(s1, s2)\n    return dist(p, q)\n\n\n# 2\u7DDA\
    \u5206\u304C\u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\u3059\
    \u308B\u5834\u5408\u3082 True\ndef segment_intersect(s1: Line3D, s2: Line3D) ->\
    \ bool:\n    return segment_distance(s1, s2) <= eps\n\n\n# \u70B9 p \u304C\u5E73\
    \u9762 h \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_plane(p: Point3D, h: Plane3D)\
    \ -> bool:\n    plane_point, normal = h\n    assert length(normal) > eps\n   \
    \ return abs(dot(sub(p, plane_point), normal)) <= eps * length(normal)\n\n\n#\
    \ \u70B9 p \u304B\u3089\u5E73\u9762 h \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\
    \u306E\u8DB3\ndef projection_on_plane(p: Point3D, h: Plane3D) -> Point3D:\n  \
    \  plane_point, normal = h\n    assert length(normal) > eps\n    return sub(p,\
    \ mul(normal, dot(sub(p, plane_point), normal) / norm(normal)))\n\n\n# \u70B9\
    \ p \u3092\u5E73\u9762 h \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\
    \u305F\u70B9\ndef reflection_about_plane(p: Point3D, h: Plane3D) -> Point3D:\n\
    \    return sub(mul(projection_on_plane(p, h), 2), p)\n\n\n# \u70B9 p \u3068\u5E73\
    \u9762 h \u306E\u7B26\u53F7\u4ED8\u304D\u8DDD\u96E2\u3002\u6CD5\u7DDA\u65B9\u5411\
    \u304C\u6B63\ndef signed_point_plane_distance(p: Point3D, h: Plane3D) -> float:\n\
    \    plane_point, normal = h\n    assert length(normal) > eps\n    return dot(sub(p,\
    \ plane_point), normal) / length(normal)\n\n\n# \u70B9 p \u3068\u5E73\u9762 h\
    \ \u306E\u8DDD\u96E2\ndef point_plane_distance(p: Point3D, h: Plane3D) -> float:\n\
    \    return abs(signed_point_plane_distance(p, h))\n\n\n# \u76F4\u7DDA l \u3068\
    \u5E73\u9762 h \u304C\u5E73\u884C\u304B\ndef is_parallel_line_plane(l: Line3D,\
    \ h: Plane3D) -> bool:\n    _, normal = h\n    assert length(vec(l)) > eps and\
    \ length(normal) > eps\n    return abs(dot(vec(l), normal)) < eps\n\n\n# \u76F4\
    \u7DDA l \u3068\u5E73\u9762 h \u304C\u76F4\u4EA4\u3059\u308B\u304B\ndef is_orthogonal_line_plane(l:\
    \ Line3D, h: Plane3D) -> bool:\n    _, normal = h\n    assert length(vec(l)) >\
    \ eps and length(normal) > eps\n    return length(cross(vec(l), normal)) < eps\n\
    \n\n# \u76F4\u7DDA l \u304C\u5E73\u9762 h \u4E0A\u306B\u3042\u308B\u304B\ndef\
    \ line_on_plane(l: Line3D, h: Plane3D) -> bool:\n    return point_on_plane(l[0],\
    \ h) and point_on_plane(l[1], h)\n\n\n# \u76F4\u7DDA l \u3068\u5E73\u9762 h \u306E\
    \u4EA4\u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\u843D\u3068\
    \u3059\ndef line_plane_intersection(l: Line3D, h: Plane3D) -> Point3D:\n    plane_point,\
    \ normal = h\n    assert not is_parallel_line_plane(l, h)\n    v = vec(l)\n  \
    \  t = dot(sub(plane_point, l[0]), normal) / dot(v, normal)\n    return add(l[0],\
    \ mul(v, t))\n\n\n# \u76F4\u7DDA l \u3068\u5E73\u9762 h \u306E\u8DDD\u96E2\u3002\
    \u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndef line_plane_distance(l: Line3D,\
    \ h: Plane3D) -> float:\n    if not is_parallel_line_plane(l, h):\n        return\
    \ 0.0\n    return point_plane_distance(l[0], h)\n\n\n# 2\u5E73\u9762\u304C\u5E73\
    \u884C\u304B\ndef is_parallel_planes(h1: Plane3D, h2: Plane3D) -> bool:\n    assert\
    \ length(h1[1]) > eps and length(h2[1]) > eps\n    return length(cross(h1[1],\
    \ h2[1])) < eps\n\n\n# 2\u5E73\u9762\u304C\u76F4\u4EA4\u3059\u308B\u304B\ndef\
    \ is_orthogonal_planes(h1: Plane3D, h2: Plane3D) -> bool:\n    assert length(h1[1])\
    \ > eps and length(h2[1]) > eps\n    return abs(dot(h1[1], h2[1])) < eps\n\n\n\
    # 2\u5E73\u9762\u304C\u540C\u4E00\u5E73\u9762\u304B\ndef same_plane(h1: Plane3D,\
    \ h2: Plane3D) -> bool:\n    return is_parallel_planes(h1, h2) and point_on_plane(h2[0],\
    \ h1)\n\n\n# 2\u5E73\u9762\u306E\u4EA4\u7DDA\u3002\u5E73\u884C\u306A\u5834\u5408\
    \u306F assert \u3067\u843D\u3068\u3059\ndef plane_intersection(h1: Plane3D, h2:\
    \ Plane3D) -> Line3D:\n    assert not is_parallel_planes(h1, h2)\n    p1, n1 =\
    \ h1\n    p2, n2 = h2\n    direction = cross(n1, n2)\n    d1 = dot(n1, p1)\n \
    \   d2 = dot(n2, p2)\n    point = div(cross(sub(mul(n2, d1), mul(n1, d2)), direction),\
    \ norm(direction))\n    return point, add(point, direction)\n\n\n# 2\u5E73\u9762\
    \u9593\u306E\u8DDD\u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndef\
    \ plane_plane_distance(h1: Plane3D, h2: Plane3D) -> float:\n    if not is_parallel_planes(h1,\
    \ h2):\n        return 0.0\n    return point_plane_distance(h2[0], h1)\n\n\n#\
    \ \u70B9 p \u304C\u7403 s \u306E\u5185\u90E8\u307E\u305F\u306F\u8868\u9762\u306B\
    \u3042\u308B\u304B\ndef point_in_sphere(p: Point3D, s: Sphere3D) -> bool:\n  \
    \  center, radius = s\n    return dist(p, center) <= radius + eps\n\n\n# \u70B9\
    \ p \u304C\u7403 s \u306E\u8868\u9762\u306B\u3042\u308B\u304B\ndef point_on_sphere(p:\
    \ Point3D, s: Sphere3D) -> bool:\n    center, radius = s\n    return abs(dist(p,\
    \ center) - radius) <= eps\n\n\n# \u76F4\u7DDA l \u3068\u7403 s \u306E\u4EA4\u70B9\
    \u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\u3001\u901A\u5E38\
    \u306F2\u500B\u8FD4\u3059\ndef line_sphere_intersection(l: Line3D, s: Sphere3D)\
    \ -> list[Point3D]:\n    center, radius = s\n    p = projection_on_line(center,\
    \ l)\n    d = point_line_distance(center, l)\n    if d > radius + eps:\n     \
    \   return []\n    u = unit(vec(l))\n    h = math.sqrt(max(0.0, radius * radius\
    \ - d * d))\n    if h < eps:\n        return [p]\n    return [sub(p, mul(u, h)),\
    \ add(p, mul(u, h))]\n\n\n# \u7DDA\u5206 seg \u3068\u7403 s \u306E\u4EA4\u70B9\
    \u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\u3001\u901A\u5E38\
    \u306F2\u500B\u8FD4\u3059\ndef segment_sphere_intersection(seg: Line3D, s: Sphere3D)\
    \ -> list[Point3D]:\n    return [p for p in line_sphere_intersection(seg, s) if\
    \ point_on_segment(p, seg)]\n\n\n# \u5E73\u9762 h \u3068\u7403 s \u306E\u4EA4\u5186\
    \u3002\u4EA4\u308F\u3089\u306A\u3044\u5834\u5408\u306F assert \u3067\u843D\u3068\
    \u3059\ndef plane_sphere_intersection(h: Plane3D, s: Sphere3D) -> Circle3D:\n\
    \    center, radius = s\n    c = projection_on_plane(center, h)\n    d = point_plane_distance(center,\
    \ h)\n    assert d <= radius + eps\n    r = math.sqrt(max(0.0, radius * radius\
    \ - d * d))\n    return c, h[1], r\n\n\n# 2\u7403 s1, s2 \u306E\u4EA4\u5186\u3002\
    \u4EA4\u308F\u3089\u306A\u3044\u5834\u5408\u3084\u540C\u5FC3\u7403\u306E\u5834\
    \u5408\u306F assert \u3067\u843D\u3068\u3059\ndef sphere_sphere_intersection(s1:\
    \ Sphere3D, s2: Sphere3D) -> Circle3D:\n    center1, radius1 = s1\n    center2,\
    \ radius2 = s2\n    d = dist(center1, center2)\n    assert d > eps\n    assert\
    \ abs(radius1 - radius2) <= d + eps and d <= radius1 + radius2 + eps\n    u =\
    \ div(sub(center2, center1), d)\n    x = (radius1 * radius1 - radius2 * radius2\
    \ + d * d) / (2 * d)\n    c = add(center1, mul(u, x))\n    r = math.sqrt(max(0.0,\
    \ radius1 * radius1 - x * x))\n    return c, u, r\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/geometry3d.py
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/geometry3d.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/geometry3d.py
- /library/algorithm_library/python/math/geometry3d.py.html
title: algorithm_library/python/math/geometry3d.py
---
