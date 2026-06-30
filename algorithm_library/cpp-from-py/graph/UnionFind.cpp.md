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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/UnionFind.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct UnionFind {\n    int n;\n  \
    \  vector<int> parents;\n\n    UnionFind(int n_) : n(n_), parents(n, -1) {}\n\n\
    \    int root(int x) {\n        if (parents[x] < 0) return x;\n        return\
    \ parents[x] = root(parents[x]);\n    }\n\n    int union_(int x, int y) {\n  \
    \      x = root(x);\n        y = root(y);\n        if (x == y) return x;\n   \
    \     if (parents[x] > parents[y]) swap(x, y);\n        parents[x] += parents[y];\n\
    \        parents[y] = x;\n        return x;\n    }\n\n    int size(int x) { return\
    \ -parents[root(x)]; }\n    bool isSame(int x, int y) { return root(x) == root(y);\
    \ }\n    vector<int> members(int x) {\n        int r = root(x);\n        vector<int>\
    \ res;\n        for (int i = 0; i < n; i++) if (root(i) == r) res.push_back(i);\n\
    \        return res;\n    }\n    vector<int> roots() const {\n        vector<int>\
    \ res;\n        for (int i = 0; i < n; i++) if (parents[i] < 0) res.push_back(i);\n\
    \        return res;\n    }\n    int group_count() const { return (int)roots().size();\
    \ }\n    vector<vector<int>> all_group_members() {\n        unordered_map<int,\
    \ vector<int>> mp;\n        for (int i = 0; i < n; i++) mp[root(i)].push_back(i);\n\
    \        vector<vector<int>> res;\n        for (auto& [_, v] : mp) res.push_back(v);\n\
    \        return res;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct UnionFind {\n  \
    \  int n;\n    vector<int> parents;\n\n    UnionFind(int n_) : n(n_), parents(n,\
    \ -1) {}\n\n    int root(int x) {\n        if (parents[x] < 0) return x;\n   \
    \     return parents[x] = root(parents[x]);\n    }\n\n    int union_(int x, int\
    \ y) {\n        x = root(x);\n        y = root(y);\n        if (x == y) return\
    \ x;\n        if (parents[x] > parents[y]) swap(x, y);\n        parents[x] +=\
    \ parents[y];\n        parents[y] = x;\n        return x;\n    }\n\n    int size(int\
    \ x) { return -parents[root(x)]; }\n    bool isSame(int x, int y) { return root(x)\
    \ == root(y); }\n    vector<int> members(int x) {\n        int r = root(x);\n\
    \        vector<int> res;\n        for (int i = 0; i < n; i++) if (root(i) ==\
    \ r) res.push_back(i);\n        return res;\n    }\n    vector<int> roots() const\
    \ {\n        vector<int> res;\n        for (int i = 0; i < n; i++) if (parents[i]\
    \ < 0) res.push_back(i);\n        return res;\n    }\n    int group_count() const\
    \ { return (int)roots().size(); }\n    vector<vector<int>> all_group_members()\
    \ {\n        unordered_map<int, vector<int>> mp;\n        for (int i = 0; i <\
    \ n; i++) mp[root(i)].push_back(i);\n        vector<vector<int>> res;\n      \
    \  for (auto& [_, v] : mp) res.push_back(v);\n        return res;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/UnionFind.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/UnionFind.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/UnionFind.cpp
- /library/algorithm_library/cpp-from-py/graph/UnionFind.cpp.html
title: algorithm_library/cpp-from-py/graph/UnionFind.cpp
---
