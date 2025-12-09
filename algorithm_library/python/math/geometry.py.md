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
  code: "import math\n\n\n# (x1,y1) - (x2,y2) \u306E\u6B63\u898F\u5316\u30D9\u30AF\
    \u30C8\u30EB\u3092\u8FD4\u3059\ndef normalize_vector(x1, y1, x2, y2):\n    dx\
    \ = x1 - x2\n    dy = y1 - y2\n    if dx == 0:\n        dx = 0\n        dy = 1\n\
    \    elif dy == 0:\n        dx = 1\n        dy = 0\n    else:\n        if dx <\
    \ 0:\n            dx *= -1\n            dy *= -1\n        g = math.gcd(abs(dx),\
    \ abs(dy))\n        dx //= g\n        dy //= g\n    return dx, dy\n\n\n# (x0,y0)\
    \ - (x1,y1) \u3092\u901A\u308B\u76F4\u7DDA\u306E\u4E0A\u306B (px,py) \u304C\u3042\
    \u308B\u304B\ndef on_line(x0, y0, x1, y1, px, py) -> bool:\n    return (y1 - y0)\
    \ * (px - x0) == (x1 - x0) * (py - y0)\n\n\n# 2\u70B9 (x0, y0), (x1, y1) \u3092\
    \u901A\u308B\u76F4\u7DDA ax + by + c = 0 \u306E (a, b, c) \u3092\u8FD4\u3059\n\
    def get_line_abc(x0, y0, x1, y1):\n    a = y1 - y0\n    b = x0 - x1\n    c = -(a\
    \ * x0 + b * y0)\n    return a, b, c\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/geometry.py
  requiredBy: []
  timestamp: '2025-12-09 12:08:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/geometry.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/geometry.py
- /library/algorithm_library/python/math/geometry.py.html
title: algorithm_library/python/math/geometry.py
---
