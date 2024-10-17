#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long
const int MOD = 998244353;
const int INF = 1000000000;
const ll INFll = 9223372036854775807;

vector<vector<int>> doubling(vector<vector<int>> &dp, int LEN, ll POW){
    for (int i=1; i<POW; i++){
        for (int j=0; j<LEN; j++){
            dp[i][j] = dp[i-1][dp[i-1][j]];
        }
    }
    return dp;
}

int query(vector<vector<int>> &dp, int j, ll k){
    int tmp = j; int i=0;
    while (k>0){
        if (k&1){
            tmp = dp[i][tmp];
        }
        k >>= 1;
        i += 1;
    }
    return tmp;
}