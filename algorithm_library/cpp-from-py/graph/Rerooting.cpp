#include <bits/stdc++.h>
using namespace std;

template <class T, class Merge, class CalcNodeValue, class CalcAns>
struct rerooting {
    int n;
    T identity;
    Merge merge;
    CalcNodeValue calc_node_value;
    CalcAns calc_ans;
    vector<vector<int>> adjacents, indexForAdjacents;
    vector<vector<T>> childSubTreeValue;
    vector<T> ans;
    vector<int> parent, order;

    rerooting(int n_, const vector<pair<int, int>>& edges, T identity_, Merge merge_, CalcNodeValue calc_node_value_, CalcAns calc_ans_)
        : n(n_), identity(identity_), merge(merge_), calc_node_value(calc_node_value_), calc_ans(calc_ans_),
          adjacents(n + 1), indexForAdjacents(n + 1), ans(n + 1, identity) {
        for (auto [a, b] : edges) {
            indexForAdjacents[a].push_back(adjacents[b].size());
            indexForAdjacents[b].push_back(adjacents[a].size());
            adjacents[a].push_back(b);
            adjacents[b].push_back(a);
        }
        childSubTreeValue.resize(n + 1);
        for (int i = 0; i <= n; i++) childSubTreeValue[i].assign(adjacents[i].size(), identity);
    }

    void dfs1(int root) {
        parent.assign(n + 1, -1);
        order.clear();
        vector<int> st{root};
        while (!st.empty()) {
            int v = st.back();
            st.pop_back();
            order.push_back(v);
            for (int u : adjacents[v]) {
                if (u == parent[v]) continue;
                parent[u] = v;
                st.push_back(u);
            }
        }
        for (int oi = (int)order.size() - 1; oi >= 1; oi--) {
            int v = order[oi], pv = parent[v];
            T result = identity;
            int parentIndex = -1;
            for (int i = 0; i < (int)adjacents[v].size(); i++) {
                int u = adjacents[v][i];
                if (u == pv) {
                    parentIndex = i;
                    continue;
                }
                result = merge(result, childSubTreeValue[v][i]);
            }
            childSubTreeValue[pv][indexForAdjacents[v][parentIndex]] = calc_node_value(result, v);
        }
    }

    void dfs2() {
        for (int v : order) {
            T accFromLeft = identity;
            vector<T> accFromRight(adjacents[v].size(), identity);
            for (int i = (int)adjacents[v].size() - 2; i >= 0; i--) {
                accFromRight[i] = merge(childSubTreeValue[v][i + 1], accFromRight[i + 1]);
            }
            for (int j = 0; j < (int)adjacents[v].size(); j++) {
                int u = adjacents[v][j];
                T result = calc_node_value(merge(accFromLeft, accFromRight[j]), v);
                childSubTreeValue[u][indexForAdjacents[v][j]] = result;
                accFromLeft = merge(accFromLeft, childSubTreeValue[v][j]);
            }
            ans[v] = calc_ans(accFromLeft, v);
        }
    }

    vector<T> run(int root = 1) {
        dfs1(root);
        dfs2();
        return ans;
    }
};
