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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nvector<bool> range_eratosthenes(long\
    \ long L, long long R) {\n    assert(L <= R);\n    long long sqrtR = sqrt((long\
    \ double)R) + 1;\n    vector<bool> is_prime_base(sqrtR + 1, true);\n    vector<bool>\
    \ is_prime(R - L + 1, true);\n    if (L == 0) is_prime[0] = false;\n    if (L\
    \ <= 1 && 1 <= R) is_prime[1 - L] = false;\n    for (long long p = 2; p <= sqrtR;\
    \ p++) {\n        if (!is_prime_base[p]) continue;\n        for (long long q =\
    \ p * 2; q <= sqrtR; q += p) is_prime_base[q] = false;\n        long long start\
    \ = L + ((p - L % p) % p);\n        if (start == p) start = p * 2;\n        for\
    \ (long long q = start; q <= R; q += p) is_prime[q - L] = false;\n    }\n    return\
    \ is_prime;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<bool> range_eratosthenes(long\
    \ long L, long long R) {\n    assert(L <= R);\n    long long sqrtR = sqrt((long\
    \ double)R) + 1;\n    vector<bool> is_prime_base(sqrtR + 1, true);\n    vector<bool>\
    \ is_prime(R - L + 1, true);\n    if (L == 0) is_prime[0] = false;\n    if (L\
    \ <= 1 && 1 <= R) is_prime[1 - L] = false;\n    for (long long p = 2; p <= sqrtR;\
    \ p++) {\n        if (!is_prime_base[p]) continue;\n        for (long long q =\
    \ p * 2; q <= sqrtR; q += p) is_prime_base[q] = false;\n        long long start\
    \ = L + ((p - L % p) % p);\n        if (start == p) start = p * 2;\n        for\
    \ (long long q = start; q <= R; q += p) is_prime[q - L] = false;\n    }\n    return\
    \ is_prime;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp
- /library/algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp.html
title: algorithm_library/cpp-from-py/math/RangeEratosthenes.cpp
---
