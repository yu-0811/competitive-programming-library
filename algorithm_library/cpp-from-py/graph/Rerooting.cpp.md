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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/Rerooting.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T, class Merge, class\
    \ CalcNodeValue, class CalcAns>\nstruct rerooting {\n    int n;\n    T identity;\n\
    \    Merge merge;\n    CalcNodeValue calc_node_value;\n    CalcAns calc_ans;\n\
    \    vector<vector<int>> adjacents, indexForAdjacents;\n    vector<vector<T>>\
    \ childSubTreeValue;\n    vector<T> ans;\n    vector<int> parent, order;\n\n \
    \   rerooting(int n_, const vector<pair<int, int>>& edges, T identity_, Merge\
    \ merge_, CalcNodeValue calc_node_value_, CalcAns calc_ans_)\n        : n(n_),\
    \ identity(identity_), merge(merge_), calc_node_value(calc_node_value_), calc_ans(calc_ans_),\n\
    \          adjacents(n + 1), indexForAdjacents(n + 1), ans(n + 1, identity) {\n\
    \        for (auto [a, b] : edges) {\n            indexForAdjacents[a].push_back(adjacents[b].size());\n\
    \            indexForAdjacents[b].push_back(adjacents[a].size());\n          \
    \  adjacents[a].push_back(b);\n            adjacents[b].push_back(a);\n      \
    \  }\n        childSubTreeValue.resize(n + 1);\n        for (int i = 0; i <= n;\
    \ i++) childSubTreeValue[i].assign(adjacents[i].size(), identity);\n    }\n\n\
    \    void dfs1(int root) {\n        parent.assign(n + 1, -1);\n        order.clear();\n\
    \        vector<int> st{root};\n        while (!st.empty()) {\n            int\
    \ v = st.back();\n            st.pop_back();\n            order.push_back(v);\n\
    \            for (int u : adjacents[v]) {\n                if (u == parent[v])\
    \ continue;\n                parent[u] = v;\n                st.push_back(u);\n\
    \            }\n        }\n        for (int oi = (int)order.size() - 1; oi >=\
    \ 1; oi--) {\n            int v = order[oi], pv = parent[v];\n            T result\
    \ = identity;\n            int parentIndex = -1;\n            for (int i = 0;\
    \ i < (int)adjacents[v].size(); i++) {\n                int u = adjacents[v][i];\n\
    \                if (u == pv) {\n                    parentIndex = i;\n      \
    \              continue;\n                }\n                result = merge(result,\
    \ childSubTreeValue[v][i]);\n            }\n            childSubTreeValue[pv][indexForAdjacents[v][parentIndex]]\
    \ = calc_node_value(result, v);\n        }\n    }\n\n    void dfs2() {\n     \
    \   for (int v : order) {\n            T accFromLeft = identity;\n           \
    \ vector<T> accFromRight(adjacents[v].size(), identity);\n            for (int\
    \ i = (int)adjacents[v].size() - 2; i >= 0; i--) {\n                accFromRight[i]\
    \ = merge(childSubTreeValue[v][i + 1], accFromRight[i + 1]);\n            }\n\
    \            for (int j = 0; j < (int)adjacents[v].size(); j++) {\n          \
    \      int u = adjacents[v][j];\n                T result = calc_node_value(merge(accFromLeft,\
    \ accFromRight[j]), v);\n                childSubTreeValue[u][indexForAdjacents[v][j]]\
    \ = result;\n                accFromLeft = merge(accFromLeft, childSubTreeValue[v][j]);\n\
    \            }\n            ans[v] = calc_ans(accFromLeft, v);\n        }\n  \
    \  }\n\n    vector<T> run(int root = 1) {\n        dfs1(root);\n        dfs2();\n\
    \        return ans;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T, class\
    \ Merge, class CalcNodeValue, class CalcAns>\nstruct rerooting {\n    int n;\n\
    \    T identity;\n    Merge merge;\n    CalcNodeValue calc_node_value;\n    CalcAns\
    \ calc_ans;\n    vector<vector<int>> adjacents, indexForAdjacents;\n    vector<vector<T>>\
    \ childSubTreeValue;\n    vector<T> ans;\n    vector<int> parent, order;\n\n \
    \   rerooting(int n_, const vector<pair<int, int>>& edges, T identity_, Merge\
    \ merge_, CalcNodeValue calc_node_value_, CalcAns calc_ans_)\n        : n(n_),\
    \ identity(identity_), merge(merge_), calc_node_value(calc_node_value_), calc_ans(calc_ans_),\n\
    \          adjacents(n + 1), indexForAdjacents(n + 1), ans(n + 1, identity) {\n\
    \        for (auto [a, b] : edges) {\n            indexForAdjacents[a].push_back(adjacents[b].size());\n\
    \            indexForAdjacents[b].push_back(adjacents[a].size());\n          \
    \  adjacents[a].push_back(b);\n            adjacents[b].push_back(a);\n      \
    \  }\n        childSubTreeValue.resize(n + 1);\n        for (int i = 0; i <= n;\
    \ i++) childSubTreeValue[i].assign(adjacents[i].size(), identity);\n    }\n\n\
    \    void dfs1(int root) {\n        parent.assign(n + 1, -1);\n        order.clear();\n\
    \        vector<int> st{root};\n        while (!st.empty()) {\n            int\
    \ v = st.back();\n            st.pop_back();\n            order.push_back(v);\n\
    \            for (int u : adjacents[v]) {\n                if (u == parent[v])\
    \ continue;\n                parent[u] = v;\n                st.push_back(u);\n\
    \            }\n        }\n        for (int oi = (int)order.size() - 1; oi >=\
    \ 1; oi--) {\n            int v = order[oi], pv = parent[v];\n            T result\
    \ = identity;\n            int parentIndex = -1;\n            for (int i = 0;\
    \ i < (int)adjacents[v].size(); i++) {\n                int u = adjacents[v][i];\n\
    \                if (u == pv) {\n                    parentIndex = i;\n      \
    \              continue;\n                }\n                result = merge(result,\
    \ childSubTreeValue[v][i]);\n            }\n            childSubTreeValue[pv][indexForAdjacents[v][parentIndex]]\
    \ = calc_node_value(result, v);\n        }\n    }\n\n    void dfs2() {\n     \
    \   for (int v : order) {\n            T accFromLeft = identity;\n           \
    \ vector<T> accFromRight(adjacents[v].size(), identity);\n            for (int\
    \ i = (int)adjacents[v].size() - 2; i >= 0; i--) {\n                accFromRight[i]\
    \ = merge(childSubTreeValue[v][i + 1], accFromRight[i + 1]);\n            }\n\
    \            for (int j = 0; j < (int)adjacents[v].size(); j++) {\n          \
    \      int u = adjacents[v][j];\n                T result = calc_node_value(merge(accFromLeft,\
    \ accFromRight[j]), v);\n                childSubTreeValue[u][indexForAdjacents[v][j]]\
    \ = result;\n                accFromLeft = merge(accFromLeft, childSubTreeValue[v][j]);\n\
    \            }\n            ans[v] = calc_ans(accFromLeft, v);\n        }\n  \
    \  }\n\n    vector<T> run(int root = 1) {\n        dfs1(root);\n        dfs2();\n\
    \        return ans;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/Rerooting.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/Rerooting.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/Rerooting.cpp
- /library/algorithm_library/cpp-from-py/graph/Rerooting.cpp.html
title: algorithm_library/cpp-from-py/graph/Rerooting.cpp
---
