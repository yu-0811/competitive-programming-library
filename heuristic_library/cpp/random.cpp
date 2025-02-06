#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long

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