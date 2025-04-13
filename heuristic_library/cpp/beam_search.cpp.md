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
  bundledCode: "#line 1 \"heuristic_library/cpp/beam_search.cpp\"\n#include <bits/stdc++.h>\n\
    #line 3 \"heuristic_library/cpp/beam_search.cpp\"\nusing namespace std;\n#define\
    \ rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\nusing u64\
    \ = unsigned long long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nconst int INF = 10000000;\nunordered_set<u64>\
    \ visited;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ########################################\n\
    const int beam_width = 380;\nconst int beam_depth = 120;\nconst int penalty =\
    \ 1;\nconst int bonus = 1000;\nconst int finish = bonus * 40 * -10;\n//#####################################################\n\
    \n// Zobrist Hash ########################################\nclass Random {\n \
    \   // 32\u30D3\u30C3\u30C8\u7248\u306E xorshift \u3092\u7528\u610F\uFF08\u72B6\
    \u614B\u306Fstatic\u5909\u6570\u3067\u7BA1\u7406\uFF09\n    static uint32_t xorshift32()\
    \ {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629, w =\
    \ 88675123; \n        uint32_t t = x ^ (x << 11);\n        x = y; y = z; z = w;\n\
    \        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    //\
    \ 64\u30D3\u30C3\u30C8\u7248\u4E71\u6570\uFF1A32\u30D3\u30C3\u30C8\u306E xorshift\
    \ \u30922\u56DE\u547C\u3073\u51FA\u3057\u3001\u7D50\u5408\u3059\u308B\n    inline\
    \ static uint64_t xorshift64() {\n         uint64_t high = xorshift32();\n   \
    \      uint64_t low  = xorshift32();\n         return (high << 32) | low;\n  \
    \  }\n    // [0, x)\n    inline static uint64_t randrange(uint64_t x) { return\
    \ xorshift64() % x; }\n    // [x, y)\n    inline static uint64_t randrange(uint64_t\
    \ x, uint64_t y) { return randrange(y - x) + x; }\n    // [0.0, 1.0)\n    inline\
    \ static double random() { \n        return (xorshift64() + 0.5) * (1.0 / (double)ULLONG_MAX);\
    \ \n    }\n};\nu64 zobrist[N][N][3];\nvoid init_zobrist() {\n    for (int i =\
    \ 0; i < N; i++) {\n        for (int j = 0; j < N; j++) {\n            for (int\
    \ k = 0; k < 3; k++) {\n                zobrist[i][j][k] = Random::randrange((1ULL\
    \ << 63)-1);\n            }\n        }\n    }\n}\n//#####################################################\n\
    \n// \u72B6\u614B #############################################\nstruct Move {\n\
    \  char d; int p;\n};\n\nstruct xy {\n  int x, y;\n};\n\nstruct State {\n  int\
    \ score;\n  int depth;\n  Move move_history[beam_depth];\n\n  State() : score(0),\
    \ depth(0) {};\n};\n\n// \u30BD\u30FC\u30C8\u95A2\u6570########################################\n\
    // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\nbool comp_max(const\
    \ State &a1, const State &a2){\n    return a1.score > a2.score;\n}\n// \u30B9\u30B3\
    \u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\nbool comp_min(const State &a1, const\
    \ State &a2){\n    return a1.score < a2.score;\n}\n//#####################################################\n\
    \n// \u8A55\u4FA1\u95A2\u6570########################################\n// \u5C0F\
    \u3055\u3044\u65B9\u304C\u3044\u3044\n// \u5404\u9B3C\u306E\u5916\u5468\u304B\u3089\
    \u306E\u8DDD\u96E2\u306E\u5408\u8A08\u3092\u8A55\u4FA1\u5024\u3068\u3059\u308B\
    \n// \u305F\u3060\u3057\u3001\u6700\u3082\u8FD1\u3044\u5916\u5468\u307E\u3067\u306B\
    \u798F\u304C\u3044\u308B\u306A\u3089 penalty \u3092\u52A0\u7B97\u3059\u308B\n\
    // \u798F\u304C\u843D\u3061\u308B\u76E4\u9762\u306F\u8A31\u3055\u306A\u3044\u3088\
    \u3046\u306B inf \u30DA\u30CA\u30EB\u30C6\u30A3\u30FC\u3092\u4E0E\u3048\u308B\n\
    // \u5012\u3057\u305F\u9B3C\u306E\u6570 * bonus \u3092\u6E1B\u7B97\u3059\u308B\
    \nint calc_eval(const State &s){\n  int eval = 0;\n\n  return eval;\n}\n//#####################################################\n\
    \n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State apply_move(const State &s, Move &mv){\n  State nex = s;\n  // \u72B6\u614B\
    \u9077\u79FB\n  return nex;\n}\n//#####################################################\n\
    \n// \u76E4\u9762\u30CF\u30C3\u30B7\u30E5########################################\n\
    inline int pieceIndex(int c) {\n    // \u76E4\u9762\u306E\u72B6\u614B\u306B\u5408\
    \u308F\u305B\u3066\u5BFE\u5FDC\u4ED8\u3051\u308B\n    if (c == -1) return 0; //\
    \ 'o'\n    else if (c == -2) return 1; // '.'\n    else return 2; // 'x'\n}\n\
    u64 board_to_u64(const int (&board)[N][N]) {\n    u64 hash = 0;\n    rep(i, N)\
    \ {\n        rep(j, N) {\n            int idx = pieceIndex(board[i][j]);\n   \
    \         hash ^= zobrist[i][j][idx];\n        }\n    }\n    return hash;\n}\n\
    \n//#####################################################\n\nauto beam_search(State\
    \ &init_state, int beam_width, int beam_depth){\n    vector<State> now;\n    now.emplace_back(init_state);\n\
    \    vector<State> next;\n    visited.emplace(board_to_u64(init_state.board));\n\
    \n    // \u9077\u79FB\u5019\u88DC ########################################\n \
    \   vector<Move> possible_moves;\n    //#################################################\n\
    \n    for (int i=0; i<beam_depth; i++){\n        bool sorted = false;\n      \
    \  for (auto &s : now){\n            // \u72B6\u614B\u3092\u9077\u79FB\u3055\u305B\
    \u308B\n            for (auto &mv: possible_moves){\n                // \u72B6\
    \u614B\u3092\u5909\u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\u5024\
    \u3092\u8A08\u7B97########\n                // \u3053\u308C\u305F\u3076\u3093\u5B9F\
    \u969B\u306B\u76E4\u9762\u3092\u52D5\u304B\u3055\u305A\u306B\u8A55\u4FA1\u5024\
    \u3060\u3051\u8A08\u7B97\u3067\u304D\u305F\u307B\u3046\u304C\u9AD8\u901F\u5316\
    \u3067\u304D\u308B\n                auto nex_s = apply_move(s, mv);\n        \
    \        if (nex_s.score == INF) continue;\n                //###########################################\n\
    \n                // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D, \u30BD\
    \u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\u306E\u8A55\u4FA1\u5024\
    \u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\u307F\u9077\u79FB\n   \
    \             //if (sorted && nex_s.score <= next[beam_width-1].score) continue;\n\
    \                // \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D, \u30BD\
    \u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5927\u306E\u8A55\u4FA1\u5024\
    \u3088\u308A\u3082\u5C0F\u3055\u3044\u5834\u5408\u306E\u307F\u9077\u79FB\n   \
    \             if (sorted && nex_s.score >= next[beam_width-1].score) continue;\n\
    \n                // \u65E2\u306B\u8A2A\u308C\u305F\u72B6\u614B\u306F\u30B9\u30AD\
    \u30C3\u30D7\n                u64 board_hash = board_to_u64(nex_s.board);\n  \
    \              if (visited.count(board_hash)) continue;\n                visited.emplace(board_hash);\n\
    \                next.emplace_back(nex_s);\n\n                if (nex_s.score\
    \ <= finish){\n                    return nex_s;\n                }\n\n      \
    \          if (next.size() >= 2*beam_width){\n                    sort(next.begin(),\
    \ next.end(), comp_min);\n                    next.resize(beam_width);\n     \
    \               sorted = true;\n                }\n            }\n        }\n\
    \        if (next.empty()) break;\n        sort(next.begin(), next.end(), comp_min);\n\
    \        next.resize(beam_width);\n        swap(now, next);\n        next.clear();\n\
    \    }\n  return now[0];\n}\n\nint main() {\n  ios::sync_with_stdio(false); cin.tie(0);\n\
    \  init_zobrist();\n\n  auto best_move = beam_search(init_state, beam_width, beam_depth);\n\
    \  for (int i=0; i<best_move.depth; i++){\n    cout << best_move.move_history[i].d\
    \ << \" \" << best_move.move_history[i].p << endl;\n  }\n}\n"
  code: "#include <bits/stdc++.h>\n#include <cassert>\nusing namespace std;\n#define\
    \ rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\nusing u64\
    \ = unsigned long long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nconst int INF = 10000000;\nunordered_set<u64>\
    \ visited;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ########################################\n\
    const int beam_width = 380;\nconst int beam_depth = 120;\nconst int penalty =\
    \ 1;\nconst int bonus = 1000;\nconst int finish = bonus * 40 * -10;\n//#####################################################\n\
    \n// Zobrist Hash ########################################\nclass Random {\n \
    \   // 32\u30D3\u30C3\u30C8\u7248\u306E xorshift \u3092\u7528\u610F\uFF08\u72B6\
    \u614B\u306Fstatic\u5909\u6570\u3067\u7BA1\u7406\uFF09\n    static uint32_t xorshift32()\
    \ {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629, w =\
    \ 88675123; \n        uint32_t t = x ^ (x << 11);\n        x = y; y = z; z = w;\n\
    \        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    //\
    \ 64\u30D3\u30C3\u30C8\u7248\u4E71\u6570\uFF1A32\u30D3\u30C3\u30C8\u306E xorshift\
    \ \u30922\u56DE\u547C\u3073\u51FA\u3057\u3001\u7D50\u5408\u3059\u308B\n    inline\
    \ static uint64_t xorshift64() {\n         uint64_t high = xorshift32();\n   \
    \      uint64_t low  = xorshift32();\n         return (high << 32) | low;\n  \
    \  }\n    // [0, x)\n    inline static uint64_t randrange(uint64_t x) { return\
    \ xorshift64() % x; }\n    // [x, y)\n    inline static uint64_t randrange(uint64_t\
    \ x, uint64_t y) { return randrange(y - x) + x; }\n    // [0.0, 1.0)\n    inline\
    \ static double random() { \n        return (xorshift64() + 0.5) * (1.0 / (double)ULLONG_MAX);\
    \ \n    }\n};\nu64 zobrist[N][N][3];\nvoid init_zobrist() {\n    for (int i =\
    \ 0; i < N; i++) {\n        for (int j = 0; j < N; j++) {\n            for (int\
    \ k = 0; k < 3; k++) {\n                zobrist[i][j][k] = Random::randrange((1ULL\
    \ << 63)-1);\n            }\n        }\n    }\n}\n//#####################################################\n\
    \n// \u72B6\u614B #############################################\nstruct Move {\n\
    \  char d; int p;\n};\n\nstruct xy {\n  int x, y;\n};\n\nstruct State {\n  int\
    \ score;\n  int depth;\n  Move move_history[beam_depth];\n\n  State() : score(0),\
    \ depth(0) {};\n};\n\n// \u30BD\u30FC\u30C8\u95A2\u6570########################################\n\
    // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\nbool comp_max(const\
    \ State &a1, const State &a2){\n    return a1.score > a2.score;\n}\n// \u30B9\u30B3\
    \u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\nbool comp_min(const State &a1, const\
    \ State &a2){\n    return a1.score < a2.score;\n}\n//#####################################################\n\
    \n// \u8A55\u4FA1\u95A2\u6570########################################\n// \u5C0F\
    \u3055\u3044\u65B9\u304C\u3044\u3044\n// \u5404\u9B3C\u306E\u5916\u5468\u304B\u3089\
    \u306E\u8DDD\u96E2\u306E\u5408\u8A08\u3092\u8A55\u4FA1\u5024\u3068\u3059\u308B\
    \n// \u305F\u3060\u3057\u3001\u6700\u3082\u8FD1\u3044\u5916\u5468\u307E\u3067\u306B\
    \u798F\u304C\u3044\u308B\u306A\u3089 penalty \u3092\u52A0\u7B97\u3059\u308B\n\
    // \u798F\u304C\u843D\u3061\u308B\u76E4\u9762\u306F\u8A31\u3055\u306A\u3044\u3088\
    \u3046\u306B inf \u30DA\u30CA\u30EB\u30C6\u30A3\u30FC\u3092\u4E0E\u3048\u308B\n\
    // \u5012\u3057\u305F\u9B3C\u306E\u6570 * bonus \u3092\u6E1B\u7B97\u3059\u308B\
    \nint calc_eval(const State &s){\n  int eval = 0;\n\n  return eval;\n}\n//#####################################################\n\
    \n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State apply_move(const State &s, Move &mv){\n  State nex = s;\n  // \u72B6\u614B\
    \u9077\u79FB\n  return nex;\n}\n//#####################################################\n\
    \n// \u76E4\u9762\u30CF\u30C3\u30B7\u30E5########################################\n\
    inline int pieceIndex(int c) {\n    // \u76E4\u9762\u306E\u72B6\u614B\u306B\u5408\
    \u308F\u305B\u3066\u5BFE\u5FDC\u4ED8\u3051\u308B\n    if (c == -1) return 0; //\
    \ 'o'\n    else if (c == -2) return 1; // '.'\n    else return 2; // 'x'\n}\n\
    u64 board_to_u64(const int (&board)[N][N]) {\n    u64 hash = 0;\n    rep(i, N)\
    \ {\n        rep(j, N) {\n            int idx = pieceIndex(board[i][j]);\n   \
    \         hash ^= zobrist[i][j][idx];\n        }\n    }\n    return hash;\n}\n\
    \n//#####################################################\n\nauto beam_search(State\
    \ &init_state, int beam_width, int beam_depth){\n    vector<State> now;\n    now.emplace_back(init_state);\n\
    \    vector<State> next;\n    visited.emplace(board_to_u64(init_state.board));\n\
    \n    // \u9077\u79FB\u5019\u88DC ########################################\n \
    \   vector<Move> possible_moves;\n    //#################################################\n\
    \n    for (int i=0; i<beam_depth; i++){\n        bool sorted = false;\n      \
    \  for (auto &s : now){\n            // \u72B6\u614B\u3092\u9077\u79FB\u3055\u305B\
    \u308B\n            for (auto &mv: possible_moves){\n                // \u72B6\
    \u614B\u3092\u5909\u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\u5024\
    \u3092\u8A08\u7B97########\n                // \u3053\u308C\u305F\u3076\u3093\u5B9F\
    \u969B\u306B\u76E4\u9762\u3092\u52D5\u304B\u3055\u305A\u306B\u8A55\u4FA1\u5024\
    \u3060\u3051\u8A08\u7B97\u3067\u304D\u305F\u307B\u3046\u304C\u9AD8\u901F\u5316\
    \u3067\u304D\u308B\n                auto nex_s = apply_move(s, mv);\n        \
    \        if (nex_s.score == INF) continue;\n                //###########################################\n\
    \n                // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D, \u30BD\
    \u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\u306E\u8A55\u4FA1\u5024\
    \u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\u307F\u9077\u79FB\n   \
    \             //if (sorted && nex_s.score <= next[beam_width-1].score) continue;\n\
    \                // \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D, \u30BD\
    \u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5927\u306E\u8A55\u4FA1\u5024\
    \u3088\u308A\u3082\u5C0F\u3055\u3044\u5834\u5408\u306E\u307F\u9077\u79FB\n   \
    \             if (sorted && nex_s.score >= next[beam_width-1].score) continue;\n\
    \n                // \u65E2\u306B\u8A2A\u308C\u305F\u72B6\u614B\u306F\u30B9\u30AD\
    \u30C3\u30D7\n                u64 board_hash = board_to_u64(nex_s.board);\n  \
    \              if (visited.count(board_hash)) continue;\n                visited.emplace(board_hash);\n\
    \                next.emplace_back(nex_s);\n\n                if (nex_s.score\
    \ <= finish){\n                    return nex_s;\n                }\n\n      \
    \          if (next.size() >= 2*beam_width){\n                    sort(next.begin(),\
    \ next.end(), comp_min);\n                    next.resize(beam_width);\n     \
    \               sorted = true;\n                }\n            }\n        }\n\
    \        if (next.empty()) break;\n        sort(next.begin(), next.end(), comp_min);\n\
    \        next.resize(beam_width);\n        swap(now, next);\n        next.clear();\n\
    \    }\n  return now[0];\n}\n\nint main() {\n  ios::sync_with_stdio(false); cin.tie(0);\n\
    \  init_zobrist();\n\n  auto best_move = beam_search(init_state, beam_width, beam_depth);\n\
    \  for (int i=0; i<best_move.depth; i++){\n    cout << best_move.move_history[i].d\
    \ << \" \" << best_move.move_history[i].p << endl;\n  }\n}"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/beam_search.cpp
  requiredBy: []
  timestamp: '2025-04-13 13:24:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/beam_search.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/beam_search.cpp
- /library/heuristic_library/cpp/beam_search.cpp.html
title: heuristic_library/cpp/beam_search.cpp
---
