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
    \ * x0 + b * y0)\n    return a, b, c\n\n\ndef pos_after_t(sx, sy, gx, gy, t, v,\
    \ dist=None):\n    \"\"\"\n    \u59CB\u70B9(sx, sy) \u2192 \u7D42\u70B9(gx, gy)\
    \ \u3092\u901F\u3055 v \u3067\u52D5\u304F\u3068\u304D\u3001\n    t \u79D2\u5F8C\
    \u306E\u4F4D\u7F6E\u3092\u8FD4\u3059\uFF08\u5230\u9054\u3057\u305F\u3089\u30B4\
    \u30FC\u30EB\u306B\u3068\u3069\u307E\u308B\uFF09\u3002\n    dist = \u59CB\u70B9\
    \u3068\u7D42\u70B9\u306E\u8DDD\u96E2\uFF08\u524D\u8A08\u7B97\u3057\u3068\u3044\
    \u305F\u65B9\u304C\u901F\u3044\uFF09\n    \"\"\"\n    # (dx,dy) = \u65B9\u5411\
    \u30D9\u30AF\u30C8\u30EB\n    dx = gx - sx\n    dy = gy - sy\n    if dist is None:\n\
    \        dist = math.sqrt(dx * dx + dy * dy)\n\n    # \u59CB\u70B9\u3068\u7D42\
    \u70B9\u304C\u540C\u3058\n    if dist == 0 or v <= 0:\n        return sx, sy\n\
    \n    # \u9032\u3093\u3060\u8DDD\u96E2\n    move = v * t\n\n    # \u3059\u3067\
    \u306B\uFF08\u307E\u305F\u306F\u3061\u3087\u3046\u3069\uFF09\u5230\u9054\u3057\
    \u3066\u3044\u308B\n    if move >= dist:\n        return gx, gy\n\n    # \u5168\
    \u4F53\u306E\u4F55\u5272\u9032\u3093\u3060\u304B\n    u = move / dist\n\n    #\
    \ \u65B9\u5411\u30D9\u30AF\u30C8\u30EB\u306B\u9032\u3093\u3060\u8DDD\u96E2\u3092\
    \u304B\u3051\u308B\n    x = sx + dx * u\n    y = sy + dy * u\n    return x, y\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/geometry.py
  requiredBy: []
  timestamp: '2025-12-09 13:42:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/geometry.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/geometry.py
- /library/algorithm_library/python/math/geometry.py.html
title: algorithm_library/python/math/geometry.py
---
