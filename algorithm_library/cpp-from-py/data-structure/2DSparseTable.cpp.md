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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T, class Op>\n\
    struct SparseTable2D {\n    int H, W, K, L;\n    Op op;\n    vector<vector<vector<vector<T>>>>\
    \ table;\n\n    SparseTable2D(const vector<vector<T>>& grid, Op op) : op(op) {\n\
    \        H = (int)grid.size();\n        W = (int)grid[0].size();\n        K =\
    \ 32 - __builtin_clz(H);\n        L = 32 - __builtin_clz(W);\n        table.assign(K,\
    \ vector<vector<vector<T>>>(L, vector<vector<T>>(H, vector<T>(W))));\n       \
    \ for (int i = 0; i < H; i++) {\n            for (int j = 0; j < W; j++) table[0][0][i][j]\
    \ = grid[i][j];\n        }\n        for (int l = 1; l < L; l++) {\n          \
    \  int width = 1 << l, half = width >> 1;\n            for (int i = 0; i < H;\
    \ i++) {\n                for (int j = 0; j + width <= W; j++) {\n           \
    \         table[0][l][i][j] = op(table[0][l - 1][i][j], table[0][l - 1][i][j +\
    \ half]);\n                }\n            }\n        }\n        for (int k = 1;\
    \ k < K; k++) {\n            int height = 1 << k, half = height >> 1;\n      \
    \      for (int l = 0; l < L; l++) {\n                int width = 1 << l;\n  \
    \              for (int i = 0; i + height <= H; i++) {\n                    for\
    \ (int j = 0; j + width <= W; j++) {\n                        table[k][l][i][j]\
    \ = op(table[k - 1][l][i][j], table[k - 1][l][i + half][j]);\n               \
    \     }\n                }\n            }\n        }\n    }\n\n    T query(int\
    \ r1, int c1, int r2, int c2) const {\n        assert(0 <= r1 && r1 <= r2 && r2\
    \ < H);\n        assert(0 <= c1 && c1 <= c2 && c2 < W);\n        int height =\
    \ r2 - r1 + 1, width = c2 - c1 + 1;\n        int k = 31 - __builtin_clz(height);\n\
    \        int l = 31 - __builtin_clz(width);\n        int r2_start = r2 - (1 <<\
    \ k) + 1;\n        int c2_start = c2 - (1 << l) + 1;\n        T tl = table[k][l][r1][c1];\n\
    \        T tr = table[k][l][r1][c2_start];\n        T bl = table[k][l][r2_start][c1];\n\
    \        T br = table[k][l][r2_start][c2_start];\n        return op(op(tl, tr),\
    \ op(bl, br));\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T, class\
    \ Op>\nstruct SparseTable2D {\n    int H, W, K, L;\n    Op op;\n    vector<vector<vector<vector<T>>>>\
    \ table;\n\n    SparseTable2D(const vector<vector<T>>& grid, Op op) : op(op) {\n\
    \        H = (int)grid.size();\n        W = (int)grid[0].size();\n        K =\
    \ 32 - __builtin_clz(H);\n        L = 32 - __builtin_clz(W);\n        table.assign(K,\
    \ vector<vector<vector<T>>>(L, vector<vector<T>>(H, vector<T>(W))));\n       \
    \ for (int i = 0; i < H; i++) {\n            for (int j = 0; j < W; j++) table[0][0][i][j]\
    \ = grid[i][j];\n        }\n        for (int l = 1; l < L; l++) {\n          \
    \  int width = 1 << l, half = width >> 1;\n            for (int i = 0; i < H;\
    \ i++) {\n                for (int j = 0; j + width <= W; j++) {\n           \
    \         table[0][l][i][j] = op(table[0][l - 1][i][j], table[0][l - 1][i][j +\
    \ half]);\n                }\n            }\n        }\n        for (int k = 1;\
    \ k < K; k++) {\n            int height = 1 << k, half = height >> 1;\n      \
    \      for (int l = 0; l < L; l++) {\n                int width = 1 << l;\n  \
    \              for (int i = 0; i + height <= H; i++) {\n                    for\
    \ (int j = 0; j + width <= W; j++) {\n                        table[k][l][i][j]\
    \ = op(table[k - 1][l][i][j], table[k - 1][l][i + half][j]);\n               \
    \     }\n                }\n            }\n        }\n    }\n\n    T query(int\
    \ r1, int c1, int r2, int c2) const {\n        assert(0 <= r1 && r1 <= r2 && r2\
    \ < H);\n        assert(0 <= c1 && c1 <= c2 && c2 < W);\n        int height =\
    \ r2 - r1 + 1, width = c2 - c1 + 1;\n        int k = 31 - __builtin_clz(height);\n\
    \        int l = 31 - __builtin_clz(width);\n        int r2_start = r2 - (1 <<\
    \ k) + 1;\n        int c2_start = c2 - (1 << l) + 1;\n        T tl = table[k][l][r1][c1];\n\
    \        T tr = table[k][l][r1][c2_start];\n        T bl = table[k][l][r2_start][c1];\n\
    \        T br = table[k][l][r2_start][c2_start];\n        return op(op(tl, tr),\
    \ op(bl, br));\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp
- /library/algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp.html
title: algorithm_library/cpp-from-py/data-structure/2DSparseTable.cpp
---
