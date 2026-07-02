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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nstruct PotentialUnionFind\
    \ {\n    int N;\n    vector<int> parents;\n    vector<long long> potential;\n\
    \    vector<bool> inconsistent;\n    const long long inf = (long long)1e18;\n\n\
    \    PotentialUnionFind(int N_) : N(N_), parents(N + 1, -1), potential(N + 1,\
    \ 0), inconsistent(N + 1, false) {}\n\n    int root(int x) {\n        if (parents[x]\
    \ < 0) return x;\n        int p = parents[x];\n        int r = root(p);\n    \
    \    potential[x] += potential[p];\n        parents[x] = r;\n        return r;\n\
    \    }\n\n    long long dist(int x, int y) {\n        int rx = root(x), ry = root(y);\n\
    \        if (rx == ry) return potential[y] - potential[x];\n        return inf;\n\
    \    }\n\n    bool union_(int x, int y, long long w) {\n        int rx = root(x),\
    \ ry = root(y);\n        if (rx == ry) {\n            if (potential[y] - potential[x]\
    \ != w) inconsistent[rx] = true;\n            return potential[y] - potential[x]\
    \ == w;\n        }\n        if (parents[ry] > parents[rx]) {\n            parents[rx]\
    \ += parents[ry];\n            potential[ry] = potential[x] + w - potential[y];\n\
    \            parents[ry] = rx;\n        } else {\n            parents[ry] += parents[rx];\n\
    \            potential[rx] = potential[y] - w - potential[x];\n            parents[rx]\
    \ = ry;\n        }\n        return true;\n    }\n\n    int size(int x) { return\
    \ -parents[root(x)]; }\n    bool isSame(int x, int y) { return root(x) == root(y);\
    \ }\n    vector<int> members(int x) {\n        int r = root(x);\n        vector<int>\
    \ res;\n        for (int i = 1; i <= N; i++) if (root(i) == r) res.push_back(i);\n\
    \        return res;\n    }\n    vector<int> roots() {\n        vector<int> res;\n\
    \        for (int i = 1; i <= N; i++) if (parents[i] < 0) res.push_back(i);\n\
    \        return res;\n    }\n    int group_count() { return (int)roots().size();\
    \ }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct PotentialUnionFind\
    \ {\n    int N;\n    vector<int> parents;\n    vector<long long> potential;\n\
    \    vector<bool> inconsistent;\n    const long long inf = (long long)1e18;\n\n\
    \    PotentialUnionFind(int N_) : N(N_), parents(N + 1, -1), potential(N + 1,\
    \ 0), inconsistent(N + 1, false) {}\n\n    int root(int x) {\n        if (parents[x]\
    \ < 0) return x;\n        int p = parents[x];\n        int r = root(p);\n    \
    \    potential[x] += potential[p];\n        parents[x] = r;\n        return r;\n\
    \    }\n\n    long long dist(int x, int y) {\n        int rx = root(x), ry = root(y);\n\
    \        if (rx == ry) return potential[y] - potential[x];\n        return inf;\n\
    \    }\n\n    bool union_(int x, int y, long long w) {\n        int rx = root(x),\
    \ ry = root(y);\n        if (rx == ry) {\n            if (potential[y] - potential[x]\
    \ != w) inconsistent[rx] = true;\n            return potential[y] - potential[x]\
    \ == w;\n        }\n        if (parents[ry] > parents[rx]) {\n            parents[rx]\
    \ += parents[ry];\n            potential[ry] = potential[x] + w - potential[y];\n\
    \            parents[ry] = rx;\n        } else {\n            parents[ry] += parents[rx];\n\
    \            potential[rx] = potential[y] - w - potential[x];\n            parents[rx]\
    \ = ry;\n        }\n        return true;\n    }\n\n    int size(int x) { return\
    \ -parents[root(x)]; }\n    bool isSame(int x, int y) { return root(x) == root(y);\
    \ }\n    vector<int> members(int x) {\n        int r = root(x);\n        vector<int>\
    \ res;\n        for (int i = 1; i <= N; i++) if (root(i) == r) res.push_back(i);\n\
    \        return res;\n    }\n    vector<int> roots() {\n        vector<int> res;\n\
    \        for (int i = 1; i <= N; i++) if (parents[i] < 0) res.push_back(i);\n\
    \        return res;\n    }\n    int group_count() { return (int)roots().size();\
    \ }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp
- /library/algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp.html
title: algorithm_library/cpp-from-py/graph/PotentialUnionFind.cpp
---
