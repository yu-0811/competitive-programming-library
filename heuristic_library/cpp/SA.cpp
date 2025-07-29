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
        uint32_t t = x ^ (x << 11);
        x = y; y = z; z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }
public:
    // [0, x)
    inline static uint32_t randrange(unsigned x) { return xorshift() % x; }
    // [x, y)
    inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x) + x; }
    // [0.0, 1.0)
    inline static double random() { return (xorshift() + 0.5) * (1.0 / UINT_MAX); }
};

// 時間計測
class Timer {
    chrono::time_point<chrono::steady_clock> start;
public:
    Timer() : start(chrono::steady_clock::now()) {}
    long long get_ms() { // 経過時間を返す
        auto now_time = chrono::steady_clock::now();
        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();
    }
};
Timer timer;

// パラメータ ///////////////////////////////////
constexpr int time_limit = 1990; // 単位 ms
// 提出用
constexpr double start_temp = 200;
constexpr double end_temp = 1;

// optuna 用
// constexpr double default_start_temp = 200;
// constexpr double default_end_temp = 1;
// double start_temp = defalut_start_temp;
// double end_temp = defalut_end_temp;
// void get_param() {
//   const char* st = std::getenv("start_temp");
//   if (st != nullptr) {
//       start_temp = std::stoi(std::string(st));
//   }
//   const char* et = std::getenv("end_temp");
//   if (et != nullptr) {
//       end_temp = std::stod(std::string(et));
//   }
// }
////////////////////////////////////////////////

// 線形温度管理
double linear_temp(double &SA_start_time, double &now_time) {
    return start_temp - (start_temp - end_temp) * (now_time - SA_start_time) / time_limit;
}

// 遷移確率関数
// スコア最大化のとき
double calc_prob_maximize(auto &now_score, auto &next_score, double &temp) {
    if (next_score > now_score) return 1.0;
    return exp((next_score - now_score) / temp);
}

// スコア最小化のとき
double calc_prob_minimize(auto &now_score, auto &next_score, double &temp) {
    if (next_score < now_score) return 1.0;
    return exp((now_score - next_score) / temp);
}

double calc_score(int &idx){
  return;
}

auto initialize_score(){
  return;
}

// 近傍生成 + スコア計算 + 受容判定 -> 新しいスコアを返す /////////////////
auto generate_neighborhood(auto &now_score, auto &temp){
  // 近傍生成 //////////////////////////////////////

  //////////////////////////////////////////////////
  // スコア計算 ////////////////////////////////////
  auto next_score
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

unsigned int counter = 0;
void SA() {
  double SA_start_time = timer.get_ms();
  unsigned int iter = 1;
  double temp = start_temp;
  double now_score = initialize_score();
  cerr << "start score: " << now_score << endl;
  while (true) {
    if (counter == 500) {
      double now_time = timer.get_ms();
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