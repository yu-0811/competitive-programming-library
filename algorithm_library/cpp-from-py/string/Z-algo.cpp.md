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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/string/Z-algo.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<int> z_algo(const\
    \ T& S) {\n    int n = (int)S.size();\n    vector<int> Z(n);\n    if (n == 0)\
    \ return Z;\n    Z[0] = n;\n    int i = 1, j = 0;\n    while (i < n) {\n     \
    \   while (i + j < n && S[j] == S[i + j]) j++;\n        Z[i] = j;\n        if\
    \ (j == 0) {\n            i++;\n            continue;\n        }\n        int\
    \ k = 1;\n        while (k < j && k + Z[k] < j) {\n            Z[i + k] = Z[k];\n\
    \            k++;\n        }\n        i += k;\n        j -= k;\n    }\n    return\
    \ Z;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<int>\
    \ z_algo(const T& S) {\n    int n = (int)S.size();\n    vector<int> Z(n);\n  \
    \  if (n == 0) return Z;\n    Z[0] = n;\n    int i = 1, j = 0;\n    while (i <\
    \ n) {\n        while (i + j < n && S[j] == S[i + j]) j++;\n        Z[i] = j;\n\
    \        if (j == 0) {\n            i++;\n            continue;\n        }\n \
    \       int k = 1;\n        while (k < j && k + Z[k] < j) {\n            Z[i +\
    \ k] = Z[k];\n            k++;\n        }\n        i += k;\n        j -= k;\n\
    \    }\n    return Z;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/string/Z-algo.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/string/Z-algo.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/string/Z-algo.cpp
- /library/algorithm_library/cpp-from-py/string/Z-algo.cpp.html
title: algorithm_library/cpp-from-py/string/Z-algo.cpp
---
