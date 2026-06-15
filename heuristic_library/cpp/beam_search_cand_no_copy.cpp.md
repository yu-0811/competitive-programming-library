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
  bundledCode: "#line 1 \"heuristic_library/cpp/beam_search_cand_no_copy.cpp\"\n///\
    \ \u5019\u88DC\u6BB5\u968E\u3067\u306F\u72B6\u614B\u3092\u30B3\u30D4\u30FC\u3057\
    \u306A\u3044\u5B9F\u88C5\n/// \u72B6\u614B\u9077\u79FB\u304C State \u306E\u30B3\
    \u30D4\u30FC\u3088\u308A\u9AD8\u901F\u306A\u3068\u304D\u306B\u4F7F\u3046\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\n#pragma GCC target(\"avx2\")\n#pragma\
    \ GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nusing u64 =\
    \ unsigned long long;\nconst int INF = 10000000;\n\nusing HashType = u64;\nusing\
    \ ScoreType = int;\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\nTimer timer;\n\n#ifndef ONLINE_JUDGE\n    constexpr\
    \ int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit = 1987;\n\
    #endif\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF\nconst int beam_width = 380;\n\n//\
    \ \u30CF\u30C3\u30B7\u30E5\u7528\u306E\u30C6\u30FC\u30D6\u30EB\nstruct FixedHashSet\
    \ {\n    static constexpr int LOG_CAP = 20;\n    static constexpr int CAP = 1\
    \ << LOG_CAP;\n    static constexpr int MASK = CAP - 1;\n\n    array<u64, CAP>\
    \ keys{};\n    array<uint16_t, CAP> stamps{};\n    uint16_t cur_stamp = 1;\n\n\
    \    static u64 mix(u64 x) {\n        x += 0x9e3779b97f4a7c15ULL;\n        x =\
    \ (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;\n        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;\n\
    \        return x ^ (x >> 31);\n    }\n\n    void clear() {\n        ++cur_stamp;\n\
    \        if (cur_stamp == 0) {\n            stamps.fill(0);\n            cur_stamp\
    \ = 1;\n        }\n    }\n\n    bool contains_or_insert(u64 key) {\n        int\
    \ slot = static_cast<int>(mix(key) & MASK);\n        while (stamps[slot] == cur_stamp)\
    \ {\n            if (keys[slot] == key) return true;\n            slot = (slot\
    \ + 1) & MASK;\n        }\n        stamps[slot] = cur_stamp;\n        keys[slot]\
    \ = key;\n        return false;\n    }\n};\n\nFixedHashSet visited;\n\n// Zobrist\
    \ Hash\nclass Random {\n    inline static u64 state = 88172645463325252ULL;\n\n\
    public:\n    inline static uint64_t xorshift64() {\n        u64 x = state;\n \
    \       x ^= x << 7;\n        x ^= x >> 9;\n        return state = x;\n    }\n\
    };\n\nstruct ZobristHash2D {\n    int H = 0;\n    int W = 0;\n    int kinds =\
    \ 0;\n    vector<u64> table;\n\n    void init(int h, int w, int kind_count) {\n\
    \        H = h;\n        W = w;\n        kinds = kind_count;\n        table.resize(static_cast<size_t>(H)\
    \ * W * kinds);\n        for (u64& x : table) x = Random::xorshift64();\n    }\n\
    \n    inline u64 value(int r, int c, int kind) const {\n        return table[(r\
    \ * W + c) * kinds + kind];\n    }\n\n    inline void apply_change(u64& hash,\
    \ int r, int c, int before_kind, int after_kind) const {\n        hash ^= value(r,\
    \ c, before_kind);\n        hash ^= value(r, c, after_kind);\n    }\n\n    template\
    \ <class Board, class Indexer>\n    u64 build(const Board& board, Indexer&& to_kind)\
    \ const {\n        u64 hash = 0;\n        for (int i = 0; i < H; i++) {\n    \
    \        for (int j = 0; j < W; j++) {\n                hash ^= value(i, j, to_kind(board[i][j]));\n\
    \            }\n        }\n        return hash;\n    }\n};\n\n/// \u72B6\u614B\
    \ \n// State \u3068 Candidate \u306F\u8EFD\u3044\u65B9\u304C\u3044\u3044\nstruct\
    \ Action { // State \u306B\u5BFE\u3059\u308B\u9077\u79FB\u64CD\u4F5C\n    // TODO\n\
    };\n\nstruct State { // \u30D3\u30FC\u30E0\u306B\u5165\u308C\u308B\u72B6\u614B\
    \n    ScoreType score = 0;\n    HashType hash = 0; // \u5DEE\u5206\u66F4\u65B0\
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n    // TODO: // \u554F\
    \u984C\u7279\u6709\u306E\u72B6\u614B\u3092\u5165\u308C\u308B\n\n    // \u72B6\u614B\
    \u306B action \u3092\u9069\u7528\u3059\u308B\n    // \u7D42\u4E86\u72B6\u614B\u306B\
    \u306A\u308B\u306A\u3089 true\n    // \u5019\u88DC\u304C\u63A1\u7528\u3055\u308C\
    \u3066\u304B\u3089\u5B9F\u884C\u3059\u308B\n    bool do_(const Action& action)\
    \ {\n        (void)action;\n    } \n};\n\n// TODO: \u30B9\u30B3\u30A2\u306E\u5DEE\
    \u5206\u66F4\u65B0\uFF08\u5C0F\u3055\u3044\u65B9\u304C\u3044\u3044\uFF09\nScoreType\
    \ calc_eval(const State& s, const Action& action) {\n    (void)action;\n}\n\n\
    // TODO: \u30CF\u30C3\u30B7\u30E5\u306E\u5DEE\u5206\u66F4\u65B0\nHashType calc_hash(const\
    \ State& s, const Action& action) {\n    (void)action;\n}\n\n// \u2193\u3053\u3053\
    \u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\u3066\u3044\u3044\nstruct\
    \ Candidate { // \u63A1\u7528\u524D\u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx\
    \ = -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int score = INF;\n    u64 hash = 0;\n\n    Candidate() = default;\n\n   \
    \ Candidate(int parent_idx_, Action action_, int score_, u64 hash_)\n        :\
    \ parent_idx(parent_idx_), action(action_), score(score_), hash(hash_) {}\n};\n\
    \nstruct FinishCandidate { // \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx\
    \ = -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int score = INF;\n};\n\nstruct WorkSpace {\n    State s;\n    vector<Action>\
    \ actions;\n};\n\nstruct BeamNode {\n    State state;\n    int parent = -1;\n\
    \    Action last_action{};\n};\n\nstruct BeamSearchResult {\n    State final_state;\n\
    \    vector<Action> move_history;\n};\n// \u2191\u3053\u3053\u307E\u3067\n\n//\
    \ \u9077\u79FB\u64CD\u4F5C\u5019\u88DC\u751F\u6210\n// actions \u306B s \u306B\
    \u5BFE\u3057\u3066\u53EF\u80FD\u306A\u64CD\u4F5C\u3092\u5165\u308C\u308B\nvoid\
    \ generate_possible_actions(const State& s, vector<Action>& actions) {\n    (void)s;\n\
    \    (void)actions;\n}\n\n// \u64CD\u4F5C\u5C65\u6B74\u5FA9\u5143\u95A2\u6570\n\
    vector<Action> restore_move_history(const vector<BeamNode>& nodes, int node_idx)\
    \ {\n    vector<Action> history;\n    while (node_idx != -1 && nodes[node_idx].parent\
    \ != -1) {\n        history.emplace_back(nodes[node_idx].last_action);\n     \
    \   node_idx = nodes[node_idx].parent;\n    }\n    reverse(history.begin(), history.end());\n\
    \    return history;\n}\n\nBeamSearchResult run_beam_search(State& init_state,\
    \ int beam_width) {\n    vector<BeamNode> nodes; // \u30D3\u30FC\u30E0\u306E\u5168\
    \u30CE\u30FC\u30C9\u3092\u5165\u308C\u308B\n    vector<int> now; // nodes \u306E\
    \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    vector<int> next;\n\n    nodes.emplace_back(BeamNode{init_state,\
    \ -1, Action{}});\n    now.emplace_back(0);\n\n    vector<Candidate> candidates;\
    \ // \u9077\u79FB\u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9 + \u64CD\u4F5C\
    \ + \u8A55\u4FA1\u5024\uFF09\n    WorkSpace ws;\n    FinishCandidate best_cand;\n\
    \n    now.reserve(beam_width);\n    next.reserve(beam_width);\n    // \u78BA\u4FDD\
    \u9818\u57DF\u306F\u554F\u984C\u3054\u3068\u306B\u8ABF\u6574\u3059\u308B\n   \
    \ nodes.reserve(2 * beam_width * 100);\n    candidates.reserve(4 * beam_width);\n\
    \n    while (!now.empty() && timer.get_ms() < time_limit) {\n        next.clear();\n\
    \        candidates.clear();\n        visited.clear();\n\n        // \u9077\u79FB\
    \u5148\u3092\u5217\u6319\u3059\u308B\n        for (int beam_idx = 0; beam_idx\
    \ < (int)now.size(); beam_idx++) {\n            const int parent_idx = now[beam_idx];\n\
    \            const State& parent_state = nodes[parent_idx].state;\n          \
    \  ws.actions.clear();\n            generate_possible_actions(parent_state, ws.actions);\n\
    \            for (const auto& action : ws.actions) {\n                ws.s = parent_state;\n\
    \                Candidate cand(parent_idx, action, calc_eval(ws.s, action), calc_hash(ws.s,\
    \ action));\n                candidates.emplace_back(cand);\n            }\n \
    \       }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\u53D6\u308B\
    \n        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const\
    \ Candidate& b) {\n            return a.score < b.score;\n        });\n\n    \
    \    for (const auto& cand : candidates) {\n            ws.s = nodes[cand.parent_idx].state;\n\
    \            ws.s.score = cand.score;\n            ws.s.hash = cand.hash;\n  \
    \          bool is_finished = ws.s.do_(cand.action);\n            if (is_finished)\
    \ {\n                if (cand.score < best_cand.score) {\n                   \
    \ best_cand = FinishCandidate{cand.parent_idx, cand.action, cand.score};\n   \
    \             }\n                continue;\n            }\n            // \u91CD\
    \u8907\u9664\u53BB\n            if (visited.contains_or_insert(cand.hash)) continue;\n\
    \            const int node_idx = static_cast<int>(nodes.size());\n          \
    \  nodes.emplace_back(BeamNode{ws.s, cand.parent_idx, cand.action});\n       \
    \     next.emplace_back(node_idx);\n            if ((int)next.size() >= beam_width)\
    \ break;\n        }\n        if (next.empty()) break;\n        swap(now, next);\n\
    \    }\n\n    BeamSearchResult result;\n    assert(best_cand.parent_idx != -1);\n\
    \n    result.final_state = nodes[best_cand.parent_idx].state;\n    result.final_state.do_(best_cand.action);\n\
    \    result.move_history = restore_move_history(nodes, best_cand.parent_idx);\n\
    \    result.move_history.emplace_back(best_cand.action);\n    return result;\n\
    }\n\nint main() {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n    timer\
    \ = Timer();\n\n    State init_state;\n    BeamSearchResult result = run_beam_search(init_state,\
    \ beam_width);\n\n    return 0;\n}\n"
  code: "/// \u5019\u88DC\u6BB5\u968E\u3067\u306F\u72B6\u614B\u3092\u30B3\u30D4\u30FC\
    \u3057\u306A\u3044\u5B9F\u88C5\n/// \u72B6\u614B\u9077\u79FB\u304C State \u306E\
    \u30B3\u30D4\u30FC\u3088\u308A\u9AD8\u901F\u306A\u3068\u304D\u306B\u4F7F\u3046\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\n#pragma GCC target(\"avx2\"\
    )\n#pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nusing\
    \ u64 = unsigned long long;\nconst int INF = 10000000;\n\nusing HashType = u64;\n\
    using ScoreType = int;\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\nTimer timer;\n\n#ifndef ONLINE_JUDGE\n    constexpr\
    \ int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit = 1987;\n\
    #endif\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF\nconst int beam_width = 380;\n\n//\
    \ \u30CF\u30C3\u30B7\u30E5\u7528\u306E\u30C6\u30FC\u30D6\u30EB\nstruct FixedHashSet\
    \ {\n    static constexpr int LOG_CAP = 20;\n    static constexpr int CAP = 1\
    \ << LOG_CAP;\n    static constexpr int MASK = CAP - 1;\n\n    array<u64, CAP>\
    \ keys{};\n    array<uint16_t, CAP> stamps{};\n    uint16_t cur_stamp = 1;\n\n\
    \    static u64 mix(u64 x) {\n        x += 0x9e3779b97f4a7c15ULL;\n        x =\
    \ (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;\n        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;\n\
    \        return x ^ (x >> 31);\n    }\n\n    void clear() {\n        ++cur_stamp;\n\
    \        if (cur_stamp == 0) {\n            stamps.fill(0);\n            cur_stamp\
    \ = 1;\n        }\n    }\n\n    bool contains_or_insert(u64 key) {\n        int\
    \ slot = static_cast<int>(mix(key) & MASK);\n        while (stamps[slot] == cur_stamp)\
    \ {\n            if (keys[slot] == key) return true;\n            slot = (slot\
    \ + 1) & MASK;\n        }\n        stamps[slot] = cur_stamp;\n        keys[slot]\
    \ = key;\n        return false;\n    }\n};\n\nFixedHashSet visited;\n\n// Zobrist\
    \ Hash\nclass Random {\n    inline static u64 state = 88172645463325252ULL;\n\n\
    public:\n    inline static uint64_t xorshift64() {\n        u64 x = state;\n \
    \       x ^= x << 7;\n        x ^= x >> 9;\n        return state = x;\n    }\n\
    };\n\nstruct ZobristHash2D {\n    int H = 0;\n    int W = 0;\n    int kinds =\
    \ 0;\n    vector<u64> table;\n\n    void init(int h, int w, int kind_count) {\n\
    \        H = h;\n        W = w;\n        kinds = kind_count;\n        table.resize(static_cast<size_t>(H)\
    \ * W * kinds);\n        for (u64& x : table) x = Random::xorshift64();\n    }\n\
    \n    inline u64 value(int r, int c, int kind) const {\n        return table[(r\
    \ * W + c) * kinds + kind];\n    }\n\n    inline void apply_change(u64& hash,\
    \ int r, int c, int before_kind, int after_kind) const {\n        hash ^= value(r,\
    \ c, before_kind);\n        hash ^= value(r, c, after_kind);\n    }\n\n    template\
    \ <class Board, class Indexer>\n    u64 build(const Board& board, Indexer&& to_kind)\
    \ const {\n        u64 hash = 0;\n        for (int i = 0; i < H; i++) {\n    \
    \        for (int j = 0; j < W; j++) {\n                hash ^= value(i, j, to_kind(board[i][j]));\n\
    \            }\n        }\n        return hash;\n    }\n};\n\n/// \u72B6\u614B\
    \ \n// State \u3068 Candidate \u306F\u8EFD\u3044\u65B9\u304C\u3044\u3044\nstruct\
    \ Action { // State \u306B\u5BFE\u3059\u308B\u9077\u79FB\u64CD\u4F5C\n    // TODO\n\
    };\n\nstruct State { // \u30D3\u30FC\u30E0\u306B\u5165\u308C\u308B\u72B6\u614B\
    \n    ScoreType score = 0;\n    HashType hash = 0; // \u5DEE\u5206\u66F4\u65B0\
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n    // TODO: // \u554F\
    \u984C\u7279\u6709\u306E\u72B6\u614B\u3092\u5165\u308C\u308B\n\n    // \u72B6\u614B\
    \u306B action \u3092\u9069\u7528\u3059\u308B\n    // \u7D42\u4E86\u72B6\u614B\u306B\
    \u306A\u308B\u306A\u3089 true\n    // \u5019\u88DC\u304C\u63A1\u7528\u3055\u308C\
    \u3066\u304B\u3089\u5B9F\u884C\u3059\u308B\n    bool do_(const Action& action)\
    \ {\n        (void)action;\n    } \n};\n\n// TODO: \u30B9\u30B3\u30A2\u306E\u5DEE\
    \u5206\u66F4\u65B0\uFF08\u5C0F\u3055\u3044\u65B9\u304C\u3044\u3044\uFF09\nScoreType\
    \ calc_eval(const State& s, const Action& action) {\n    (void)action;\n}\n\n\
    // TODO: \u30CF\u30C3\u30B7\u30E5\u306E\u5DEE\u5206\u66F4\u65B0\nHashType calc_hash(const\
    \ State& s, const Action& action) {\n    (void)action;\n}\n\n// \u2193\u3053\u3053\
    \u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\u3066\u3044\u3044\nstruct\
    \ Candidate { // \u63A1\u7528\u524D\u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx\
    \ = -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int score = INF;\n    u64 hash = 0;\n\n    Candidate() = default;\n\n   \
    \ Candidate(int parent_idx_, Action action_, int score_, u64 hash_)\n        :\
    \ parent_idx(parent_idx_), action(action_), score(score_), hash(hash_) {}\n};\n\
    \nstruct FinishCandidate { // \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx\
    \ = -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int score = INF;\n};\n\nstruct WorkSpace {\n    State s;\n    vector<Action>\
    \ actions;\n};\n\nstruct BeamNode {\n    State state;\n    int parent = -1;\n\
    \    Action last_action{};\n};\n\nstruct BeamSearchResult {\n    State final_state;\n\
    \    vector<Action> move_history;\n};\n// \u2191\u3053\u3053\u307E\u3067\n\n//\
    \ \u9077\u79FB\u64CD\u4F5C\u5019\u88DC\u751F\u6210\n// actions \u306B s \u306B\
    \u5BFE\u3057\u3066\u53EF\u80FD\u306A\u64CD\u4F5C\u3092\u5165\u308C\u308B\nvoid\
    \ generate_possible_actions(const State& s, vector<Action>& actions) {\n    (void)s;\n\
    \    (void)actions;\n}\n\n// \u64CD\u4F5C\u5C65\u6B74\u5FA9\u5143\u95A2\u6570\n\
    vector<Action> restore_move_history(const vector<BeamNode>& nodes, int node_idx)\
    \ {\n    vector<Action> history;\n    while (node_idx != -1 && nodes[node_idx].parent\
    \ != -1) {\n        history.emplace_back(nodes[node_idx].last_action);\n     \
    \   node_idx = nodes[node_idx].parent;\n    }\n    reverse(history.begin(), history.end());\n\
    \    return history;\n}\n\nBeamSearchResult run_beam_search(State& init_state,\
    \ int beam_width) {\n    vector<BeamNode> nodes; // \u30D3\u30FC\u30E0\u306E\u5168\
    \u30CE\u30FC\u30C9\u3092\u5165\u308C\u308B\n    vector<int> now; // nodes \u306E\
    \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    vector<int> next;\n\n    nodes.emplace_back(BeamNode{init_state,\
    \ -1, Action{}});\n    now.emplace_back(0);\n\n    vector<Candidate> candidates;\
    \ // \u9077\u79FB\u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9 + \u64CD\u4F5C\
    \ + \u8A55\u4FA1\u5024\uFF09\n    WorkSpace ws;\n    FinishCandidate best_cand;\n\
    \n    now.reserve(beam_width);\n    next.reserve(beam_width);\n    // \u78BA\u4FDD\
    \u9818\u57DF\u306F\u554F\u984C\u3054\u3068\u306B\u8ABF\u6574\u3059\u308B\n   \
    \ nodes.reserve(2 * beam_width * 100);\n    candidates.reserve(4 * beam_width);\n\
    \n    while (!now.empty() && timer.get_ms() < time_limit) {\n        next.clear();\n\
    \        candidates.clear();\n        visited.clear();\n\n        // \u9077\u79FB\
    \u5148\u3092\u5217\u6319\u3059\u308B\n        for (int beam_idx = 0; beam_idx\
    \ < (int)now.size(); beam_idx++) {\n            const int parent_idx = now[beam_idx];\n\
    \            const State& parent_state = nodes[parent_idx].state;\n          \
    \  ws.actions.clear();\n            generate_possible_actions(parent_state, ws.actions);\n\
    \            for (const auto& action : ws.actions) {\n                ws.s = parent_state;\n\
    \                Candidate cand(parent_idx, action, calc_eval(ws.s, action), calc_hash(ws.s,\
    \ action));\n                candidates.emplace_back(cand);\n            }\n \
    \       }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\u53D6\u308B\
    \n        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const\
    \ Candidate& b) {\n            return a.score < b.score;\n        });\n\n    \
    \    for (const auto& cand : candidates) {\n            ws.s = nodes[cand.parent_idx].state;\n\
    \            ws.s.score = cand.score;\n            ws.s.hash = cand.hash;\n  \
    \          bool is_finished = ws.s.do_(cand.action);\n            if (is_finished)\
    \ {\n                if (cand.score < best_cand.score) {\n                   \
    \ best_cand = FinishCandidate{cand.parent_idx, cand.action, cand.score};\n   \
    \             }\n                continue;\n            }\n            // \u91CD\
    \u8907\u9664\u53BB\n            if (visited.contains_or_insert(cand.hash)) continue;\n\
    \            const int node_idx = static_cast<int>(nodes.size());\n          \
    \  nodes.emplace_back(BeamNode{ws.s, cand.parent_idx, cand.action});\n       \
    \     next.emplace_back(node_idx);\n            if ((int)next.size() >= beam_width)\
    \ break;\n        }\n        if (next.empty()) break;\n        swap(now, next);\n\
    \    }\n\n    BeamSearchResult result;\n    assert(best_cand.parent_idx != -1);\n\
    \n    result.final_state = nodes[best_cand.parent_idx].state;\n    result.final_state.do_(best_cand.action);\n\
    \    result.move_history = restore_move_history(nodes, best_cand.parent_idx);\n\
    \    result.move_history.emplace_back(best_cand.action);\n    return result;\n\
    }\n\nint main() {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n    timer\
    \ = Timer();\n\n    State init_state;\n    BeamSearchResult result = run_beam_search(init_state,\
    \ beam_width);\n\n    return 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/beam_search_cand_no_copy.cpp
  requiredBy: []
  timestamp: '2026-06-15 14:58:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/beam_search_cand_no_copy.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/beam_search_cand_no_copy.cpp
- /library/heuristic_library/cpp/beam_search_cand_no_copy.cpp.html
title: heuristic_library/cpp/beam_search_cand_no_copy.cpp
---
