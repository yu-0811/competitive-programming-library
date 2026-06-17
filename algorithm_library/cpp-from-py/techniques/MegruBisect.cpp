#include <bits/stdc++.h>
using namespace std;

template <class Judge>
pair<long long, long long> megru_bisect(long long ng, long long ok, Judge judge) {
    while (abs(ok - ng) > 1) {
        long long mid = (ok + ng) / 2;
        if (judge(mid)) ok = mid;
        else ng = mid;
    }
    return {ng, ok};
}
