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
  bundledCode: "#line 1 \"algo_library/cpp/RollingHash.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nclass RollingHash {\nprivate:\n    long long base;\n \
    \   vector<unsigned long long> hash, base_pow;\n    const unsigned long long MASK30\
    \ = (1UL << 30) - 1;\n    const unsigned long long MASK31 = (1UL << 31) - 1;\n\
    \    const unsigned long long MOD = (1UL << 61) - 1;\n    const unsigned long\
    \ long MASK61 = MOD;\n    const unsigned long long POSITIVIZER = MOD * 4;\n\n\
    \    // a*b mod 2^61-1\u3092\u8FD4\u3059\u95A2\u6570\n    unsigned long long Mul(unsigned\
    \ long long a, unsigned long long b) {\n        unsigned long long au = a >> 31;\n\
    \        unsigned long long ad = a & MASK31;\n        unsigned long long bu =\
    \ b >> 31;\n        unsigned long long bd = b & MASK31;\n        unsigned long\
    \ long mid = ad * bu + au * bd;\n        unsigned long long midu = mid >> 30;\n\
    \        unsigned long long midd = mid & MASK30;\n        return CalcMod(au *\
    \ bu * 2 + midu + (midd << 31) + ad * bd);\n    }\n\n    // mod 2^61-1\u3092\u8A08\
    \u7B97\u3059\u308B\u95A2\u6570\n    unsigned long long CalcMod(unsigned long long\
    \ x) {\n        unsigned long long xu = x >> 61;\n        unsigned long long xd\
    \ = x & MASK61;\n        unsigned long long res = xu + xd;\n        if (res >=\
    \ MOD) res -= MOD;\n        return res;\n    }\n\npublic:\n    RollingHash(const\
    \ string &S,long long base = 1237) : base(base) {\n        int N = S.size();\n\
    \        hash.assign(N + 1, 0);\n        base_pow.assign(N + 1, 1);\n        for\
    \ (int i = 0; i < N; ++i) {\n            base_pow[i + 1] = Mul(base_pow[i], base);\n\
    \        }\n        for (int i = 0; i < N; ++i) {\n            long long tmp =\
    \ S[i] - 'a' + 1; // 0 \u3092\u5272\u308A\u5F53\u3066\u3066\u306F\u3044\u3051\u306A\
    \u3044\n            hash[i + 1] = CalcMod(Mul(hash[i], base) + tmp);\n       \
    \ }\n    }\n\n    unsigned long long get_hash(int l, int r) { // [l, r)\n    \
    \    unsigned long long result = CalcMod(hash[r] + POSITIVIZER - Mul(hash[l],\
    \ base_pow[r - l]));\n        return result;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nclass RollingHash {\nprivate:\n\
    \    long long base;\n    vector<unsigned long long> hash, base_pow;\n    const\
    \ unsigned long long MASK30 = (1UL << 30) - 1;\n    const unsigned long long MASK31\
    \ = (1UL << 31) - 1;\n    const unsigned long long MOD = (1UL << 61) - 1;\n  \
    \  const unsigned long long MASK61 = MOD;\n    const unsigned long long POSITIVIZER\
    \ = MOD * 4;\n\n    // a*b mod 2^61-1\u3092\u8FD4\u3059\u95A2\u6570\n    unsigned\
    \ long long Mul(unsigned long long a, unsigned long long b) {\n        unsigned\
    \ long long au = a >> 31;\n        unsigned long long ad = a & MASK31;\n     \
    \   unsigned long long bu = b >> 31;\n        unsigned long long bd = b & MASK31;\n\
    \        unsigned long long mid = ad * bu + au * bd;\n        unsigned long long\
    \ midu = mid >> 30;\n        unsigned long long midd = mid & MASK30;\n       \
    \ return CalcMod(au * bu * 2 + midu + (midd << 31) + ad * bd);\n    }\n\n    //\
    \ mod 2^61-1\u3092\u8A08\u7B97\u3059\u308B\u95A2\u6570\n    unsigned long long\
    \ CalcMod(unsigned long long x) {\n        unsigned long long xu = x >> 61;\n\
    \        unsigned long long xd = x & MASK61;\n        unsigned long long res =\
    \ xu + xd;\n        if (res >= MOD) res -= MOD;\n        return res;\n    }\n\n\
    public:\n    RollingHash(const string &S,long long base = 1237) : base(base) {\n\
    \        int N = S.size();\n        hash.assign(N + 1, 0);\n        base_pow.assign(N\
    \ + 1, 1);\n        for (int i = 0; i < N; ++i) {\n            base_pow[i + 1]\
    \ = Mul(base_pow[i], base);\n        }\n        for (int i = 0; i < N; ++i) {\n\
    \            long long tmp = S[i] - 'a' + 1; // 0 \u3092\u5272\u308A\u5F53\u3066\
    \u3066\u306F\u3044\u3051\u306A\u3044\n            hash[i + 1] = CalcMod(Mul(hash[i],\
    \ base) + tmp);\n        }\n    }\n\n    unsigned long long get_hash(int l, int\
    \ r) { // [l, r)\n        unsigned long long result = CalcMod(hash[r] + POSITIVIZER\
    \ - Mul(hash[l], base_pow[r - l]));\n        return result;\n    }\n};"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/cpp/RollingHash.cpp
  requiredBy: []
  timestamp: '2024-11-10 12:05:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/cpp/RollingHash.cpp
layout: document
redirect_from:
- /library/algo_library/cpp/RollingHash.cpp
- /library/algo_library/cpp/RollingHash.cpp.html
title: algo_library/cpp/RollingHash.cpp
---
