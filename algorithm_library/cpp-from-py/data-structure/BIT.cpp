#include <bits/stdc++.h>
using namespace std;

struct BIT {
    int n;
    vector<vector<long long>> bit;

    BIT(int n_) : n(n_ + 1), bit(2, vector<long long>(n, 0)) {}

    void _add_sub(int p, int i, long long x) {
        for (int idx = i; idx < n; idx += idx & -idx) bit[p][idx] += x;
    }

    void add(int l, int r, long long x) {
        _add_sub(0, l, -x * (l - 1));
        _add_sub(0, r, x * (r - 1));
        _add_sub(1, l, x);
        _add_sub(1, r, -x);
    }

    long long _sum_sub(int p, int i) const {
        long long s = 0;
        for (int idx = i; idx > 0; idx -= idx & -idx) s += bit[p][idx];
        return s;
    }

    long long SUM(int i) const {
        return _sum_sub(0, i) + _sum_sub(1, i) * i;
    }

    long long range_sum(int l, int r) const {
        return SUM(r - 1) - SUM(l - 1);
    }

    int lower_bound(long long w) const {
        if (w <= 0) return 0;
        int x = 0, len = 1;
        while (len < n) len <<= 1;
        while (len > 0) {
            if (x + len < n && bit[1][x + len] < w) {
                w -= bit[1][x + len];
                x += len;
            }
            len >>= 1;
        }
        return x + 1;
    }
};
