#include <bits/stdc++.h>
using namespace std;

template <class T>
vector<int> z_algo(const T& S) {
    int n = (int)S.size();
    vector<int> Z(n);
    if (n == 0) return Z;
    Z[0] = n;
    int i = 1, j = 0;
    while (i < n) {
        while (i + j < n && S[j] == S[i + j]) j++;
        Z[i] = j;
        if (j == 0) {
            i++;
            continue;
        }
        int k = 1;
        while (k < j && k + Z[k] < j) {
            Z[i + k] = Z[k];
            k++;
        }
        i += k;
        j -= k;
    }
    return Z;
}
