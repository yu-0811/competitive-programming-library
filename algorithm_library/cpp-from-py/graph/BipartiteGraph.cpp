#include <bits/stdc++.h>
using namespace std;

pair<bool, vector<int>> is_bipartite_graph(const vector<vector<int>>& G, int N) {
    vector<int> col(N + 1, -1);
    auto bfs = [&](int s) {
        queue<int> que;
        que.push(s);
        while (!que.empty()) {
            int v = que.front();
            que.pop();
            for (int v2 : G[v]) {
                if (col[v2] != -1) {
                    if (col[v] == col[v2]) return false;
                    continue;
                }
                col[v2] = 1 - col[v];
                que.push(v2);
            }
        }
        return true;
    };
    for (int v = 1; v <= N; v++) {
        if (col[v] != -1) continue;
        col[v] = 1;
        if (!bfs(v)) return {false, {}};
    }
    return {true, col};
}
