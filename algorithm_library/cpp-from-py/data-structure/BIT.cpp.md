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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/BIT.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nstruct BIT {\n    int n;\n \
    \   vector<vector<long long>> bit;\n\n    BIT(int n_) : n(n_ + 1), bit(2, vector<long\
    \ long>(n, 0)) {}\n\n    void _add_sub(int p, int i, long long x) {\n        for\
    \ (int idx = i; idx < n; idx += idx & -idx) bit[p][idx] += x;\n    }\n\n    void\
    \ add(int l, int r, long long x) {\n        _add_sub(0, l, -x * (l - 1));\n  \
    \      _add_sub(0, r, x * (r - 1));\n        _add_sub(1, l, x);\n        _add_sub(1,\
    \ r, -x);\n    }\n\n    long long _sum_sub(int p, int i) const {\n        long\
    \ long s = 0;\n        for (int idx = i; idx > 0; idx -= idx & -idx) s += bit[p][idx];\n\
    \        return s;\n    }\n\n    long long SUM(int i) const {\n        return\
    \ _sum_sub(0, i) + _sum_sub(1, i) * i;\n    }\n\n    long long range_sum(int l,\
    \ int r) const {\n        return SUM(r - 1) - SUM(l - 1);\n    }\n\n    int lower_bound(long\
    \ long w) const {\n        if (w <= 0) return 0;\n        int x = 0, len = 1;\n\
    \        while (len < n) len <<= 1;\n        while (len > 0) {\n            if\
    \ (x + len < n && bit[1][x + len] < w) {\n                w -= bit[1][x + len];\n\
    \                x += len;\n            }\n            len >>= 1;\n        }\n\
    \        return x + 1;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct BIT {\n    int n;\n\
    \    vector<vector<long long>> bit;\n\n    BIT(int n_) : n(n_ + 1), bit(2, vector<long\
    \ long>(n, 0)) {}\n\n    void _add_sub(int p, int i, long long x) {\n        for\
    \ (int idx = i; idx < n; idx += idx & -idx) bit[p][idx] += x;\n    }\n\n    void\
    \ add(int l, int r, long long x) {\n        _add_sub(0, l, -x * (l - 1));\n  \
    \      _add_sub(0, r, x * (r - 1));\n        _add_sub(1, l, x);\n        _add_sub(1,\
    \ r, -x);\n    }\n\n    long long _sum_sub(int p, int i) const {\n        long\
    \ long s = 0;\n        for (int idx = i; idx > 0; idx -= idx & -idx) s += bit[p][idx];\n\
    \        return s;\n    }\n\n    long long SUM(int i) const {\n        return\
    \ _sum_sub(0, i) + _sum_sub(1, i) * i;\n    }\n\n    long long range_sum(int l,\
    \ int r) const {\n        return SUM(r - 1) - SUM(l - 1);\n    }\n\n    int lower_bound(long\
    \ long w) const {\n        if (w <= 0) return 0;\n        int x = 0, len = 1;\n\
    \        while (len < n) len <<= 1;\n        while (len > 0) {\n            if\
    \ (x + len < n && bit[1][x + len] < w) {\n                w -= bit[1][x + len];\n\
    \                x += len;\n            }\n            len >>= 1;\n        }\n\
    \        return x + 1;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/BIT.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/BIT.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/BIT.cpp
- /library/algorithm_library/cpp-from-py/data-structure/BIT.cpp.html
title: algorithm_library/cpp-from-py/data-structure/BIT.cpp
---
