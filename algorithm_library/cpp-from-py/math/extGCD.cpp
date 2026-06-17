#include <bits/stdc++.h>
using namespace std;

tuple<long long, long long, long long> extGCD(long long a, long long b) {
    if (b == 0) return {a, 1, 0};
    auto [g, s, t] = extGCD(b, a % b);
    long long x = t;
    long long y = s - a / b * t;
    return {g, x, y};
}

long long modinv(long long a, long long m) {
    auto [g, x, y] = extGCD(a, m);
    assert(g == 1);
    x %= m;
    if (x < 0) x += m;
    return x;
}

optional<long long> modlin(long long a, long long b, long long m) {
    auto [g, x, y] = extGCD(a, m);
    if (b % g != 0) return nullopt;
    a /= g;
    b /= g;
    m /= g;
    return modinv(a, m) * b % m;
}

pair<optional<long long>, optional<long long>> chineseRem(const vector<long long>& B, const vector<long long>& M) {
    assert(B.size() == M.size());
    long long r = 0, m = 1;
    for (int i = 0; i < (int)B.size(); i++) {
        auto [d, p, q] = extGCD(m, M[i]);
        if ((B[i] - r) % d != 0) return {nullopt, nullopt};
        long long tmp = ((B[i] - r) / d * p) % (M[i] / d);
        r += m * tmp;
        m *= M[i] / d;
        r %= m;
        if (r < 0) r += m;
    }
    return {r, m};
}
