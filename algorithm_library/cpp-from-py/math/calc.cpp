#include <bits/stdc++.h>
using namespace std;

long long ceilDiv(long long p, long long q) {
    return (p + q - 1) / q;
}

long long max_leq_congruent(long long R, long long r, long long m) {
    r %= m;
    if (r < 0) r += m;
    return R - ((R - r) % m + m) % m;
}

long long min_geq_congruent(long long L, long long r, long long m) {
    assert(m > 0);
    r %= m;
    if (r < 0) r += m;
    return L + ((r - L) % m + m) % m;
}
