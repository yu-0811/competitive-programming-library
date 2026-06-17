#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> WarshallFloyd(int N, const vector<vector<pair<int, long long>>>& G, long long inf = (long long)1e18) {
    vector<vector<long long>> dist(N + 1, vector<long long>(N + 1, inf));
    for (int i = 0; i <= N; i++) dist[i][i] = 0;
    for (int i = 1; i <= N; i++) {
        for (auto [j, c] : G[i]) {
            dist[i][j] = min(dist[i][j], c);
            dist[j][i] = min(dist[j][i], c);
        }
    }
    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (dist[i][k] == inf || dist[k][j] == inf) continue;
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    return dist;
}
