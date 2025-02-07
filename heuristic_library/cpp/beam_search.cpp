#include <bits/stdc++.h>
#include <cassert>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long
using u64 = unsigned long long;
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

const int INF = 10000000;
unordered_set<u64> visited;

// パラメータ ########################################
const int beam_width = 380;
const int beam_depth = 120;
const int penalty = 1;
const int bonus = 1000;
const int finish = bonus * 40 * -10;
//#####################################################

// Zobrist Hash ########################################
class Random {
    // 32ビット版の xorshift を用意（状態はstatic変数で管理）
    static uint32_t xorshift32() {
        static uint32_t x = 123456789, y = 362436039, z = 521288629, w = 88675123; 
        uint32_t t = x ^ (x << 11);
        x = y; y = z; z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }
public:
    // 64ビット版乱数：32ビットの xorshift を2回呼び出し、結合する
    inline static uint64_t xorshift64() {
         uint64_t high = xorshift32();
         uint64_t low  = xorshift32();
         return (high << 32) | low;
    }
    // [0, x)
    inline static uint64_t randrange(uint64_t x) { return xorshift64() % x; }
    // [x, y)
    inline static uint64_t randrange(uint64_t x, uint64_t y) { return randrange(y - x) + x; }
    // [0.0, 1.0)
    inline static double random() { 
        return (xorshift64() + 0.5) * (1.0 / (double)ULLONG_MAX); 
    }
};
u64 zobrist[N][N][3];
void init_zobrist() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < 3; k++) {
                zobrist[i][j][k] = Random::randrange((1ULL << 63)-1);
            }
        }
    }
}
//#####################################################

// 状態 #############################################
struct Move {
  char d; int p;
};

struct xy {
  int x, y;
};

struct State {
  int score;
  int depth;
  Move move_history[beam_depth];

  State() : score(0), depth(0) {};
};

// ソート関数########################################
// スコア最大化のとき
bool comp_max(const State &a1, const State &a2){
    return a1.score > a2.score;
}
// スコア最小化のとき
bool comp_min(const State &a1, const State &a2){
    return a1.score < a2.score;
}
//#####################################################

// 評価関数########################################
// 小さい方がいい
// 各鬼の外周からの距離の合計を評価値とする
// ただし、最も近い外周までに福がいるなら penalty を加算する
// 福が落ちる盤面は許さないように inf ペナルティーを与える
// 倒した鬼の数 * bonus を減算する
int calc_eval(const State &s){
  int eval = 0;

  return eval;
}
//#####################################################

// 状態遷移関数########################################
State apply_move(const State &s, Move &mv){
  State nex = s;
  // 状態遷移
  return nex;
}
//#####################################################

// 盤面ハッシュ########################################
inline int pieceIndex(int c) {
    // 盤面の状態に合わせて対応付ける
    if (c == -1) return 0; // 'o'
    else if (c == -2) return 1; // '.'
    else return 2; // 'x'
}
u64 board_to_u64(const int (&board)[N][N]) {
    u64 hash = 0;
    rep(i, N) {
        rep(j, N) {
            int idx = pieceIndex(board[i][j]);
            hash ^= zobrist[i][j][idx];
        }
    }
    return hash;
}

//#####################################################

auto beam_search(State &init_state, int beam_width, int beam_depth){
    vector<State> now;
    now.emplace_back(init_state);
    vector<State> next;
    visited.emplace(board_to_u64(init_state.board));

    // 遷移候補 ########################################
    vector<Move> possible_moves;
    //#################################################

    for (int i=0; i<beam_depth; i++){
        bool sorted = false;
        for (auto &s : now){
            // 状態を遷移させる
            for (auto &mv: possible_moves){
                // 状態を変化させたときの評価値を計算########
                // これたぶん実際に盤面を動かさずに評価値だけ計算できたほうが高速化できる
                auto nex_s = apply_move(s, mv);
                if (nex_s.score == INF) continue;
                //###########################################

                // スコア最大化のとき, ソート済みの中で最小の評価値よりも大きい場合のみ遷移
                //if (sorted && nex_s.score <= next[beam_width-1].score) continue;
                // スコア最小化のとき, ソート済みの中で最大の評価値よりも小さい場合のみ遷移
                if (sorted && nex_s.score >= next[beam_width-1].score) continue;

                // 既に訪れた状態はスキップ
                u64 board_hash = board_to_u64(nex_s.board);
                if (visited.count(board_hash)) continue;
                visited.emplace(board_hash);
                next.emplace_back(nex_s);

                if (nex_s.score <= finish){
                    return nex_s;
                }

                if (next.size() >= 2*beam_width){
                    sort(next.begin(), next.end(), comp_min);
                    next.resize(beam_width);
                    sorted = true;
                }
            }
        }
        if (next.empty()) break;
        sort(next.begin(), next.end(), comp_min);
        next.resize(beam_width);
        swap(now, next);
        next.clear();
    }
  return now[0];
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);
  init_zobrist();

  auto best_move = beam_search(init_state, beam_width, beam_depth);
  for (int i=0; i<best_move.depth; i++){
    cout << best_move.move_history[i].d << " " << best_move.move_history[i].p << endl;
  }
}