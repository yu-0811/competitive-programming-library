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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/factorization.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> init_factorization(int\
    \ N) {\n    vector<int> D(N + 1, 1);\n    for (int i = 2; i <= N; i++) {\n   \
    \     if (D[i] != 1) continue;\n        for (int j = i; j <= N; j += i) {\n  \
    \          if (D[j] == 1) D[j] = i;\n        }\n    }\n    return D;\n}\n\nmap<int,\
    \ int> factorization(int x, const vector<int>& D) {\n    map<int, int> res;\n\
    \    while (x != 1) {\n        res[D[x]]++;\n        x /= D[x];\n    }\n    return\
    \ res;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> init_factorization(int\
    \ N) {\n    vector<int> D(N + 1, 1);\n    for (int i = 2; i <= N; i++) {\n   \
    \     if (D[i] != 1) continue;\n        for (int j = i; j <= N; j += i) {\n  \
    \          if (D[j] == 1) D[j] = i;\n        }\n    }\n    return D;\n}\n\nmap<int,\
    \ int> factorization(int x, const vector<int>& D) {\n    map<int, int> res;\n\
    \    while (x != 1) {\n        res[D[x]]++;\n        x /= D[x];\n    }\n    return\
    \ res;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/factorization.cpp
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/factorization.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/factorization.cpp
- /library/algorithm_library/cpp-from-py/math/factorization.cpp.html
title: algorithm_library/cpp-from-py/math/factorization.cpp
---
