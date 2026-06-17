#include <bits/stdc++.h>
using namespace std;

struct eratosthenes {
    int MAX;
    vector<bool> isprime;
    vector<int> mebius, min_factor;

    eratosthenes(int MAX_) : MAX(MAX_), isprime(MAX + 1, true), mebius(MAX + 1, 1), min_factor(MAX + 1, -1) {
        if (MAX >= 0) isprime[0] = false, min_factor[0] = 0;
        if (MAX >= 1) isprime[1] = false, min_factor[1] = 1;
        for (int i = 2; i <= MAX; i++) {
            if (!isprime[i]) continue;
            mebius[i] = -1;
            min_factor[i] = i;
            for (long long j = 2LL * i; j <= MAX; j += i) {
                isprime[j] = false;
                if ((j / i) % i == 0) mebius[j] = 0;
                else mebius[j] *= -1;
                if (min_factor[j] == -1) min_factor[j] = i;
            }
        }
    }

    vector<pair<int, int>> prime_factors(int n) const {
        vector<pair<int, int>> res;
        while (n != 1) {
            int prime = min_factor[n], exp = 0;
            while (n != 1 && min_factor[n] == prime) {
                exp++;
                n /= prime;
            }
            res.emplace_back(prime, exp);
        }
        return res;
    }

    vector<int> divisors(int n) const {
        vector<int> res{1};
        for (auto [prime, exp] : prime_factors(n)) {
            int current_size = (int)res.size();
            for (int i = 0; i < current_size; i++) {
                int value = 1;
                for (int j = 0; j < exp; j++) {
                    value *= prime;
                    res.push_back(res[i] * value);
                }
            }
        }
        return res;
    }
};
