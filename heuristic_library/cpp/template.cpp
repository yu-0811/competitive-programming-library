#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using u64 = unsigned long long;
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

class Random {
    static uint32_t xorshift32() {
        static uint32_t x = 123456789, y = 362436039, z = 521288629, w = 88675123; 
        uint32_t t = x ^ (x << 11);
        x = y; y = z; z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }
public:
    inline static u64 xorshift64() {
        static u64 state = 88172645463325252ULL;
        u64 x = state;
        x ^= x << 7;
        x ^= x >> 9;
        return state = x;
    }
    // [0, x)
    inline static uint32_t randrange(unsigned x) { return xorshift32() % x; }
    // [x, y)
    inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x) + x; }
    // [0.0, 1.0)
    inline static double random() { return (xorshift32() + 0.5) * (1.0 / UINT_MAX); }
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
inline Timer timer;
