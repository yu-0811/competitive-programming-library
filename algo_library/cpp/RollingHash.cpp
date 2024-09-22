#include <bits/stdc++.h>
using namespace std;

class RollingHash {
private:
    long long base;
    vector<unsigned long long> hash, base_pow;
    const unsigned long long MASK30 = (1UL << 30) - 1;
    const unsigned long long MASK31 = (1UL << 31) - 1;
    const unsigned long long MOD = (1UL << 61) - 1;
    const unsigned long long MASK61 = MOD;
    const unsigned long long POSITIVIZER = MOD * 4;

    // a*b mod 2^61-1を返す関数
    unsigned long long Mul(unsigned long long a, unsigned long long b) {
        unsigned long long au = a >> 31;
        unsigned long long ad = a & MASK31;
        unsigned long long bu = b >> 31;
        unsigned long long bd = b & MASK31;
        unsigned long long mid = ad * bu + au * bd;
        unsigned long long midu = mid >> 30;
        unsigned long long midd = mid & MASK30;
        return CalcMod(au * bu * 2 + midu + (midd << 31) + ad * bd);
    }

    // mod 2^61-1を計算する関数
    unsigned long long CalcMod(unsigned long long x) {
        unsigned long long xu = x >> 61;
        unsigned long long xd = x & MASK61;
        unsigned long long res = xu + xd;
        if (res >= MOD) res -= MOD;
        return res;
    }

public:
    RollingHash(const string &S,long long base = 1237) : base(base) {
        int N = S.size();
        hash.assign(N + 1, 0);
        base_pow.assign(N + 1, 1);
        for (int i = 0; i < N; ++i) {
            base_pow[i + 1] = Mul(base_pow[i], base);
        }
        for (int i = 0; i < N; ++i) {
            long long tmp = S[i] - 'a' + 1; // 0 を割り当ててはいけない
            hash[i + 1] = CalcMod(Mul(hash[i], base) + tmp);
        }
    }

    unsigned long long get_hash(int l, int r) { // [l, r)
        unsigned long long result = CalcMod(hash[r] + POSITIVIZER - Mul(hash[l], base_pow[r - l]));
        return result;
    }
};