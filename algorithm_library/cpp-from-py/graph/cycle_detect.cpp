#include <bits/stdc++.h>
using namespace std;

vector<int> cycle_detect(int start, const vector<vector<int>>& G) {
    int N = (int)G.size() - 1;
    vector<bool> vis(N + 1, false), fin(N + 1, false);
    vector<int> history;
    stack<pair<int, int>> sta;
    sta.emplace(start, 0);
    int cycle_start = -1;
    while (!sta.empty() && cycle_start == -1) {
        auto [v, prev] = sta.top();
        sta.pop();
        if (prev == -1) {
            if (!history.empty()) history.pop_back();
            fin[v] = true;
            continue;
        }
        if (vis[v]) continue;
        vis[v] = true;
        history.push_back(v);
        for (int v2 : G[v]) {
            if (v2 == prev || fin[v2]) continue;
            if (vis[v2]) {
                cycle_start = v2;
                break;
            }
            sta.emplace(v2, -1);
            sta.emplace(v2, v);
        }
    }
    vector<int> cycle;
    if (cycle_start == -1) return cycle;
    while (!history.empty()) {
        int v = history.back();
        history.pop_back();
        cycle.push_back(v);
        if (v == cycle_start) break;
    }
    return cycle;
}
