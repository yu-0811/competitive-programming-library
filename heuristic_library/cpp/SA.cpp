#include "template.cpp"

// パラメータ ///////////////////////////////////
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
// スコアの差分更新に使う配列などを持つ
struct WorkSpace {
    Score score;
};

// 最良解を保持するための構造体
// WorkSpace のうち、スコアと解の出力に必要な情報だけを持つ
struct Answer {
    Score score;
    // 「Answer = WorkSpace」という代入を可能にする (演算子オーバーロード)
    Answer& operator=(const WorkSpace& sol) {
        score = sol.score;
        return *this;
    }
};

// 入力

// 初期解生成
WorkSpace make_initial_solution(){
    WorkSpace res{};

    return res;
}

Score initialize_score(WorkSpace &sol) {
    Score score = 0;

    return score;
}

// 近傍生成 + スコア計算 + 受容判定 + 状態更新 -> 近傍生成が成功したかどうか を返す
// 状態は sol を直接書き換える
bool generate_neighborhood(auto &temp, WorkSpace &sol) {
    // 近傍生成


    // スコア計算 


    if (calc_prob(now_score, next_score, temp) > Random::random()) {

        return true;
    }
    else {
        // 状態をもとに戻す

        return true;
    }
}

Answer SA() {
    unsigned int counter = 0; unsigned int iter = 0; unsigned int failed_neighborhood = 0;
    auto SA_start_time = timer.get_ms();
    float temp = start_temp;

    WorkSpace current_solution = make_initial_solution();
    auto best_score = current_solution.score;
    Answer best_ans;
    best_ans = current_solution;
    cerr << "start score: " << current_solution.score << "\n";
    auto now_time = timer.get_ms();

    while (true) {
        if (counter == 30) {
            now_time = timer.get_ms();
            if (now_time > time_limit) break;
            temp = linear_temp(SA_start_time, now_time);
            counter = 0;
        }
        if (!generate_neighborhood(temp, current_solution)) {
            failed_neighborhood++;
        }
        if (is_better(current_solution.score, best_score)) {
            best_score = current_solution.score;
            best_ans = current_solution;
        }
        iter++; counter++;
    }
    cerr << "best score: " << best_score << "\n";
    cerr << "iter: " << iter << "\n";
    cerr << "successful neighborhood: " << iter - failed_neighborhood << "\n";
    return best_ans;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(0);
    timer = Timer();
    // get_param(); // optuna を使うときはコメントアウトを外す

    // 入力 //////////////////////////////////////////
    
    //////////////////////////////////////////////////

    Answer best_ans = SA();

    // 出力 //////////////////////////////////////////

    //////////////////////////////////////////////////
}
