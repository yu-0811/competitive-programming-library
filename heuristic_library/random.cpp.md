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
  bundledCode: "#line 1 \"heuristic_library/random.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define\
    \ ll long long\n\nclass Random {\n    static uint32_t xorshift() {\n        static\
    \ uint32_t x = 123456789, y = 362436039, z = 521288629, w = 88675123; \n     \
    \   uint32_t t = x ^ (x << 11);\n        x = y; y = z; z = w;\n        return\
    \ w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    // [0, x)\n    inline\
    \ static uint32_t randrange(unsigned x) { return xorshift() % x; }\n    // [x,\
    \ y)\n    inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y\
    \ - x) + x; }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n#define rep(i, n) for (int\
    \ i = 0; i < (int)(n); i++)\n#define ll long long\n\nclass Random {\n    static\
    \ uint32_t xorshift() {\n        static uint32_t x = 123456789, y = 362436039,\
    \ z = 521288629, w = 88675123; \n        uint32_t t = x ^ (x << 11);\n       \
    \ x = y; y = z; z = w;\n        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n\
    \    }\npublic:\n    // [0, x)\n    inline static uint32_t randrange(unsigned\
    \ x) { return xorshift() % x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned\
    \ x, unsigned y) { return randrange(y - x) + x; }\n    // [0.0, 1.0)\n    inline\
    \ static double random() { return (xorshift() + 0.5) * (1.0 / UINT_MAX); }\n\n\
    };"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/random.cpp
  requiredBy: []
  timestamp: '2025-01-06 22:05:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/random.cpp
layout: document
redirect_from:
- /library/heuristic_library/random.cpp
- /library/heuristic_library/random.cpp.html
title: heuristic_library/random.cpp
---
