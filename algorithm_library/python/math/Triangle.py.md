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
  code: "def triangle_area2(a: tuple[int,int], b: tuple[int,int], c: tuple[int,int]):\n\
    \    \"\"\"\n    \u4E09\u89D2\u5F62ABC\u306E\u9762\u7A4D\u306E2\u500D\u3092\u8FD4\
    \u3059\u3002\n    \u5EA7\u6A19\u304C\u6574\u6570\u306A\u3089\u7D50\u679C\u3082\
    \u6574\u6570\u3002\n    \"\"\"\n    ax, ay = a\n    bx, by = b\n    cx, cy = c\n\
    \    return abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))\n\n\ndef triangle_area(a:\
    \ tuple[int,int], b: tuple[int,int], c: tuple[int,int]):\n    \"\"\"\n    \u4E09\
    \u89D2\u5F62ABC\u306E\u9762\u7A4D\u3092\u8FD4\u3059\u3002\n    \"\"\"\n    return\
    \ triangle_area2(a, b, c) / 2"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/Triangle.py
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/Triangle.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/Triangle.py
- /library/algorithm_library/python/math/Triangle.py.html
title: algorithm_library/python/math/Triangle.py
---
