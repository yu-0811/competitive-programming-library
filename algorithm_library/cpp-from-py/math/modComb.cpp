#include <bits/stdc++.h>
using namespace std;

struct Comb {
    int k;
    long long mod;
    vector<long long> fact_inv, inv;

    Comb(int k_, long long mod_) : k(k_), mod(mod_), fact_inv(k + 1, 0), inv(k + 1, 0) {
        fact_inv[0] = 1;
        if (k >= 1) fact_inv[1] = 1, inv[1] = 1;
        for (int i = 2; i <= k; i++) {
            inv[i] = mod - inv[mod % i] * (mod / i) % mod;
            fact_inv[i] = fact_inv[i - 1] * inv[i] % mod;
        }
    }

    long long nCk(long long n, int kk) const {
        if (kk < 0 || kk > n) return 0;
        if (kk > k) throw invalid_argument("precomputed k is too small");
        long long ans = 1;
        for (int i = 0; i < kk; i++) ans = ans * ((n - i) % mod) % mod;
        return ans * fact_inv[kk] % mod;
    }
};

struct CombAll {
    int n;
    long long mod;
    vector<long long> fact, factinv, inv;

    CombAll(int n_, long long mod_) : n(n_), mod(mod_), fact{1, 1}, factinv{1, 1}, inv{0, 1} {
        for (int i = 2; i <= n; i++) {
            fact.push_back(fact[i - 1] * i % mod);
            inv.push_back((mod - inv[mod % i] * (mod / i) % mod) % mod);
            factinv.push_back(factinv[i - 1] * inv[i] % mod);
        }
    }

    long long C(int nn, int kk) const {
        assert(nn <= n);
        if (kk < 0 || nn < 0 || nn < kk) return 0;
        if (kk == 1) return nn;
        kk = min(kk, nn - kk);
        return fact[nn] * factinv[kk] % mod * factinv[nn - kk] % mod;
    }

    long long H(int nn, int r) const {
        return C(nn + r - 1, r);
    }
};
