---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: heuristic_library/cpp/template.cpp
    title: heuristic_library/cpp/template.cpp
  _extendedRequiredBy: []
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
    \ y) { \n        assert(x < y);\n        return randrange(y - x) + x;\n    }\n\
    \    // [0.0, 1.0)\n    inline static double random() { return (xorshift32() +\
    \ 0.5) * (1.0 / UINT_MAX); }\n};\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\ninline Timer timer;\n\n#ifndef ONLINE_JUDGE\n\
    \    constexpr int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit\
    \ = 1987;\n#endif\n#line 2 \"heuristic_library/cpp/1DHash.cpp\"\n\n// \u4E00\u6B21\
    \u5143 Zobrist Hash\n// \u76E4\u9762\u306E\u9577\u3055\u3001\u76E4\u9762\u306E\
    \u5024\u306E\u7A2E\u985E\u6570\u3092\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\u5F15\
    \u6570\u3068\u3057\u3066\u53D7\u3051\u53D6\u308B\n// \u3082\u3046\u3061\u3087\u3063\
    \u3068\u3044\u3044\u611F\u3058\u306B\u3067\u304D\u305D\u3046\u3001\u7279\u306B\
    \ getValueIndex \u306E\u90E8\u5206\n// LEN: \u76E4\u9762\u306E\u30B5\u30A4\u30BA\
    \n// NumValue: \u5024\u306E\u30D0\u30EA\u30A8\u30FC\u30B7\u30E7\u30F3\u306E\u6570\
    \uFF08\u914D\u5217\u306E\u78BA\u4FDD\u30B5\u30A4\u30BA\uFF09\n// MIN_VAL: \u5024\
    \u306E\u6700\u5C0F\u5024\uFF08\u3053\u308C\u3092\u4F7F\u3063\u3066\u30AA\u30D5\
    \u30BB\u30C3\u30C8\u3059\u308B\uFF09\ntemplate<int LEN, int NumValue, int MIN_VAL\
    \ = 0> \nstruct ZobristHash1D {\nprivate:\n    array<array<HashType, NumValue>,\
    \ LEN> table;\n\n    // \u5024\u3092\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u306B\
    \u5909\u63DB\n    static constexpr int getValueIndex(int value) {\n        int\
    \ index = value - MIN_VAL;\n        assert(index >= 0 && index < NumValue); \n\
    \        \n        return index;\n    }\n\npublic:\n    // \u30B3\u30F3\u30B9\u30C8\
    \u30E9\u30AF\u30BF\uFF1A\u30AA\u30D6\u30B8\u30A7\u30AF\u30C8\u751F\u6210\u6642\
    \u306B\u30CF\u30C3\u30B7\u30E5\u30C6\u30FC\u30D6\u30EB\u3092\u4E71\u6570\u3067\
    \u521D\u671F\u5316\u3059\u308B\n    ZobristHash1D() {\n        for (int i = 0;\
    \ i < LEN; ++i) {\n            for (int k = 0; k < NumValue; ++k) {\n        \
    \        table[i][k] = Random::xorshift64(); // 32\u30D3\u30C3\u30C8\u3067\u3044\
    \u3044\u3068\u304D\u306F xorshift32() \u3067\u3082\u826F\u3044\n            }\n\
    \        }\n    }\n\n    // \u521D\u671F\u76E4\u9762\u304B\u3089\u30CF\u30C3\u30B7\
    \u30E5\u5024\u3092\u8A08\u7B97\u3059\u308B\n    template<typename Board> // \u4EFB\
    \u610F\u306E\u76E4\u9762\u306E\u578B\u3092\u53D6\u308C\u308B\u3088\u3046\u306B\
    \u306A\u308B\n    HashType initialize_hash(const Board& board) const {\n     \
    \   assert (board.size() == LEN);\n        HashType hash = 0;\n        for (int\
    \ i = 0; i < LEN; ++i) {\n            int index = getValueIndex(board[i]);\n \
    \           hash ^= table[i][index];\n        }\n        return hash;\n    }\n\
    \n    // 1\u30DE\u30B9\u306E\u5909\u5316\u304B\u3089\u30CF\u30C3\u30B7\u30E5\u5024\
    \u3092\u9AD8\u901F\u306B\u66F4\u65B0\uFF08\u5DEE\u5206\u66F4\u65B0\uFF09\u3059\
    \u308B\n    // current_hash: \u66F4\u65B0\u524D\u306E\u30CF\u30C3\u30B7\u30E5\u5024\
    \n    // pos: \u5909\u5316\u3057\u305F\u30DE\u30B9\u306E\u4F4D\u7F6E\n    // old_value:\
    \ \u5909\u5316\u524D\u306E\u5024\n    // new_value: \u5909\u5316\u5F8C\u306E\u5024\
    \n    // \u30AF\u30E9\u30B9\u5185\u90E8\u306B\u8FFD\u52A0\u30FB\u4FEE\u6B63\n\
    \    HashType update_hash(HashType current_hash, int pos, int old_value, int new_value)\
    \ const {\n        current_hash ^= table[pos][getValueIndex(old_value)];\n   \
    \     current_hash ^= table[pos][getValueIndex(new_value)];\n        return current_hash;\n\
    \    }\n};\n// TODO\nusing HashType = uint32_t; \nconst int LEN = 50; // \u76E4\
    \u9762\u306E\u9577\u3055\nconst int MIN_VAL = 0; // \u76E4\u9762\u306E\u5024\u306E\
    \u6700\u5C0F\u5024\nconst int NumValue = 100000; // \u76E4\u9762\u306E\u5024\u306E\
    \u30D0\u30EA\u30A8\u30FC\u30B7\u30E7\u30F3\u6570\nZobristHash1D<LEN, NumValue,\
    \ MIN_VAL> zobrist_hash;\n"
  code: "#include \"template.cpp\"\n\n// \u4E00\u6B21\u5143 Zobrist Hash\n// \u76E4\
    \u9762\u306E\u9577\u3055\u3001\u76E4\u9762\u306E\u5024\u306E\u7A2E\u985E\u6570\
    \u3092\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\u5F15\u6570\u3068\u3057\u3066\u53D7\
    \u3051\u53D6\u308B\n// \u3082\u3046\u3061\u3087\u3063\u3068\u3044\u3044\u611F\u3058\
    \u306B\u3067\u304D\u305D\u3046\u3001\u7279\u306B getValueIndex \u306E\u90E8\u5206\
    \n// LEN: \u76E4\u9762\u306E\u30B5\u30A4\u30BA\n// NumValue: \u5024\u306E\u30D0\
    \u30EA\u30A8\u30FC\u30B7\u30E7\u30F3\u306E\u6570\uFF08\u914D\u5217\u306E\u78BA\
    \u4FDD\u30B5\u30A4\u30BA\uFF09\n// MIN_VAL: \u5024\u306E\u6700\u5C0F\u5024\uFF08\
    \u3053\u308C\u3092\u4F7F\u3063\u3066\u30AA\u30D5\u30BB\u30C3\u30C8\u3059\u308B\
    \uFF09\ntemplate<int LEN, int NumValue, int MIN_VAL = 0> \nstruct ZobristHash1D\
    \ {\nprivate:\n    array<array<HashType, NumValue>, LEN> table;\n\n    // \u5024\
    \u3092\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u306B\u5909\u63DB\n    static constexpr\
    \ int getValueIndex(int value) {\n        int index = value - MIN_VAL;\n     \
    \   assert(index >= 0 && index < NumValue); \n        \n        return index;\n\
    \    }\n\npublic:\n    // \u30B3\u30F3\u30B9\u30C8\u30E9\u30AF\u30BF\uFF1A\u30AA\
    \u30D6\u30B8\u30A7\u30AF\u30C8\u751F\u6210\u6642\u306B\u30CF\u30C3\u30B7\u30E5\
    \u30C6\u30FC\u30D6\u30EB\u3092\u4E71\u6570\u3067\u521D\u671F\u5316\u3059\u308B\
    \n    ZobristHash1D() {\n        for (int i = 0; i < LEN; ++i) {\n           \
    \ for (int k = 0; k < NumValue; ++k) {\n                table[i][k] = Random::xorshift64();\
    \ // 32\u30D3\u30C3\u30C8\u3067\u3044\u3044\u3068\u304D\u306F xorshift32() \u3067\
    \u3082\u826F\u3044\n            }\n        }\n    }\n\n    // \u521D\u671F\u76E4\
    \u9762\u304B\u3089\u30CF\u30C3\u30B7\u30E5\u5024\u3092\u8A08\u7B97\u3059\u308B\
    \n    template<typename Board> // \u4EFB\u610F\u306E\u76E4\u9762\u306E\u578B\u3092\
    \u53D6\u308C\u308B\u3088\u3046\u306B\u306A\u308B\n    HashType initialize_hash(const\
    \ Board& board) const {\n        assert (board.size() == LEN);\n        HashType\
    \ hash = 0;\n        for (int i = 0; i < LEN; ++i) {\n            int index =\
    \ getValueIndex(board[i]);\n            hash ^= table[i][index];\n        }\n\
    \        return hash;\n    }\n\n    // 1\u30DE\u30B9\u306E\u5909\u5316\u304B\u3089\
    \u30CF\u30C3\u30B7\u30E5\u5024\u3092\u9AD8\u901F\u306B\u66F4\u65B0\uFF08\u5DEE\
    \u5206\u66F4\u65B0\uFF09\u3059\u308B\n    // current_hash: \u66F4\u65B0\u524D\u306E\
    \u30CF\u30C3\u30B7\u30E5\u5024\n    // pos: \u5909\u5316\u3057\u305F\u30DE\u30B9\
    \u306E\u4F4D\u7F6E\n    // old_value: \u5909\u5316\u524D\u306E\u5024\n    // new_value:\
    \ \u5909\u5316\u5F8C\u306E\u5024\n    // \u30AF\u30E9\u30B9\u5185\u90E8\u306B\u8FFD\
    \u52A0\u30FB\u4FEE\u6B63\n    HashType update_hash(HashType current_hash, int\
    \ pos, int old_value, int new_value) const {\n        current_hash ^= table[pos][getValueIndex(old_value)];\n\
    \        current_hash ^= table[pos][getValueIndex(new_value)];\n        return\
    \ current_hash;\n    }\n};\n// TODO\nusing HashType = uint32_t; \nconst int LEN\
    \ = 50; // \u76E4\u9762\u306E\u9577\u3055\nconst int MIN_VAL = 0; // \u76E4\u9762\
    \u306E\u5024\u306E\u6700\u5C0F\u5024\nconst int NumValue = 100000; // \u76E4\u9762\
    \u306E\u5024\u306E\u30D0\u30EA\u30A8\u30FC\u30B7\u30E7\u30F3\u6570\nZobristHash1D<LEN,\
    \ NumValue, MIN_VAL> zobrist_hash;\n"
  dependsOn:
  - heuristic_library/cpp/template.cpp
  isVerificationFile: false
  path: heuristic_library/cpp/1DHash.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/1DHash.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/1DHash.cpp
- /library/heuristic_library/cpp/1DHash.cpp.html
title: heuristic_library/cpp/1DHash.cpp
---
