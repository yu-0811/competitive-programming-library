/// apply_move で状態をコピーする実装
/// apply_move の処理が State のコピーと同程度に重いときに使う
#include <bits/stdc++.h>
using namespace std;

#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

using u64 = unsigned long long;
const int INF = 10000000;

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
};

struct Candidate { // 採用前の走査候補
    int parent_idx = -1; // nodes のインデックス
    Action action{};
    int appliedstate_idx = -1;
    int score = INF;
    bool is_finished = false;
    u64 hash = 0;

    Candidate() = default;

    Candidate(int parent_idx_, Action action_, int appliedstate_idx_, int score_, bool is_finished_, u64 hash_)
        : parent_idx(parent_idx_), action(action_), appliedstate_idx(appliedstate_idx_), is_finished(is_finished_), score(score_), hash(hash_) {}
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
    State state;
    int parent = -1;
    Action last_action{};
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

// 状態遷移関数
// applied_state に「parent に action を適用した結果の状態」を書き込む。
// applied_state.score と applied_state.hash も更新する
// 戻り値：終了状態になるなら true
bool apply_move(const State& parent, const Action& action, State& applied_state) {
    applied_state = parent;

    // 状態遷移
    applied_state.score = calc_eval(applied_state);
    applied_state.hash = calc_hash(applied_state);

    return false;
}

// 遷移操作候補生成
// actions に s に対して可能な操作を入れる
void generate_possible_actions(const State& s, vector<Action>& actions) {
    
}

// ハッシュ
u64 calc_hash(const State& s) {

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

BeamSearchResult run_beam_search(State& init_state, int beam_width) {
    vector<BeamNode> nodes; // ビームの全ノードを入れる
    vector<int> now; // nodes のインデックス
    vector<int> next;

    nodes.emplace_back(BeamNode{init_state, -1, Action{}});
    now.emplace_back(0);

    vector<Candidate> candidates; // 遷移先候補（親ノード + 操作 + 適用済み状態への参照）
    vector<State> appliedstates;  // 候補の状態本体。採用されるまで nodes には入れない
    WorkSpace ws;
    FinishCandidate best_cand;

    // 確保領域は問題ごとに調整する
    nodes.reserve(1 + 2 * beam_width * 100);
    now.reserve(beam_width);
    next.reserve(beam_width);
    candidates.reserve(2 * beam_width);
    appliedstates.reserve(2 * beam_width);

    while (!now.empty() && timer.get_ms() < time_limit) {
        next.clear();
        candidates.clear();
        appliedstates.clear();
        visited.clear();

        // 遷移先を列挙する
        for (int beam_idx = 0; beam_idx < (int)now.size(); beam_idx++) {
            const int parent_idx = now[beam_idx];
            const State& parent_state = nodes[parent_idx].state;
            ws.actions.clear();
            generate_possible_actions(parent_state, ws.actions);
            for (const auto& action : ws.actions) {
                bool is_finished = apply_move(parent_state, action, ws.s);
                const int appliedstate_idx = static_cast<int>(appliedstates.size());
                appliedstates.emplace_back(ws.s);
                Candidate cand(parent_idx, action, appliedstate_idx, ws.s.score, is_finished, ws.s.hash);
                candidates.emplace_back(cand);
            }
        }

        // 上位 beam_width 件だけ取る
        sort(candidates.begin(), candidates.end(), [](const Candidate& a, const Candidate& b) {
            return a.score < b.score;
        });

        for (const auto& cand : candidates) {
            if (cand.is_finished) {
                if (cand.score < best_cand.score) {
                    best_cand = FinishCandidate{cand.parent_idx, cand.action, cand.score};
                }
                continue;
            }
            if (visited.contains_or_insert(cand.hash)) continue;

            const int node_idx = static_cast<int>(nodes.size());
            nodes.emplace_back(BeamNode{appliedstates[cand.appliedstate_idx], cand.parent_idx, cand.action});
            next.emplace_back(node_idx);
            if ((int)next.size() >= beam_width) break;
        }
        if (next.empty()) break;
        swap(now, next);
    }

    assert(best_cand.parent_idx != -1);
    BeamSearchResult result;
    result.final_state = nodes[best_cand.parent_idx].state;
    [[maybe_unused]] const bool ok = apply_move(result.final_state, best_cand.action, result.final_state);
    assert(ok);
    result.move_history = restore_move_history(nodes, best_cand.parent_idx);
    result.move_history.emplace_back(best_cand.action);
    return result;
}

int main() {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    timer = Timer();

    State init_state;
    BeamSearchResult result = run_beam_search(init_state, beam_width);

    return 0;
}
