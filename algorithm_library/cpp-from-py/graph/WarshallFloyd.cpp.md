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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nvector<vector<long long>> WarshallFloyd(int\
    \ N, const vector<vector<pair<int, long long>>>& G, long long inf = (long long)1e18)\
    \ {\n    vector<vector<long long>> dist(N + 1, vector<long long>(N + 1, inf));\n\
    \    for (int i = 0; i <= N; i++) dist[i][i] = 0;\n    for (int i = 1; i <= N;\
    \ i++) {\n        for (auto [j, c] : G[i]) {\n            dist[i][j] = min(dist[i][j],\
    \ c);\n            dist[j][i] = min(dist[j][i], c);\n        }\n    }\n    for\
    \ (int k = 1; k <= N; k++) {\n        for (int i = 1; i <= N; i++) {\n       \
    \     for (int j = 1; j <= N; j++) {\n                if (dist[i][k] == inf ||\
    \ dist[k][j] == inf) continue;\n                dist[i][j] = min(dist[i][j], dist[i][k]\
    \ + dist[k][j]);\n            }\n        }\n    }\n    return dist;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<vector<long long>>\
    \ WarshallFloyd(int N, const vector<vector<pair<int, long long>>>& G, long long\
    \ inf = (long long)1e18) {\n    vector<vector<long long>> dist(N + 1, vector<long\
    \ long>(N + 1, inf));\n    for (int i = 0; i <= N; i++) dist[i][i] = 0;\n    for\
    \ (int i = 1; i <= N; i++) {\n        for (auto [j, c] : G[i]) {\n           \
    \ dist[i][j] = min(dist[i][j], c);\n            dist[j][i] = min(dist[j][i], c);\n\
    \        }\n    }\n    for (int k = 1; k <= N; k++) {\n        for (int i = 1;\
    \ i <= N; i++) {\n            for (int j = 1; j <= N; j++) {\n               \
    \ if (dist[i][k] == inf || dist[k][j] == inf) continue;\n                dist[i][j]\
    \ = min(dist[i][j], dist[i][k] + dist[k][j]);\n            }\n        }\n    }\n\
    \    return dist;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp
- /library/algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp.html
title: algorithm_library/cpp-from-py/graph/WarshallFloyd.cpp
---
