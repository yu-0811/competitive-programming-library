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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class Add, class\
    \ Del, class Answer>\nauto mos_algorithm(int n, const vector<pair<int, int>>&\
    \ queries, Add add, Del del, Answer answer) {\n    int q = (int)queries.size();\n\
    \    int B = max(1, (int)ceil(sqrt(3.0) * n / (sqrt(2.0) * sqrt(max(1, q)))));\n\
    \    vector<int> order(q);\n    iota(order.begin(), order.end(), 0);\n    sort(order.begin(),\
    \ order.end(), [&](int i, int j) {\n        auto [li, ri] = queries[i];\n    \
    \    auto [lj, rj] = queries[j];\n        int bi = li / B, bj = lj / B;\n    \
    \    if (bi != bj) return bi < bj;\n        return (bi & 1) ? ri < rj : ri > rj;\n\
    \    });\n    using R = decltype(answer(0));\n    vector<R> ret(q);\n    int L\
    \ = 0, Rr = 0;\n    for (int i : order) {\n        auto [l, r] = queries[i];\n\
    \        while (Rr < r) add(Rr++);\n        while (Rr > r) del(--Rr);\n      \
    \  while (L < l) del(L++);\n        while (L > l) add(--L);\n        ret[i] =\
    \ answer(i);\n    }\n    return ret;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class Add, class\
    \ Del, class Answer>\nauto mos_algorithm(int n, const vector<pair<int, int>>&\
    \ queries, Add add, Del del, Answer answer) {\n    int q = (int)queries.size();\n\
    \    int B = max(1, (int)ceil(sqrt(3.0) * n / (sqrt(2.0) * sqrt(max(1, q)))));\n\
    \    vector<int> order(q);\n    iota(order.begin(), order.end(), 0);\n    sort(order.begin(),\
    \ order.end(), [&](int i, int j) {\n        auto [li, ri] = queries[i];\n    \
    \    auto [lj, rj] = queries[j];\n        int bi = li / B, bj = lj / B;\n    \
    \    if (bi != bj) return bi < bj;\n        return (bi & 1) ? ri < rj : ri > rj;\n\
    \    });\n    using R = decltype(answer(0));\n    vector<R> ret(q);\n    int L\
    \ = 0, Rr = 0;\n    for (int i : order) {\n        auto [l, r] = queries[i];\n\
    \        while (Rr < r) add(Rr++);\n        while (Rr > r) del(--Rr);\n      \
    \  while (L < l) del(L++);\n        while (L > l) add(--L);\n        ret[i] =\
    \ answer(i);\n    }\n    return ret;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp
- /library/algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp.html
title: algorithm_library/cpp-from-py/data-structure/Mos_algorithm.cpp
---
