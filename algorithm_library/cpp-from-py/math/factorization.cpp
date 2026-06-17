#include <bits/stdc++.h>
using namespace std;

vector<int> init_factorization(int N) {
    vector<int> D(N + 1, 1);
    for (int i = 2; i <= N; i++) {
        if (D[i] != 1) continue;
        for (int j = i; j <= N; j += i) {
            if (D[j] == 1) D[j] = i;
        }
    }
    return D;
}

map<int, int> factorization(int x, const vector<int>& D) {
    map<int, int> res;
    while (x != 1) {
        res[D[x]]++;
        x /= D[x];
    }
    return res;
}
