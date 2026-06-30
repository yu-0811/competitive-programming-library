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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/PascalsTriangle.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nstruct PascalsTriangle {\n\
    \    long long mod;\n    vector<vector<long long>> binom;\n\n    PascalsTriangle(int\
    \ N, long long mod_) : mod(mod_), binom(N + 1, vector<long long>(N + 1, 0)) {\n\
    \        for (int i = 0; i <= N; i++) {\n            binom[i][0] = 1;\n      \
    \      for (int j = 1; j <= i; j++) binom[i][j] = (binom[i - 1][j - 1] + binom[i\
    \ - 1][j]) % mod;\n        }\n    }\n\n    long long C(int n, int k) const {\n\
    \        assert(0 <= k && k <= n);\n        return binom[n][k];\n    }\n\n   \
    \ long long H(int n, int k) const {\n        assert(n >= 0 && k >= 0);\n     \
    \   return C(n + k - 1, k);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct PascalsTriangle\
    \ {\n    long long mod;\n    vector<vector<long long>> binom;\n\n    PascalsTriangle(int\
    \ N, long long mod_) : mod(mod_), binom(N + 1, vector<long long>(N + 1, 0)) {\n\
    \        for (int i = 0; i <= N; i++) {\n            binom[i][0] = 1;\n      \
    \      for (int j = 1; j <= i; j++) binom[i][j] = (binom[i - 1][j - 1] + binom[i\
    \ - 1][j]) % mod;\n        }\n    }\n\n    long long C(int n, int k) const {\n\
    \        assert(0 <= k && k <= n);\n        return binom[n][k];\n    }\n\n   \
    \ long long H(int n, int k) const {\n        assert(n >= 0 && k >= 0);\n     \
    \   return C(n + k - 1, k);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/PascalsTriangle.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/PascalsTriangle.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/PascalsTriangle.cpp
- /library/algorithm_library/cpp-from-py/math/PascalsTriangle.cpp.html
title: algorithm_library/cpp-from-py/math/PascalsTriangle.cpp
---
