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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/eratosthenes.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\npair<vector<int>, vector<bool>>\
    \ eratosthenes(int N) {\n    vector<int> prime_number;\n    vector<bool> isprime(N\
    \ + 1, true);\n    if (N >= 0) isprime[0] = false;\n    if (N >= 1) isprime[1]\
    \ = false;\n    for (int p = 2; p <= N; p++) {\n        if (!isprime[p]) continue;\n\
    \        for (long long q = 2LL * p; q <= N; q += p) isprime[q] = false;\n   \
    \ }\n    for (int p = 2; p <= N; p++) if (isprime[p]) prime_number.push_back(p);\n\
    \    return {prime_number, isprime};\n}\n\nvector<int> res_primeList(int M) {\n\
    \    vector<bool> isprime(M + 1, true);\n    if (M >= 0) isprime[0] = false;\n\
    \    if (M >= 1) isprime[1] = false;\n    for (int i = 2; i <= M && 1LL * i *\
    \ i <= M; i++) {\n        if (isprime[i]) for (long long j = 1LL * i * i; j <=\
    \ M; j += i) isprime[j] = false;\n    }\n    vector<int> res;\n    for (int i\
    \ = 2; i <= M; i++) if (isprime[i]) res.push_back(i);\n    return res;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\npair<vector<int>, vector<bool>>\
    \ eratosthenes(int N) {\n    vector<int> prime_number;\n    vector<bool> isprime(N\
    \ + 1, true);\n    if (N >= 0) isprime[0] = false;\n    if (N >= 1) isprime[1]\
    \ = false;\n    for (int p = 2; p <= N; p++) {\n        if (!isprime[p]) continue;\n\
    \        for (long long q = 2LL * p; q <= N; q += p) isprime[q] = false;\n   \
    \ }\n    for (int p = 2; p <= N; p++) if (isprime[p]) prime_number.push_back(p);\n\
    \    return {prime_number, isprime};\n}\n\nvector<int> res_primeList(int M) {\n\
    \    vector<bool> isprime(M + 1, true);\n    if (M >= 0) isprime[0] = false;\n\
    \    if (M >= 1) isprime[1] = false;\n    for (int i = 2; i <= M && 1LL * i *\
    \ i <= M; i++) {\n        if (isprime[i]) for (long long j = 1LL * i * i; j <=\
    \ M; j += i) isprime[j] = false;\n    }\n    vector<int> res;\n    for (int i\
    \ = 2; i <= M; i++) if (isprime[i]) res.push_back(i);\n    return res;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/eratosthenes.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/eratosthenes.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/eratosthenes.cpp
- /library/algorithm_library/cpp-from-py/math/eratosthenes.cpp.html
title: algorithm_library/cpp-from-py/math/eratosthenes.cpp
---
