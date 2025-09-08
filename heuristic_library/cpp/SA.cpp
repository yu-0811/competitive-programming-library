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
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

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
    constexpr int time_limit = 1985 + 2000; 
#else
    constexpr int time_limit = 1990; // ジャッジでは 1990 ms
#endif
// 提出用
constexpr float start_temp = 200;
constexpr float end_temp = 1;

// optuna 用
// constexpr float default_start_temp = 200;
// constexpr float default_end_temp = 1;
// float start_temp = default_start_temp;
// float end_temp = default_end_temp;
void get_param() {
    const char* p;
    // p = std::getenv("r_1"); assert(p); r1 = std::stof(p);
    // p = std::getenv("r_2"); assert(p); r2 = std::stof(p);
    // p = std::getenv("r_3"); assert(p); r3 = std::stof(p);
    // p = std::getenv("r_4"); assert(p); r4 = std::stof(p);
}
////////////////////////////////////////////////

// 線形温度管理
float linear_temp(unsigned short &SA_start_time, unsigned short &now_time) {
    return start_temp - (start_temp - end_temp) * (now_time - SA_start_time) / time_limit;
}

// 遷移確率関数
// スコア最大化のとき
float calc_prob_maximize(auto &now_score, auto &next_score, float &temp) {
    if (next_score > now_score) return 1.0;
    return exp((next_score - now_score) / temp);
}

// スコア最小化のとき
float calc_prob_minimize(auto &now_score, auto &next_score, float &temp) {
    if (next_score < now_score) return 1.0;
    return exp((now_score - next_score) / temp);
}

float calc_score(){
  return 0.0;
}

auto initialize_score(){
  return 0.0;
}

// 近傍生成 + スコア計算 + 受容判定 -> 新しいスコアを返す /////////////////
auto generate_neighborhood(auto &now_score, auto &temp){
  // 近傍生成 //////////////////////////////////////

  //////////////////////////////////////////////////
  // スコア計算 ////////////////////////////////////
  auto next_score = calc_score();
  if (calc_prob_maximize(now_score, next_score, temp) > Random::random()) {
    // 必要であれば状態を更新 ////////////////////

    //////////////////////////////////////////////
    return next_score;
  }
  else {
    // 状態をもとに戻す //////////////////////////

    //////////////////////////////////////////////
    return now_score;
  }
}

void SA() {
  unsigned int counter = 0; unsigned int iter = 0;
  auto SA_start_time = timer.get_ms();
  float temp = start_temp;
  float now_score = initialize_score();
  cerr << "start score: " << now_score << endl;
  while (true) {
    if (counter == 500) {
      auto now_time = timer.get_ms();
      if (now_time > time_limit) break;
      temp = linear_temp(SA_start_time, now_time);
      counter = 0;
    }
    now_score = generate_neighborhood(now_score, temp);
    iter++; counter++;
  }
  cerr << "end score: " << now_score << endl;
  cerr << "iter: " << iter << endl;
}

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  timer = Timer(); // タイマー初期化
  // get_param(); // optuna を使うときはコメントアウトを外す

  // 入力 //////////////////////////////////////////

  //////////////////////////////////////////////////

  SA();

  // 出力 //////////////////////////////////////////

  //////////////////////////////////////////////////
}