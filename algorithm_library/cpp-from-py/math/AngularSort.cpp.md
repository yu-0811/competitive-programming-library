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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/AngularSort.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nint compare(pair<long long, long long>\
    \ a, pair<long long, long long> b) {\n    auto [ax, ay] = a;\n    auto [bx, by]\
    \ = b;\n    int ah = (ay < 0 || (ay == 0 && ax < 0)) ? 1 : 0;\n    int bh = (by\
    \ < 0 || (by == 0 && bx < 0)) ? 1 : 0;\n    if (ah != bh) return ah < bh ? -1\
    \ : 1;\n    long long cross = ax * by - ay * bx;\n    if (cross > 0) return -1;\n\
    \    if (cross < 0) return 1;\n    return 0;\n}\n\nbool angular_less(pair<long\
    \ long, long long> a, pair<long long, long long> b) {\n    return compare(a, b)\
    \ < 0;\n}\n\nbool is_same_angle(pair<long long, long long> p1, pair<long long,\
    \ long long> p2) {\n    auto [ax, ay] = p1;\n    auto [bx, by] = p2;\n    if (ax\
    \ * by - ay * bx != 0) return false;\n    return ax * bx + ay * by > 0;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nint compare(pair<long long,\
    \ long long> a, pair<long long, long long> b) {\n    auto [ax, ay] = a;\n    auto\
    \ [bx, by] = b;\n    int ah = (ay < 0 || (ay == 0 && ax < 0)) ? 1 : 0;\n    int\
    \ bh = (by < 0 || (by == 0 && bx < 0)) ? 1 : 0;\n    if (ah != bh) return ah <\
    \ bh ? -1 : 1;\n    long long cross = ax * by - ay * bx;\n    if (cross > 0) return\
    \ -1;\n    if (cross < 0) return 1;\n    return 0;\n}\n\nbool angular_less(pair<long\
    \ long, long long> a, pair<long long, long long> b) {\n    return compare(a, b)\
    \ < 0;\n}\n\nbool is_same_angle(pair<long long, long long> p1, pair<long long,\
    \ long long> p2) {\n    auto [ax, ay] = p1;\n    auto [bx, by] = p2;\n    if (ax\
    \ * by - ay * bx != 0) return false;\n    return ax * bx + ay * by > 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/AngularSort.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/AngularSort.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/AngularSort.cpp
- /library/algorithm_library/cpp-from-py/math/AngularSort.cpp.html
title: algorithm_library/cpp-from-py/math/AngularSort.cpp
---
