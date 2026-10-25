---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/yu-0811/competitive-programming-library/tree/main/heuristic_library
  bundledCode: "#line 1 \"heuristic_library/cpp/shortAHC.cpp\"\n// library: https://github.com/yu-0811/competitive-programming-library/tree/main/heuristic_library\n\
    #include <iostream>\n#include <vector>\n#include <algorithm>\n#include <unordered_set>\n\
    #include <utility>\n#include <climits>\n#include <deque>\n#include <set>\n#include\
    \ <queue>\n#include <bitset>\n#include <cmath>\n#include <string>\n#include <cstdlib>\n\
    #include <cassert>\n#include <chrono>\n#include <cstring>\nusing namespace std;\n\
    #define rep(i, n) for (int i = 0; i < (int)(n); i++)\nusing ll = long long;\n\
    using u64 = unsigned long long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nclass Random {\n    static uint32_t\
    \ xorshift32() {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629,\
    \ w = 88675123; \n        uint32_t t = x ^ (x << 11);\n        x = y; y = z; z\
    \ = w;\n        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n\
    \    inline static u64 xorshift64() {\n        static u64 state = 88172645463325252ULL;\n\
    \        u64 x = state;\n        x ^= x << 7;\n        x ^= x >> 9;\n        return\
    \ state = x;\n    }\n    // [0, x)\n    inline static uint32_t randrange(unsigned\
    \ x) { return xorshift32() % x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned\
    \ x, unsigned y) { \n        assert(x < y);\n        return randrange(y - x) +\
    \ x;\n    }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift32()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n};\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\ninline Timer timer;\n\n#ifndef ONLINE_JUDGE\n\
    \    constexpr int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit\
    \ = 1987;\n#endif\n\n/*\n\u3053\u3053\u306B\u554F\u984C\u6587\u3092\u8CBC\u308B\
    \n*/\n\nint main(){\n    ios::sync_with_stdio(false); cin.tie(0);\n    timer =\
    \ Timer(); // \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\n\n}\n"
  code: "// library: https://github.com/yu-0811/competitive-programming-library/tree/main/heuristic_library\n\
    #include <iostream>\n#include <vector>\n#include <algorithm>\n#include <unordered_set>\n\
    #include <utility>\n#include <climits>\n#include <deque>\n#include <set>\n#include\
    \ <queue>\n#include <bitset>\n#include <cmath>\n#include <string>\n#include <cstdlib>\n\
    #include <cassert>\n#include <chrono>\n#include <cstring>\nusing namespace std;\n\
    #define rep(i, n) for (int i = 0; i < (int)(n); i++)\nusing ll = long long;\n\
    using u64 = unsigned long long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nclass Random {\n    static uint32_t\
    \ xorshift32() {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629,\
    \ w = 88675123; \n        uint32_t t = x ^ (x << 11);\n        x = y; y = z; z\
    \ = w;\n        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n\
    \    inline static u64 xorshift64() {\n        static u64 state = 88172645463325252ULL;\n\
    \        u64 x = state;\n        x ^= x << 7;\n        x ^= x >> 9;\n        return\
    \ state = x;\n    }\n    // [0, x)\n    inline static uint32_t randrange(unsigned\
    \ x) { return xorshift32() % x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned\
    \ x, unsigned y) { \n        assert(x < y);\n        return randrange(y - x) +\
    \ x;\n    }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift32()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n};\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\ninline Timer timer;\n\n#ifndef ONLINE_JUDGE\n\
    \    constexpr int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit\
    \ = 1987;\n#endif\n\n/*\n\u3053\u3053\u306B\u554F\u984C\u6587\u3092\u8CBC\u308B\
    \n*/\n\nint main(){\n    ios::sync_with_stdio(false); cin.tie(0);\n    timer =\
    \ Timer(); // \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\n\n}"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/shortAHC.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/shortAHC.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/shortAHC.cpp
- /library/heuristic_library/cpp/shortAHC.cpp.html
title: heuristic_library/cpp/shortAHC.cpp
---
