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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/extGCD.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\ntuple<long long, long long, long long>\
    \ extGCD(long long a, long long b) {\n    if (b == 0) return {a, 1, 0};\n    auto\
    \ [g, s, t] = extGCD(b, a % b);\n    long long x = t;\n    long long y = s - a\
    \ / b * t;\n    return {g, x, y};\n}\n\nlong long modinv(long long a, long long\
    \ m) {\n    auto [g, x, y] = extGCD(a, m);\n    assert(g == 1);\n    x %= m;\n\
    \    if (x < 0) x += m;\n    return x;\n}\n\noptional<long long> modlin(long long\
    \ a, long long b, long long m) {\n    auto [g, x, y] = extGCD(a, m);\n    if (b\
    \ % g != 0) return nullopt;\n    a /= g;\n    b /= g;\n    m /= g;\n    return\
    \ modinv(a, m) * b % m;\n}\n\npair<optional<long long>, optional<long long>> chineseRem(const\
    \ vector<long long>& B, const vector<long long>& M) {\n    assert(B.size() ==\
    \ M.size());\n    long long r = 0, m = 1;\n    for (int i = 0; i < (int)B.size();\
    \ i++) {\n        auto [d, p, q] = extGCD(m, M[i]);\n        if ((B[i] - r) %\
    \ d != 0) return {nullopt, nullopt};\n        long long tmp = ((B[i] - r) / d\
    \ * p) % (M[i] / d);\n        r += m * tmp;\n        m *= M[i] / d;\n        r\
    \ %= m;\n        if (r < 0) r += m;\n    }\n    return {r, m};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntuple<long long, long long,\
    \ long long> extGCD(long long a, long long b) {\n    if (b == 0) return {a, 1,\
    \ 0};\n    auto [g, s, t] = extGCD(b, a % b);\n    long long x = t;\n    long\
    \ long y = s - a / b * t;\n    return {g, x, y};\n}\n\nlong long modinv(long long\
    \ a, long long m) {\n    auto [g, x, y] = extGCD(a, m);\n    assert(g == 1);\n\
    \    x %= m;\n    if (x < 0) x += m;\n    return x;\n}\n\noptional<long long>\
    \ modlin(long long a, long long b, long long m) {\n    auto [g, x, y] = extGCD(a,\
    \ m);\n    if (b % g != 0) return nullopt;\n    a /= g;\n    b /= g;\n    m /=\
    \ g;\n    return modinv(a, m) * b % m;\n}\n\npair<optional<long long>, optional<long\
    \ long>> chineseRem(const vector<long long>& B, const vector<long long>& M) {\n\
    \    assert(B.size() == M.size());\n    long long r = 0, m = 1;\n    for (int\
    \ i = 0; i < (int)B.size(); i++) {\n        auto [d, p, q] = extGCD(m, M[i]);\n\
    \        if ((B[i] - r) % d != 0) return {nullopt, nullopt};\n        long long\
    \ tmp = ((B[i] - r) / d * p) % (M[i] / d);\n        r += m * tmp;\n        m *=\
    \ M[i] / d;\n        r %= m;\n        if (r < 0) r += m;\n    }\n    return {r,\
    \ m};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/extGCD.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/extGCD.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/extGCD.cpp
- /library/algorithm_library/cpp-from-py/math/extGCD.cpp.html
title: algorithm_library/cpp-from-py/math/extGCD.cpp
---
