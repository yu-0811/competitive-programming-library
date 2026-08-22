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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nstruct CrossAccumulate {\n\
    \    int H, W;\n    vector<vector<long long>> s;\n\n    CrossAccumulate(const\
    \ vector<vector<long long>>& grid) {\n        H = (int)grid.size();\n        W\
    \ = (int)grid[0].size();\n        s.assign(H + 1, vector<long long>(W + 1, 0));\n\
    \        for (int i = 0; i < H; i++) {\n            for (int j = 0; j < W; j++)\
    \ {\n                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + grid[i][j];\n\
    \            }\n        }\n    }\n\n    long long query(int r1, int c1, int r2,\
    \ int c2) const {\n        assert(0 <= r1 && r1 <= r2 && r2 < H && 0 <= c1 &&\
    \ c1 <= c2 && c2 < W);\n        return s[r2 + 1][c2 + 1] - s[r1][c2 + 1] - s[r2\
    \ + 1][c1] + s[r1][c1];\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct CrossAccumulate\
    \ {\n    int H, W;\n    vector<vector<long long>> s;\n\n    CrossAccumulate(const\
    \ vector<vector<long long>>& grid) {\n        H = (int)grid.size();\n        W\
    \ = (int)grid[0].size();\n        s.assign(H + 1, vector<long long>(W + 1, 0));\n\
    \        for (int i = 0; i < H; i++) {\n            for (int j = 0; j < W; j++)\
    \ {\n                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + grid[i][j];\n\
    \            }\n        }\n    }\n\n    long long query(int r1, int c1, int r2,\
    \ int c2) const {\n        assert(0 <= r1 && r1 <= r2 && r2 < H && 0 <= c1 &&\
    \ c1 <= c2 && c2 < W);\n        return s[r2 + 1][c2 + 1] - s[r1][c2 + 1] - s[r2\
    \ + 1][c1] + s[r1][c1];\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp
- /library/algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp.html
title: algorithm_library/cpp-from-py/techniques/CrossAccumulate.cpp
---
