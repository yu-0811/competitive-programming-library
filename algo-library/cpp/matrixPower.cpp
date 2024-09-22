#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std; using namespace atcoder;
using mint = modint998244353;

// 行列積
vector<vector<mint>> mat_mul(vector<vector<mint>> &A, vector<vector<mint>> &B) {
    vector<vector<mint>> res(A.size(), vector<mint>(B[0].size(), 0));
    for (int i=0; i<A.size(); i++){
        for (int j=0; j<B[0].size(); j++){
            for (int k=0; k<B.size(); k++){
                res[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    return res;
}

// 行列累乗
vector<vector<mint>> mat_pow(vector<vector<mint>> &M, long long K) {
    vector<vector<mint>> res(M.size(), vector<mint>(M.size(), 0));
    // 単位行列初期化
    for (int i=0; i<M.size(); i++) res[i][i] = 1;

    while (K > 0) {
        if (K & 1) res = mat_mul(res, M);
        M = mat_mul(M, M);
        K >>= 1;
    }
    return res;
} 