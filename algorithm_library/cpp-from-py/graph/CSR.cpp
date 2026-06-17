#include <bits/stdc++.h>
using namespace std;

pair<vector<int>, vector<int>> csr(int N, const vector<pair<int, int>>& graphEdges) {
    vector<int> start(N + 1, 0), endList(graphEdges.size());
    for (auto [u, v] : graphEdges) start[u + 1]++;
    for (int i = 1; i <= N; i++) start[i] += start[i - 1];
    vector<int> pointer = start;
    for (auto [u, v] : graphEdges) endList[pointer[u]++] = v;
    return {start, endList};
}

template <class Cost = long long>
struct Graph {
    int N, M;
    vector<int> start;
    vector<tuple<int, int, optional<Cost>>> buf;
    vector<pair<int, optional<Cost>>> endList;

    Graph(int n, int m) : N(n + 1), M(m), start(N + 1, 0), endList(m) {}

    void add_edge(int u, int v, optional<Cost> cost = nullopt) {
        buf.emplace_back(u, v, cost);
        start[u]++;
        if ((int)buf.size() == M) build();
    }

    void build() {
        partial_sum(start.begin(), start.end(), start.begin());
        for (auto [u, v, c] : buf) {
            start[u]--;
            endList[start[u]] = {v, c};
        }
    }

    vector<pair<int, optional<Cost>>> get_edges(int u) const {
        return vector<pair<int, optional<Cost>>>(endList.begin() + start[u], endList.begin() + start[u + 1]);
    }
};
