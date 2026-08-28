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
  code: "Point = tuple[int, int]\nLine = tuple[Point, Point]\n\n\n# \u7B26\u53F7\u3092\
    \u8FD4\u3059\u3002\u6B63: 1, \u8CA0: -1, 0: 0\ndef sgn(x: int) -> int:\n    if\
    \ x > 0:\n        return 1\n    if x < 0:\n        return -1\n    return 0\n\n\
    \n# 2\u70B9\u30FB2\u30D9\u30AF\u30C8\u30EB\u304C\u7B49\u3057\u3044\u304B\ndef\
    \ point_eq(p: Point, q: Point) -> bool:\n    return p[0] == q[0] and p[1] == q[1]\n\
    \n\n# set/sort \u7528\u306E\u8F9E\u66F8\u9806\u6BD4\u8F03\ndef point_lt(p: Point,\
    \ q: Point) -> bool:\n    if p[0] != q[0]:\n        return p[0] < q[0]\n    return\
    \ p[1] < q[1]\n\n\n# \u30D9\u30AF\u30C8\u30EB p + q\ndef add(p: Point, q: Point)\
    \ -> Point:\n    return p[0] + q[0], p[1] + q[1]\n\n\n# \u30D9\u30AF\u30C8\u30EB\
    \ p - q\ndef sub(p: Point, q: Point) -> Point:\n    return p[0] - q[0], p[1] -\
    \ q[1]\n\n\n# \u30D9\u30AF\u30C8\u30EB p \u306E\u6574\u6570 k \u500D\ndef mul(p:\
    \ Point, k: int) -> Point:\n    return p[0] * k, p[1] * k\n\n\n# \u76F4\u7DDA\u30FB\
    \u7DDA\u5206 l \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB B - A\ndef vec(l: Line)\
    \ -> Point:\n    return sub(l[1], l[0])\n\n\n# \u5185\u7A4D\ndef dot(p: Point,\
    \ q: Point) -> int:\n    return p[0] * q[0] + p[1] * q[1]\n\n\n# \u5916\u7A4D\n\
    def cross(p: Point, q: Point) -> int:\n    return p[0] * q[1] - p[1] * q[0]\n\n\
    \n# \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\u306E 2 \u4E57\ndef norm(p: Point)\
    \ -> int:\n    return dot(p, p)\n\n\n# 2\u70B9\u9593\u8DDD\u96E2\u306E 2 \u4E57\
    \ndef dist2(p: Point, q: Point) -> int:\n    return norm(sub(p, q))\n\n\n# \u53CD\
    \u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\u56DE\u8EE2\ndef rotate90(p: Point) ->\
    \ Point:\n    return -p[1], p[0]\n\n\n# \u70B9 c \u304C\u6709\u5411\u7DDA\u5206\
    \ ab \u306B\u5BFE\u3057\u3066\u3069\u306E\u4F4D\u7F6E\u306B\u3042\u308B\u304B\n\
    # 1: \u53CD\u6642\u8A08\u56DE\u308A, -1: \u6642\u8A08\u56DE\u308A, 2: a-b-c, -2:\
    \ c-a-b, 0: a-c-b\ndef ccw(a: Point, b: Point, c: Point) -> int:\n    ab = sub(b,\
    \ a)\n    ac = sub(c, a)\n    cr = cross(ab, ac)\n    if cr > 0:\n        return\
    \ 1\n    if cr < 0:\n        return -1\n    if dot(ab, ac) < 0:\n        return\
    \ 2\n    if norm(ab) < norm(ac):\n        return -2\n    return 0\n\n\n# \u70B9\
    \ p \u304C\u76F4\u7DDA l \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_line(p:\
    \ Point, l: Line) -> bool:\n    return cross(sub(p, l[0]), vec(l)) == 0\n\n\n\
    # \u70B9 p \u304C\u7DDA\u5206 l \u4E0A\u306B\u3042\u308B\u304B\ndef point_on_segment(p:\
    \ Point, l: Line) -> bool:\n    return point_on_line(p, l) and dot(sub(p, l[0]),\
    \ sub(p, l[1])) <= 0\n\n\n# 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\ndef is_parallel(l1:\
    \ Line, l2: Line) -> bool:\n    return cross(vec(l1), vec(l2)) == 0\n\n\n# 2\u76F4\
    \u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\ndef is_orthogonal(l1: Line, l2: Line)\
    \ -> bool:\n    return dot(vec(l1), vec(l2)) == 0\n\n\n# 2\u7DDA\u5206\u304C\u4EA4\
    \u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\u5834\u5408\
    \u3082 True\ndef segment_intersect(l1: Line, l2: Line) -> bool:\n    return (\n\
    \        ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) <= 0\n        and\
    \ ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) <= 0\n    )\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/line_int.py
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/line_int.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/line_int.py
- /library/algorithm_library/python/math/line_int.py.html
title: algorithm_library/python/math/line_int.py
---
