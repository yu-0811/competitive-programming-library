---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/math/line.py
    title: algorithm_library/python/math/line.py
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
  code: "from algorithm_library.python.math.line import add, sub, mul, div, vec, dot,\
    \ cross, norm, length, dist, rotate90\n\nimport math\n\neps = 1e-10\nINF = 10**18\n\
    \nPoint = tuple[float, float]\nLine = tuple[Point, Point]\nCircle = tuple[Point,\
    \ float]\n\n\n# \u76F4\u7DDA l \u3068\u5186 c \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\
    \u304C\u306A\u3044\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ndef line_circle_intersection(l:\
    \ Line, c: Circle) -> tuple[Point, Point]:\n    center, radius = c\n    v = vec(l)\n\
    \    v_len = length(v)\n    assert v_len > eps\n    rel = sub(center, l[0])\n\
    \    p = add(l[0], mul(v, dot(rel, v) / norm(v)))\n    d = abs(cross(rel, v))\
    \ / v_len\n    assert d <= radius + eps\n    h = math.sqrt(max(0.0, radius * radius\
    \ - d * d))\n    u = div(v, v_len)\n    return add(p, mul(u, h)), sub(p, mul(u,\
    \ h))\n\n\n# 2\u5186 c1, c2 \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\
    \u5834\u5408\u3084\u540C\u5FC3\u5186\u306E\u5834\u5408\u306F assert \u3067\u843D\
    \u3068\u3059\ndef circle_intersection(c1: Circle, c2: Circle) -> tuple[Point,\
    \ Point]:\n    center1, radius1 = c1\n    center2, radius2 = c2\n    d = dist(center1,\
    \ center2)\n    assert d > eps\n    assert abs(radius1 - radius2) <= d + eps and\
    \ d <= radius1 + radius2 + eps\n    m = (radius1 * radius1 - radius2 * radius2\
    \ + d * d) / (d * 2)\n    midpoint = add(center1, mul(div(sub(center2, center1),\
    \ d), m))\n    h = math.sqrt(max(0.0, radius1 * radius1 - m * m))\n    normal\
    \ = mul(div(rotate90(sub(center2, center1)), d), h)\n    return sub(midpoint,\
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
  dependsOn:
  - algorithm_library/python/math/line.py
  isVerificationFile: false
  path: algorithm_library/python/math/circle.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/circle.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/circle.py
- /library/algorithm_library/python/math/circle.py.html
title: algorithm_library/python/math/circle.py
---
