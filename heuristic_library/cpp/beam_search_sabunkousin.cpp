/// 差分更新ビームサーチ（木の上のビームサーチ）
/// 参考：https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639
#include <bits/stdc++.h>
using namespace std;

#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

using u64 = unsigned long long;
const int INF = 10000000;

struct State;
u64 calc_hash(const State& s);

class Timer {
    chrono::time_point<chrono::steady_clock> start;
public:
    Timer() : start(chrono::steady_clock::now()) {}
    unsigned short get_ms() { // 経過時間を返す
        auto now_time = chrono::steady_clock::now();
        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();
    }
};
Timer timer;

#ifndef ONLINE_JUDGE
    constexpr int time_limit = 1990 + 1000;
#else
    constexpr int time_limit = 1987;
#endif

// パラメータ
const int beam_width = 380;

// ハッシュ用のテーブル
struct FixedHashSet {
    static constexpr int LOG_CAP = 20;
    static constexpr int CAP = 1 << LOG_CAP;
    static constexpr int MASK = CAP - 1;

    array<u64, CAP> keys{};
    array<uint16_t, CAP> stamps{};
    uint16_t cur_stamp = 1;

    static u64 mix(u64 x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }

    void clear() {
        ++cur_stamp;
        if (cur_stamp == 0) {
            stamps.fill(0);
            cur_stamp = 1;
        }
    }

    bool contains_or_insert(u64 key) {
        int slot = static_cast<int>(mix(key) & MASK);
        while (stamps[slot] == cur_stamp) {
            if (keys[slot] == key) return true;
            slot = (slot + 1) & MASK;
        }
        stamps[slot] = cur_stamp;
        keys[slot] = key;
        return false;
    }
};

FixedHashSet visited;

// Zobrist Hash
class Random {
    inline static u64 state = 88172645463325252ULL;

public:
    inline static uint64_t xorshift64() {
        u64 x = state;
        x ^= x << 7;
        x ^= x >> 9;
        return state = x;
    }
};

struct ZobristHash2D {
    int H = 0;
    int W = 0;
    int kinds = 0;
    vector<u64> table;

    void init(int h, int w, int kind_count) {
        H = h;
        W = w;
        kinds = kind_count;
        table.resize(static_cast<size_t>(H) * W * kinds);
        for (u64& x : table) x = Random::xorshift64();
    }

    inline u64 value(int r, int c, int kind) const {
        return table[(r * W + c) * kinds + kind];
    }

    inline void apply_change(u64& hash, int r, int c, int before_kind, int after_kind) const {
        hash ^= value(r, c, before_kind);
        hash ^= value(r, c, after_kind);
    }

    template <class Board, class Indexer>
    u64 build(const Board& board, Indexer&& to_kind) const {
        u64 hash = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                hash ^= value(i, j, to_kind(board[i][j]));
            }
        }
        return hash;
    }
};

/// 状態 
// State と Candidate は軽い方がいい
struct Action { // State に対する遷移操作
    char d;
    int p;
};

struct State { // ビームに入れる状態
    // 問題特有の状態を入れる
    int score = 0;
    u64 hash = 0; // 差分更新しないならいらない

    // 終了条件満たすなら true 返す
    bool do_(const Action& action) {
        (void)action;
        return false;
    } 
    void undo_(const Action& action) {
        (void)action;
    }
    void calc_eval(const Action& action) {
        (void)action;
    }
    void calc_hash(const Action& action) {
        (void)action;
    }
};

struct Candidate { // 採用前の走査候補
    int parent_idx = -1; // nodes のインデックス
    Action action{};
    int score = INF;
    bool is_finished = false;
    u64 hash = 0;

    Candidate() = default;

    Candidate(int parent_idx_, Action action_, int score_, bool is_finished_, u64 hash_)
        : parent_idx(parent_idx_), action(action_), score(score_), is_finished(is_finished_), hash(hash_) {}
};

struct FinishCandidate { // 最良解候補
    int parent_idx = -1; // nodes のインデックス
    Action action{};
    int score = INF;
};

// ↓ここからは書き換えなくていい
struct WorkSpace {
    State s;
    vector<Action> actions;
};

struct BeamNode {
    int parent = -1;
    Action last_action{};
    int first_child = -1;
    int last_child = -1;
    int prev_sibling = -1;
    int next_sibling = -1;
    int score = INF;
    u64 hash = 0;
    int depth = 0;
};

struct BeamSearchResult {
    State final_state;
    vector<Action> move_history;
};
// ↑ここまで

// 評価関数 小さい方が良い
int calc_eval(const State& s) {
    int eval = 0;
    (void)s;
    return eval;
}

// 遷移操作候補生成
// actions に s に対して可能な操作を入れる
void generate_possible_actions(const State& s, vector<Action>& actions) {
    
}

// 操作履歴復元関数
vector<Action> restore_move_history(const vector<BeamNode>& nodes, int node_idx) {
    vector<Action> history;
    while (node_idx != -1 && nodes[node_idx].parent != -1) {
        history.emplace_back(nodes[node_idx].last_action);
        node_idx = nodes[node_idx].parent;
    }
    reverse(history.begin(), history.end());
    return history;
}

