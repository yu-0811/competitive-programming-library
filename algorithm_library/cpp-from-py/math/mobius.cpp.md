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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/mobius.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<T>& mobius(vector<T>&\
    \ A) {\n    int n = 0;\n    while ((1 << n) < (int)A.size()) n++;\n    assert((int)A.size()\
    \ == (1 << n));\n    for (int i = 0; i < n; i++) {\n        int bit = 1 << i;\n\
    \        for (int mask = 0; mask < (1 << n); mask++) {\n            if (!(mask\
    \ & bit)) A[mask] -= A[mask | bit];\n        }\n    }\n    return A;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nvector<T>&\
    \ mobius(vector<T>& A) {\n    int n = 0;\n    while ((1 << n) < (int)A.size())\
    \ n++;\n    assert((int)A.size() == (1 << n));\n    for (int i = 0; i < n; i++)\
    \ {\n        int bit = 1 << i;\n        for (int mask = 0; mask < (1 << n); mask++)\
    \ {\n            if (!(mask & bit)) A[mask] -= A[mask | bit];\n        }\n   \
    \ }\n    return A;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/mobius.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/mobius.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/mobius.cpp
- /library/algorithm_library/cpp-from-py/math/mobius.cpp.html
title: algorithm_library/cpp-from-py/math/mobius.cpp
---
