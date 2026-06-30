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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/SCC.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct SCC {\n    int N;\n    vector<pair<int,\
    \ int>> graphEdges;\n\n    SCC(int N_) : N(N_) {}\n\n    void addEdge(int frm,\
    \ int to) {\n        assert(0 <= frm && frm <= N);\n        assert(0 <= to &&\
    \ to <= N);\n        graphEdges.emplace_back(frm, to);\n    }\n\n    pair<vector<int>,\
    \ vector<int>> toCSR(int N, const vector<pair<int, int>>& edges) const {\n   \
    \     vector<int> start(N + 1), endList(edges.size());\n        for (auto [u,\
    \ v] : edges) start[u + 1]++;\n        for (int i = 1; i <= N; i++) start[i] +=\
    \ start[i - 1];\n        vector<int> pointer = start;\n        for (auto [u, v]\
    \ : edges) endList[pointer[u]++] = v;\n        return {start, endList};\n    }\n\
    \n    pair<int, vector<int>> decomposeToSCC() const {\n        auto [start, endList]\
    \ = toCSR(N, graphEdges);\n        int nowOrder = 0, groupNum = 0;\n        vector<int>\
    \ lowlink(N), order(N, -1), groupId(N), pendingStack;\n        function<void(int)>\
    \ dfs = [&](int v) {\n            lowlink[v] = order[v] = nowOrder++;\n      \
    \      pendingStack.push_back(v);\n            for (int i = start[v]; i < start[v\
    \ + 1]; i++) {\n                int to = endList[i];\n                if (order[to]\
    \ == -1) {\n                    dfs(to);\n                    lowlink[v] = min(lowlink[v],\
    \ lowlink[to]);\n                } else {\n                    lowlink[v] = min(lowlink[v],\
    \ order[to]);\n                }\n            }\n            if (lowlink[v] ==\
    \ order[v]) {\n                while (true) {\n                    int u = pendingStack.back();\n\
    \                    pendingStack.pop_back();\n                    order[u] =\
    \ N;\n                    groupId[u] = groupNum;\n                    if (u ==\
    \ v) break;\n                }\n                groupNum++;\n            }\n \
    \       };\n        for (int v = 0; v < N; v++) if (order[v] == -1) dfs(v);\n\
    \        for (int v = 0; v < N; v++) groupId[v] = groupNum - 1 - groupId[v];\n\
    \        return {groupNum, groupId};\n    }\n\n    vector<vector<int>> build_scc()\
    \ const {\n        auto [groupNum, groupId] = decomposeToSCC();\n        vector<vector<int>>\
    \ groups(groupNum);\n        for (int v = 0; v < N; v++) groups[groupId[v]].push_back(v);\n\
    \        return groups;\n    }\n\n    vector<vector<int>> build_dag() const {\n\
    \        auto [groupNum, groupId] = decomposeToSCC();\n        vector<vector<int>>\
    \ dag(groupNum);\n        for (auto [u, v] : graphEdges) {\n            if (groupId[u]\
    \ != groupId[v]) dag[groupId[u]].push_back(groupId[v]);\n        }\n        return\
    \ dag;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct SCC {\n    int N;\n\
    \    vector<pair<int, int>> graphEdges;\n\n    SCC(int N_) : N(N_) {}\n\n    void\
    \ addEdge(int frm, int to) {\n        assert(0 <= frm && frm <= N);\n        assert(0\
    \ <= to && to <= N);\n        graphEdges.emplace_back(frm, to);\n    }\n\n   \
    \ pair<vector<int>, vector<int>> toCSR(int N, const vector<pair<int, int>>& edges)\
    \ const {\n        vector<int> start(N + 1), endList(edges.size());\n        for\
    \ (auto [u, v] : edges) start[u + 1]++;\n        for (int i = 1; i <= N; i++)\
    \ start[i] += start[i - 1];\n        vector<int> pointer = start;\n        for\
    \ (auto [u, v] : edges) endList[pointer[u]++] = v;\n        return {start, endList};\n\
    \    }\n\n    pair<int, vector<int>> decomposeToSCC() const {\n        auto [start,\
    \ endList] = toCSR(N, graphEdges);\n        int nowOrder = 0, groupNum = 0;\n\
    \        vector<int> lowlink(N), order(N, -1), groupId(N), pendingStack;\n   \
    \     function<void(int)> dfs = [&](int v) {\n            lowlink[v] = order[v]\
    \ = nowOrder++;\n            pendingStack.push_back(v);\n            for (int\
    \ i = start[v]; i < start[v + 1]; i++) {\n                int to = endList[i];\n\
    \                if (order[to] == -1) {\n                    dfs(to);\n      \
    \              lowlink[v] = min(lowlink[v], lowlink[to]);\n                } else\
    \ {\n                    lowlink[v] = min(lowlink[v], order[to]);\n          \
    \      }\n            }\n            if (lowlink[v] == order[v]) {\n         \
    \       while (true) {\n                    int u = pendingStack.back();\n   \
    \                 pendingStack.pop_back();\n                    order[u] = N;\n\
    \                    groupId[u] = groupNum;\n                    if (u == v) break;\n\
    \                }\n                groupNum++;\n            }\n        };\n \
    \       for (int v = 0; v < N; v++) if (order[v] == -1) dfs(v);\n        for (int\
    \ v = 0; v < N; v++) groupId[v] = groupNum - 1 - groupId[v];\n        return {groupNum,\
    \ groupId};\n    }\n\n    vector<vector<int>> build_scc() const {\n        auto\
    \ [groupNum, groupId] = decomposeToSCC();\n        vector<vector<int>> groups(groupNum);\n\
    \        for (int v = 0; v < N; v++) groups[groupId[v]].push_back(v);\n      \
    \  return groups;\n    }\n\n    vector<vector<int>> build_dag() const {\n    \
    \    auto [groupNum, groupId] = decomposeToSCC();\n        vector<vector<int>>\
    \ dag(groupNum);\n        for (auto [u, v] : graphEdges) {\n            if (groupId[u]\
    \ != groupId[v]) dag[groupId[u]].push_back(groupId[v]);\n        }\n        return\
    \ dag;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/SCC.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/SCC.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/SCC.cpp
- /library/algorithm_library/cpp-from-py/graph/SCC.cpp.html
title: algorithm_library/cpp-from-py/graph/SCC.cpp
---
