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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/hash/ZobristHash.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct ZobristHash\
    \ {\n    static constexpr unsigned long long MAXV = (1ULL << 61) - 1;\n    unordered_map<T,\
    \ unsigned long long> hash_value;\n    vector<unsigned long long> hashA, hashB;\n\
    \    mt19937_64 rng;\n\n    ZobristHash(const vector<T>& A, const vector<T>& B)\
    \ : rng(chrono::steady_clock::now().time_since_epoch().count()) {\n        for\
    \ (const auto& a : A) hash_value[a] = randint();\n        for (const auto& b :\
    \ B) hash_value[b] = randint();\n        hashA = {0};\n        hashB = {0};\n\
    \        unordered_set<T> setA, setB;\n        for (const auto& a : A) {\n   \
    \         if (setA.count(a)) hashA.push_back(hashA.back());\n            else\
    \ {\n                hashA.push_back(hashA.back() ^ hash_value[a]);\n        \
    \        setA.insert(a);\n            }\n        }\n        for (const auto& b\
    \ : B) {\n            if (setB.count(b)) hashB.push_back(hashB.back());\n    \
    \        else {\n                hashB.push_back(hashB.back() ^ hash_value[b]);\n\
    \                setB.insert(b);\n            }\n        }\n    }\n\n    unsigned\
    \ long long randint() {\n        return uniform_int_distribution<unsigned long\
    \ long>(1, MAXV)(rng);\n    }\n\n    bool isEqual(int al, int ar, int bl, int\
    \ br) const {\n        return (hashA[ar] ^ hashA[al - 1]) == (hashB[br] ^ hashB[bl\
    \ - 1]);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ ZobristHash {\n    static constexpr unsigned long long MAXV = (1ULL << 61) -\
    \ 1;\n    unordered_map<T, unsigned long long> hash_value;\n    vector<unsigned\
    \ long long> hashA, hashB;\n    mt19937_64 rng;\n\n    ZobristHash(const vector<T>&\
    \ A, const vector<T>& B) : rng(chrono::steady_clock::now().time_since_epoch().count())\
    \ {\n        for (const auto& a : A) hash_value[a] = randint();\n        for (const\
    \ auto& b : B) hash_value[b] = randint();\n        hashA = {0};\n        hashB\
    \ = {0};\n        unordered_set<T> setA, setB;\n        for (const auto& a : A)\
    \ {\n            if (setA.count(a)) hashA.push_back(hashA.back());\n         \
    \   else {\n                hashA.push_back(hashA.back() ^ hash_value[a]);\n \
    \               setA.insert(a);\n            }\n        }\n        for (const\
    \ auto& b : B) {\n            if (setB.count(b)) hashB.push_back(hashB.back());\n\
    \            else {\n                hashB.push_back(hashB.back() ^ hash_value[b]);\n\
    \                setB.insert(b);\n            }\n        }\n    }\n\n    unsigned\
    \ long long randint() {\n        return uniform_int_distribution<unsigned long\
    \ long>(1, MAXV)(rng);\n    }\n\n    bool isEqual(int al, int ar, int bl, int\
    \ br) const {\n        return (hashA[ar] ^ hashA[al - 1]) == (hashB[br] ^ hashB[bl\
    \ - 1]);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/hash/ZobristHash.cpp
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/hash/ZobristHash.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/hash/ZobristHash.cpp
- /library/algorithm_library/cpp-from-py/hash/ZobristHash.cpp.html
title: algorithm_library/cpp-from-py/hash/ZobristHash.cpp
---
