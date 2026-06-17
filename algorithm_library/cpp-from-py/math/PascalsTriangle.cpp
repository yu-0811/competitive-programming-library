#include <bits/stdc++.h>
using namespace std;

struct PascalsTriangle {
    long long mod;
    vector<vector<long long>> binom;

    PascalsTriangle(int N, long long mod_) : mod(mod_), binom(N + 1, vector<long long>(N + 1, 0)) {
        for (int i = 0; i <= N; i++) {
            binom[i][0] = 1;
            for (int j = 1; j <= i; j++) binom[i][j] = (binom[i - 1][j - 1] + binom[i - 1][j]) % mod;
        }
    }

    long long C(int n, int k) const {
        assert(0 <= k && k <= n);
        return binom[n][k];
    }

    long long H(int n, int k) const {
        assert(n >= 0 && k >= 0);
        return C(n + k - 1, k);
    }
};
