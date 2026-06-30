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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/hash/MultisetHash.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct MultisetHash\
    \ {\n    static constexpr unsigned long long mod = (1ULL << 61) - 1;\n    unordered_map<T,\
    \ unsigned long long> hash_value;\n    vector<unsigned long long> hashA, hashB;\n\
    \    mt19937_64 rng;\n\n    MultisetHash(const vector<T>& A, const vector<T>&\
    \ B) : rng(chrono::steady_clock::now().time_since_epoch().count()) {\n       \
    \ for (const auto& a : A) hash_value[a] = randint();\n        for (const auto&\
    \ b : B) hash_value[b] = randint();\n        hashA = {0};\n        hashB = {0};\n\
    \        for (const auto& a : A) hashA.push_back((hashA.back() + hash_value[a])\
    \ % mod);\n        for (const auto& b : B) hashB.push_back((hashB.back() + hash_value[b])\
    \ % mod);\n    }\n\n    unsigned long long randint() {\n        return uniform_int_distribution<unsigned\
    \ long long>(1, mod - 1)(rng);\n    }\n\n    bool isEqual(int al, int ar, int\
    \ bl, int br) const {\n        return (hashA[ar] + mod - hashA[al - 1]) % mod\
    \ == (hashB[br] + mod - hashB[bl - 1]) % mod;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class T>\nstruct\
    \ MultisetHash {\n    static constexpr unsigned long long mod = (1ULL << 61) -\
    \ 1;\n    unordered_map<T, unsigned long long> hash_value;\n    vector<unsigned\
    \ long long> hashA, hashB;\n    mt19937_64 rng;\n\n    MultisetHash(const vector<T>&\
    \ A, const vector<T>& B) : rng(chrono::steady_clock::now().time_since_epoch().count())\
    \ {\n        for (const auto& a : A) hash_value[a] = randint();\n        for (const\
    \ auto& b : B) hash_value[b] = randint();\n        hashA = {0};\n        hashB\
    \ = {0};\n        for (const auto& a : A) hashA.push_back((hashA.back() + hash_value[a])\
    \ % mod);\n        for (const auto& b : B) hashB.push_back((hashB.back() + hash_value[b])\
    \ % mod);\n    }\n\n    unsigned long long randint() {\n        return uniform_int_distribution<unsigned\
    \ long long>(1, mod - 1)(rng);\n    }\n\n    bool isEqual(int al, int ar, int\
    \ bl, int br) const {\n        return (hashA[ar] + mod - hashA[al - 1]) % mod\
    \ == (hashB[br] + mod - hashB[bl - 1]) % mod;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/hash/MultisetHash.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/hash/MultisetHash.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/hash/MultisetHash.cpp
- /library/algorithm_library/cpp-from-py/hash/MultisetHash.cpp.html
title: algorithm_library/cpp-from-py/hash/MultisetHash.cpp
---
