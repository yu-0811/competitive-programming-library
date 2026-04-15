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
  bundledCode: "#line 1 \"algorithm_library/cpp/DisjointSparseTable.cpp\"\n#include\
    \ <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\
    \n// S: Disjoint Sparse Table \u3067\u6271\u3046\u30C7\u30FC\u30BF\u578B\n// op:\
    \ \u6F14\u7B97\u95A2\u6570 (S op(S, S))\ntemplate <class S, S (*op)(S, S)>\nclass\
    \ DisjointSparseTable {\n    int n;\n    vector<vector<S>> table;\n    vector<int>\
    \ log_table;\n\npublic:\n    DisjointSparseTable() {}\n    DisjointSparseTable(const\
    \ vector<S>& v) {\n        n = v.size();\n        \n        // bit_length\u76F8\
    \u5F53\u306E\u30C6\u30FC\u30D6\u30EB\u30B5\u30A4\u30BA\u78BA\u4FDD\n        int\
    \ b = 1;\n        while (b <= n) b <<= 1;\n        log_table.resize(b + 1);\n\
    \        log_table[1] = 0;\n        for (int i = 2; i <= b; i++) log_table[i]\
    \ = log_table[i >> 1] + 1;\n\n        int max_k = (n == 0) ? 0 : log_table[n]\
    \ + 1;\n        // \u914D\u5217\u306E\u30B5\u30A4\u30BA\u304C2\u306E\u7D2F\u4E57\
    \u3067\u306A\u3044\u5834\u5408\u306E\u305F\u3081\u306B\u5C11\u3057\u4F59\u88D5\
    \u3092\u3082\u305F\u305B\u308B\u8A08\u7B97\n        if ((1 << (max_k - 1)) < n)\
    \ max_k++;\n\n        table.assign(max_k, vector<S>(n));\n\n        for (int k\
    \ = 0; k < max_k; k++) {\n            int block_size = 1 << (k + 1);\n       \
    \     int half = 1 << k;\n\n            for (int start = 0; start < n; start +=\
    \ block_size) {\n                int mid = min(start + half, n);\n           \
    \     int end = min(start + block_size, n);\n\n                // \u5DE6\u5074\
    \ [start, mid)\n                if (start < mid) {\n                    table[k][mid\
    \ - 1] = v[mid - 1];\n                    for (int i = mid - 2; i >= start; i--)\
    \ {\n                        table[k][i] = op(v[i], table[k][i + 1]);\n      \
    \              }\n                }\n\n                // \u53F3\u5074 [mid, end)\n\
    \                if (mid < end) {\n                    table[k][mid] = v[mid];\n\
    \                    for (int i = mid + 1; i < end; i++) {\n                 \
    \       table[k][i] = op(table[k][i - 1], v[i]);\n                    }\n    \
    \            }\n            }\n        }\n    }\n\n    S query(int l, int r) {\n\
    \        if (l == r - 1) return table[0][l];\n        int k = log_table[l ^ (r\
    \ - 1)];\n        return op(table[k][l], table[k][r - 1]);\n    }\n};\n"
  code: "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace\
    \ std;\n\n// S: Disjoint Sparse Table \u3067\u6271\u3046\u30C7\u30FC\u30BF\u578B\
    \n// op: \u6F14\u7B97\u95A2\u6570 (S op(S, S))\ntemplate <class S, S (*op)(S,\
    \ S)>\nclass DisjointSparseTable {\n    int n;\n    vector<vector<S>> table;\n\
    \    vector<int> log_table;\n\npublic:\n    DisjointSparseTable() {}\n    DisjointSparseTable(const\
    \ vector<S>& v) {\n        n = v.size();\n        \n        // bit_length\u76F8\
    \u5F53\u306E\u30C6\u30FC\u30D6\u30EB\u30B5\u30A4\u30BA\u78BA\u4FDD\n        int\
    \ b = 1;\n        while (b <= n) b <<= 1;\n        log_table.resize(b + 1);\n\
    \        log_table[1] = 0;\n        for (int i = 2; i <= b; i++) log_table[i]\
    \ = log_table[i >> 1] + 1;\n\n        int max_k = (n == 0) ? 0 : log_table[n]\
    \ + 1;\n        // \u914D\u5217\u306E\u30B5\u30A4\u30BA\u304C2\u306E\u7D2F\u4E57\
    \u3067\u306A\u3044\u5834\u5408\u306E\u305F\u3081\u306B\u5C11\u3057\u4F59\u88D5\
    \u3092\u3082\u305F\u305B\u308B\u8A08\u7B97\n        if ((1 << (max_k - 1)) < n)\
    \ max_k++;\n\n        table.assign(max_k, vector<S>(n));\n\n        for (int k\
    \ = 0; k < max_k; k++) {\n            int block_size = 1 << (k + 1);\n       \
    \     int half = 1 << k;\n\n            for (int start = 0; start < n; start +=\
    \ block_size) {\n                int mid = min(start + half, n);\n           \
    \     int end = min(start + block_size, n);\n\n                // \u5DE6\u5074\
    \ [start, mid)\n                if (start < mid) {\n                    table[k][mid\
    \ - 1] = v[mid - 1];\n                    for (int i = mid - 2; i >= start; i--)\
    \ {\n                        table[k][i] = op(v[i], table[k][i + 1]);\n      \
    \              }\n                }\n\n                // \u53F3\u5074 [mid, end)\n\
    \                if (mid < end) {\n                    table[k][mid] = v[mid];\n\
    \                    for (int i = mid + 1; i < end; i++) {\n                 \
    \       table[k][i] = op(table[k][i - 1], v[i]);\n                    }\n    \
    \            }\n            }\n        }\n    }\n\n    S query(int l, int r) {\n\
    \        if (l == r - 1) return table[0][l];\n        int k = log_table[l ^ (r\
    \ - 1)];\n        return op(table[k][l], table[k][r - 1]);\n    }\n};"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/DisjointSparseTable.cpp
  requiredBy: []
  timestamp: '2026-04-15 17:42:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/DisjointSparseTable.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/DisjointSparseTable.cpp
- /library/algorithm_library/cpp/DisjointSparseTable.cpp.html
title: algorithm_library/cpp/DisjointSparseTable.cpp
---
