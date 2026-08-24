---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: heuristic_library/cpp/1DHash.cpp
    title: heuristic_library/cpp/1DHash.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/2Dhash.cpp
    title: heuristic_library/cpp/2Dhash.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/RandomSet.cpp
    title: heuristic_library/cpp/RandomSet.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/SA.cpp
    title: heuristic_library/cpp/SA.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/beam_search_cand_no_copy.cpp
    title: heuristic_library/cpp/beam_search_cand_no_copy.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/beam_search_naive.cpp
    title: heuristic_library/cpp/beam_search_naive.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/beam_search_no_hash.cpp
    title: heuristic_library/cpp/beam_search_no_hash.cpp
  - icon: ':warning:'
    path: heuristic_library/cpp/beam_search_sabunkousin.cpp
    title: heuristic_library/cpp/beam_search_sabunkousin.cpp
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"heuristic_library/cpp/template.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\nusing\
    \ ll = long long;\nusing u64 = unsigned long long;\n#pragma GCC target(\"avx2\"\
    )\n#pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nclass\
    \ Random {\n    static uint32_t xorshift32() {\n        static uint32_t x = 123456789,\
    \ y = 362436039, z = 521288629, w = 88675123; \n        uint32_t t = x ^ (x <<\
    \ 11);\n        x = y; y = z; z = w;\n        return w = (w ^ (w >> 19)) ^ (t\
    \ ^ (t >> 8));\n    }\npublic:\n    inline static u64 xorshift64() {\n       \
    \ static u64 state = 88172645463325252ULL;\n        u64 x = state;\n        x\
    \ ^= x << 7;\n        x ^= x >> 9;\n        return state = x;\n    }\n    // [0,\
    \ x)\n    inline static uint32_t randrange(unsigned x) { return xorshift32() %\
    \ x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned x, unsigned\
    \ y) { return randrange(y - x) + x; }\n    // [0.0, 1.0)\n    inline static double\
    \ random() { return (xorshift32() + 0.5) * (1.0 / UINT_MAX); }\n};\n\nclass Timer\
    \ {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n    Timer()\
    \ : start(chrono::steady_clock::now()) {}\n    unsigned short get_ms() { // \u7D4C\
    \u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\ninline Timer timer;\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n#define rep(i, n) for (int\
    \ i = 0; i < (int)(n); i++)\nusing ll = long long;\nusing u64 = unsigned long\
    \ long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"O3\")\n#pragma GCC\
    \ optimize(\"unroll-loops\")\n\nclass Random {\n    static uint32_t xorshift32()\
    \ {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629, w =\
    \ 88675123; \n        uint32_t t = x ^ (x << 11);\n        x = y; y = z; z = w;\n\
    \        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    inline\
    \ static u64 xorshift64() {\n        static u64 state = 88172645463325252ULL;\n\
    \        u64 x = state;\n        x ^= x << 7;\n        x ^= x >> 9;\n        return\
    \ state = x;\n    }\n    // [0, x)\n    inline static uint32_t randrange(unsigned\
    \ x) { return xorshift32() % x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned\
    \ x, unsigned y) { return randrange(y - x) + x; }\n    // [0.0, 1.0)\n    inline\
    \ static double random() { return (xorshift32() + 0.5) * (1.0 / UINT_MAX); }\n\
    };\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n\
    \    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned short get_ms()\
    \ { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\ninline Timer timer;\n"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/template.cpp
  requiredBy:
  - heuristic_library/cpp/RandomSet.cpp
  - heuristic_library/cpp/SA.cpp
  - heuristic_library/cpp/2Dhash.cpp
  - heuristic_library/cpp/beam_search_cand_no_copy.cpp
  - heuristic_library/cpp/beam_search_sabunkousin.cpp
  - heuristic_library/cpp/1DHash.cpp
  - heuristic_library/cpp/beam_search_naive.cpp
  - heuristic_library/cpp/beam_search_no_hash.cpp
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/template.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/template.cpp
- /library/heuristic_library/cpp/template.cpp.html
title: heuristic_library/cpp/template.cpp
---
