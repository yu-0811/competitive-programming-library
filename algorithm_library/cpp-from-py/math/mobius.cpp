#include <bits/stdc++.h>
using namespace std;

template <class T>
vector<T>& mobius(vector<T>& A) {
    int n = 0;
    while ((1 << n) < (int)A.size()) n++;
    assert((int)A.size() == (1 << n));
    for (int i = 0; i < n; i++) {
        int bit = 1 << i;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (!(mask & bit)) A[mask] -= A[mask | bit];
        }
    }
    return A;
}
