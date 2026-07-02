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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/CSR.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\npair<vector<int>, vector<int>> csr(int\
    \ N, const vector<pair<int, int>>& graphEdges) {\n    vector<int> start(N + 1,\
    \ 0), endList(graphEdges.size());\n    for (auto [u, v] : graphEdges) start[u\
    \ + 1]++;\n    for (int i = 1; i <= N; i++) start[i] += start[i - 1];\n    vector<int>\
    \ pointer = start;\n    for (auto [u, v] : graphEdges) endList[pointer[u]++] =\
    \ v;\n    return {start, endList};\n}\n\ntemplate <class Cost = long long>\nstruct\
    \ Graph {\n    int N, M;\n    vector<int> start;\n    vector<tuple<int, int, optional<Cost>>>\
    \ buf;\n    vector<pair<int, optional<Cost>>> endList;\n\n    Graph(int n, int\
    \ m) : N(n + 1), M(m), start(N + 1, 0), endList(m) {}\n\n    void add_edge(int\
    \ u, int v, optional<Cost> cost = nullopt) {\n        buf.emplace_back(u, v, cost);\n\
    \        start[u]++;\n        if ((int)buf.size() == M) build();\n    }\n\n  \
    \  void build() {\n        partial_sum(start.begin(), start.end(), start.begin());\n\
    \        for (auto [u, v, c] : buf) {\n            start[u]--;\n            endList[start[u]]\
    \ = {v, c};\n        }\n    }\n\n    vector<pair<int, optional<Cost>>> get_edges(int\
    \ u) const {\n        return vector<pair<int, optional<Cost>>>(endList.begin()\
    \ + start[u], endList.begin() + start[u + 1]);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\npair<vector<int>, vector<int>>\
    \ csr(int N, const vector<pair<int, int>>& graphEdges) {\n    vector<int> start(N\
    \ + 1, 0), endList(graphEdges.size());\n    for (auto [u, v] : graphEdges) start[u\
    \ + 1]++;\n    for (int i = 1; i <= N; i++) start[i] += start[i - 1];\n    vector<int>\
    \ pointer = start;\n    for (auto [u, v] : graphEdges) endList[pointer[u]++] =\
    \ v;\n    return {start, endList};\n}\n\ntemplate <class Cost = long long>\nstruct\
    \ Graph {\n    int N, M;\n    vector<int> start;\n    vector<tuple<int, int, optional<Cost>>>\
    \ buf;\n    vector<pair<int, optional<Cost>>> endList;\n\n    Graph(int n, int\
    \ m) : N(n + 1), M(m), start(N + 1, 0), endList(m) {}\n\n    void add_edge(int\
    \ u, int v, optional<Cost> cost = nullopt) {\n        buf.emplace_back(u, v, cost);\n\
    \        start[u]++;\n        if ((int)buf.size() == M) build();\n    }\n\n  \
    \  void build() {\n        partial_sum(start.begin(), start.end(), start.begin());\n\
    \        for (auto [u, v, c] : buf) {\n            start[u]--;\n            endList[start[u]]\
    \ = {v, c};\n        }\n    }\n\n    vector<pair<int, optional<Cost>>> get_edges(int\
    \ u) const {\n        return vector<pair<int, optional<Cost>>>(endList.begin()\
    \ + start[u], endList.begin() + start[u + 1]);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/CSR.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/CSR.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/CSR.cpp
- /library/algorithm_library/cpp-from-py/graph/CSR.cpp.html
title: algorithm_library/cpp-from-py/graph/CSR.cpp
---
