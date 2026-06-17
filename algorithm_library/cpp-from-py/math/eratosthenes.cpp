#include <bits/stdc++.h>
using namespace std;

pair<vector<int>, vector<bool>> eratosthenes(int N) {
    vector<int> prime_number;
    vector<bool> isprime(N + 1, true);
    if (N >= 0) isprime[0] = false;
    if (N >= 1) isprime[1] = false;
    for (int p = 2; p <= N; p++) {
        if (!isprime[p]) continue;
        for (long long q = 2LL * p; q <= N; q += p) isprime[q] = false;
    }
    for (int p = 2; p <= N; p++) if (isprime[p]) prime_number.push_back(p);
    return {prime_number, isprime};
}

vector<int> res_primeList(int M) {
    vector<bool> isprime(M + 1, true);
    if (M >= 0) isprime[0] = false;
    if (M >= 1) isprime[1] = false;
    for (int i = 2; i <= M && 1LL * i * i <= M; i++) {
        if (isprime[i]) for (long long j = 1LL * i * i; j <= M; j += i) isprime[j] = false;
    }
    vector<int> res;
    for (int i = 2; i <= M; i++) if (isprime[i]) res.push_back(i);
    return res;
}
