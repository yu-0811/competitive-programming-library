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
    - https://atcoder.jp/contests/abc440/submissions/72666963
  bundledCode: "#line 1 \"algorithm_library/cpp/hash.cpp\"\n// \u4F7F\u7528\u4F8B\
    https://atcoder.jp/contests/abc440/submissions/72666963\n\n// 64bit\u6574\u6570\
    \u7528\u306E\u9AD8\u54C1\u8CEA\u306A\u30DF\u30AD\u30B7\u30F3\u30B0\u95A2\u6570\
    \n// (SplitMix64\u306E\u5B9A\u6570\u306A\u3069\u3092\u4F7F\u7528)\nuint64_t mix(uint64_t\
    \ x) {\n    x += 0x9e3779b97f4a7c15;\n    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;\n\
    \    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;\n    return x ^ (x >> 31);\n}\n\
    \n// vector\u3092\u53D7\u3051\u53D6\u3063\u3066\u30CF\u30C3\u30B7\u30E5\u3092\u8FD4\
    \u3059\u95A2\u6570\nuint64_t get_vector_hash(const vector<int>& vec) {\n    uint64_t\
    \ seed = vec.size();\n    for (const auto& val : vec) {\n        seed ^= mix(static_cast<uint64_t>(val))\
    \ + 0x9e3779b9 + (seed << 6) + (seed >> 2);\n    }\n    return seed;\n}\n"
  code: "// \u4F7F\u7528\u4F8Bhttps://atcoder.jp/contests/abc440/submissions/72666963\n\
    \n// 64bit\u6574\u6570\u7528\u306E\u9AD8\u54C1\u8CEA\u306A\u30DF\u30AD\u30B7\u30F3\
    \u30B0\u95A2\u6570\n// (SplitMix64\u306E\u5B9A\u6570\u306A\u3069\u3092\u4F7F\u7528\
    )\nuint64_t mix(uint64_t x) {\n    x += 0x9e3779b97f4a7c15;\n    x = (x ^ (x >>\
    \ 30)) * 0xbf58476d1ce4e5b9;\n    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;\n\
    \    return x ^ (x >> 31);\n}\n\n// vector\u3092\u53D7\u3051\u53D6\u3063\u3066\
    \u30CF\u30C3\u30B7\u30E5\u3092\u8FD4\u3059\u95A2\u6570\nuint64_t get_vector_hash(const\
    \ vector<int>& vec) {\n    uint64_t seed = vec.size();\n    for (const auto& val\
    \ : vec) {\n        seed ^= mix(static_cast<uint64_t>(val)) + 0x9e3779b9 + (seed\
    \ << 6) + (seed >> 2);\n    }\n    return seed;\n}"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/hash.cpp
  requiredBy: []
  timestamp: '2026-04-15 17:42:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/hash.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/hash.cpp
- /library/algorithm_library/cpp/hash.cpp.html
title: algorithm_library/cpp/hash.cpp
---
