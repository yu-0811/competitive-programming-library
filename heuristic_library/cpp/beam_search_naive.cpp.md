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
  bundledCode: "#line 1 \"heuristic_library/cpp/beam_search_naive.cpp\"\n/// apply_move\
    \ \u3067\u72B6\u614B\u3092\u30B3\u30D4\u30FC\u3059\u308B\u5B9F\u88C5\n/// apply_move\
    \ \u306E\u51E6\u7406\u304C State \u306E\u30B3\u30D4\u30FC\u3068\u540C\u7A0B\u5EA6\
    \u306B\u91CD\u3044\u3068\u304D\u306B\u4F7F\u3046\n#include <bits/stdc++.h>\nusing\
    \ namespace std;\n\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"O3\"\
    )\n#pragma GCC optimize(\"unroll-loops\")\n\nusing u64 = unsigned long long;\n\
    const int INF = 10000000;\n\nu64 calc_hash(const State& s);\n\nclass Timer {\n\
    \    chrono::time_point<chrono::steady_clock> start;\npublic:\n    Timer() : start(chrono::steady_clock::now())\
    \ {}\n    unsigned short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\
    \n        auto now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
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
    \ Action { // State \u306B\u5BFE\u3059\u308B\u9077\u79FB\u64CD\u4F5C\n    char\
    \ d;\n    int p;\n};\n\nstruct State { // \u30D3\u30FC\u30E0\u306B\u5165\u308C\
    \u308B\u72B6\u614B\n    // \u554F\u984C\u7279\u6709\u306E\u72B6\u614B\u3092\u5165\
    \u308C\u308B\n    int score = 0;\n    u64 hash = 0; // \u5DEE\u5206\u66F4\u65B0\
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n};\n\nstruct Candidate\
    \ { // \u63A1\u7528\u524D\u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx =\
    \ -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int appliedstate_idx = -1;\n    int score = INF;\n    bool is_finished =\
    \ false;\n    u64 hash = 0;\n\n    Candidate() = default;\n\n    Candidate(int\
    \ parent_idx_, Action action_, int appliedstate_idx_, int score_, bool is_finished_,\
    \ u64 hash_)\n        : parent_idx(parent_idx_), action(action_), appliedstate_idx(appliedstate_idx_),\
    \ is_finished(is_finished_), score(score_), hash(hash_) {}\n};\n\nstruct FinishCandidate\
    \ { // \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\
    \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n\
    };\n\n// \u2193\u3053\u3053\u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\
    \u3066\u3044\u3044\nstruct WorkSpace {\n    State s;\n    vector<Action> actions;\n\
    };\n\nstruct BeamNode {\n    State state;\n    int parent = -1;\n    Action last_action{};\n\
    };\n\nstruct BeamSearchResult {\n    State final_state;\n    vector<Action> move_history;\n\
    };\n// \u2191\u3053\u3053\u307E\u3067\n\n// \u8A55\u4FA1\u95A2\u6570 \u5C0F\u3055\
    \u3044\u65B9\u304C\u826F\u3044\nint calc_eval(const State& s) {\n    int eval\
    \ = 0;\n    (void)s;\n    return eval;\n}\n\n// \u72B6\u614B\u9077\u79FB\u95A2\
    \u6570\n// applied_state \u306B\u300Cparent \u306B action \u3092\u9069\u7528\u3057\
    \u305F\u7D50\u679C\u306E\u72B6\u614B\u300D\u3092\u66F8\u304D\u8FBC\u3080\u3002\
    \n// applied_state.score \u3068 applied_state.hash \u3082\u66F4\u65B0\u3059\u308B\
    \n// \u623B\u308A\u5024\uFF1A\u7D42\u4E86\u72B6\u614B\u306B\u306A\u308B\u306A\u3089\
    \ true\nbool apply_move(const State& parent, const Action& action, State& applied_state)\
    \ {\n    applied_state = parent;\n\n    // \u72B6\u614B\u9077\u79FB\n    applied_state.score\
    \ = calc_eval(applied_state);\n    applied_state.hash = calc_hash(applied_state);\n\
    \n    return false;\n}\n\n// \u9077\u79FB\u64CD\u4F5C\u5019\u88DC\u751F\u6210\n\
    // actions \u306B s \u306B\u5BFE\u3057\u3066\u53EF\u80FD\u306A\u64CD\u4F5C\u3092\
    \u5165\u308C\u308B\nvoid generate_possible_actions(const State& s, vector<Action>&\
    \ actions) {\n    \n}\n\n// \u30CF\u30C3\u30B7\u30E5\nu64 calc_hash(const State&\
    \ s) {\n\n}\n\n// \u64CD\u4F5C\u5C65\u6B74\u5FA9\u5143\u95A2\u6570\nvector<Action>\
    \ restore_move_history(const vector<BeamNode>& nodes, int node_idx) {\n    vector<Action>\
    \ history;\n    while (node_idx != -1 && nodes[node_idx].parent != -1) {\n   \
    \     history.emplace_back(nodes[node_idx].last_action);\n        node_idx = nodes[node_idx].parent;\n\
    \    }\n    reverse(history.begin(), history.end());\n    return history;\n}\n\
    \nBeamSearchResult run_beam_search(State& init_state, int beam_width) {\n    vector<BeamNode>\
    \ nodes; // \u30D3\u30FC\u30E0\u306E\u5168\u30CE\u30FC\u30C9\u3092\u5165\u308C\
    \u308B\n    vector<int> now; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    \n    vector<int> next;\n\n    nodes.emplace_back(BeamNode{init_state, -1, Action{}});\n\
    \    now.emplace_back(0);\n\n    vector<Candidate> candidates; // \u9077\u79FB\
    \u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9 + \u64CD\u4F5C + \u9069\u7528\
    \u6E08\u307F\u72B6\u614B\u3078\u306E\u53C2\u7167\uFF09\n    vector<State> appliedstates;\
    \  // \u5019\u88DC\u306E\u72B6\u614B\u672C\u4F53\u3002\u63A1\u7528\u3055\u308C\
    \u308B\u307E\u3067 nodes \u306B\u306F\u5165\u308C\u306A\u3044\n    WorkSpace ws;\n\
    \    FinishCandidate best_cand;\n\n    // \u78BA\u4FDD\u9818\u57DF\u306F\u554F\
    \u984C\u3054\u3068\u306B\u8ABF\u6574\u3059\u308B\n    nodes.reserve(1 + 2 * beam_width\
    \ * 100);\n    now.reserve(beam_width);\n    next.reserve(beam_width);\n    candidates.reserve(2\
    \ * beam_width);\n    appliedstates.reserve(2 * beam_width);\n\n    while (!now.empty()\
    \ && timer.get_ms() < time_limit) {\n        next.clear();\n        candidates.clear();\n\
    \        appliedstates.clear();\n        visited.clear();\n\n        // \u9077\
    \u79FB\u5148\u3092\u5217\u6319\u3059\u308B\n        for (int beam_idx = 0; beam_idx\
    \ < (int)now.size(); beam_idx++) {\n            const int parent_idx = now[beam_idx];\n\
    \            const State& parent_state = nodes[parent_idx].state;\n          \
    \  ws.actions.clear();\n            generate_possible_actions(parent_state, ws.actions);\n\
    \            for (const auto& action : ws.actions) {\n                bool is_finished\
    \ = apply_move(parent_state, action, ws.s);\n                const int appliedstate_idx\
    \ = static_cast<int>(appliedstates.size());\n                appliedstates.emplace_back(ws.s);\n\
    \                Candidate cand(parent_idx, action, appliedstate_idx, ws.s.score,\
    \ is_finished, ws.s.hash);\n                candidates.emplace_back(cand);\n \
    \           }\n        }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\
    \u53D6\u308B\n        sort(candidates.begin(), candidates.end(), [](const Candidate&\
    \ a, const Candidate& b) {\n            return a.score < b.score;\n        });\n\
    \n        for (const auto& cand : candidates) {\n            if (cand.is_finished)\
    \ {\n                if (cand.score < best_cand.score) {\n                   \
    \ best_cand = FinishCandidate{cand.parent_idx, cand.action, cand.score};\n   \
    \             }\n                continue;\n            }\n            if (visited.contains_or_insert(cand.hash))\
    \ continue;\n\n            const int node_idx = static_cast<int>(nodes.size());\n\
    \            nodes.emplace_back(BeamNode{appliedstates[cand.appliedstate_idx],\
    \ cand.parent_idx, cand.action});\n            next.emplace_back(node_idx);\n\
    \            if ((int)next.size() >= beam_width) break;\n        }\n        if\
    \ (next.empty()) break;\n        swap(now, next);\n    }\n\n    assert(best_cand.parent_idx\
    \ != -1);\n    BeamSearchResult result;\n    result.final_state = nodes[best_cand.parent_idx].state;\n\
    \    [[maybe_unused]] const bool ok = apply_move(result.final_state, best_cand.action,\
    \ result.final_state);\n    assert(ok);\n    result.move_history = restore_move_history(nodes,\
    \ best_cand.parent_idx);\n    result.move_history.emplace_back(best_cand.action);\n\
    \    return result;\n}\n\nint main() {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n\
    \    timer = Timer();\n\n    State init_state;\n    BeamSearchResult result =\
    \ run_beam_search(init_state, beam_width);\n\n    return 0;\n}\n"
  code: "/// apply_move \u3067\u72B6\u614B\u3092\u30B3\u30D4\u30FC\u3059\u308B\u5B9F\
    \u88C5\n/// apply_move \u306E\u51E6\u7406\u304C State \u306E\u30B3\u30D4\u30FC\
    \u3068\u540C\u7A0B\u5EA6\u306B\u91CD\u3044\u3068\u304D\u306B\u4F7F\u3046\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\n#pragma GCC target(\"avx2\")\n#pragma\
    \ GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nusing u64 =\
    \ unsigned long long;\nconst int INF = 10000000;\n\nu64 calc_hash(const State&\
    \ s);\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock> start;\n\
    public:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned short\
    \ get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time\
    \ = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
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
    \ Action { // State \u306B\u5BFE\u3059\u308B\u9077\u79FB\u64CD\u4F5C\n    char\
    \ d;\n    int p;\n};\n\nstruct State { // \u30D3\u30FC\u30E0\u306B\u5165\u308C\
    \u308B\u72B6\u614B\n    // \u554F\u984C\u7279\u6709\u306E\u72B6\u614B\u3092\u5165\
    \u308C\u308B\n    int score = 0;\n    u64 hash = 0; // \u5DEE\u5206\u66F4\u65B0\
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n};\n\nstruct Candidate\
    \ { // \u63A1\u7528\u524D\u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx =\
    \ -1; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n\
    \    int appliedstate_idx = -1;\n    int score = INF;\n    bool is_finished =\
    \ false;\n    u64 hash = 0;\n\n    Candidate() = default;\n\n    Candidate(int\
    \ parent_idx_, Action action_, int appliedstate_idx_, int score_, bool is_finished_,\
    \ u64 hash_)\n        : parent_idx(parent_idx_), action(action_), appliedstate_idx(appliedstate_idx_),\
    \ is_finished(is_finished_), score(score_), hash(hash_) {}\n};\n\nstruct FinishCandidate\
    \ { // \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\
    \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n\
    };\n\n// \u2193\u3053\u3053\u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\
    \u3066\u3044\u3044\nstruct WorkSpace {\n    State s;\n    vector<Action> actions;\n\
    };\n\nstruct BeamNode {\n    State state;\n    int parent = -1;\n    Action last_action{};\n\
    };\n\nstruct BeamSearchResult {\n    State final_state;\n    vector<Action> move_history;\n\
    };\n// \u2191\u3053\u3053\u307E\u3067\n\n// \u8A55\u4FA1\u95A2\u6570 \u5C0F\u3055\
    \u3044\u65B9\u304C\u826F\u3044\nint calc_eval(const State& s) {\n    int eval\
    \ = 0;\n    (void)s;\n    return eval;\n}\n\n// \u72B6\u614B\u9077\u79FB\u95A2\
    \u6570\n// applied_state \u306B\u300Cparent \u306B action \u3092\u9069\u7528\u3057\
    \u305F\u7D50\u679C\u306E\u72B6\u614B\u300D\u3092\u66F8\u304D\u8FBC\u3080\u3002\
    \n// applied_state.score \u3068 applied_state.hash \u3082\u66F4\u65B0\u3059\u308B\
    \n// \u623B\u308A\u5024\uFF1A\u7D42\u4E86\u72B6\u614B\u306B\u306A\u308B\u306A\u3089\
    \ true\nbool apply_move(const State& parent, const Action& action, State& applied_state)\
    \ {\n    applied_state = parent;\n\n    // \u72B6\u614B\u9077\u79FB\n    applied_state.score\
    \ = calc_eval(applied_state);\n    applied_state.hash = calc_hash(applied_state);\n\
    \n    return false;\n}\n\n// \u9077\u79FB\u64CD\u4F5C\u5019\u88DC\u751F\u6210\n\
    // actions \u306B s \u306B\u5BFE\u3057\u3066\u53EF\u80FD\u306A\u64CD\u4F5C\u3092\
    \u5165\u308C\u308B\nvoid generate_possible_actions(const State& s, vector<Action>&\
    \ actions) {\n    \n}\n\n// \u30CF\u30C3\u30B7\u30E5\nu64 calc_hash(const State&\
    \ s) {\n\n}\n\n// \u64CD\u4F5C\u5C65\u6B74\u5FA9\u5143\u95A2\u6570\nvector<Action>\
    \ restore_move_history(const vector<BeamNode>& nodes, int node_idx) {\n    vector<Action>\
    \ history;\n    while (node_idx != -1 && nodes[node_idx].parent != -1) {\n   \
    \     history.emplace_back(nodes[node_idx].last_action);\n        node_idx = nodes[node_idx].parent;\n\
    \    }\n    reverse(history.begin(), history.end());\n    return history;\n}\n\
    \nBeamSearchResult run_beam_search(State& init_state, int beam_width) {\n    vector<BeamNode>\
    \ nodes; // \u30D3\u30FC\u30E0\u306E\u5168\u30CE\u30FC\u30C9\u3092\u5165\u308C\
    \u308B\n    vector<int> now; // nodes \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    \n    vector<int> next;\n\n    nodes.emplace_back(BeamNode{init_state, -1, Action{}});\n\
    \    now.emplace_back(0);\n\n    vector<Candidate> candidates; // \u9077\u79FB\
    \u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9 + \u64CD\u4F5C + \u9069\u7528\
    \u6E08\u307F\u72B6\u614B\u3078\u306E\u53C2\u7167\uFF09\n    vector<State> appliedstates;\
    \  // \u5019\u88DC\u306E\u72B6\u614B\u672C\u4F53\u3002\u63A1\u7528\u3055\u308C\
    \u308B\u307E\u3067 nodes \u306B\u306F\u5165\u308C\u306A\u3044\n    WorkSpace ws;\n\
    \    FinishCandidate best_cand;\n\n    // \u78BA\u4FDD\u9818\u57DF\u306F\u554F\
    \u984C\u3054\u3068\u306B\u8ABF\u6574\u3059\u308B\n    nodes.reserve(1 + 2 * beam_width\
    \ * 100);\n    now.reserve(beam_width);\n    next.reserve(beam_width);\n    candidates.reserve(2\
    \ * beam_width);\n    appliedstates.reserve(2 * beam_width);\n\n    while (!now.empty()\
    \ && timer.get_ms() < time_limit) {\n        next.clear();\n        candidates.clear();\n\
    \        appliedstates.clear();\n        visited.clear();\n\n        // \u9077\
    \u79FB\u5148\u3092\u5217\u6319\u3059\u308B\n        for (int beam_idx = 0; beam_idx\
    \ < (int)now.size(); beam_idx++) {\n            const int parent_idx = now[beam_idx];\n\
    \            const State& parent_state = nodes[parent_idx].state;\n          \
    \  ws.actions.clear();\n            generate_possible_actions(parent_state, ws.actions);\n\
    \            for (const auto& action : ws.actions) {\n                bool is_finished\
    \ = apply_move(parent_state, action, ws.s);\n                const int appliedstate_idx\
    \ = static_cast<int>(appliedstates.size());\n                appliedstates.emplace_back(ws.s);\n\
    \                Candidate cand(parent_idx, action, appliedstate_idx, ws.s.score,\
    \ is_finished, ws.s.hash);\n                candidates.emplace_back(cand);\n \
    \           }\n        }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\
    \u53D6\u308B\n        sort(candidates.begin(), candidates.end(), [](const Candidate&\
    \ a, const Candidate& b) {\n            return a.score < b.score;\n        });\n\
    \n        for (const auto& cand : candidates) {\n            if (cand.is_finished)\
    \ {\n                if (cand.score < best_cand.score) {\n                   \
    \ best_cand = FinishCandidate{cand.parent_idx, cand.action, cand.score};\n   \
    \             }\n                continue;\n            }\n            if (visited.contains_or_insert(cand.hash))\
    \ continue;\n\n            const int node_idx = static_cast<int>(nodes.size());\n\
    \            nodes.emplace_back(BeamNode{appliedstates[cand.appliedstate_idx],\
    \ cand.parent_idx, cand.action});\n            next.emplace_back(node_idx);\n\
    \            if ((int)next.size() >= beam_width) break;\n        }\n        if\
    \ (next.empty()) break;\n        swap(now, next);\n    }\n\n    assert(best_cand.parent_idx\
    \ != -1);\n    BeamSearchResult result;\n    result.final_state = nodes[best_cand.parent_idx].state;\n\
    \    [[maybe_unused]] const bool ok = apply_move(result.final_state, best_cand.action,\
    \ result.final_state);\n    assert(ok);\n    result.move_history = restore_move_history(nodes,\
    \ best_cand.parent_idx);\n    result.move_history.emplace_back(best_cand.action);\n\
    \    return result;\n}\n\nint main() {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n\
    \    timer = Timer();\n\n    State init_state;\n    BeamSearchResult result =\
    \ run_beam_search(init_state, beam_width);\n\n    return 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/beam_search_naive.cpp
  requiredBy: []
  timestamp: '2026-04-15 17:42:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/beam_search_naive.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/beam_search_naive.cpp
- /library/heuristic_library/cpp/beam_search_naive.cpp.html
title: heuristic_library/cpp/beam_search_naive.cpp
---
