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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\npair<bool, vector<int>> is_bipartite_graph(const\
    \ vector<vector<int>>& G, int N) {\n    vector<int> col(N + 1, -1);\n    auto\
    \ bfs = [&](int s) {\n        queue<int> que;\n        que.push(s);\n        while\
    \ (!que.empty()) {\n            int v = que.front();\n            que.pop();\n\
    \            for (int v2 : G[v]) {\n                if (col[v2] != -1) {\n   \
    \                 if (col[v] == col[v2]) return false;\n                    continue;\n\
    \                }\n                col[v2] = 1 - col[v];\n                que.push(v2);\n\
    \            }\n        }\n        return true;\n    };\n    for (int v = 1; v\
    \ <= N; v++) {\n        if (col[v] != -1) continue;\n        col[v] = 1;\n   \
    \     if (!bfs(v)) return {false, {}};\n    }\n    return {true, col};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\npair<bool, vector<int>>\
    \ is_bipartite_graph(const vector<vector<int>>& G, int N) {\n    vector<int> col(N\
    \ + 1, -1);\n    auto bfs = [&](int s) {\n        queue<int> que;\n        que.push(s);\n\
    \        while (!que.empty()) {\n            int v = que.front();\n          \
    \  que.pop();\n            for (int v2 : G[v]) {\n                if (col[v2]\
    \ != -1) {\n                    if (col[v] == col[v2]) return false;\n       \
    \             continue;\n                }\n                col[v2] = 1 - col[v];\n\
    \                que.push(v2);\n            }\n        }\n        return true;\n\
    \    };\n    for (int v = 1; v <= N; v++) {\n        if (col[v] != -1) continue;\n\
    \        col[v] = 1;\n        if (!bfs(v)) return {false, {}};\n    }\n    return\
    \ {true, col};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp
- /library/algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp.html
title: algorithm_library/cpp-from-py/graph/BipartiteGraph.cpp
---
