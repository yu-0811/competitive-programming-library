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
  bundledCode: "#line 1 \"algorithm_library/cpp/SparseTable.cpp\"\n\n// S: Sparse\
    \ Table \u3067\u6271\u3046\u30C7\u30FC\u30BF\u578B\n// op: \u6F14\u7B97\u95A2\u6570\
    \ (S op(S, S))\ntemplate <class S, S (*op)(S, S)>\nclass SparseTable {\n    int\
    \ n;\n    vector<vector<S>> table;\n    vector<int> log_table;\n\npublic:\n  \
    \  SparseTable() {}\n    SparseTable(const vector<S>& v) {\n        n = v.size();\n\
    \        log_table.resize(n + 1);\n        log_table[1] = 0;\n        for (int\
    \ i = 2; i <= n; i++) log_table[i] = log_table[i >> 1] + 1;\n\n        int max_k\
    \ = log_table[n] + 1;\n        table.assign(max_k, vector<S>(n));\n\n        for\
    \ (int i = 0; i < n; i++) table[0][i] = v[i];\n\n        for (int k = 1; k < max_k;\
    \ k++) {\n            int half = 1 << (k - 1);\n            for (int i = 0; i\
    \ + (1 << k) <= n; i++) {\n                table[k][i] = op(table[k - 1][i], table[k\
    \ - 1][i + half]);\n            }\n        }\n    }\n\n    S prod(int l, int r)\
    \ {\n        int b = r - l;\n        int k = log_table[b];\n        return op(table[k][l],\
    \ table[k][r - (1 << k)]);\n    }\n};\n"
  code: "\n// S: Sparse Table \u3067\u6271\u3046\u30C7\u30FC\u30BF\u578B\n// op: \u6F14\
    \u7B97\u95A2\u6570 (S op(S, S))\ntemplate <class S, S (*op)(S, S)>\nclass SparseTable\
    \ {\n    int n;\n    vector<vector<S>> table;\n    vector<int> log_table;\n\n\
    public:\n    SparseTable() {}\n    SparseTable(const vector<S>& v) {\n       \
    \ n = v.size();\n        log_table.resize(n + 1);\n        log_table[1] = 0;\n\
    \        for (int i = 2; i <= n; i++) log_table[i] = log_table[i >> 1] + 1;\n\n\
    \        int max_k = log_table[n] + 1;\n        table.assign(max_k, vector<S>(n));\n\
    \n        for (int i = 0; i < n; i++) table[0][i] = v[i];\n\n        for (int\
    \ k = 1; k < max_k; k++) {\n            int half = 1 << (k - 1);\n           \
    \ for (int i = 0; i + (1 << k) <= n; i++) {\n                table[k][i] = op(table[k\
    \ - 1][i], table[k - 1][i + half]);\n            }\n        }\n    }\n\n    S\
    \ prod(int l, int r) {\n        int b = r - l;\n        int k = log_table[b];\n\
    \        return op(table[k][l], table[k][r - (1 << k)]);\n    }\n};"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/SparseTable.cpp
  requiredBy: []
  timestamp: '2026-04-15 17:42:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/SparseTable.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/SparseTable.cpp
- /library/algorithm_library/cpp/SparseTable.cpp.html
title: algorithm_library/cpp/SparseTable.cpp
---
