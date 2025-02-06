#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long

const int beam_width = 70000;

struct Move {
    char d; int p;
};

struct State {
    int score;
    vector<Move> move_history;
    vector<string> board;
    
    State() : score(0), move_history(0) {}
};

// 評価関数########################################
// スコア最大化のとき
bool comp_max(const State &a1, const State &a2){
    return a1.score > a2.score;
}
// スコア最小化のとき
bool comp_min(const State &a1, const State &a2){
    return a1.score < a2.score;
}
//#####################################################


// 状態遷移関数########################################
State operate(State s, int op, int &i){

}
//#####################################################

auto beam_search(State &init_state, int beam_width, int depth){
    vector<State> now;
    now.emplace_back(init_state);
    vector<State> next;

    for (int i=0; i<depth; i++){
        bool sorted = false;
        for (auto &s : now){
            // 状態を遷移させる
            for (auto op: {-1,1}){
                // 状態を変化させたときの評価値を計算###############
                int nex_score;
                //#################################################

                // スコア最大化のとき, ソート済みの中で最小の評価値よりも大きい場合のみ遷移
                if (sorted && nex_score <= next[beam_width-1].score) continue;
                // スコア最小化のとき, ソート済みの中で最大の評価値よりも小さい場合のみ遷移
                // if (sorted && nex_score >= next[beam_width-1].score) continue;

                auto nex = operate(s, op, i);
                next.emplace_back(nex);

                if (next.size() >= 2*beam_width){
                    sort(next.begin(), next.end(), comp_max);
                    next.resize(beam_width);
                    sorted = true;
                }
            }
        }
        sort(next.begin(), next.end(), comp_max);
        swap(now, next);
        next.clear();
    }

    return now[0].move_history;
}