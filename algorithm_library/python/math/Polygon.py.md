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
  code: "from algorithm_library.python.math.line import sub, dot, cross\n\neps = 1e-10\n\
    \n# contains \u306E\u8FD4\u308A\u5024\n# _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A\
    , _IN: \u5185\u90E8\n_OUT = 0\n_ON = 1\n_IN = 2\n\nPoint = tuple[float, float]\n\
    Polygon = list[Point]\n\n\n# \u591A\u89D2\u5F62 q \u3068\u70B9 p \u306E\u5305\u542B\
    \u5224\u5B9A\n# _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A, _IN: \u5185\u90E8\ndef\
    \ contains(q: Polygon, p: Point) -> int:\n    inside = False\n    n = len(q)\n\
    \    for i in range(n):\n        a = sub(q[i], p)\n        b = sub(q[(i + 1) %\
    \ n], p)\n        if a[1] > b[1]:\n            a, b = b, a\n        if a[1] <=\
    \ eps and eps < b[1] and cross(a, b) < -eps:\n            inside = not inside\n\
    \        if abs(cross(a, b)) < eps and dot(a, b) <= eps:\n            return _ON\n\
    \    return _IN if inside else _OUT\n"
  dependsOn:
  - algorithm_library/python/math/line.py
  isVerificationFile: false
  path: algorithm_library/python/math/Polygon.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/Polygon.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/Polygon.py
- /library/algorithm_library/python/math/Polygon.py.html
title: algorithm_library/python/math/Polygon.py
---
