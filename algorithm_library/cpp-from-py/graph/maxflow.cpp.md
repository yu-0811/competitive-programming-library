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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/maxflow.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct maxflow_edge {\n    int to,\
    \ rev_idx;\n    long long cap;\n};\n\nstruct maximum_flow {\n    int N;\n    vector<vector<maxflow_edge>>\
    \ G;\n    vector<bool> vis;\n\n    maximum_flow(int N_) : N(N_), G(N + 1) {}\n\
    \n    void add_edge(int a, int b, long long c) {\n        G[a].push_back({b, (int)G[b].size(),\
    \ c});\n        G[b].push_back({a, (int)G[a].size() - 1, 0});\n    }\n\n    long\
    \ long dfs(int v, int goal, long long f) {\n        if (v == goal) return f;\n\
    \        vis[v] = true;\n        for (auto& edge : G[v]) {\n            if (edge.cap\
    \ > 0 && !vis[edge.to]) {\n                long long flow = dfs(edge.to, goal,\
    \ min(f, edge.cap));\n                if (flow >= 1) {\n                    edge.cap\
    \ -= flow;\n                    G[edge.to][edge.rev_idx].cap += flow;\n      \
    \              return flow;\n                }\n            }\n        }\n   \
    \     return 0;\n    }\n\n    long long maxflow(int start, int goal) {\n     \
    \   long long total_flow = 0;\n        while (true) {\n            vis.assign(N\
    \ + 1, false);\n            long long res = dfs(start, goal, (long long)1e18);\n\
    \            if (res > 0) total_flow += res;\n            else break;\n      \
    \  }\n        return total_flow;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct maxflow_edge {\n\
    \    int to, rev_idx;\n    long long cap;\n};\n\nstruct maximum_flow {\n    int\
    \ N;\n    vector<vector<maxflow_edge>> G;\n    vector<bool> vis;\n\n    maximum_flow(int\
    \ N_) : N(N_), G(N + 1) {}\n\n    void add_edge(int a, int b, long long c) {\n\
    \        G[a].push_back({b, (int)G[b].size(), c});\n        G[b].push_back({a,\
    \ (int)G[a].size() - 1, 0});\n    }\n\n    long long dfs(int v, int goal, long\
    \ long f) {\n        if (v == goal) return f;\n        vis[v] = true;\n      \
    \  for (auto& edge : G[v]) {\n            if (edge.cap > 0 && !vis[edge.to]) {\n\
    \                long long flow = dfs(edge.to, goal, min(f, edge.cap));\n    \
    \            if (flow >= 1) {\n                    edge.cap -= flow;\n       \
    \             G[edge.to][edge.rev_idx].cap += flow;\n                    return\
    \ flow;\n                }\n            }\n        }\n        return 0;\n    }\n\
    \n    long long maxflow(int start, int goal) {\n        long long total_flow =\
    \ 0;\n        while (true) {\n            vis.assign(N + 1, false);\n        \
    \    long long res = dfs(start, goal, (long long)1e18);\n            if (res >\
    \ 0) total_flow += res;\n            else break;\n        }\n        return total_flow;\n\
    \    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/maxflow.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/maxflow.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/maxflow.cpp
- /library/algorithm_library/cpp-from-py/graph/maxflow.cpp.html
title: algorithm_library/cpp-from-py/graph/maxflow.cpp
---
