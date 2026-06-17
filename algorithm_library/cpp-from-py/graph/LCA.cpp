#include <bits/stdc++.h>
using namespace std;

struct LCA {
    int N, bit;
    vector<vector<int>> parent;
    vector<int> depth;

    LCA(int N_, const vector<vector<int>>& G, int root) : N(N_) {
        bit = 32 - __builtin_clz(N) + 2;
        parent.assign(bit, vector<int>(N + 1, -1));
        depth.assign(N + 1, -1);
        depth[root] = 0;
        queue<int> que;
        que.push(root);
        while (!que.empty()) {
            int v = que.front();
            que.pop();
            for (int v2 : G[v]) {
                if (depth[v2] == -1) {
                    depth[v2] = depth[v] + 1;
                    parent[0][v2] = v;
                    que.push(v2);
                }
            }
        }
        for (int i = 1; i < bit; i++) {
            for (int j = 0; j <= N; j++) {
                if (parent[i - 1][j] != -1) parent[i][j] = parent[i - 1][parent[i - 1][j]];
            }
        }
    }

    int lca(int u, int v) const {
        if (depth[u] < depth[v]) swap(u, v);
        for (int k = 0; k < bit; k++) if (((depth[u] - depth[v]) >> k) & 1) u = parent[k][u];
        if (u == v) return u;
        for (int k = bit - 1; k >= 0; k--) {
            if (parent[k][u] != parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    }

    int get_distance(int u, int v) const {
        return depth[u] + depth[v] - 2 * depth[lca(u, v)];
    }

    bool is_on_path(int u, int v, int a) const {
        return get_distance(u, a) + get_distance(a, v) == get_distance(u, v);
    }
};
