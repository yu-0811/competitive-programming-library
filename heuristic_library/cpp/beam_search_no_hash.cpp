#include <bits/stdc++.h>
#include <cassert>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long
using u64 = unsigned long long;
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

constexpr int T = 100;
short P[T], Q[T], R[T];

// パラメータ ########################################
const int beam_width = 60000;
const int MAX_TURN = 100;
//#####################################################

// 状態 #############################################
struct Operation {
  char dx;
};

using EvalType = int; // TODO

struct State {
  EvalType eval;
  int zero_count;
  short X[100];
  Operation history[MAX_TURN];

  State(int eval, int zero_count) : eval(eval), zero_count(zero_count) {}
};

struct Evaluator {
  EvalType eval;
  int zero_count;
  unsigned short parent_state_index;
  unsigned char operation_index;

  Evaluator() = default; 

  Evaluator(EvalType eval, int zero_count, unsigned short parent_state_index, unsigned char operation_index) :
    eval(eval), zero_count(zero_count), parent_state_index(parent_state_index), operation_index(operation_index) {}
};

// ソート関数########################################
// スコア最大化のとき
bool comp_max(const Evaluator &a1, const Evaluator &a2){
    return a1.eval > a2.eval;
}
// スコア最小化のとき
bool comp_min(const Evaluator &a1, const Evaluator &a2){
    return a1.eval < a2.eval;
}
//#####################################################

// 評価関数########################################
Evaluator calc_new_eval(const State &s, const size_t state_idx, Operation &op, const size_t op_idx,  const int& turn){
  EvalType new_zero_count = s.zero_count;
  if (s.X[P[turn]] + op.dx == 0) new_zero_count++;
  else if (s.X[P[turn]] == 0) new_zero_count--;
  if (s.X[Q[turn]] + op.dx == 0) new_zero_count++;
  else if (s.X[Q[turn]] == 0) new_zero_count--;
  if (s.X[R[turn]] + op.dx == 0) new_zero_count++;
  else if (s.X[R[turn]] == 0) new_zero_count--;
  EvalType new_score = s.eval + new_zero_count;
  Evaluator new_evaluator(new_score, new_zero_count, state_idx, op_idx);
  return new_evaluator;
}
//#####################################################

// 状態遷移関数########################################
State operate(const State& s, const Evaluator& e, const Operation& op, int turn){
  State new_s = s;
  new_s.zero_count = e.zero_count;
  new_s.eval = e.eval;
  new_s.X[P[turn]] += op.dx;
  new_s.X[Q[turn]] += op.dx;
  new_s.X[R[turn]] += op.dx;
  new_s.history[turn] = op;
  return new_s;
}
//#####################################################

auto beam_search(State &init_state){
    vector<State> now;
    now.emplace_back(init_state);
    vector<State> next;
    vector<Evaluator> cand;
    now.reserve(beam_width);
    next.reserve(beam_width);
    cand.reserve(2*beam_width);

    // 遷移候補 
    vector<Operation> possible_op = {
      {1},
      {-1}
    };


    for (int turn = 0; turn < MAX_TURN; turn++){
        bool sorted = false;
        for (int i = 0; i < now.size(); i++){
            const State& s = now[i];
            // 候補を生成
            for (int j = 0; j < possible_op.size(); j++){
                // 状態を変化させたときの評価値を計
                auto new_evaluator = calc_new_eval(s, i, possible_op[j], j, turn);

                // スコア最大化のとき, ソート済みの中で最小の評価値よりも大きい場合のみ追加
                if (sorted && new_evaluator.eval <= cand[beam_width-1].eval) continue;
                // スコア最小化のとき, ソート済みの中で最大の評価値よりも小さい場合のみ追加
                // if (sorted && new_evaluator.eval >= cand[beam_width-1].eval) continue;

                cand.emplace_back(new_evaluator);

                // ソート
                if (cand.size() >= 2*beam_width){
                    sort(cand.begin(), cand.end(), comp_max);
                    cand.resize(beam_width);
                    sorted = true;
                }
            }
        }
        if (cand.empty()) break;
        sort(cand.begin(), cand.end(), comp_max);
        if (cand.size() > beam_width) cand.resize(beam_width);
        // 遷移を実行
        for (auto &e: cand){
            State new_s = operate(now[e.parent_state_index], e, possible_op[e.operation_index], turn);
            next.emplace_back(new_s);
        }

        swap(now, next);
        if (turn != MAX_TURN-1) {
          cand.clear();
          next.clear();
        }
    }
  return now[0];
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);
  int _T; cin >> _T;
  for (int i=0; i<T; i++){
    cin >> P[i] >> Q[i] >> R[i];
    P[i]--; Q[i]--; R[i]--;
  }

  State init_state(0, 100);
  fill(init_state.X, init_state.X+100, 0);

  auto best_state = beam_search(init_state);
  cerr << "best eval: " << best_state.eval << "\n";
  for (auto op: best_state.history){
    if (op.dx == 1) cout << 'A' << "\n";
    else cout << 'B' << "\n";
  }
}