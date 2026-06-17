#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> normalize_vector(long long x1, long long y1, long long x2, long long y2) {
    long long dx = x1 - x2, dy = y1 - y2;
    if (dx == 0) {
        dx = 0;
        dy = 1;
    } else if (dy == 0) {
        dx = 1;
        dy = 0;
    } else {
        if (dx < 0) dx *= -1, dy *= -1;
        long long g = gcd(abs(dx), abs(dy));
        dx /= g;
        dy /= g;
    }
    return {dx, dy};
}

bool on_line(long long x0, long long y0, long long x1, long long y1, long long px, long long py) {
    return (y1 - y0) * (px - x0) == (x1 - x0) * (py - y0);
}

tuple<long long, long long, long long> get_line_abc(long long x0, long long y0, long long x1, long long y1) {
    long long a = y1 - y0;
    long long b = x0 - x1;
    long long c = -(a * x0 + b * y0);
    return {a, b, c};
}

pair<double, double> pos_after_t(double sx, double sy, double gx, double gy, double t, double v, optional<double> dist = nullopt) {
    double dx = gx - sx, dy = gy - sy;
    double d = dist.value_or(sqrt(dx * dx + dy * dy));
    if (d == 0 || v <= 0) return {sx, sy};
    double move = v * t;
    if (move >= d) return {gx, gy};
    double u = move / d;
    return {sx + dx * u, sy + dy * u};
}
