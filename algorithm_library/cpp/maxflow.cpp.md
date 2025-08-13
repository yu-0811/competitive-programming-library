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
  bundledCode: "#line 1 \"algorithm_library/cpp/maxflow.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define\
    \ print_vec(v) { rep(i, v.size()) cout << v[i] << \" \"; cout << endl; }\n#define\
    \ ll long long\nconst int MOD = 998244353;\nconst int INF = 1000000000;\nconst\
    \ ll INFll = 9223372036854775807;\n\nstruct maxflow_edge{\n    int to, cap, rev_idx;\n\
    };\n\nclass maximumflow{\n    public:\n        vector<vector<maxflow_edge>> G;\n\
    \        vector<bool> vis;\n\n        void init(int N){\n            G.resize(N+1);\n\
    \            vis.resize(N+1,false);\n        }\n\n        void add_edge(int a,\
    \ int b, int c){\n            int ga_size = G[a].size();\n            int gb_size\
    \ = G[b].size();\n            G[a].emplace_back(maxflow_edge{b,c,gb_size});\n\
    \            G[b].emplace_back(maxflow_edge{a,0,ga_size});\n        }\n\n    \
    \    int dfs(int v, int goal, int f){\n            if (v==goal) return f;\n  \
    \          vis[v] = true;\n            for (auto &edge : G[v]){\n            \
    \    if (edge.cap == 0) continue;\n                if (vis[edge.to]) continue;\n\
    \                int flow = dfs(edge.to, goal, min(f, edge.cap));\n          \
    \      if (flow > 0){\n                    edge.cap -= flow;\n               \
    \     G[edge.to][edge.rev_idx].cap += flow;\n                    return flow;\n\
    \                }\n            }\n            return 0;\n        }\n\n      \
    \  int maxflow(int N, int M, int start, int goal){\n            int total_flow\
    \ = 0;\n            while (true){\n                for (int i=0; i<=N; i++) vis[i]\
    \ = false;\n                const int INF = 1000000000;\n                int res\
    \ = dfs(start,goal,INF);\n                if (res==0) break;\n               \
    \ total_flow += res;\n            }\n            return total_flow;\n        }\n\
    };\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n#define rep(i, n) for (int\
    \ i = 0; i < (int)(n); i++)\n#define print_vec(v) { rep(i, v.size()) cout << v[i]\
    \ << \" \"; cout << endl; }\n#define ll long long\nconst int MOD = 998244353;\n\
    const int INF = 1000000000;\nconst ll INFll = 9223372036854775807;\n\nstruct maxflow_edge{\n\
    \    int to, cap, rev_idx;\n};\n\nclass maximumflow{\n    public:\n        vector<vector<maxflow_edge>>\
    \ G;\n        vector<bool> vis;\n\n        void init(int N){\n            G.resize(N+1);\n\
    \            vis.resize(N+1,false);\n        }\n\n        void add_edge(int a,\
    \ int b, int c){\n            int ga_size = G[a].size();\n            int gb_size\
    \ = G[b].size();\n            G[a].emplace_back(maxflow_edge{b,c,gb_size});\n\
    \            G[b].emplace_back(maxflow_edge{a,0,ga_size});\n        }\n\n    \
    \    int dfs(int v, int goal, int f){\n            if (v==goal) return f;\n  \
    \          vis[v] = true;\n            for (auto &edge : G[v]){\n            \
    \    if (edge.cap == 0) continue;\n                if (vis[edge.to]) continue;\n\
    \                int flow = dfs(edge.to, goal, min(f, edge.cap));\n          \
    \      if (flow > 0){\n                    edge.cap -= flow;\n               \
    \     G[edge.to][edge.rev_idx].cap += flow;\n                    return flow;\n\
    \                }\n            }\n            return 0;\n        }\n\n      \
    \  int maxflow(int N, int M, int start, int goal){\n            int total_flow\
    \ = 0;\n            while (true){\n                for (int i=0; i<=N; i++) vis[i]\
    \ = false;\n                const int INF = 1000000000;\n                int res\
    \ = dfs(start,goal,INF);\n                if (res==0) break;\n               \
    \ total_flow += res;\n            }\n            return total_flow;\n        }\n\
    };\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/maxflow.cpp
  requiredBy: []
  timestamp: '2025-08-13 17:42:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/maxflow.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/maxflow.cpp
- /library/algorithm_library/cpp/maxflow.cpp.html
title: algorithm_library/cpp/maxflow.cpp
---
