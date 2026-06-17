#include <bits/stdc++.h>
using namespace std;

struct maxflow_edge {
    int to, rev_idx;
    long long cap;
};

struct maximum_flow {
    int N;
    vector<vector<maxflow_edge>> G;
    vector<bool> vis;

    maximum_flow(int N_) : N(N_), G(N + 1) {}

    void add_edge(int a, int b, long long c) {
        G[a].push_back({b, (int)G[b].size(), c});
        G[b].push_back({a, (int)G[a].size() - 1, 0});
    }

    long long dfs(int v, int goal, long long f) {
        if (v == goal) return f;
        vis[v] = true;
        for (auto& edge : G[v]) {
            if (edge.cap > 0 && !vis[edge.to]) {
                long long flow = dfs(edge.to, goal, min(f, edge.cap));
                if (flow >= 1) {
                    edge.cap -= flow;
                    G[edge.to][edge.rev_idx].cap += flow;
                    return flow;
                }
            }
        }
        return 0;
    }

    long long maxflow(int start, int goal) {
        long long total_flow = 0;
        while (true) {
            vis.assign(N + 1, false);
            long long res = dfs(start, goal, (long long)1e18);
            if (res > 0) total_flow += res;
            else break;
        }
        return total_flow;
    }
};
