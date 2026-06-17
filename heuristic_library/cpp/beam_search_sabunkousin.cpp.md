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
    - https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639
  bundledCode: "#line 1 \"heuristic_library/cpp/beam_search_sabunkousin.cpp\"\n///\
    \ \u5DEE\u5206\u66F4\u65B0\u30D3\u30FC\u30E0\u30B5\u30FC\u30C1\uFF08\u6728\u306E\
    \u4E0A\u306E\u30D3\u30FC\u30E0\u30B5\u30FC\u30C1\uFF09\n/// \u53C2\u8003\uFF1A\
    https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639\n#include <bits/stdc++.h>\n\
    using namespace std;\n\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nusing u64 = unsigned long long;\n\
    const int INF = 10000000;\n\nstruct State;\nu64 calc_hash(const State& s);\n\n\
    class Timer {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n\
    \    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned short get_ms()\
    \ { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\nTimer timer;\n\n#ifndef ONLINE_JUDGE\n    constexpr int time_limit\
    \ = 1990 + 1000;\n#else\n    constexpr int time_limit = 1987;\n#endif\n\n// \u30D1\
    \u30E9\u30E1\u30FC\u30BF\nconst int beam_width = 380;\n\n// \u30CF\u30C3\u30B7\
    \u30E5\u7528\u306E\u30C6\u30FC\u30D6\u30EB\nstruct FixedHashSet {\n    static\
    \ constexpr int LOG_CAP = 20;\n    static constexpr int CAP = 1 << LOG_CAP;\n\
    \    static constexpr int MASK = CAP - 1;\n\n    array<u64, CAP> keys{};\n   \
    \ array<uint16_t, CAP> stamps{};\n    uint16_t cur_stamp = 1;\n\n    static u64\
    \ mix(u64 x) {\n        x += 0x9e3779b97f4a7c15ULL;\n        x = (x ^ (x >> 30))\
    \ * 0xbf58476d1ce4e5b9ULL;\n        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;\n\
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
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n\n    // \u7D42\u4E86\u6761\
    \u4EF6\u6E80\u305F\u3059\u306A\u3089 true \u8FD4\u3059\n    bool do_(const Action&\
    \ action) {\n        (void)action;\n        return false;\n    } \n    void undo_(const\
    \ Action& action) {\n        (void)action;\n    }\n    void calc_eval(const Action&\
    \ action) {\n        (void)action;\n    }\n    void calc_hash(const Action& action)\
    \ {\n        (void)action;\n    }\n};\n\nstruct Candidate { // \u63A1\u7528\u524D\
    \u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n \
    \   bool is_finished = false;\n    u64 hash = 0;\n\n    Candidate() = default;\n\
    \n    Candidate(int parent_idx_, Action action_, int score_, bool is_finished_,\
    \ u64 hash_)\n        : parent_idx(parent_idx_), action(action_), score(score_),\
    \ is_finished(is_finished_), hash(hash_) {}\n};\n\nstruct FinishCandidate { //\
    \ \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n};\n\
    \n// \u2193\u3053\u3053\u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\u3066\
    \u3044\u3044\nstruct WorkSpace {\n    State s;\n    vector<Action> actions;\n\
    };\n\nstruct BeamNode {\n    int parent = -1;\n    Action last_action{};\n   \
    \ int first_child = -1;\n    int last_child = -1;\n    int prev_sibling = -1;\n\
    \    int next_sibling = -1;\n    int score = INF;\n    u64 hash = 0;\n    int\
    \ depth = 0;\n};\n\nstruct BeamSearchResult {\n    State final_state;\n    vector<Action>\
    \ move_history;\n};\n// \u2191\u3053\u3053\u307E\u3067\n\n// \u8A55\u4FA1\u95A2\
    \u6570 \u5C0F\u3055\u3044\u65B9\u304C\u826F\u3044\nint calc_eval(const State&\
    \ s) {\n    int eval = 0;\n    (void)s;\n    return eval;\n}\n\n// \u9077\u79FB\
    \u64CD\u4F5C\u5019\u88DC\u751F\u6210\n// actions \u306B s \u306B\u5BFE\u3057\u3066\
    \u53EF\u80FD\u306A\u64CD\u4F5C\u3092\u5165\u308C\u308B\nvoid generate_possible_actions(const\
    \ State& s, vector<Action>& actions) {\n    \n}\n\n// \u64CD\u4F5C\u5C65\u6B74\
    \u5FA9\u5143\u95A2\u6570\nvector<Action> restore_move_history(const vector<BeamNode>&\
    \ nodes, int node_idx) {\n    vector<Action> history;\n    while (node_idx !=\
    \ -1 && nodes[node_idx].parent != -1) {\n        history.emplace_back(nodes[node_idx].last_action);\n\
    \        node_idx = nodes[node_idx].parent;\n    }\n    reverse(history.begin(),\
    \ history.end());\n    return history;\n}\n\nint move_to_leftmost_leaf(const vector<BeamNode>&\
    \ nodes, State& state) {\n    int node_idx = 0;\n    while (nodes[node_idx].first_child\
    \ != -1) {\n        node_idx = nodes[node_idx].first_child;\n        [[maybe_unused]]\
    \ const bool finished = state.do_(nodes[node_idx].last_action);\n    }\n    return\
    \ node_idx;\n}\n\nint move_to_next_leaf(const vector<BeamNode>& nodes, int node_idx,\
    \ State& state) {\n    if (node_idx == 0) return -1;\n\n    int cur = node_idx;\n\
    \    while (true) {\n        if (nodes[cur].next_sibling != -1) {\n          \
    \  state.undo_(nodes[cur].last_action);\n            cur = nodes[cur].next_sibling;\n\
    \            [[maybe_unused]] const bool finished = state.do_(nodes[cur].last_action);\n\
    \            while (nodes[cur].first_child != -1) {\n                cur = nodes[cur].first_child;\n\
    \                [[maybe_unused]] const bool finished2 = state.do_(nodes[cur].last_action);\n\
    \            }\n            return cur;\n        }\n        state.undo_(nodes[cur].last_action);\n\
    \        cur = nodes[cur].parent;\n        if (cur == 0) return -1;\n    }\n}\n\
    \nint add_child(vector<BeamNode>& nodes, int parent_idx, const Candidate& cand)\
    \ {\n    const int node_idx = static_cast<int>(nodes.size());\n    nodes.emplace_back(BeamNode{\n\
    \        parent_idx,\n        cand.action,\n        -1,\n        -1,\n       \
    \ nodes[parent_idx].last_child,\n        -1,\n        cand.score,\n        cand.hash,\n\
    \        nodes[parent_idx].depth + 1\n    });\n\n    if (nodes[parent_idx].first_child\
    \ == -1) {\n        nodes[parent_idx].first_child = node_idx;\n    } else {\n\
    \        nodes[nodes[parent_idx].last_child].next_sibling = node_idx;\n    }\n\
    \    nodes[parent_idx].last_child = node_idx;\n    return node_idx;\n}\n\nvoid\
    \ prune_if_unnecessary(vector<BeamNode>& nodes, int node_idx) {\n    int cur =\
    \ node_idx;\n    while (cur != 0 && nodes[cur].first_child == -1) {\n        const\
    \ int parent_idx = nodes[cur].parent;\n        const int prev_idx = nodes[cur].prev_sibling;\n\
    \        const int next_idx = nodes[cur].next_sibling;\n\n        if (prev_idx\
    \ != -1) {\n            nodes[prev_idx].next_sibling = next_idx;\n        } else\
    \ {\n            nodes[parent_idx].first_child = next_idx;\n        }\n      \
    \  if (next_idx != -1) {\n            nodes[next_idx].prev_sibling = prev_idx;\n\
    \        } else {\n            nodes[parent_idx].last_child = prev_idx;\n    \
    \    }\n\n        nodes[cur].parent = -1;\n        nodes[cur].prev_sibling = -1;\n\
    \        nodes[cur].next_sibling = -1;\n        cur = parent_idx;\n    }\n}\n\n\
    BeamSearchResult run_beam_search(State& init_state, int beam_width) {\n    vector<BeamNode>\
    \ nodes; // \u63A2\u7D22\u6728\n    nodes.emplace_back(BeamNode{\n        -1,\n\
    \        Action{},\n        -1,\n        -1,\n        -1,\n        -1,\n     \
    \   init_state.score,\n        init_state.hash,\n        0\n    });\n\n    vector<Candidate>\
    \ candidates; // \u9077\u79FB\u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9\
    \ + \u64CD\u4F5C + \u8A55\u4FA1\u5024\uFF09\n    vector<int> expanded_leaf_indices;\n\
    \    WorkSpace ws;\n    BeamSearchResult best_result;\n    int best_score = INF;\n\
    \n    // \u78BA\u4FDD\u9818\u57DF\u306F\u554F\u984C\u3054\u3068\u306B\u8ABF\u6574\
    \u3059\u308B\n    nodes.reserve(2 * beam_width * 100);\n    candidates.reserve(4\
    \ * beam_width);\n    expanded_leaf_indices.reserve(beam_width);\n    ws.s = init_state;\n\
    \n    while (timer.get_ms() < time_limit) {\n        candidates.clear();\n   \
    \     expanded_leaf_indices.clear();\n        visited.clear();\n\n        // \u8449\
    \u3092 Euler Tour \u9806\u306B\u8D70\u67FB\u3059\u308B\u3002\n        // move_to_next_leaf\
    \ \u306F undo_/do_ \u3060\u3051\u3067\u96A3\u306E\u8449\u3078\u79FB\u52D5\u3059\
    \u308B\u3002\n        int leaf_idx = move_to_leftmost_leaf(nodes, ws.s);\n   \
    \     while (leaf_idx != -1) {\n            expanded_leaf_indices.emplace_back(leaf_idx);\n\
    \            ws.actions.clear();\n            generate_possible_actions(ws.s,\
    \ ws.actions);\n            for (const auto& action : ws.actions) {\n        \
    \        const bool is_finished = ws.s.do_(action);\n                if (is_finished)\
    \ {\n                    if (ws.s.score < best_score) {\n                    \
    \    best_score = ws.s.score;\n                        best_result.final_state\
    \ = ws.s;\n                        best_result.move_history = restore_move_history(nodes,\
    \ leaf_idx);\n                        best_result.move_history.emplace_back(action);\n\
    \                    }\n                } else {\n                    candidates.emplace_back(leaf_idx,\
    \ action, ws.s.score, false, ws.s.hash);\n                }\n                ws.s.undo_(action);\n\
    \            }\n            leaf_idx = move_to_next_leaf(nodes, leaf_idx, ws.s);\n\
    \        }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\u53D6\u308B\
    \n        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const\
    \ Candidate& b) {\n            return a.score < b.score;\n        });\n\n    \
    \    int selected_count = 0;\n        for (const auto& cand : candidates) {\n\
    \            if (visited.contains_or_insert(cand.hash)) continue;\n          \
    \  add_child(nodes, cand.parent_idx, cand);\n            ++selected_count;\n \
    \           if (selected_count >= beam_width) break;\n        }\n\n        for\
    \ (int node_idx : expanded_leaf_indices) {\n            if (nodes[node_idx].parent\
    \ != -1 && nodes[node_idx].first_child == -1) {\n                prune_if_unnecessary(nodes,\
    \ node_idx);\n            }\n        }\n\n        if (selected_count == 0) break;\n\
    \    }\n\n    assert(best_score != INF);\n    return best_result;\n}\n\nint main()\
    \ {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n    timer = Timer();\n\
    \n    State init_state;\n    BeamSearchResult result = run_beam_search(init_state,\
    \ beam_width);\n\n    return 0;\n}\n"
  code: "/// \u5DEE\u5206\u66F4\u65B0\u30D3\u30FC\u30E0\u30B5\u30FC\u30C1\uFF08\u6728\
    \u306E\u4E0A\u306E\u30D3\u30FC\u30E0\u30B5\u30FC\u30C1\uFF09\n/// \u53C2\u8003\
    \uFF1Ahttps://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\n#pragma GCC target(\"avx2\")\n#pragma\
    \ GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nusing u64 =\
    \ unsigned long long;\nconst int INF = 10000000;\n\nstruct State;\nu64 calc_hash(const\
    \ State& s);\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock> start;\n\
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
    \u3057\u306A\u3044\u306A\u3089\u3044\u3089\u306A\u3044\n\n    // \u7D42\u4E86\u6761\
    \u4EF6\u6E80\u305F\u3059\u306A\u3089 true \u8FD4\u3059\n    bool do_(const Action&\
    \ action) {\n        (void)action;\n        return false;\n    } \n    void undo_(const\
    \ Action& action) {\n        (void)action;\n    }\n    void calc_eval(const Action&\
    \ action) {\n        (void)action;\n    }\n    void calc_hash(const Action& action)\
    \ {\n        (void)action;\n    }\n};\n\nstruct Candidate { // \u63A1\u7528\u524D\
    \u306E\u8D70\u67FB\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n \
    \   bool is_finished = false;\n    u64 hash = 0;\n\n    Candidate() = default;\n\
    \n    Candidate(int parent_idx_, Action action_, int score_, bool is_finished_,\
    \ u64 hash_)\n        : parent_idx(parent_idx_), action(action_), score(score_),\
    \ is_finished(is_finished_), hash(hash_) {}\n};\n\nstruct FinishCandidate { //\
    \ \u6700\u826F\u89E3\u5019\u88DC\n    int parent_idx = -1; // nodes \u306E\u30A4\
    \u30F3\u30C7\u30C3\u30AF\u30B9\n    Action action{};\n    int score = INF;\n};\n\
    \n// \u2193\u3053\u3053\u304B\u3089\u306F\u66F8\u304D\u63DB\u3048\u306A\u304F\u3066\
    \u3044\u3044\nstruct WorkSpace {\n    State s;\n    vector<Action> actions;\n\
    };\n\nstruct BeamNode {\n    int parent = -1;\n    Action last_action{};\n   \
    \ int first_child = -1;\n    int last_child = -1;\n    int prev_sibling = -1;\n\
    \    int next_sibling = -1;\n    int score = INF;\n    u64 hash = 0;\n    int\
    \ depth = 0;\n};\n\nstruct BeamSearchResult {\n    State final_state;\n    vector<Action>\
    \ move_history;\n};\n// \u2191\u3053\u3053\u307E\u3067\n\n// \u8A55\u4FA1\u95A2\
    \u6570 \u5C0F\u3055\u3044\u65B9\u304C\u826F\u3044\nint calc_eval(const State&\
    \ s) {\n    int eval = 0;\n    (void)s;\n    return eval;\n}\n\n// \u9077\u79FB\
    \u64CD\u4F5C\u5019\u88DC\u751F\u6210\n// actions \u306B s \u306B\u5BFE\u3057\u3066\
    \u53EF\u80FD\u306A\u64CD\u4F5C\u3092\u5165\u308C\u308B\nvoid generate_possible_actions(const\
    \ State& s, vector<Action>& actions) {\n    \n}\n\n// \u64CD\u4F5C\u5C65\u6B74\
    \u5FA9\u5143\u95A2\u6570\nvector<Action> restore_move_history(const vector<BeamNode>&\
    \ nodes, int node_idx) {\n    vector<Action> history;\n    while (node_idx !=\
    \ -1 && nodes[node_idx].parent != -1) {\n        history.emplace_back(nodes[node_idx].last_action);\n\
    \        node_idx = nodes[node_idx].parent;\n    }\n    reverse(history.begin(),\
    \ history.end());\n    return history;\n}\n\nint move_to_leftmost_leaf(const vector<BeamNode>&\
    \ nodes, State& state) {\n    int node_idx = 0;\n    while (nodes[node_idx].first_child\
    \ != -1) {\n        node_idx = nodes[node_idx].first_child;\n        [[maybe_unused]]\
    \ const bool finished = state.do_(nodes[node_idx].last_action);\n    }\n    return\
    \ node_idx;\n}\n\nint move_to_next_leaf(const vector<BeamNode>& nodes, int node_idx,\
    \ State& state) {\n    if (node_idx == 0) return -1;\n\n    int cur = node_idx;\n\
    \    while (true) {\n        if (nodes[cur].next_sibling != -1) {\n          \
    \  state.undo_(nodes[cur].last_action);\n            cur = nodes[cur].next_sibling;\n\
    \            [[maybe_unused]] const bool finished = state.do_(nodes[cur].last_action);\n\
    \            while (nodes[cur].first_child != -1) {\n                cur = nodes[cur].first_child;\n\
    \                [[maybe_unused]] const bool finished2 = state.do_(nodes[cur].last_action);\n\
    \            }\n            return cur;\n        }\n        state.undo_(nodes[cur].last_action);\n\
    \        cur = nodes[cur].parent;\n        if (cur == 0) return -1;\n    }\n}\n\
    \nint add_child(vector<BeamNode>& nodes, int parent_idx, const Candidate& cand)\
    \ {\n    const int node_idx = static_cast<int>(nodes.size());\n    nodes.emplace_back(BeamNode{\n\
    \        parent_idx,\n        cand.action,\n        -1,\n        -1,\n       \
    \ nodes[parent_idx].last_child,\n        -1,\n        cand.score,\n        cand.hash,\n\
    \        nodes[parent_idx].depth + 1\n    });\n\n    if (nodes[parent_idx].first_child\
    \ == -1) {\n        nodes[parent_idx].first_child = node_idx;\n    } else {\n\
    \        nodes[nodes[parent_idx].last_child].next_sibling = node_idx;\n    }\n\
    \    nodes[parent_idx].last_child = node_idx;\n    return node_idx;\n}\n\nvoid\
    \ prune_if_unnecessary(vector<BeamNode>& nodes, int node_idx) {\n    int cur =\
    \ node_idx;\n    while (cur != 0 && nodes[cur].first_child == -1) {\n        const\
    \ int parent_idx = nodes[cur].parent;\n        const int prev_idx = nodes[cur].prev_sibling;\n\
    \        const int next_idx = nodes[cur].next_sibling;\n\n        if (prev_idx\
    \ != -1) {\n            nodes[prev_idx].next_sibling = next_idx;\n        } else\
    \ {\n            nodes[parent_idx].first_child = next_idx;\n        }\n      \
    \  if (next_idx != -1) {\n            nodes[next_idx].prev_sibling = prev_idx;\n\
    \        } else {\n            nodes[parent_idx].last_child = prev_idx;\n    \
    \    }\n\n        nodes[cur].parent = -1;\n        nodes[cur].prev_sibling = -1;\n\
    \        nodes[cur].next_sibling = -1;\n        cur = parent_idx;\n    }\n}\n\n\
    BeamSearchResult run_beam_search(State& init_state, int beam_width) {\n    vector<BeamNode>\
    \ nodes; // \u63A2\u7D22\u6728\n    nodes.emplace_back(BeamNode{\n        -1,\n\
    \        Action{},\n        -1,\n        -1,\n        -1,\n        -1,\n     \
    \   init_state.score,\n        init_state.hash,\n        0\n    });\n\n    vector<Candidate>\
    \ candidates; // \u9077\u79FB\u5148\u5019\u88DC\uFF08\u89AA\u30CE\u30FC\u30C9\
    \ + \u64CD\u4F5C + \u8A55\u4FA1\u5024\uFF09\n    vector<int> expanded_leaf_indices;\n\
    \    WorkSpace ws;\n    BeamSearchResult best_result;\n    int best_score = INF;\n\
    \n    // \u78BA\u4FDD\u9818\u57DF\u306F\u554F\u984C\u3054\u3068\u306B\u8ABF\u6574\
    \u3059\u308B\n    nodes.reserve(2 * beam_width * 100);\n    candidates.reserve(4\
    \ * beam_width);\n    expanded_leaf_indices.reserve(beam_width);\n    ws.s = init_state;\n\
    \n    while (timer.get_ms() < time_limit) {\n        candidates.clear();\n   \
    \     expanded_leaf_indices.clear();\n        visited.clear();\n\n        // \u8449\
    \u3092 Euler Tour \u9806\u306B\u8D70\u67FB\u3059\u308B\u3002\n        // move_to_next_leaf\
    \ \u306F undo_/do_ \u3060\u3051\u3067\u96A3\u306E\u8449\u3078\u79FB\u52D5\u3059\
    \u308B\u3002\n        int leaf_idx = move_to_leftmost_leaf(nodes, ws.s);\n   \
    \     while (leaf_idx != -1) {\n            expanded_leaf_indices.emplace_back(leaf_idx);\n\
    \            ws.actions.clear();\n            generate_possible_actions(ws.s,\
    \ ws.actions);\n            for (const auto& action : ws.actions) {\n        \
    \        const bool is_finished = ws.s.do_(action);\n                if (is_finished)\
    \ {\n                    if (ws.s.score < best_score) {\n                    \
    \    best_score = ws.s.score;\n                        best_result.final_state\
    \ = ws.s;\n                        best_result.move_history = restore_move_history(nodes,\
    \ leaf_idx);\n                        best_result.move_history.emplace_back(action);\n\
    \                    }\n                } else {\n                    candidates.emplace_back(leaf_idx,\
    \ action, ws.s.score, false, ws.s.hash);\n                }\n                ws.s.undo_(action);\n\
    \            }\n            leaf_idx = move_to_next_leaf(nodes, leaf_idx, ws.s);\n\
    \        }\n\n        // \u4E0A\u4F4D beam_width \u4EF6\u3060\u3051\u53D6\u308B\
    \n        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const\
    \ Candidate& b) {\n            return a.score < b.score;\n        });\n\n    \
    \    int selected_count = 0;\n        for (const auto& cand : candidates) {\n\
    \            if (visited.contains_or_insert(cand.hash)) continue;\n          \
    \  add_child(nodes, cand.parent_idx, cand);\n            ++selected_count;\n \
    \           if (selected_count >= beam_width) break;\n        }\n\n        for\
    \ (int node_idx : expanded_leaf_indices) {\n            if (nodes[node_idx].parent\
    \ != -1 && nodes[node_idx].first_child == -1) {\n                prune_if_unnecessary(nodes,\
    \ node_idx);\n            }\n        }\n\n        if (selected_count == 0) break;\n\
    \    }\n\n    assert(best_score != INF);\n    return best_result;\n}\n\nint main()\
    \ {\n    ios::sync_with_stdio(false);cin.tie(nullptr);\n    timer = Timer();\n\
    \n    State init_state;\n    BeamSearchResult result = run_beam_search(init_state,\
    \ beam_width);\n\n    return 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/beam_search_sabunkousin.cpp
  requiredBy: []
  timestamp: '2026-06-17 12:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/beam_search_sabunkousin.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/beam_search_sabunkousin.cpp
- /library/heuristic_library/cpp/beam_search_sabunkousin.cpp.html
title: heuristic_library/cpp/beam_search_sabunkousin.cpp
---
