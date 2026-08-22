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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nstruct TwoWayList {\n    static\
    \ constexpr long long HEAD = -1;\n    static constexpr long long TAIL = (long\
    \ long)1e18;\n    unordered_map<long long, long long> front, back;\n\n    TwoWayList(const\
    \ vector<long long>& L) {\n        vector<long long> v;\n        v.push_back(HEAD);\n\
    \        v.insert(v.end(), L.begin(), L.end());\n        v.push_back(TAIL);\n\
    \        for (int i = 0; i + 1 < (int)v.size(); i++) {\n            back[v[i]]\
    \ = v[i + 1];\n            front[v[i + 1]] = v[i];\n        }\n    }\n\n    void\
    \ insert_front(long long x, long long y) {\n        long long a = front[x];\n\
    \        back[a] = y;\n        front[x] = y;\n        back[y] = x;\n        front[y]\
    \ = a;\n    }\n\n    void insert_back(long long x, long long y) {\n        long\
    \ long b = back[x];\n        back[x] = y;\n        front[y] = x;\n        back[y]\
    \ = b;\n        front[b] = y;\n    }\n\n    void del_x(long long x) {\n      \
    \  long long a = front[x], b = back[x];\n        back[a] = b;\n        front[b]\
    \ = a;\n        front.erase(x);\n        back.erase(x);\n    }\n\n    vector<long\
    \ long> res_LIST() const {\n        vector<long long> ans;\n        long long\
    \ cur = back.at(HEAD);\n        while (cur != TAIL) {\n            ans.push_back(cur);\n\
    \            cur = back.at(cur);\n        }\n        return ans;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct TwoWayList {\n \
    \   static constexpr long long HEAD = -1;\n    static constexpr long long TAIL\
    \ = (long long)1e18;\n    unordered_map<long long, long long> front, back;\n\n\
    \    TwoWayList(const vector<long long>& L) {\n        vector<long long> v;\n\
    \        v.push_back(HEAD);\n        v.insert(v.end(), L.begin(), L.end());\n\
    \        v.push_back(TAIL);\n        for (int i = 0; i + 1 < (int)v.size(); i++)\
    \ {\n            back[v[i]] = v[i + 1];\n            front[v[i + 1]] = v[i];\n\
    \        }\n    }\n\n    void insert_front(long long x, long long y) {\n     \
    \   long long a = front[x];\n        back[a] = y;\n        front[x] = y;\n   \
    \     back[y] = x;\n        front[y] = a;\n    }\n\n    void insert_back(long\
    \ long x, long long y) {\n        long long b = back[x];\n        back[x] = y;\n\
    \        front[y] = x;\n        back[y] = b;\n        front[b] = y;\n    }\n\n\
    \    void del_x(long long x) {\n        long long a = front[x], b = back[x];\n\
    \        back[a] = b;\n        front[b] = a;\n        front.erase(x);\n      \
    \  back.erase(x);\n    }\n\n    vector<long long> res_LIST() const {\n       \
    \ vector<long long> ans;\n        long long cur = back.at(HEAD);\n        while\
    \ (cur != TAIL) {\n            ans.push_back(cur);\n            cur = back.at(cur);\n\
    \        }\n        return ans;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp
- /library/algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp.html
title: algorithm_library/cpp-from-py/data-structure/TwoWayList.cpp
---
