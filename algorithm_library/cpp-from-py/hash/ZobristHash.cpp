#include <bits/stdc++.h>
using namespace std;

template <class T>
struct ZobristHash {
    static constexpr unsigned long long MAXV = (1ULL << 61) - 1;
    unordered_map<T, unsigned long long> hash_value;
    vector<unsigned long long> hashA, hashB;
    mt19937_64 rng;

    ZobristHash(const vector<T>& A, const vector<T>& B) : rng(chrono::steady_clock::now().time_since_epoch().count()) {
        for (const auto& a : A) hash_value[a] = randint();
        for (const auto& b : B) hash_value[b] = randint();
        hashA = {0};
        hashB = {0};
        unordered_set<T> setA, setB;
        for (const auto& a : A) {
            if (setA.count(a)) hashA.push_back(hashA.back());
            else {
                hashA.push_back(hashA.back() ^ hash_value[a]);
                setA.insert(a);
            }
        }
        for (const auto& b : B) {
            if (setB.count(b)) hashB.push_back(hashB.back());
            else {
                hashB.push_back(hashB.back() ^ hash_value[b]);
                setB.insert(b);
            }
        }
    }

    unsigned long long randint() {
        return uniform_int_distribution<unsigned long long>(1, MAXV)(rng);
    }

    bool isEqual(int al, int ar, int bl, int br) const {
        return (hashA[ar] ^ hashA[al - 1]) == (hashB[br] ^ hashB[bl - 1]);
    }
};
