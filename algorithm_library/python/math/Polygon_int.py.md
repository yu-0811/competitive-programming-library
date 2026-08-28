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
  code: "# contains \u306E\u8FD4\u308A\u5024\n# _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A\
    , _IN: \u5185\u90E8\n_OUT = 0\n_ON = 1\n_IN = 2\n\nPoint = tuple[int, int]\nPolygon\
    \ = list[Point]\n\n\n# \u30D9\u30AF\u30C8\u30EB p - q\ndef sub(p: Point, q: Point)\
    \ -> Point:\n    return p[0] - q[0], p[1] - q[1]\n\n\n# \u5185\u7A4D\ndef dot(p:\
    \ Point, q: Point) -> int:\n    return p[0] * q[0] + p[1] * q[1]\n\n\n# \u5916\
    \u7A4D\ndef cross(p: Point, q: Point) -> int:\n    return p[0] * q[1] - p[1] *\
    \ q[0]\n\n\n# \u591A\u89D2\u5F62 q \u3068\u70B9 p \u306E\u5305\u542B\u5224\u5B9A\
    \n# _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A, _IN: \u5185\u90E8\ndef contains(q:\
    \ Polygon, p: Point) -> int:\n    inside = False\n    n = len(q)\n    for i in\
    \ range(n):\n        a = sub(q[i], p)\n        b = sub(q[(i + 1) % n], p)\n  \
    \      if a[1] > b[1]:\n            a, b = b, a\n        if a[1] <= 0 < b[1] and\
    \ cross(a, b) < 0:\n            inside = not inside\n        if cross(a, b) ==\
    \ 0 and dot(a, b) <= 0:\n            return _ON\n    return _IN if inside else\
    \ _OUT\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/Polygon_int.py
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/Polygon_int.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/Polygon_int.py
- /library/algorithm_library/python/math/Polygon_int.py.html
title: algorithm_library/python/math/Polygon_int.py
---
