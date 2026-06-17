#include <bits/stdc++.h>
using namespace std;

int compare(pair<long long, long long> a, pair<long long, long long> b) {
    auto [ax, ay] = a;
    auto [bx, by] = b;
    int ah = (ay < 0 || (ay == 0 && ax < 0)) ? 1 : 0;
    int bh = (by < 0 || (by == 0 && bx < 0)) ? 1 : 0;
    if (ah != bh) return ah < bh ? -1 : 1;
    long long cross = ax * by - ay * bx;
    if (cross > 0) return -1;
    if (cross < 0) return 1;
    return 0;
}

bool angular_less(pair<long long, long long> a, pair<long long, long long> b) {
    return compare(a, b) < 0;
}

bool is_same_angle(pair<long long, long long> p1, pair<long long, long long> p2) {
    auto [ax, ay] = p1;
    auto [bx, by] = p2;
    if (ax * by - ay * bx != 0) return false;
    return ax * bx + ay * by > 0;
}
