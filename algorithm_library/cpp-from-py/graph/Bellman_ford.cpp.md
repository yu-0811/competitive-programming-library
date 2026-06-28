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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/Bellman_ford.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nconst long long inf = (long\
    \ long)1e18;\n\npair<vector<long long>, bool> bellman_ford(const vector<tuple<int,\
    \ int, long long>>& Edges, int N, int s) {\n    vector<long long> dist(N + 1,\
    \ inf);\n    dist[s] = 0;\n    int cnt = 0;\n    while (cnt < N) {\n        bool\
    \ end = true;\n        for (auto [fro, to, cost] : Edges) {\n            if (dist[fro]\
    \ == inf) continue;\n            if (dist[to] > dist[fro] + cost) {\n        \
    \        dist[to] = dist[fro] + cost;\n                end = false;\n        \
    \    }\n        }\n        if (end) break;\n        cnt++;\n    }\n    return\
    \ {dist, cnt == N};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nconst long long inf = (long\
    \ long)1e18;\n\npair<vector<long long>, bool> bellman_ford(const vector<tuple<int,\
    \ int, long long>>& Edges, int N, int s) {\n    vector<long long> dist(N + 1,\
    \ inf);\n    dist[s] = 0;\n    int cnt = 0;\n    while (cnt < N) {\n        bool\
    \ end = true;\n        for (auto [fro, to, cost] : Edges) {\n            if (dist[fro]\
    \ == inf) continue;\n            if (dist[to] > dist[fro] + cost) {\n        \
    \        dist[to] = dist[fro] + cost;\n                end = false;\n        \
    \    }\n        }\n        if (end) break;\n        cnt++;\n    }\n    return\
    \ {dist, cnt == N};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/Bellman_ford.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/Bellman_ford.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/Bellman_ford.cpp
- /library/algorithm_library/cpp-from-py/graph/Bellman_ford.cpp.html
title: algorithm_library/cpp-from-py/graph/Bellman_ford.cpp
---
