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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/Compression.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<int>\
    \ compression(const vector<T>& A) {\n    vector<T> xs = A;\n    sort(xs.begin(),\
    \ xs.end());\n    xs.erase(unique(xs.begin(), xs.end()), xs.end());\n    vector<int>\
    \ B(A.size());\n    for (int i = 0; i < (int)A.size(); i++) {\n        B[i] =\
    \ lower_bound(xs.begin(), xs.end(), A[i]) - xs.begin();\n    }\n    return B;\n\
    }\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<int>\
    \ compression(const vector<T>& A) {\n    vector<T> xs = A;\n    sort(xs.begin(),\
    \ xs.end());\n    xs.erase(unique(xs.begin(), xs.end()), xs.end());\n    vector<int>\
    \ B(A.size());\n    for (int i = 0; i < (int)A.size(); i++) {\n        B[i] =\
    \ lower_bound(xs.begin(), xs.end(), A[i]) - xs.begin();\n    }\n    return B;\n\
    }\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/Compression.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/Compression.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/Compression.cpp
- /library/algorithm_library/cpp-from-py/techniques/Compression.cpp.html
title: algorithm_library/cpp-from-py/techniques/Compression.cpp
---
