#include <bits/stdc++.h>
using namespace std;

struct SumSegtree {
    int n, size, log;
    unsigned long long mod;
    vector<unsigned long long> data;

    SumSegtree() {}
    SumSegtree(const vector<unsigned long long>& V, unsigned long long mod_) : n(V.size()), mod(mod_) {
        log = 0;
        size = 1;
        while (size < n) size <<= 1, log++;
        data.assign(2 * size, 0);
        for (int i = 0; i < n; i++) data[size + i] = V[i] % mod;
        for (int i = size - 1; i > 0; i--) update(i);
    }

    void update(int k) { data[k] = (data[2 * k] + data[2 * k + 1]) % mod; }
    void set_val(int p, unsigned long long x) {
        assert(0 <= p && p < n);
        p += size;
        data[p] = x % mod;
        for (int i = 1; i <= log; i++) update(p >> i);
    }
    unsigned long long prod(int l, int r) const {
        assert(0 <= l && l <= r && r <= n);
        unsigned long long sml = 0, smr = 0;
        for (l += size, r += size; l < r; l >>= 1, r >>= 1) {
            if (l & 1) sml = (sml + data[l++]) % mod;
            if (r & 1) smr = (data[--r] + smr) % mod;
        }
        return (sml + smr) % mod;
    }
};

struct changeable_RollingHash {
    int N;
    int ord_base = 'a';
    unsigned long long base, mod, inv;
    vector<unsigned long long> base_pow, base_inv;
    SumSegtree seg;

    changeable_RollingHash(const string& S, unsigned long long base_ = 1237, unsigned long long mod_ = (1ULL << 61) - 1)
        : N(S.size()), base(base_), mod(mod_) {
        inv = mod_pow(base, mod - 2);
        base_pow.assign(N + 1, 1);
        base_inv.assign(N + 1, 1);
        for (int i = 0; i < N; i++) {
            base_pow[i + 1] = mul(base_pow[i], base);
            base_inv[i + 1] = mul(base_inv[i], inv);
        }
        vector<unsigned long long> h(N);
        for (int idx = 0; idx < N; idx++) h[idx] = mul(S[idx] - ord_base + 1, base_pow[N - idx - 1]);
        seg = SumSegtree(h, mod);
    }

    unsigned long long mul(unsigned long long a, unsigned long long b) const {
        return (__uint128_t)a * b % mod;
    }

    unsigned long long mod_pow(unsigned long long a, unsigned long long e) const {
        unsigned long long r = 1;
        while (e) {
            if (e & 1) r = (__uint128_t)r * a % mod;
            a = (__uint128_t)a * a % mod;
            e >>= 1;
        }
        return r;
    }

    void change(int x, char c) {
        seg.set_val(x, mul(c - ord_base + 1, base_pow[N - x - 1]));
    }

    unsigned long long get_hash(int l, int r) const {
        return mul(seg.prod(l, r), base_inv[N - r]);
    }
};
