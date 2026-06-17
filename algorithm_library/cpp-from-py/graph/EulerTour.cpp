#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> data;
    FenwickTree(int N = 0) : n(N), data(N, 0) {}
    void add(int p, long long x) {
        assert(0 <= p && p < n);
        for (p++; p <= n; p += p & -p) data[p - 1] += x;
    }
    long long sum0(int r) const {
        long long s = 0;
        for (; r > 0; r -= r & -r) s += data[r - 1];
        return s;
    }
    long long sum(int l, int r) const {
        assert(0 <= l && l <= r && r <= n);
        return sum0(r) - sum0(l);
    }
};

struct PairMinSegtree {
    int n, size;
    pair<long long, int> e = {(long long)1e18, (int)1e9};
    vector<pair<long long, int>> data;
    PairMinSegtree() {}
    PairMinSegtree(const vector<pair<long long, int>>& V) {
        n = (int)V.size();
        size = 1;
        while (size < n) size <<= 1;
        data.assign(2 * size, e);
        for (int i = 0; i < n; i++) data[size + i] = V[i];
        for (int i = size - 1; i > 0; i--) data[i] = min(data[2 * i], data[2 * i + 1]);
    }
    pair<long long, int> prod(int l, int r) const {
        pair<long long, int> sml = e, smr = e;
        for (l += size, r += size; l < r; l >>= 1, r >>= 1) {
            if (l & 1) sml = min(sml, data[l++]);
            if (r & 1) smr = min(data[--r], smr);
        }
        return min(sml, smr);
    }
};

struct EulerTour {
    int N, edge_cnt = 0, root = 1;
    vector<vector<tuple<int, long long, int>>> G;
    vector<int> in, out, edge_order, vertex_order, edge_idx_plus, edge_idx_minus;
    vector<long long> edge_cost, depth;
    vector<bool> vis;
    FenwickTree fen;
    PairMinSegtree lca_seg;

    EulerTour(int N_) : N(N_), G(N + 1), in(N + 1, -1), out(N + 1, -1), depth{-1} {}

    void add_edge(int u, int v, long long w) {
        edge_cnt++;
        G[u].emplace_back(v, w, edge_cnt);
        G[v].emplace_back(u, w, edge_cnt);
    }

    void dfs(int root_) {
        vector<tuple<int, int, long long, int>> st;
        st.emplace_back(0, root_, 0, 0);
        while (!st.empty()) {
            auto [state, v, w, idx] = st.back();
            st.pop_back();
            if (state == 0) {
                if (vis[v]) continue;
                vis[v] = true;
                depth.push_back(depth.back() + 1);
                edge_order.push_back(idx);
                edge_cost.push_back(w);
                in[v] = (int)edge_order.size() - 1;
                out[v] = (int)edge_order.size() - 1;
                vertex_order.push_back(v);
                for (auto [u, ww, edge_idx] : G[v]) {
                    if (vis[u]) continue;
                    st.emplace_back(1, v, ww, edge_idx);
                    st.emplace_back(0, u, ww, edge_idx);
                }
            } else {
                depth.push_back(depth.back() - 1);
                vertex_order.push_back(-v);
                edge_order.push_back(-idx);
                edge_cost.push_back(-w);
                out[v] = (int)edge_order.size() - 1;
            }
        }
    }

    void build(int root_) {
        root = root_;
        edge_idx_plus.assign(edge_cnt + 1, -1);
        edge_idx_minus.assign(edge_cnt + 1, -1);
        vis.assign(N + 1, false);
        dfs(root);
        depth.erase(depth.begin());
        fen = FenwickTree(edge_cost.size());
        for (int i = 1; i < (int)edge_cost.size(); i++) fen.add(i, edge_cost[i]);
        vector<pair<long long, int>> s;
        for (int i = 0; i < (int)depth.size(); i++) s.emplace_back(depth[i], abs(vertex_order[i]));
        lca_seg = PairMinSegtree(s);
    }

    long long subtree_sum(int u) const { return fen.sum0(in[u] + 1); }
    long long path_sum(int u) const { return fen.sum0(in[u] + 1); }
    int lca(int u, int v) const {
        int in_u = in[u], in_v = in[v];
        if (in_u > in_v) swap(in_u, in_v);
        return lca_seg.prod(in_u, in_v + 1).second;
    }
    long long get_distance(int u, int v) const {
        int w = lca(u, v);
        return subtree_sum(u) + subtree_sum(v) - 2 * subtree_sum(w);
    }
};
