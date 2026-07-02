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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/imos.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct imos {\n    vector<vector<long\
    \ long>> grid;\n\n    imos(int H, int W) : grid(H, vector<long long>(W, 0)) {}\n\
    \n    void add(int i0, int j0, int i1, int j1, long long increment) {\n      \
    \  assert(0 <= i0 && i0 <= i1 && i1 < (int)grid.size());\n        assert(0 <=\
    \ j0 && j0 <= j1 && j1 < (int)grid[0].size());\n        grid[i0][j0] += increment;\n\
    \        if (i1 + 1 < (int)grid.size()) grid[i1 + 1][j0] -= increment;\n     \
    \   if (j1 + 1 < (int)grid[0].size()) grid[i0][j1 + 1] -= increment;\n       \
    \ if (i1 + 1 < (int)grid.size() && j1 + 1 < (int)grid[0].size()) grid[i1 + 1][j1\
    \ + 1] += increment;\n    }\n\n    vector<vector<long long>> cross_accumulate()\
    \ {\n        for (auto& row : grid) {\n            for (int j = 1; j < (int)row.size();\
    \ j++) row[j] += row[j - 1];\n        }\n        for (int j = 0; j < (int)grid[0].size();\
    \ j++) {\n            for (int i = 1; i < (int)grid.size(); i++) grid[i][j] +=\
    \ grid[i - 1][j];\n        }\n        return grid;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct imos {\n    vector<vector<long\
    \ long>> grid;\n\n    imos(int H, int W) : grid(H, vector<long long>(W, 0)) {}\n\
    \n    void add(int i0, int j0, int i1, int j1, long long increment) {\n      \
    \  assert(0 <= i0 && i0 <= i1 && i1 < (int)grid.size());\n        assert(0 <=\
    \ j0 && j0 <= j1 && j1 < (int)grid[0].size());\n        grid[i0][j0] += increment;\n\
    \        if (i1 + 1 < (int)grid.size()) grid[i1 + 1][j0] -= increment;\n     \
    \   if (j1 + 1 < (int)grid[0].size()) grid[i0][j1 + 1] -= increment;\n       \
    \ if (i1 + 1 < (int)grid.size() && j1 + 1 < (int)grid[0].size()) grid[i1 + 1][j1\
    \ + 1] += increment;\n    }\n\n    vector<vector<long long>> cross_accumulate()\
    \ {\n        for (auto& row : grid) {\n            for (int j = 1; j < (int)row.size();\
    \ j++) row[j] += row[j - 1];\n        }\n        for (int j = 0; j < (int)grid[0].size();\
    \ j++) {\n            for (int i = 1; i < (int)grid.size(); i++) grid[i][j] +=\
    \ grid[i - 1][j];\n        }\n        return grid;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/imos.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/imos.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/imos.cpp
- /library/algorithm_library/cpp-from-py/techniques/imos.cpp.html
title: algorithm_library/cpp-from-py/techniques/imos.cpp
---
