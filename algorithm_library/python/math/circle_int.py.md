---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/math/line_int.py
    title: algorithm_library/python/math/line_int.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from algorithm_library.python.math.line_int import sgn, sub, mul, vec, dot,\
    \ cross, norm, dist2\n\nPoint = tuple[int, int]\nLine = tuple[Point, Point]\n\
    Circle = tuple[Point, int]\n\n\ndef radius2(c: Circle) -> int:\n    assert c[1]\
    \ >= 0\n    return c[1] * c[1]\n\n\n# \u70B9 p \u3068\u5186 c \u306E\u4F4D\u7F6E\
    \u95A2\u4FC2\u3002-1: \u5185\u90E8, 0: \u5186\u5468\u4E0A, 1: \u5916\u90E8\ndef\
    \ point_circle_relation(p: Point, c: Circle) -> int:\n    return sgn(dist2(p,\
    \ c[0]) - radius2(c))\n\n\n# \u70B9 p \u304C\u5186 c \u306E\u5186\u5468\u4E0A\u306B\
    \u3042\u308B\u304B\ndef point_on_circle(p: Point, c: Circle) -> bool:\n    return\
    \ point_circle_relation(p, c) == 0\n\n\n# \u70B9 p \u304C\u5186 c \u306E\u5185\
    \u90E8\u307E\u305F\u306F\u5186\u5468\u4E0A\u306B\u3042\u308B\u304B\ndef point_in_circle(p:\
    \ Point, c: Circle) -> bool:\n    return point_circle_relation(p, c) <= 0\n\n\n\
    # \u76F4\u7DDA l \u3068\u5186 c \u306E\u4EA4\u70B9\u6570\u3002\u30BC\u30ED\u9577\
    \u76F4\u7DDA\u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ndef line_circle_intersection_count(l:\
    \ Line, c: Circle) -> int:\n    v2 = norm(vec(l))\n    assert v2 > 0\n    cr =\
    \ cross(sub(c[0], l[0]), vec(l))\n    x = cr * cr - radius2(c) * v2\n    if x\
    \ > 0:\n        return 0\n    return 1 if x == 0 else 2\n\n\n# \u76F4\u7DDA l\
    \ \u3068\u5186 c \u304C\u4EA4\u308F\u308B\u304B\u3002\u63A5\u3059\u308B\u5834\u5408\
    \u3082 True\ndef line_circle_intersect(l: Line, c: Circle) -> bool:\n    return\
    \ line_circle_intersection_count(l, c) > 0\n\n\n# \u7DDA\u5206 l \u3068\u5186\
    \ c \u306E\u5186\u5468\u304C\u4EA4\u308F\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\
    \u3059\u308B\u5834\u5408\u3082 True\ndef segment_circle_intersect(l: Line, c:\
    \ Circle) -> bool:\n    r2 = radius2(c)\n    d0 = dist2(l[0], c[0])\n    d1 =\
    \ dist2(l[1], c[0])\n    if l[0] == l[1]:\n        return d0 == r2\n    if d0\
    \ == r2 or d1 == r2:\n        return True\n    if d0 < r2 and d1 < r2:\n     \
    \   return False\n    if (d0 < r2) != (d1 < r2):\n        return True\n\n    v\
    \ = vec(l)\n    v2 = norm(v)\n    assert v2 > 0\n    if dot(sub(c[0], l[0]), v)\
    \ < 0 or dot(sub(c[0], l[1]), mul(v, -1)) < 0:\n        return False\n    cr =\
    \ cross(sub(c[0], l[0]), v)\n    return cr * cr <= r2 * v2\n\n\n# 2\u5186 c1,\
    \ c2 \u306E\u4EA4\u70B9\u6570\u3002\u5B8C\u5168\u306B\u4E00\u81F4\u3059\u308B\u5834\
    \u5408\u306F -1 \u3092\u8FD4\u3059\ndef circle_intersection_count(c1: Circle,\
    \ c2: Circle) -> int:\n    center1, radius1 = c1\n    center2, radius2_ = c2\n\
    \    assert radius1 >= 0 and radius2_ >= 0\n    d2 = dist2(center1, center2)\n\
    \    if d2 == 0:\n        return -1 if radius1 == radius2_ else 0\n\n    diff2\
    \ = abs(radius1 - radius2_) ** 2\n    sum2 = (radius1 + radius2_) ** 2\n    if\
    \ d2 < diff2 or sum2 < d2:\n        return 0\n    if d2 == diff2 or d2 == sum2:\n\
    \        return 1\n    return 2\n\n\n# 2\u5186 c1, c2 \u306E\u5186\u5468\u304C\
    \u4EA4\u308F\u308B\u304B\u3002\u5B8C\u5168\u306B\u4E00\u81F4\u3059\u308B\u5834\
    \u5408\u3082 True\ndef circle_intersect(c1: Circle, c2: Circle) -> bool:\n   \
    \ return circle_intersection_count(c1, c2) != 0\n\n\n# 2\u5186 c1, c2 \u306E\u5171\
    \u901A\u63A5\u7DDA\u306E\u672C\u6570\u3002\u5B8C\u5168\u306B\u4E00\u81F4\u3059\
    \u308B\u5834\u5408\u306F -1 \u3092\u8FD4\u3059\ndef common_tangent_count(c1: Circle,\
    \ c2: Circle) -> int:\n    center1, radius1 = c1\n    center2, radius2_ = c2\n\
    \    assert radius1 >= 0 and radius2_ >= 0\n    d2 = dist2(center1, center2)\n\
    \    if d2 == 0 and radius1 == radius2_:\n        return -1\n\n    diff2 = abs(radius1\
    \ - radius2_) ** 2\n    sum2 = (radius1 + radius2_) ** 2\n    if d2 < diff2:\n\
    \        return 0\n    if d2 == diff2:\n        return 1\n    if d2 < sum2:\n\
    \        return 2\n    if d2 == sum2:\n        return 3\n    return 4\n"
  dependsOn:
  - algorithm_library/python/math/line_int.py
  isVerificationFile: false
  path: algorithm_library/python/math/circle_int.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/circle_int.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/circle_int.py
- /library/algorithm_library/python/math/circle_int.py.html
title: algorithm_library/python/math/circle_int.py
---
