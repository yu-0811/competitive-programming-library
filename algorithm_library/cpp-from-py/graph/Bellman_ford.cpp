#include <bits/stdc++.h>
using namespace std;

const long long inf = (long long)1e18;

pair<vector<long long>, bool> bellman_ford(const vector<tuple<int, int, long long>>& Edges, int N, int s) {
    vector<long long> dist(N + 1, inf);
    dist[s] = 0;
    int cnt = 0;
    while (cnt < N) {
        bool end = true;
        for (auto [fro, to, cost] : Edges) {
            if (dist[fro] == inf) continue;
            if (dist[to] > dist[fro] + cost) {
                dist[to] = dist[fro] + cost;
                end = false;
            }
        }
        if (end) break;
        cnt++;
    }
    return {dist, cnt == N};
}
