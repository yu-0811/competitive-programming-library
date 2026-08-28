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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ MergeSortTree {\n    int n, size;\n    vector<vector<T>> tree;\n\n    MergeSortTree(const\
    \ vector<T>& data) {\n        n = (int)data.size();\n        size = 1;\n     \
    \   while (size < n) size <<= 1;\n        tree.assign(2 * size, {});\n       \
    \ for (int i = 0; i < n; i++) tree[size + i] = {data[i]};\n        for (int i\
    \ = size - 1; i > 0; i--) {\n            tree[i].resize(tree[2 * i].size() + tree[2\
    \ * i + 1].size());\n            merge(tree[2 * i].begin(), tree[2 * i].end(),\
    \ tree[2 * i + 1].begin(), tree[2 * i + 1].end(), tree[i].begin());\n        }\n\
    \    }\n\n    int query_leq(int l, int r, const T& x) const {\n        l += size;\n\
    \        r += size;\n        int res = 0;\n        while (l < r) {\n         \
    \   if (l & 1) res += upper_bound(tree[l].begin(), tree[l].end(), x) - tree[l].begin(),\
    \ l++;\n            if (r & 1) --r, res += upper_bound(tree[r].begin(), tree[r].end(),\
    \ x) - tree[r].begin();\n            l >>= 1;\n            r >>= 1;\n        }\n\
    \        return res;\n    }\n\n    int query_range(int l, int r, const T& a, const\
    \ T& b) const {\n        l += size;\n        r += size;\n        int res = 0;\n\
    \        while (l < r) {\n            if (l & 1) {\n                res += lower_bound(tree[l].begin(),\
    \ tree[l].end(), b) - lower_bound(tree[l].begin(), tree[l].end(), a);\n      \
    \          l++;\n            }\n            if (r & 1) {\n                --r;\n\
    \                res += lower_bound(tree[r].begin(), tree[r].end(), b) - lower_bound(tree[r].begin(),\
    \ tree[r].end(), a);\n            }\n            l >>= 1;\n            r >>= 1;\n\
    \        }\n        return res;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ MergeSortTree {\n    int n, size;\n    vector<vector<T>> tree;\n\n    MergeSortTree(const\
    \ vector<T>& data) {\n        n = (int)data.size();\n        size = 1;\n     \
    \   while (size < n) size <<= 1;\n        tree.assign(2 * size, {});\n       \
    \ for (int i = 0; i < n; i++) tree[size + i] = {data[i]};\n        for (int i\
    \ = size - 1; i > 0; i--) {\n            tree[i].resize(tree[2 * i].size() + tree[2\
    \ * i + 1].size());\n            merge(tree[2 * i].begin(), tree[2 * i].end(),\
    \ tree[2 * i + 1].begin(), tree[2 * i + 1].end(), tree[i].begin());\n        }\n\
    \    }\n\n    int query_leq(int l, int r, const T& x) const {\n        l += size;\n\
    \        r += size;\n        int res = 0;\n        while (l < r) {\n         \
    \   if (l & 1) res += upper_bound(tree[l].begin(), tree[l].end(), x) - tree[l].begin(),\
    \ l++;\n            if (r & 1) --r, res += upper_bound(tree[r].begin(), tree[r].end(),\
    \ x) - tree[r].begin();\n            l >>= 1;\n            r >>= 1;\n        }\n\
    \        return res;\n    }\n\n    int query_range(int l, int r, const T& a, const\
    \ T& b) const {\n        l += size;\n        r += size;\n        int res = 0;\n\
    \        while (l < r) {\n            if (l & 1) {\n                res += lower_bound(tree[l].begin(),\
    \ tree[l].end(), b) - lower_bound(tree[l].begin(), tree[l].end(), a);\n      \
    \          l++;\n            }\n            if (r & 1) {\n                --r;\n\
    \                res += lower_bound(tree[r].begin(), tree[r].end(), b) - lower_bound(tree[r].begin(),\
    \ tree[r].end(), a);\n            }\n            l >>= 1;\n            r >>= 1;\n\
    \        }\n        return res;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp
- /library/algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp.html
title: algorithm_library/cpp-from-py/data-structure/MargeSortTree.cpp
---
