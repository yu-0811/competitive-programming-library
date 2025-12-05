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
  bundledCode: "#line 1 \"heuristic_library/cpp/2Dhash.cpp\"\n// \u4E8C\u6B21\u5143\
    \ Zobrist Hash\n// \u76E4\u9762\u306E\u9AD8\u3055\u3068\u5E45\u3001\u99D2\u306E\
    \u7A2E\u985E\u6570\u3092\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\u5F15\u6570\u3068\
    \u3057\u3066\u53D7\u3051\u53D6\u308B\n// \u3082\u3046\u3061\u3087\u3063\u3068\u3044\
    \u3044\u611F\u3058\u306B\u3067\u304D\u305D\u3046\u3001\u7279\u306B getValueIndex\
    \ \u306E\u90E8\u5206\nusing HashType = uint32_t; // TODO\ntemplate<short Height,\
    \ short Width, short NumValue>\nstruct ZobristHash2D {\nprivate:\n    // \u30CF\
    \u30C3\u30B7\u30E5\u5024\u3092\u683C\u7D0D\u3059\u308B\u30C6\u30FC\u30D6\u30EB\
    \n    array<array<array<HashType, NumValue>, Width>, Height> table;\n    \n  \
    \  // \u76E4\u9762\u306E\u7A2E\u985E\u3092\u8868\u3059\u5024\u304B\u3089\u3001\
    \u30C6\u30FC\u30D6\u30EB\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u306B\u5909\
    \u63DB\u3059\u308B\n    static constexpr short getValueIndex(short value) { //\
    \ <<< \u5909\u66F4\n        if (value == -1) return 0; // 'o'\n        if (value\
    \ == -2) return 1; // '.'\n        return 2;                       // 'x'\n  \
    \  }\n\npublic:\n    // \u30B3\u30F3\u30B9\u30C8\u30E9\u30AF\u30BF\uFF1A\u30AA\
    \u30D6\u30B8\u30A7\u30AF\u30C8\u751F\u6210\u6642\u306B\u30CF\u30C3\u30B7\u30E5\
    \u30C6\u30FC\u30D6\u30EB\u3092\u4E71\u6570\u3067\u521D\u671F\u5316\u3059\u308B\
    \n    ZobristHash2D() {\n        for (int i = 0; i < Height; ++i) {\n        \
    \    for (int j = 0; j < Width; ++j) {\n                for (int k = 0; k < NumValue;\
    \ ++k) {\n                    table[i][j][k] = Random::xorshift64(); // 32\u30D3\
    \u30C3\u30C8\u3067\u3044\u3044\u3068\u304D\u306F xorshift32() \u3067\u3082\u826F\
    \u3044\n                }\n            }\n        }\n    }\n\n    // \u521D\u671F\
    \u76E4\u9762\u304B\u3089\u30CF\u30C3\u30B7\u30E5\u5024\u3092\u8A08\u7B97\u3059\
    \u308B\n    template<typename Board> // \u4EFB\u610F\u306E\u76E4\u9762\u306E\u578B\
    \u3092\u53D6\u308C\u308B\u3088\u3046\u306B\u306A\u308B\n    HashType initialize_hash(const\
    \ Board& board) const {\n        assert (board.size() == Height && board[0].size()\
    \ == Width);\n        HashType hash = 0;\n        for (int i = 0; i < Height;\
    \ ++i) {\n            for (int j = 0; j < Width; ++j) {\n                int index\
    \ = getValueIndex(board[i][j]);\n                hash ^= table[i][j][index];\n\
    \            }\n        }\n        return hash;\n    }\n\n    // 1\u30DE\u30B9\
    \u306E\u5909\u5316\u304B\u3089\u30CF\u30C3\u30B7\u30E5\u5024\u3092\u9AD8\u901F\
    \u306B\u66F4\u65B0\uFF08\u5DEE\u5206\u66F4\u65B0\uFF09\u3059\u308B\n    // current_hash:\
    \ \u66F4\u65B0\u524D\u306E\u30CF\u30C3\u30B7\u30E5\u5024\n    // r, c: \u5909\u5316\
    \u304C\u3042\u3063\u305F\u30DE\u30B9\u306E\u5EA7\u6A19\n    // old_value: \u5909\
    \u5316\u524D\u306E\u76E4\u9762\n    // new_value: \u5909\u5316\u5F8C\u306E\u76E4\
    \u9762\n    HashType update_hash(HashType current_hash, short r, short c, short\
    \ old_value, short new_value) const {\n        short old_index = getValueIndex(old_value);\n\
    \        short new_index = getValueIndex(new_value);\n        return current_hash\
    \ ^ table[r][c][old_index] ^ table[r][c][new_index];\n    }\n};\nconst short Height\
    \ = N, Width = N, NumValue = 3; // TODO\nZobristHash2D<Height, Width, NumValue>\
    \ zobrist_hash;\n"
  code: "// \u4E8C\u6B21\u5143 Zobrist Hash\n// \u76E4\u9762\u306E\u9AD8\u3055\u3068\
    \u5E45\u3001\u99D2\u306E\u7A2E\u985E\u6570\u3092\u30C6\u30F3\u30D7\u30EC\u30FC\
    \u30C8\u5F15\u6570\u3068\u3057\u3066\u53D7\u3051\u53D6\u308B\n// \u3082\u3046\u3061\
    \u3087\u3063\u3068\u3044\u3044\u611F\u3058\u306B\u3067\u304D\u305D\u3046\u3001\
    \u7279\u306B getValueIndex \u306E\u90E8\u5206\nusing HashType = uint32_t; // TODO\n\
    template<short Height, short Width, short NumValue>\nstruct ZobristHash2D {\n\
    private:\n    // \u30CF\u30C3\u30B7\u30E5\u5024\u3092\u683C\u7D0D\u3059\u308B\u30C6\
    \u30FC\u30D6\u30EB\n    array<array<array<HashType, NumValue>, Width>, Height>\
    \ table;\n    \n    // \u76E4\u9762\u306E\u7A2E\u985E\u3092\u8868\u3059\u5024\u304B\
    \u3089\u3001\u30C6\u30FC\u30D6\u30EB\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    \u306B\u5909\u63DB\u3059\u308B\n    static constexpr short getValueIndex(short\
    \ value) { // <<< \u5909\u66F4\n        if (value == -1) return 0; // 'o'\n  \
    \      if (value == -2) return 1; // '.'\n        return 2;                  \
    \     // 'x'\n    }\n\npublic:\n    // \u30B3\u30F3\u30B9\u30C8\u30E9\u30AF\u30BF\
    \uFF1A\u30AA\u30D6\u30B8\u30A7\u30AF\u30C8\u751F\u6210\u6642\u306B\u30CF\u30C3\
    \u30B7\u30E5\u30C6\u30FC\u30D6\u30EB\u3092\u4E71\u6570\u3067\u521D\u671F\u5316\
    \u3059\u308B\n    ZobristHash2D() {\n        for (int i = 0; i < Height; ++i)\
    \ {\n            for (int j = 0; j < Width; ++j) {\n                for (int k\
    \ = 0; k < NumValue; ++k) {\n                    table[i][j][k] = Random::xorshift64();\
    \ // 32\u30D3\u30C3\u30C8\u3067\u3044\u3044\u3068\u304D\u306F xorshift32() \u3067\
    \u3082\u826F\u3044\n                }\n            }\n        }\n    }\n\n   \
    \ // \u521D\u671F\u76E4\u9762\u304B\u3089\u30CF\u30C3\u30B7\u30E5\u5024\u3092\u8A08\
    \u7B97\u3059\u308B\n    template<typename Board> // \u4EFB\u610F\u306E\u76E4\u9762\
    \u306E\u578B\u3092\u53D6\u308C\u308B\u3088\u3046\u306B\u306A\u308B\n    HashType\
    \ initialize_hash(const Board& board) const {\n        assert (board.size() ==\
    \ Height && board[0].size() == Width);\n        HashType hash = 0;\n        for\
    \ (int i = 0; i < Height; ++i) {\n            for (int j = 0; j < Width; ++j)\
    \ {\n                int index = getValueIndex(board[i][j]);\n               \
    \ hash ^= table[i][j][index];\n            }\n        }\n        return hash;\n\
    \    }\n\n    // 1\u30DE\u30B9\u306E\u5909\u5316\u304B\u3089\u30CF\u30C3\u30B7\
    \u30E5\u5024\u3092\u9AD8\u901F\u306B\u66F4\u65B0\uFF08\u5DEE\u5206\u66F4\u65B0\
    \uFF09\u3059\u308B\n    // current_hash: \u66F4\u65B0\u524D\u306E\u30CF\u30C3\u30B7\
    \u30E5\u5024\n    // r, c: \u5909\u5316\u304C\u3042\u3063\u305F\u30DE\u30B9\u306E\
    \u5EA7\u6A19\n    // old_value: \u5909\u5316\u524D\u306E\u76E4\u9762\n    // new_value:\
    \ \u5909\u5316\u5F8C\u306E\u76E4\u9762\n    HashType update_hash(HashType current_hash,\
    \ short r, short c, short old_value, short new_value) const {\n        short old_index\
    \ = getValueIndex(old_value);\n        short new_index = getValueIndex(new_value);\n\
    \        return current_hash ^ table[r][c][old_index] ^ table[r][c][new_index];\n\
    \    }\n};\nconst short Height = N, Width = N, NumValue = 3; // TODO\nZobristHash2D<Height,\
    \ Width, NumValue> zobrist_hash;"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/2Dhash.cpp
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/2Dhash.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/2Dhash.cpp
- /library/heuristic_library/cpp/2Dhash.cpp.html
title: heuristic_library/cpp/2Dhash.cpp
---