int move_to_leftmost_leaf(const vector<BeamNode>& nodes, State& state) {
    int node_idx = 0;
    while (nodes[node_idx].first_child != -1) {
        node_idx = nodes[node_idx].first_child;
        [[maybe_unused]] const bool finished = state.do_(nodes[node_idx].last_action);
    }
    return node_idx;
}

int move_to_next_leaf(const vector<BeamNode>& nodes, int node_idx, State& state) {
    if (node_idx == 0) return -1;

    int cur = node_idx;
    while (true) {
        if (nodes[cur].next_sibling != -1) {
            state.undo_(nodes[cur].last_action);
            cur = nodes[cur].next_sibling;
            [[maybe_unused]] const bool finished = state.do_(nodes[cur].last_action);
            while (nodes[cur].first_child != -1) {
                cur = nodes[cur].first_child;
                [[maybe_unused]] const bool finished2 = state.do_(nodes[cur].last_action);
            }
            return cur;
        }
        state.undo_(nodes[cur].last_action);
        cur = nodes[cur].parent;
        if (cur == 0) return -1;
    }
}

int add_child(vector<BeamNode>& nodes, int parent_idx, const Candidate& cand) {
    const int node_idx = static_cast<int>(nodes.size());
    nodes.emplace_back(BeamNode{
        parent_idx,
        cand.action,
        -1,
        -1,
        nodes[parent_idx].last_child,
        -1,
        cand.score,
        cand.hash,
        nodes[parent_idx].depth + 1
    });

    if (nodes[parent_idx].first_child == -1) {
        nodes[parent_idx].first_child = node_idx;
    } else {
        nodes[nodes[parent_idx].last_child].next_sibling = node_idx;
    }
    nodes[parent_idx].last_child = node_idx;
    return node_idx;
}

void prune_if_unnecessary(vector<BeamNode>& nodes, int node_idx) {
    int cur = node_idx;
    while (cur != 0 && nodes[cur].first_child == -1) {
        const int parent_idx = nodes[cur].parent;
        const int prev_idx = nodes[cur].prev_sibling;
        const int next_idx = nodes[cur].next_sibling;

        if (prev_idx != -1) {
            nodes[prev_idx].next_sibling = next_idx;
        } else {
            nodes[parent_idx].first_child = next_idx;
        }
        if (next_idx != -1) {
            nodes[next_idx].prev_sibling = prev_idx;
        } else {
            nodes[parent_idx].last_child = prev_idx;
        }

        nodes[cur].parent = -1;
        nodes[cur].prev_sibling = -1;
        nodes[cur].next_sibling = -1;
        cur = parent_idx;
    }
}

BeamSearchResult run_beam_search(State& init_state, int beam_width) {
    vector<BeamNode> nodes; // 探索木
    nodes.emplace_back(BeamNode{
        -1,
        Action{},
        -1,
        -1,
        -1,
        -1,
        init_state.score,
        init_state.hash,
        0
    });

    vector<Candidate> candidates; // 遷移先候補（親ノード + 操作 + 評価値）
    vector<int> expanded_leaf_indices;
    WorkSpace ws;
    BeamSearchResult best_result;
    int best_score = INF;

    // 確保領域は問題ごとに調整する
    nodes.reserve(2 * beam_width * 100);
    candidates.reserve(4 * beam_width);
    expanded_leaf_indices.reserve(beam_width);
    ws.s = init_state;

    while (timer.get_ms() < time_limit) {
        candidates.clear();
        expanded_leaf_indices.clear();
        visited.clear();

        // 葉を Euler Tour 順に走査する。
        // move_to_next_leaf は undo_/do_ だけで隣の葉へ移動する。
        int leaf_idx = move_to_leftmost_leaf(nodes, ws.s);
        while (leaf_idx != -1) {
            expanded_leaf_indices.emplace_back(leaf_idx);
            ws.actions.clear();
            generate_possible_actions(ws.s, ws.actions);
            for (const auto& action : ws.actions) {
                const bool is_finished = ws.s.do_(action);
                if (is_finished) {
                    if (ws.s.score < best_score) {
                        best_score = ws.s.score;
                        best_result.final_state = ws.s;
                        best_result.move_history = restore_move_history(nodes, leaf_idx);
                        best_result.move_history.emplace_back(action);
                    }
                } else {
                    candidates.emplace_back(leaf_idx, action, ws.s.score, false, ws.s.hash);
                }
                ws.s.undo_(action);
            }
            leaf_idx = move_to_next_leaf(nodes, leaf_idx, ws.s);
        }

        // 上位 beam_width 件だけ取る
        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const Candidate& b) {
            return a.score < b.score;
        });

        int selected_count = 0;
        for (const auto& cand : candidates) {
            if (visited.contains_or_insert(cand.hash)) continue;
            add_child(nodes, cand.parent_idx, cand);
            ++selected_count;
            if (selected_count >= beam_width) break;
        }

        for (int node_idx : expanded_leaf_indices) {
            if (nodes[node_idx].parent != -1 && nodes[node_idx].first_child == -1) {
                prune_if_unnecessary(nodes, node_idx);
            }
        }

        if (selected_count == 0) break;
    }

    assert(best_score != INF);
    return best_result;
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    timer = Timer();

    State init_state;
    BeamSearchResult result = run_beam_search(init_state, beam_width);

    return 0;
}
