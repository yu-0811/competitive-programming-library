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
  bundledCode: "#line 1 \"algorithm_library/cpp/itertools.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\n// combinations: n \u500B\u304B\u3089 r \u500B\u9078\u3076\
    \ntemplate <class T>\nvector<vector<T>> combinations(const vector<T>& a, int r)\
    \ {\n    int n = (int)a.size();\n    vector<vector<T>> res;\n\n    if (r < 0 ||\
    \ r > n) return res;\n\n    vector<T> cur;\n\n    auto dfs = [&](auto&& dfs, int\
    \ start) -> void {\n        if ((int)cur.size() == r) {\n            res.push_back(cur);\n\
    \            return;\n        }\n\n        int need = r - (int)cur.size();\n\n\
    \        for (int i = start; i <= n - need; i++) {\n            cur.push_back(a[i]);\n\
    \            dfs(dfs, i + 1);\n            cur.pop_back();\n        }\n    };\n\
    \n    dfs(dfs, 0);\n    return res;\n}\n\n// permutations: \u9577\u3055 r \u306E\
    \u9806\u5217\ntemplate <class T>\nvector<vector<T>> permutations(const vector<T>&\
    \ a, int r = -1) {\n    int n = (int)a.size();\n    if (r == -1) r = n;\n\n  \
    \  vector<vector<T>> res;\n    if (r < 0 || r > n) return res;\n\n    vector<T>\
    \ cur;\n    vector<int> used(n, 0);\n\n    auto dfs = [&](auto&& dfs) -> void\
    \ {\n        if ((int)cur.size() == r) {\n            res.push_back(cur);\n  \
    \          return;\n        }\n\n        for (int i = 0; i < n; i++) {\n     \
    \       if (used[i]) continue;\n\n            used[i] = 1;\n            cur.push_back(a[i]);\n\
    \n            dfs(dfs);\n\n            cur.pop_back();\n            used[i] =\
    \ 0;\n        }\n    };\n\n    dfs(dfs);\n    return res;\n}\n\n\n// product(a,\
    \ repeat): Python \u306E itertools.product(a, repeat=k)\ntemplate <class T>\n\
    vector<vector<T>> product(const vector<T>& a, int repeat) {\n    vector<vector<T>>\
    \ pools(repeat, a);\n    return product(pools);\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\n// combinations: n \u500B\
    \u304B\u3089 r \u500B\u9078\u3076\ntemplate <class T>\nvector<vector<T>> combinations(const\
    \ vector<T>& a, int r) {\n    int n = (int)a.size();\n    vector<vector<T>> res;\n\
    \n    if (r < 0 || r > n) return res;\n\n    vector<T> cur;\n\n    auto dfs =\
    \ [&](auto&& dfs, int start) -> void {\n        if ((int)cur.size() == r) {\n\
    \            res.push_back(cur);\n            return;\n        }\n\n        int\
    \ need = r - (int)cur.size();\n\n        for (int i = start; i <= n - need; i++)\
    \ {\n            cur.push_back(a[i]);\n            dfs(dfs, i + 1);\n        \
    \    cur.pop_back();\n        }\n    };\n\n    dfs(dfs, 0);\n    return res;\n\
    }\n\n// permutations: \u9577\u3055 r \u306E\u9806\u5217\ntemplate <class T>\n\
    vector<vector<T>> permutations(const vector<T>& a, int r = -1) {\n    int n =\
    \ (int)a.size();\n    if (r == -1) r = n;\n\n    vector<vector<T>> res;\n    if\
    \ (r < 0 || r > n) return res;\n\n    vector<T> cur;\n    vector<int> used(n,\
    \ 0);\n\n    auto dfs = [&](auto&& dfs) -> void {\n        if ((int)cur.size()\
    \ == r) {\n            res.push_back(cur);\n            return;\n        }\n\n\
    \        for (int i = 0; i < n; i++) {\n            if (used[i]) continue;\n\n\
    \            used[i] = 1;\n            cur.push_back(a[i]);\n\n            dfs(dfs);\n\
    \n            cur.pop_back();\n            used[i] = 0;\n        }\n    };\n\n\
    \    dfs(dfs);\n    return res;\n}\n\n\n// product(a, repeat): Python \u306E itertools.product(a,\
    \ repeat=k)\ntemplate <class T>\nvector<vector<T>> product(const vector<T>& a,\
    \ int repeat) {\n    vector<vector<T>> pools(repeat, a);\n    return product(pools);\n\
    }"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/itertools.cpp
  requiredBy: []
  timestamp: '2026-05-21 22:08:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/itertools.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/itertools.cpp
- /library/algorithm_library/cpp/itertools.cpp.html
title: algorithm_library/cpp/itertools.cpp
---
