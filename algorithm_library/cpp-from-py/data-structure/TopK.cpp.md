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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/data-structure/TopK.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nstruct SumTopK {\n    int N,\
    \ K;\n    vector<long long> A;\n    multiset<long long> ok, ng;\n    long long\
    \ ans = 0;\n\n    SumTopK(int N_, vector<long long> A_, int K_) : N(N_), K(K_),\
    \ A(move(A_)) {\n        for (int i = 0; i < K; i++) ok.insert(0);\n        for\
    \ (int i = 0; i < N - K; i++) ng.insert(0);\n    }\n\n    void add(long long y)\
    \ {\n        ok.insert(y);\n        ans += y;\n        long long yy = *ok.begin();\n\
    \        ans -= yy;\n        ok.erase(ok.begin());\n        ng.insert(yy);\n \
    \   }\n\n    void DEL(long long y) {\n        if (K > 0 && !ok.empty() && y >=\
    \ *ok.begin()) {\n            auto it = ok.find(y);\n            if (it != ok.end())\
    \ {\n                ok.erase(it);\n                ans -= y;\n              \
    \  if (!ng.empty()) {\n                    auto jt = prev(ng.end());\n       \
    \             long long yy = *jt;\n                    ng.erase(jt);\n       \
    \             ok.insert(yy);\n                    ans += yy;\n               \
    \ }\n            }\n        } else {\n            auto it = ng.find(y);\n    \
    \        if (it != ng.end()) ng.erase(it);\n        }\n    }\n\n    long long\
    \ update(int x, long long y) {\n        add(y);\n        DEL(A[x]);\n        A[x]\
    \ = y;\n        return ans;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct SumTopK {\n    int\
    \ N, K;\n    vector<long long> A;\n    multiset<long long> ok, ng;\n    long long\
    \ ans = 0;\n\n    SumTopK(int N_, vector<long long> A_, int K_) : N(N_), K(K_),\
    \ A(move(A_)) {\n        for (int i = 0; i < K; i++) ok.insert(0);\n        for\
    \ (int i = 0; i < N - K; i++) ng.insert(0);\n    }\n\n    void add(long long y)\
    \ {\n        ok.insert(y);\n        ans += y;\n        long long yy = *ok.begin();\n\
    \        ans -= yy;\n        ok.erase(ok.begin());\n        ng.insert(yy);\n \
    \   }\n\n    void DEL(long long y) {\n        if (K > 0 && !ok.empty() && y >=\
    \ *ok.begin()) {\n            auto it = ok.find(y);\n            if (it != ok.end())\
    \ {\n                ok.erase(it);\n                ans -= y;\n              \
    \  if (!ng.empty()) {\n                    auto jt = prev(ng.end());\n       \
    \             long long yy = *jt;\n                    ng.erase(jt);\n       \
    \             ok.insert(yy);\n                    ans += yy;\n               \
    \ }\n            }\n        } else {\n            auto it = ng.find(y);\n    \
    \        if (it != ng.end()) ng.erase(it);\n        }\n    }\n\n    long long\
    \ update(int x, long long y) {\n        add(y);\n        DEL(A[x]);\n        A[x]\
    \ = y;\n        return ans;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/data-structure/TopK.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/data-structure/TopK.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/data-structure/TopK.cpp
- /library/algorithm_library/cpp-from-py/data-structure/TopK.cpp.html
title: algorithm_library/cpp-from-py/data-structure/TopK.cpp
---
