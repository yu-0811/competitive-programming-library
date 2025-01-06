#include <bits/stdc++.h>
#include <chrono>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long

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

// 温度関数////////////////////////////////
// 開始温度
constexpr double tempInit = 500;
// 終了温度
constexpr double tempFinish = 10;
double temp = tempInit;
constexpr int timeLimit = 4950;

// 線形の温度関数
// (焼きなまし開始時間,現在時間)
double linearTemp(double &startTime, double &nowTime){
  return tempInit - (tempInit - tempFinish) * (nowTime - startTime) / timeLimit ;
}

// 遷移確率関数 /////////////////////////////
// (新スコア,旧スコア,温度)

// スコアの最大化問題のとき
// newScore>=prevScore のとき確率は 1 以上
double calcProbability_Maximum(ll &newScore, ll &prevScore, double &temp){
  return exp((newScore - prevScore)/temp);
}

// スコアの最小化問題の問題
double calcProbability_Minimum(ll &newScore, ll &prevScore, double &temp){
  return exp((prevScore - newScore)/temp);
}


// 使用例/////////////////////////////
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

// 状態遷移
void transitionState(vector<int> &state){
  
  ll nex_score;
  if (calcProbability_Maximum(nex_score,SCORE,temp) > Random::random()){
    SCORE = nex_score;
    // 遷移する
  }
  else{
    // 状態を戻す
  }
}

Timer timer;
double NOW_TIME = 0.0;
ll SCORE = 0;
vector<int> state; // 状態

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  timer = Timer(); // タイマー初期化
  
  int ITER_CNT = 0; // 焼きなまし実行回数
  double SA_START_TIME = timer.get_ms();
  // 焼きなまし開始
  while (true){
    if (ITER_CNT%1000==0){// 高速化のために 1000 回に 1 回だけ時間計測する
      NOW_TIME = timer.get_ms();
      if (NOW_TIME>timeLimit) break; 
      temp = linearTemp(SA_START_TIME, NOW_TIME); // 温度もついでに
    }

    transitionState(state);
  }
}