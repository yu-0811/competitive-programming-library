#include <bits/stdc++.h>
using namespace std;

long long cal(long long a1, long long n, long long d) {
    if (n == 0) return 0;
    return n * (2 * a1 + (n - 1) * d) / 2;
}
