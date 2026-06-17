#include <bits/stdc++.h>
using namespace std;

template <class T>
vector<int> compression(const vector<T>& A) {
    vector<T> xs = A;
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    vector<int> B(A.size());
    for (int i = 0; i < (int)A.size(); i++) {
        B[i] = lower_bound(xs.begin(), xs.end(), A[i]) - xs.begin();
    }
    return B;
}
