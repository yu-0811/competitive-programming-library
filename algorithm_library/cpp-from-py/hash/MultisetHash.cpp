#include <bits/stdc++.h>
using namespace std;

template <class T>
struct MultisetHash {
    static constexpr unsigned long long mod = (1ULL << 61) - 1;
    unordered_map<T, unsigned long long> hash_value;
    vector<unsigned long long> hashA, hashB;
    mt19937_64 rng;

    MultisetHash(const vector<T>& A, const vector<T>& B) : rng(chrono::steady_clock::now().time_since_epoch().count()) {
        for (const auto& a : A) hash_value[a] = randint();
        for (const auto& b : B) hash_value[b] = randint();
        hashA = {0};
        hashB = {0};
        for (const auto& a : A) hashA.push_back((hashA.back() + hash_value[a]) % mod);
        for (const auto& b : B) hashB.push_back((hashB.back() + hash_value[b]) % mod);
    }

    unsigned long long randint() {
        return uniform_int_distribution<unsigned long long>(1, mod - 1)(rng);
    }

    bool isEqual(int al, int ar, int bl, int br) const {
        return (hashA[ar] + mod - hashA[al - 1]) % mod == (hashB[br] + mod - hashB[bl - 1]) % mod;
    }
};
