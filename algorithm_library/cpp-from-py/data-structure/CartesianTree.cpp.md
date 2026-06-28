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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ CartesianTree {\n    int root;\n    vector<int> left, right, parent;\n\n   \
    \ CartesianTree(const vector<T>& A) {\n        int n = (int)A.size();\n      \
    \  root = 0;\n        left.assign(n, -1);\n        right.assign(n, -1);\n    \
    \    parent.assign(n, -1);\n        vector<int> st(n, -1);\n        st[0] = 0;\n\
    \        int st_top = 0;\n        for (int i = 1; i < n; i++) {\n            if\
    \ (A[st[st_top]] > A[i]) {\n                while (st_top >= 1 && A[st[st_top\
    \ - 1]] > A[i]) st_top--;\n                left[i] = st[st_top];\n           \
    \     parent[left[i]] = i;\n                if (st_top == 0) {\n             \
    \       root = i;\n                } else {\n                    parent[i] = st[st_top\
    \ - 1];\n                    right[parent[i]] = i;\n                }\n      \
    \          st[st_top] = i;\n            } else {\n                parent[i] =\
    \ st[st_top];\n                right[parent[i]] = i;\n                st_top++;\n\
    \                st[st_top] = i;\n            }\n        }\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ CartesianTree {\n    int root;\n    vector<int> left, right, parent;\n\n   \
    \ CartesianTree(const vector<T>& A) {\n        int n = (int)A.size();\n      \
    \  root = 0;\n        left.assign(n, -1);\n        right.assign(n, -1);\n    \
    \    parent.assign(n, -1);\n        vector<int> st(n, -1);\n        st[0] = 0;\n\
    \        int st_top = 0;\n        for (int i = 1; i < n; i++) {\n            if\
    \ (A[st[st_top]] > A[i]) {\n                while (st_top >= 1 && A[st[st_top\
    \ - 1]] > A[i]) st_top--;\n                left[i] = st[st_top];\n           \
    \     parent[left[i]] = i;\n                if (st_top == 0) {\n             \
    \       root = i;\n                } else {\n                    parent[i] = st[st_top\
    \ - 1];\n                    right[parent[i]] = i;\n                }\n      \
    \          st[st_top] = i;\n            } else {\n                parent[i] =\
    \ st[st_top];\n                right[parent[i]] = i;\n                st_top++;\n\
    \                st[st_top] = i;\n            }\n        }\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp
- /library/algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp.html
title: algorithm_library/cpp-from-py/data-structure/CartesianTree.cpp
---
