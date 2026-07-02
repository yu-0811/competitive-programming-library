---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/geometry.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\npair<long long, long long> normalize_vector(long\
    \ long x1, long long y1, long long x2, long long y2) {\n    long long dx = x1\
    \ - x2, dy = y1 - y2;\n    if (dx == 0) {\n        dx = 0;\n        dy = 1;\n\
    \    } else if (dy == 0) {\n        dx = 1;\n        dy = 0;\n    } else {\n \
    \       if (dx < 0) dx *= -1, dy *= -1;\n        long long g = gcd(abs(dx), abs(dy));\n\
    \        dx /= g;\n        dy /= g;\n    }\n    return {dx, dy};\n}\n\nbool on_line(long\
    \ long x0, long long y0, long long x1, long long y1, long long px, long long py)\
    \ {\n    return (y1 - y0) * (px - x0) == (x1 - x0) * (py - y0);\n}\n\ntuple<long\
    \ long, long long, long long> get_line_abc(long long x0, long long y0, long long\
    \ x1, long long y1) {\n    long long a = y1 - y0;\n    long long b = x0 - x1;\n\
    \    long long c = -(a * x0 + b * y0);\n    return {a, b, c};\n}\n\npair<double,\
    \ double> pos_after_t(double sx, double sy, double gx, double gy, double t, double\
    \ v, optional<double> dist = nullopt) {\n    double dx = gx - sx, dy = gy - sy;\n\
    \    double d = dist.value_or(sqrt(dx * dx + dy * dy));\n    if (d == 0 || v <=\
    \ 0) return {sx, sy};\n    double move = v * t;\n    if (move >= d) return {gx,\
    \ gy};\n    double u = move / d;\n    return {sx + dx * u, sy + dy * u};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\npair<long long, long long>\
    \ normalize_vector(long long x1, long long y1, long long x2, long long y2) {\n\
    \    long long dx = x1 - x2, dy = y1 - y2;\n    if (dx == 0) {\n        dx = 0;\n\
    \        dy = 1;\n    } else if (dy == 0) {\n        dx = 1;\n        dy = 0;\n\
    \    } else {\n        if (dx < 0) dx *= -1, dy *= -1;\n        long long g =\
    \ gcd(abs(dx), abs(dy));\n        dx /= g;\n        dy /= g;\n    }\n    return\
    \ {dx, dy};\n}\n\nbool on_line(long long x0, long long y0, long long x1, long\
    \ long y1, long long px, long long py) {\n    return (y1 - y0) * (px - x0) ==\
    \ (x1 - x0) * (py - y0);\n}\n\ntuple<long long, long long, long long> get_line_abc(long\
    \ long x0, long long y0, long long x1, long long y1) {\n    long long a = y1 -\
    \ y0;\n    long long b = x0 - x1;\n    long long c = -(a * x0 + b * y0);\n   \
    \ return {a, b, c};\n}\n\npair<double, double> pos_after_t(double sx, double sy,\
    \ double gx, double gy, double t, double v, optional<double> dist = nullopt) {\n\
    \    double dx = gx - sx, dy = gy - sy;\n    double d = dist.value_or(sqrt(dx\
    \ * dx + dy * dy));\n    if (d == 0 || v <= 0) return {sx, sy};\n    double move\
    \ = v * t;\n    if (move >= d) return {gx, gy};\n    double u = move / d;\n  \
    \  return {sx + dx * u, sy + dy * u};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/geometry.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/geometry.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/geometry.cpp
- /library/algorithm_library/cpp-from-py/math/geometry.cpp.html
title: algorithm_library/cpp-from-py/math/geometry.cpp
---
