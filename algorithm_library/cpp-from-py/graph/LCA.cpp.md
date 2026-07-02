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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/LCA.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct LCA {\n    int N, bit;\n   \
    \ vector<vector<int>> parent;\n    vector<int> depth;\n\n    LCA(int N_, const\
    \ vector<vector<int>>& G, int root) : N(N_) {\n        bit = 32 - __builtin_clz(N)\
    \ + 2;\n        parent.assign(bit, vector<int>(N + 1, -1));\n        depth.assign(N\
    \ + 1, -1);\n        depth[root] = 0;\n        queue<int> que;\n        que.push(root);\n\
    \        while (!que.empty()) {\n            int v = que.front();\n          \
    \  que.pop();\n            for (int v2 : G[v]) {\n                if (depth[v2]\
    \ == -1) {\n                    depth[v2] = depth[v] + 1;\n                  \
    \  parent[0][v2] = v;\n                    que.push(v2);\n                }\n\
    \            }\n        }\n        for (int i = 1; i < bit; i++) {\n         \
    \   for (int j = 0; j <= N; j++) {\n                if (parent[i - 1][j] != -1)\
    \ parent[i][j] = parent[i - 1][parent[i - 1][j]];\n            }\n        }\n\
    \    }\n\n    int lca(int u, int v) const {\n        if (depth[u] < depth[v])\
    \ swap(u, v);\n        for (int k = 0; k < bit; k++) if (((depth[u] - depth[v])\
    \ >> k) & 1) u = parent[k][u];\n        if (u == v) return u;\n        for (int\
    \ k = bit - 1; k >= 0; k--) {\n            if (parent[k][u] != parent[k][v]) {\n\
    \                u = parent[k][u];\n                v = parent[k][v];\n      \
    \      }\n        }\n        return parent[0][u];\n    }\n\n    int get_distance(int\
    \ u, int v) const {\n        return depth[u] + depth[v] - 2 * depth[lca(u, v)];\n\
    \    }\n\n    bool is_on_path(int u, int v, int a) const {\n        return get_distance(u,\
    \ a) + get_distance(a, v) == get_distance(u, v);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct LCA {\n    int N,\
    \ bit;\n    vector<vector<int>> parent;\n    vector<int> depth;\n\n    LCA(int\
    \ N_, const vector<vector<int>>& G, int root) : N(N_) {\n        bit = 32 - __builtin_clz(N)\
    \ + 2;\n        parent.assign(bit, vector<int>(N + 1, -1));\n        depth.assign(N\
    \ + 1, -1);\n        depth[root] = 0;\n        queue<int> que;\n        que.push(root);\n\
    \        while (!que.empty()) {\n            int v = que.front();\n          \
    \  que.pop();\n            for (int v2 : G[v]) {\n                if (depth[v2]\
    \ == -1) {\n                    depth[v2] = depth[v] + 1;\n                  \
    \  parent[0][v2] = v;\n                    que.push(v2);\n                }\n\
    \            }\n        }\n        for (int i = 1; i < bit; i++) {\n         \
    \   for (int j = 0; j <= N; j++) {\n                if (parent[i - 1][j] != -1)\
    \ parent[i][j] = parent[i - 1][parent[i - 1][j]];\n            }\n        }\n\
    \    }\n\n    int lca(int u, int v) const {\n        if (depth[u] < depth[v])\
    \ swap(u, v);\n        for (int k = 0; k < bit; k++) if (((depth[u] - depth[v])\
    \ >> k) & 1) u = parent[k][u];\n        if (u == v) return u;\n        for (int\
    \ k = bit - 1; k >= 0; k--) {\n            if (parent[k][u] != parent[k][v]) {\n\
    \                u = parent[k][u];\n                v = parent[k][v];\n      \
    \      }\n        }\n        return parent[0][u];\n    }\n\n    int get_distance(int\
    \ u, int v) const {\n        return depth[u] + depth[v] - 2 * depth[lca(u, v)];\n\
    \    }\n\n    bool is_on_path(int u, int v, int a) const {\n        return get_distance(u,\
    \ a) + get_distance(a, v) == get_distance(u, v);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/LCA.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/LCA.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/LCA.cpp
- /library/algorithm_library/cpp-from-py/graph/LCA.cpp.html
title: algorithm_library/cpp-from-py/graph/LCA.cpp
---
