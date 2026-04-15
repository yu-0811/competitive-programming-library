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
  code: "def compare(a: tuple[int, int], b: tuple[int, int]):\n    ax, ay = a\n  \
    \  bx, by = b\n\n    # \u9818\u57DF\u5224\u5B9A (0: \u4E0A\u534A\u5E73\u9762 [0,\
    \ 180\u5EA6), 1: \u4E0B\u534A\u5E73\u9762 [180, 360\u5EA6))\n    # ay < 0 \u307E\
    \u305F\u306F (ay == 0 \u304B\u3064 ax < 0) \u306E\u5834\u5408\u304C\u4E0B\u534A\
    \u5E73\u9762\n    ah = 1 if (ay < 0 or (ay == 0 and ax < 0)) else 0\n    bh =\
    \ 1 if (by < 0 or (by == 0 and bx < 0)) else 0\n    # \u9818\u57DF\u304C\u7570\
    \u306A\u308B\u5834\u5408\u4E0A\u534A\u5E73\u9762\u3092\u512A\u5148\n    if ah\
    \ != bh:\n        return -1 if ah < bh else 1\n\n    # \u5916\u7A4D\u8A08\u7B97\
    \ (ax*by - ay*bx)\n    # \u6B63\u306A\u3089\u53CD\u6642\u8A08\u56DE\u308A(a\u304C\
    \u5148)\u3001\u8CA0\u306A\u3089\u6642\u8A08\u56DE\u308A(b\u304C\u5148)\n    cross\
    \ = ax * by - ay * bx\n    if cross > 0:\n        return -1\n    if cross < 0:\n\
    \        return 1\n    return 0\n\n\ndef is_same_angle(p1, p2):\n    \"\"\"\n\
    \    2\u70B9 p1, p2 \u304C\u539F\u70B9\u304B\u3089\u898B\u3066\u540C\u3058\u504F\
    \u89D2\uFF08\u540C\u3058\u65B9\u5411\uFF09\u306B\u3042\u308B\u304B\u5224\u5B9A\
    \u3059\u308B\u3002\n    \u203B\u539F\u70B9(0,0)\u304C\u542B\u307E\u308C\u308B\u5834\
    \u5408\u306FFalse\n    \"\"\"\n    ax, ay = p1\n    bx, by = p2\n\n    # 1. \u5916\
    \u7A4D\u304C0\u3067\u306A\u3051\u308C\u3070\u3001\u305D\u3082\u305D\u3082\u540C\
    \u4E00\u76F4\u7DDA\u4E0A\u306B\u306A\u3044\n    if ax * by - ay * bx != 0:\n \
    \       return False\n\n    # 2. \u5185\u7A4D\u304C\u6B63\u3067\u306A\u3051\u308C\
    \u3070\u3001\u9006\u5411\u304D\uFF08180\u5EA6\u53CD\u5BFE\uFF09\u307E\u305F\u306F\
    \u539F\u70B9\u3092\u542B\u3093\u3067\u3044\u308B\n    #    \u5185\u7A4D > 0 \u306A\
    \u3089\u3070\u540C\u3058\u5411\u304D\n    if ax * bx + ay * by > 0:\n        return\
    \ True\n\n    return False\n\n\n# \u4F7F\u7528\u4F8B\n# A = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]\n\
    # A.sort(key=cmp_to_key(compare))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/AngularSort.py
  requiredBy: []
  timestamp: '2026-04-15 17:42:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/AngularSort.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/AngularSort.py
- /library/algorithm_library/python/math/AngularSort.py.html
title: algorithm_library/python/math/AngularSort.py
---
