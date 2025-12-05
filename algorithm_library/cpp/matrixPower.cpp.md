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
  bundledCode: "#line 1 \"algorithm_library/cpp/matrixPower.cpp\"\n#include <bits/stdc++.h>\n\
    #include <atcoder/all>\nusing namespace std; using namespace atcoder;\nusing mint\
    \ = modint998244353;\n\n// \u884C\u5217\u7A4D\nvector<vector<mint>> mat_mul(vector<vector<mint>>\
    \ &A, vector<vector<mint>> &B) {\n    vector<vector<mint>> res(A.size(), vector<mint>(B[0].size(),\
    \ 0));\n    for (int i=0; i<A.size(); i++){\n        for (int j=0; j<B[0].size();\
    \ j++){\n            for (int k=0; k<B.size(); k++){\n                res[i][j]\
    \ += A[i][k]*B[k][j];\n            }\n        }\n    }\n    return res;\n}\n\n\
    // \u884C\u5217\u7D2F\u4E57\nvector<vector<mint>> mat_pow(vector<vector<mint>>\
    \ &M, long long K) {\n    vector<vector<mint>> res(M.size(), vector<mint>(M.size(),\
    \ 0));\n    // \u5358\u4F4D\u884C\u5217\u521D\u671F\u5316\n    for (int i=0; i<M.size();\
    \ i++) res[i][i] = 1;\n\n    while (K > 0) {\n        if (K & 1) res = mat_mul(res,\
    \ M);\n        M = mat_mul(M, M);\n        K >>= 1;\n    }\n    return res;\n\
    } \n"
  code: "#include <bits/stdc++.h>\n#include <atcoder/all>\nusing namespace std; using\
    \ namespace atcoder;\nusing mint = modint998244353;\n\n// \u884C\u5217\u7A4D\n\
    vector<vector<mint>> mat_mul(vector<vector<mint>> &A, vector<vector<mint>> &B)\
    \ {\n    vector<vector<mint>> res(A.size(), vector<mint>(B[0].size(), 0));\n \
    \   for (int i=0; i<A.size(); i++){\n        for (int j=0; j<B[0].size(); j++){\n\
    \            for (int k=0; k<B.size(); k++){\n                res[i][j] += A[i][k]*B[k][j];\n\
    \            }\n        }\n    }\n    return res;\n}\n\n// \u884C\u5217\u7D2F\u4E57\
    \nvector<vector<mint>> mat_pow(vector<vector<mint>> &M, long long K) {\n    vector<vector<mint>>\
    \ res(M.size(), vector<mint>(M.size(), 0));\n    // \u5358\u4F4D\u884C\u5217\u521D\
    \u671F\u5316\n    for (int i=0; i<M.size(); i++) res[i][i] = 1;\n\n    while (K\
    \ > 0) {\n        if (K & 1) res = mat_mul(res, M);\n        M = mat_mul(M, M);\n\
    \        K >>= 1;\n    }\n    return res;\n} "
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/matrixPower.cpp
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/matrixPower.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/matrixPower.cpp
- /library/algorithm_library/cpp/matrixPower.cpp.html
title: algorithm_library/cpp/matrixPower.cpp
---
