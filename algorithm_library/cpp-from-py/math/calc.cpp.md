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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/calc.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nlong long ceilDiv(long long p, long\
    \ long q) {\n    return (p + q - 1) / q;\n}\n\nlong long max_leq_congruent(long\
    \ long R, long long r, long long m) {\n    r %= m;\n    if (r < 0) r += m;\n \
    \   return R - ((R - r) % m + m) % m;\n}\n\nlong long min_geq_congruent(long long\
    \ L, long long r, long long m) {\n    assert(m > 0);\n    r %= m;\n    if (r <\
    \ 0) r += m;\n    return L + ((r - L) % m + m) % m;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nlong long ceilDiv(long\
    \ long p, long long q) {\n    return (p + q - 1) / q;\n}\n\nlong long max_leq_congruent(long\
    \ long R, long long r, long long m) {\n    r %= m;\n    if (r < 0) r += m;\n \
    \   return R - ((R - r) % m + m) % m;\n}\n\nlong long min_geq_congruent(long long\
    \ L, long long r, long long m) {\n    assert(m > 0);\n    r %= m;\n    if (r <\
    \ 0) r += m;\n    return L + ((r - L) % m + m) % m;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/calc.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/calc.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/calc.cpp
- /library/algorithm_library/cpp-from-py/math/calc.cpp.html
title: algorithm_library/cpp-from-py/math/calc.cpp
---
