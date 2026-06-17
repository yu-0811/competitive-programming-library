#include <bits/stdc++.h>
using namespace std;

vector<bool> range_eratosthenes(long long L, long long R) {
    assert(L <= R);
    long long sqrtR = sqrt((long double)R) + 1;
    vector<bool> is_prime_base(sqrtR + 1, true);
    vector<bool> is_prime(R - L + 1, true);
    if (L == 0) is_prime[0] = false;
    if (L <= 1 && 1 <= R) is_prime[1 - L] = false;
    for (long long p = 2; p <= sqrtR; p++) {
        if (!is_prime_base[p]) continue;
        for (long long q = p * 2; q <= sqrtR; q += p) is_prime_base[q] = false;
        long long start = L + ((p - L % p) % p);
        if (start == p) start = p * 2;
        for (long long q = start; q <= R; q += p) is_prime[q - L] = false;
    }
    return is_prime;
}
