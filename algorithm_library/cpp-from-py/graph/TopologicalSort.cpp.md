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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/TopologicalSort.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> TopologicalSort(int\
    \ N, const vector<vector<int>>& G) {\n    vector<int> sortedVertices, indegree(N\
    \ + 1, 0);\n    for (int v = 1; v <= N; v++) for (int v2 : G[v]) indegree[v2]++;\n\
    \    queue<int> que;\n    for (int v = 1; v <= N; v++) if (indegree[v] == 0) que.push(v);\n\
    \    while (!que.empty()) {\n        int v = que.front();\n        que.pop();\n\
    \        sortedVertices.push_back(v);\n        for (int v2 : G[v]) {\n       \
    \     indegree[v2]--;\n            if (indegree[v2] == 0) que.push(v2);\n    \
    \    }\n    }\n    if ((int)sortedVertices.size() != N) return {};\n    return\
    \ sortedVertices;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> TopologicalSort(int\
    \ N, const vector<vector<int>>& G) {\n    vector<int> sortedVertices, indegree(N\
    \ + 1, 0);\n    for (int v = 1; v <= N; v++) for (int v2 : G[v]) indegree[v2]++;\n\
    \    queue<int> que;\n    for (int v = 1; v <= N; v++) if (indegree[v] == 0) que.push(v);\n\
    \    while (!que.empty()) {\n        int v = que.front();\n        que.pop();\n\
    \        sortedVertices.push_back(v);\n        for (int v2 : G[v]) {\n       \
    \     indegree[v2]--;\n            if (indegree[v2] == 0) que.push(v2);\n    \
    \    }\n    }\n    if ((int)sortedVertices.size() != N) return {};\n    return\
    \ sortedVertices;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/TopologicalSort.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/TopologicalSort.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/TopologicalSort.cpp
- /library/algorithm_library/cpp-from-py/graph/TopologicalSort.cpp.html
title: algorithm_library/cpp-from-py/graph/TopologicalSort.cpp
---
