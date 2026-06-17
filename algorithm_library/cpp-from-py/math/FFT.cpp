#include <bits/stdc++.h>
using namespace std;

struct FFT {
    int mod, g;

    FFT(int MOD) : mod(MOD), g(primitive_root_constexpr(MOD)) {}

    long long modpow(long long a, long long e) const {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }

    static int primitive_root_constexpr(int m) {
        if (m == 2) return 1;
        if (m == 167772161) return 3;
        if (m == 469762049) return 3;
        if (m == 754974721) return 11;
        if (m == 998244353) return 3;
        vector<int> divs;
        int x = (m - 1) / 2;
        divs.push_back(2);
        while (x % 2 == 0) x /= 2;
        for (long long i = 3; i * i <= x; i += 2) {
            if (x % i == 0) {
                divs.push_back((int)i);
                while (x % i == 0) x /= i;
            }
        }
        if (x > 1) divs.push_back(x);
        for (int g = 2;; g++) {
            bool ok = true;
            for (int d : divs) {
                long long r = 1, a = g, e = (m - 1) / d;
                while (e) {
                    if (e & 1) r = r * a % m;
                    a = a * a % m;
                    e >>= 1;
                }
                if (r == 1) {
                    ok = false;
                    break;
                }
            }
            if (ok) return g;
        }
    }

    void ntt(vector<long long>& a, bool inverse) const {
        int n = (int)a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }
        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = modpow(g, (mod - 1) / len);
            if (inverse) wlen = modpow(wlen, mod - 2);
            for (int i = 0; i < n; i += len) {
                long long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long long u = a[i + j];
                    long long v = a[i + j + len / 2] * w % mod;
                    a[i + j] = (u + v) % mod;
                    a[i + j + len / 2] = (u - v + mod) % mod;
                    w = w * wlen % mod;
                }
            }
        }
        if (inverse) {
            long long inv_n = modpow(n, mod - 2);
            for (auto& x : a) x = x * inv_n % mod;
        }
    }

    vector<long long> convolution(vector<long long> a, vector<long long> b) const {
        int n = (int)a.size(), m = (int)b.size();
        if (n == 0 || m == 0) return {};
        if (min(n, m) <= 40) {
            vector<long long> res(n + m - 1);
            for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) res[i + j] = (res[i + j] + a[i] * b[j]) % mod;
            return res;
        }
        int z = 1;
        while (z < n + m - 1) z <<= 1;
        a.resize(z);
        b.resize(z);
        ntt(a, false);
        ntt(b, false);
        for (int i = 0; i < z; i++) a[i] = a[i] * b[i] % mod;
        ntt(a, true);
        a.resize(n + m - 1);
        return a;
    }
};
