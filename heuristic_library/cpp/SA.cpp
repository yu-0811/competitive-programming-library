#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <utility>
#include <climits>
#include <deque>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <cassert>
#include <chrono>
#include <cstring>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long

class Random {
    static uint32_t xorshift() {
        static uint32_t x = 123456789, y = 362436039, z = 521288629, w = 88675123; 
        uint32_t t = x ^ (x << 11); x = y; y = z; z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }
public:
    inline static uint32_t randrange(unsigned x) { return xorshift() % x; } // [0, x)
    inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x) + x; } // [x, y)
    inline static float random() { return (xorshift() + 0.5) * (1.0 / UINT_MAX); } // [0.0, 1.0)
};

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

// パラメータ ///////////////////////////////////
#ifndef ONLINE_JUDGE
    constexpr int time_limit = 1990 + 1000;
#else
    constexpr int time_limit = 1987; // ジャッジでは 1990 ms
#endif
// 提出用
constexpr float start_temp = 500;
constexpr float end_temp = 1;

// optuna 用
// constexpr float default_start_temp = 200;
// constexpr float default_end_temp = 1;
// float start_temp = default_start_temp;
// float end_temp = default_end_temp;
void get_param() {
    const char* p;
    // p = std::getenv("start_temp"); assert(p); start_temp = std::stof(p);
    // p = std::getenv("end_temp"); assert(p); end_temp = std::stof(p);
}
////////////////////////////////////////////////

// 焼きなましに関する関数 /////////////////////////
// 線形温度管理
float linear_temp(unsigned short &SA_start_time, unsigned short &now_time) {
    return start_temp - (start_temp - end_temp) * (now_time - SA_start_time) / time_limit;
}

// 指数温度管理
float expo_temp(unsigned short &SA_start_time, unsigned short &now_time) {
    float p = (float)(now_time - SA_start_time) / time_limit;
    return start_temp * pow(end_temp / start_temp, p);
}

// 遷移確率関数
constexpr bool maximize = false; // false: 最小化, true: 最大化

template<class Score>
bool is_better(const Score& a, const Score& b) {
    if constexpr (maximize) return a > b;
    else return a < b;
}

template<class Score>
double calc_prob(const Score& now_score, const Score& next_score, double temp) {
    if (is_better(next_score, now_score)) return 1.0;
    if constexpr (maximize) {
        return exp((next_score - now_score) / temp);
    } else {
        return exp((now_score - next_score) / temp);
    }
}

// スコアの型
using Score = int;
///////////////////////////////////////////////////////

// ここから下に解法を書く

// 焼きなましで使う構造体
struct WorkSpace {

};

// 最良解を保持するための構造体
// スコアと解の出力に必要な情報だけを持つ
// 焼きなましで使うけど解の構築にはいらない (ex. スコアの差分更新に使う配列など) があるのでこの構成にしている
// WorkSpace が Answer を包含するイメージ
struct Answer {
    Score score;
    // 「Answer = WorkSpace」という代入を可能にする (演算子オーバーロード)
    Answer& operator=(const WorkSpace& sol) {
        return *this;
    }
};

// 入力

// 初期解生成
WorkSpace make_initial_solution(){
    WorkSpace res;

    return res;
}

Score initialize_score(WorkSpace &sol) {
    Score score = 0;

    return score;
}

// 近傍生成 + スコア計算 + 受容判定 + 状態更新 -> 新しいスコア を返す /////////////////
Score generate_neighborhood(Score &now_score, auto &temp, WorkSpace &sol) {
    // 近傍生成 //////////////////////////////////////

    //////////////////////////////////////////////////
    // スコア計算 ////////////////////////////////////

    //////////////////////////////////////////////////
    if (calc_prob(now_score, next_score, temp) > Random::random()) { // TODO: 最小化 or 最大化
        // 状態を更新

        return next_score;
    }
    else {
        // 状態をもとに戻す

        return now_score;
    }
}

Answer SA() {
    unsigned int counter = 0; unsigned int iter = 0;
    auto SA_start_time = timer.get_ms();
    float temp = start_temp;

    WorkSpace current_solution = make_initial_solution();
    Score now_score = initialize_score(current_solution);

    auto best_score = now_score;
    Answer best_solution;
    best_solution = current_solution;
    cerr << "start score: " << now_score << "\n";
    auto now_time = timer.get_ms();

    while (true) {
        if (counter == 30) {
            now_time = timer.get_ms();
            if (now_time > time_limit) break;
            temp = linear_temp(SA_start_time, now_time);
            counter = 0;
        }
        now_score = generate_neighborhood(now_score, temp, current_solution);
        if (is_better(now_score, best_score)) {
            best_score = now_score;
            best_solution = current_solution;
        }
        iter++; counter++;
    }
    cerr << "best score: " << best_score << "\n";
    cerr << "iter: " << iter << "\n";
    return best_solution;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(0);
    timer = Timer();
    // get_param(); // optuna を使うときはコメントアウトを外す

    // 入力 //////////////////////////////////////////
    
    //////////////////////////////////////////////////

    Answer best_solution = SA();

    // 出力 //////////////////////////////////////////

    //////////////////////////////////////////////////
}