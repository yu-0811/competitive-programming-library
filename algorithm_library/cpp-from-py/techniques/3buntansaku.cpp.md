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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/3buntansaku.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class F>\ntuple<double,\
    \ double, double> ternary_search_float(F f, double left, double right, double\
    \ eps = 1e-9, bool maximize = false) {\n    while (right - left > eps) {\n   \
    \     double m1 = (2 * left + right) / 3;\n        double m2 = (left + 2 * right)\
    \ / 3;\n        auto f1 = f(m1), f2 = f(m2);\n        if (!maximize) {\n     \
    \       if (f1 > f2) left = m1;\n            else right = m2;\n        } else\
    \ {\n            if (f1 < f2) left = m1;\n            else right = m2;\n     \
    \   }\n    }\n    double x = (left + right) / 2;\n    return {left, right, f(x)};\n\
    }\n\ntemplate <class F>\nauto ternary_search_int(F f, long long left, long long\
    \ right, long long eps, bool maximize = false) {\n    while (right - left > eps)\
    \ {\n        long long m1 = (2 * left + right) / 3;\n        long long m2 = (left\
    \ + 2 * right) / 3;\n        auto f1 = f(m1), f2 = f(m2);\n        if (!maximize)\
    \ {\n            if (f1 > f2) left = m1;\n            else right = m2;\n     \
    \   } else {\n            if (f1 < f2) left = m1;\n            else right = m2;\n\
    \        }\n    }\n    long long best_x = left;\n    auto best_val = f(left);\n\
    \    for (long long x = left + 1; x <= right; x++) {\n        auto val = f(x);\n\
    \        if ((maximize && val > best_val) || (!maximize && val < best_val)) {\n\
    \            best_val = val;\n            best_x = x;\n        }\n    }\n    return\
    \ pair{best_x, best_val};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class F>\ntuple<double,\
    \ double, double> ternary_search_float(F f, double left, double right, double\
    \ eps = 1e-9, bool maximize = false) {\n    while (right - left > eps) {\n   \
    \     double m1 = (2 * left + right) / 3;\n        double m2 = (left + 2 * right)\
    \ / 3;\n        auto f1 = f(m1), f2 = f(m2);\n        if (!maximize) {\n     \
    \       if (f1 > f2) left = m1;\n            else right = m2;\n        } else\
    \ {\n            if (f1 < f2) left = m1;\n            else right = m2;\n     \
    \   }\n    }\n    double x = (left + right) / 2;\n    return {left, right, f(x)};\n\
    }\n\ntemplate <class F>\nauto ternary_search_int(F f, long long left, long long\
    \ right, long long eps, bool maximize = false) {\n    while (right - left > eps)\
    \ {\n        long long m1 = (2 * left + right) / 3;\n        long long m2 = (left\
    \ + 2 * right) / 3;\n        auto f1 = f(m1), f2 = f(m2);\n        if (!maximize)\
    \ {\n            if (f1 > f2) left = m1;\n            else right = m2;\n     \
    \   } else {\n            if (f1 < f2) left = m1;\n            else right = m2;\n\
    \        }\n    }\n    long long best_x = left;\n    auto best_val = f(left);\n\
    \    for (long long x = left + 1; x <= right; x++) {\n        auto val = f(x);\n\
    \        if ((maximize && val > best_val) || (!maximize && val < best_val)) {\n\
    \            best_val = val;\n            best_x = x;\n        }\n    }\n    return\
    \ pair{best_x, best_val};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/3buntansaku.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/3buntansaku.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/3buntansaku.cpp
- /library/algorithm_library/cpp-from-py/techniques/3buntansaku.cpp.html
title: algorithm_library/cpp-from-py/techniques/3buntansaku.cpp
---
