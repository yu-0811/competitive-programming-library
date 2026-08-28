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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/cycle_detect.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> cycle_detect(int\
    \ start, const vector<vector<int>>& G) {\n    int N = (int)G.size() - 1;\n   \
    \ vector<bool> vis(N + 1, false), fin(N + 1, false);\n    vector<int> history;\n\
    \    stack<pair<int, int>> sta;\n    sta.emplace(start, 0);\n    int cycle_start\
    \ = -1;\n    while (!sta.empty() && cycle_start == -1) {\n        auto [v, prev]\
    \ = sta.top();\n        sta.pop();\n        if (prev == -1) {\n            if\
    \ (!history.empty()) history.pop_back();\n            fin[v] = true;\n       \
    \     continue;\n        }\n        if (vis[v]) continue;\n        vis[v] = true;\n\
    \        history.push_back(v);\n        for (int v2 : G[v]) {\n            if\
    \ (v2 == prev || fin[v2]) continue;\n            if (vis[v2]) {\n            \
    \    cycle_start = v2;\n                break;\n            }\n            sta.emplace(v2,\
    \ -1);\n            sta.emplace(v2, v);\n        }\n    }\n    vector<int> cycle;\n\
    \    if (cycle_start == -1) return cycle;\n    while (!history.empty()) {\n  \
    \      int v = history.back();\n        history.pop_back();\n        cycle.push_back(v);\n\
    \        if (v == cycle_start) break;\n    }\n    return cycle;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> cycle_detect(int\
    \ start, const vector<vector<int>>& G) {\n    int N = (int)G.size() - 1;\n   \
    \ vector<bool> vis(N + 1, false), fin(N + 1, false);\n    vector<int> history;\n\
    \    stack<pair<int, int>> sta;\n    sta.emplace(start, 0);\n    int cycle_start\
    \ = -1;\n    while (!sta.empty() && cycle_start == -1) {\n        auto [v, prev]\
    \ = sta.top();\n        sta.pop();\n        if (prev == -1) {\n            if\
    \ (!history.empty()) history.pop_back();\n            fin[v] = true;\n       \
    \     continue;\n        }\n        if (vis[v]) continue;\n        vis[v] = true;\n\
    \        history.push_back(v);\n        for (int v2 : G[v]) {\n            if\
    \ (v2 == prev || fin[v2]) continue;\n            if (vis[v2]) {\n            \
    \    cycle_start = v2;\n                break;\n            }\n            sta.emplace(v2,\
    \ -1);\n            sta.emplace(v2, v);\n        }\n    }\n    vector<int> cycle;\n\
    \    if (cycle_start == -1) return cycle;\n    while (!history.empty()) {\n  \
    \      int v = history.back();\n        history.pop_back();\n        cycle.push_back(v);\n\
    \        if (v == cycle_start) break;\n    }\n    return cycle;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/cycle_detect.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/cycle_detect.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/cycle_detect.cpp
- /library/algorithm_library/cpp-from-py/graph/cycle_detect.cpp.html
title: algorithm_library/cpp-from-py/graph/cycle_detect.cpp
---
