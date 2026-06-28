---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/graph/EulerTour.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct FenwickTree {\n    int n;\n\
    \    vector<long long> data;\n    FenwickTree(int N = 0) : n(N), data(N, 0) {}\n\
    \    void add(int p, long long x) {\n        assert(0 <= p && p < n);\n      \
    \  for (p++; p <= n; p += p & -p) data[p - 1] += x;\n    }\n    long long sum0(int\
    \ r) const {\n        long long s = 0;\n        for (; r > 0; r -= r & -r) s +=\
    \ data[r - 1];\n        return s;\n    }\n    long long sum(int l, int r) const\
    \ {\n        assert(0 <= l && l <= r && r <= n);\n        return sum0(r) - sum0(l);\n\
    \    }\n};\n\nstruct PairMinSegtree {\n    int n, size;\n    pair<long long, int>\
    \ e = {(long long)1e18, (int)1e9};\n    vector<pair<long long, int>> data;\n \
    \   PairMinSegtree() {}\n    PairMinSegtree(const vector<pair<long long, int>>&\
    \ V) {\n        n = (int)V.size();\n        size = 1;\n        while (size < n)\
    \ size <<= 1;\n        data.assign(2 * size, e);\n        for (int i = 0; i <\
    \ n; i++) data[size + i] = V[i];\n        for (int i = size - 1; i > 0; i--) data[i]\
    \ = min(data[2 * i], data[2 * i + 1]);\n    }\n    pair<long long, int> prod(int\
    \ l, int r) const {\n        pair<long long, int> sml = e, smr = e;\n        for\
    \ (l += size, r += size; l < r; l >>= 1, r >>= 1) {\n            if (l & 1) sml\
    \ = min(sml, data[l++]);\n            if (r & 1) smr = min(data[--r], smr);\n\
    \        }\n        return min(sml, smr);\n    }\n};\n\nstruct EulerTour {\n \
    \   int N, edge_cnt = 0, root = 1;\n    vector<vector<tuple<int, long long, int>>>\
    \ G;\n    vector<int> in, out, edge_order, vertex_order, edge_idx_plus, edge_idx_minus;\n\
    \    vector<long long> edge_cost, depth;\n    vector<bool> vis;\n    FenwickTree\
    \ fen;\n    PairMinSegtree lca_seg;\n\n    EulerTour(int N_) : N(N_), G(N + 1),\
    \ in(N + 1, -1), out(N + 1, -1), depth{-1} {}\n\n    void add_edge(int u, int\
    \ v, long long w) {\n        edge_cnt++;\n        G[u].emplace_back(v, w, edge_cnt);\n\
    \        G[v].emplace_back(u, w, edge_cnt);\n    }\n\n    void dfs(int root_)\
    \ {\n        vector<tuple<int, int, long long, int>> st;\n        st.emplace_back(0,\
    \ root_, 0, 0);\n        while (!st.empty()) {\n            auto [state, v, w,\
    \ idx] = st.back();\n            st.pop_back();\n            if (state == 0) {\n\
    \                if (vis[v]) continue;\n                vis[v] = true;\n     \
    \           depth.push_back(depth.back() + 1);\n                edge_order.push_back(idx);\n\
    \                edge_cost.push_back(w);\n                in[v] = (int)edge_order.size()\
    \ - 1;\n                out[v] = (int)edge_order.size() - 1;\n               \
    \ vertex_order.push_back(v);\n                for (auto [u, ww, edge_idx] : G[v])\
    \ {\n                    if (vis[u]) continue;\n                    st.emplace_back(1,\
    \ v, ww, edge_idx);\n                    st.emplace_back(0, u, ww, edge_idx);\n\
    \                }\n            } else {\n                depth.push_back(depth.back()\
    \ - 1);\n                vertex_order.push_back(-v);\n                edge_order.push_back(-idx);\n\
    \                edge_cost.push_back(-w);\n                out[v] = (int)edge_order.size()\
    \ - 1;\n            }\n        }\n    }\n\n    void build(int root_) {\n     \
    \   root = root_;\n        edge_idx_plus.assign(edge_cnt + 1, -1);\n        edge_idx_minus.assign(edge_cnt\
    \ + 1, -1);\n        vis.assign(N + 1, false);\n        dfs(root);\n        depth.erase(depth.begin());\n\
    \        fen = FenwickTree(edge_cost.size());\n        for (int i = 1; i < (int)edge_cost.size();\
    \ i++) fen.add(i, edge_cost[i]);\n        vector<pair<long long, int>> s;\n  \
    \      for (int i = 0; i < (int)depth.size(); i++) s.emplace_back(depth[i], abs(vertex_order[i]));\n\
    \        lca_seg = PairMinSegtree(s);\n    }\n\n    long long subtree_sum(int\
    \ u) const { return fen.sum0(in[u] + 1); }\n    long long path_sum(int u) const\
    \ { return fen.sum0(in[u] + 1); }\n    int lca(int u, int v) const {\n       \
    \ int in_u = in[u], in_v = in[v];\n        if (in_u > in_v) swap(in_u, in_v);\n\
    \        return lca_seg.prod(in_u, in_v + 1).second;\n    }\n    long long get_distance(int\
    \ u, int v) const {\n        int w = lca(u, v);\n        return subtree_sum(u)\
    \ + subtree_sum(v) - 2 * subtree_sum(w);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct FenwickTree {\n\
    \    int n;\n    vector<long long> data;\n    FenwickTree(int N = 0) : n(N), data(N,\
    \ 0) {}\n    void add(int p, long long x) {\n        assert(0 <= p && p < n);\n\
    \        for (p++; p <= n; p += p & -p) data[p - 1] += x;\n    }\n    long long\
    \ sum0(int r) const {\n        long long s = 0;\n        for (; r > 0; r -= r\
    \ & -r) s += data[r - 1];\n        return s;\n    }\n    long long sum(int l,\
    \ int r) const {\n        assert(0 <= l && l <= r && r <= n);\n        return\
    \ sum0(r) - sum0(l);\n    }\n};\n\nstruct PairMinSegtree {\n    int n, size;\n\
    \    pair<long long, int> e = {(long long)1e18, (int)1e9};\n    vector<pair<long\
    \ long, int>> data;\n    PairMinSegtree() {}\n    PairMinSegtree(const vector<pair<long\
    \ long, int>>& V) {\n        n = (int)V.size();\n        size = 1;\n        while\
    \ (size < n) size <<= 1;\n        data.assign(2 * size, e);\n        for (int\
    \ i = 0; i < n; i++) data[size + i] = V[i];\n        for (int i = size - 1; i\
    \ > 0; i--) data[i] = min(data[2 * i], data[2 * i + 1]);\n    }\n    pair<long\
    \ long, int> prod(int l, int r) const {\n        pair<long long, int> sml = e,\
    \ smr = e;\n        for (l += size, r += size; l < r; l >>= 1, r >>= 1) {\n  \
    \          if (l & 1) sml = min(sml, data[l++]);\n            if (r & 1) smr =\
    \ min(data[--r], smr);\n        }\n        return min(sml, smr);\n    }\n};\n\n\
    struct EulerTour {\n    int N, edge_cnt = 0, root = 1;\n    vector<vector<tuple<int,\
    \ long long, int>>> G;\n    vector<int> in, out, edge_order, vertex_order, edge_idx_plus,\
    \ edge_idx_minus;\n    vector<long long> edge_cost, depth;\n    vector<bool> vis;\n\
    \    FenwickTree fen;\n    PairMinSegtree lca_seg;\n\n    EulerTour(int N_) :\
    \ N(N_), G(N + 1), in(N + 1, -1), out(N + 1, -1), depth{-1} {}\n\n    void add_edge(int\
    \ u, int v, long long w) {\n        edge_cnt++;\n        G[u].emplace_back(v,\
    \ w, edge_cnt);\n        G[v].emplace_back(u, w, edge_cnt);\n    }\n\n    void\
    \ dfs(int root_) {\n        vector<tuple<int, int, long long, int>> st;\n    \
    \    st.emplace_back(0, root_, 0, 0);\n        while (!st.empty()) {\n       \
    \     auto [state, v, w, idx] = st.back();\n            st.pop_back();\n     \
    \       if (state == 0) {\n                if (vis[v]) continue;\n           \
    \     vis[v] = true;\n                depth.push_back(depth.back() + 1);\n   \
    \             edge_order.push_back(idx);\n                edge_cost.push_back(w);\n\
    \                in[v] = (int)edge_order.size() - 1;\n                out[v] =\
    \ (int)edge_order.size() - 1;\n                vertex_order.push_back(v);\n  \
    \              for (auto [u, ww, edge_idx] : G[v]) {\n                    if (vis[u])\
    \ continue;\n                    st.emplace_back(1, v, ww, edge_idx);\n      \
    \              st.emplace_back(0, u, ww, edge_idx);\n                }\n     \
    \       } else {\n                depth.push_back(depth.back() - 1);\n       \
    \         vertex_order.push_back(-v);\n                edge_order.push_back(-idx);\n\
    \                edge_cost.push_back(-w);\n                out[v] = (int)edge_order.size()\
    \ - 1;\n            }\n        }\n    }\n\n    void build(int root_) {\n     \
    \   root = root_;\n        edge_idx_plus.assign(edge_cnt + 1, -1);\n        edge_idx_minus.assign(edge_cnt\
    \ + 1, -1);\n        vis.assign(N + 1, false);\n        dfs(root);\n        depth.erase(depth.begin());\n\
    \        fen = FenwickTree(edge_cost.size());\n        for (int i = 1; i < (int)edge_cost.size();\
    \ i++) fen.add(i, edge_cost[i]);\n        vector<pair<long long, int>> s;\n  \
    \      for (int i = 0; i < (int)depth.size(); i++) s.emplace_back(depth[i], abs(vertex_order[i]));\n\
    \        lca_seg = PairMinSegtree(s);\n    }\n\n    long long subtree_sum(int\
    \ u) const { return fen.sum0(in[u] + 1); }\n    long long path_sum(int u) const\
    \ { return fen.sum0(in[u] + 1); }\n    int lca(int u, int v) const {\n       \
    \ int in_u = in[u], in_v = in[v];\n        if (in_u > in_v) swap(in_u, in_v);\n\
    \        return lca_seg.prod(in_u, in_v + 1).second;\n    }\n    long long get_distance(int\
    \ u, int v) const {\n        int w = lca(u, v);\n        return subtree_sum(u)\
    \ + subtree_sum(v) - 2 * subtree_sum(w);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/graph/EulerTour.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/graph/EulerTour.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/graph/EulerTour.cpp
- /library/algorithm_library/cpp-from-py/graph/EulerTour.cpp.html
title: algorithm_library/cpp-from-py/graph/EulerTour.cpp
---
