#include <bits/stdc++.h>
using namespace std;

template <class F>
tuple<double, double, double> ternary_search_float(F f, double left, double right, double eps = 1e-9, bool maximize = false) {
    while (right - left > eps) {
        double m1 = (2 * left + right) / 3;
        double m2 = (left + 2 * right) / 3;
        auto f1 = f(m1), f2 = f(m2);
        if (!maximize) {
            if (f1 > f2) left = m1;
            else right = m2;
        } else {
            if (f1 < f2) left = m1;
            else right = m2;
        }
    }
    double x = (left + right) / 2;
    return {left, right, f(x)};
}

template <class F>
auto ternary_search_int(F f, long long left, long long right, long long eps, bool maximize = false) {
    while (right - left > eps) {
        long long m1 = (2 * left + right) / 3;
        long long m2 = (left + 2 * right) / 3;
        auto f1 = f(m1), f2 = f(m2);
        if (!maximize) {
            if (f1 > f2) left = m1;
            else right = m2;
        } else {
            if (f1 < f2) left = m1;
            else right = m2;
        }
    }
    long long best_x = left;
    auto best_val = f(left);
    for (long long x = left + 1; x <= right; x++) {
        auto val = f(x);
        if ((maximize && val > best_val) || (!maximize && val < best_val)) {
            best_val = val;
            best_x = x;
        }
    }
    return pair{best_x, best_val};
}
