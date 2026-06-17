#include <bits/stdc++.h>
using namespace std;

struct SCC {
    int N;
    vector<pair<int, int>> graphEdges;

    SCC(int N_) : N(N_) {}

    void addEdge(int frm, int to) {
        assert(0 <= frm && frm <= N);
        assert(0 <= to && to <= N);
        graphEdges.emplace_back(frm, to);
    }

    pair<vector<int>, vector<int>> toCSR(int N, const vector<pair<int, int>>& edges) const {
        vector<int> start(N + 1), endList(edges.size());
        for (auto [u, v] : edges) start[u + 1]++;
        for (int i = 1; i <= N; i++) start[i] += start[i - 1];
        vector<int> pointer = start;
        for (auto [u, v] : edges) endList[pointer[u]++] = v;
        return {start, endList};
    }

    pair<int, vector<int>> decomposeToSCC() const {
        auto [start, endList] = toCSR(N, graphEdges);
        int nowOrder = 0, groupNum = 0;
        vector<int> lowlink(N), order(N, -1), groupId(N), pendingStack;
        function<void(int)> dfs = [&](int v) {
            lowlink[v] = order[v] = nowOrder++;
            pendingStack.push_back(v);
            for (int i = start[v]; i < start[v + 1]; i++) {
                int to = endList[i];
                if (order[to] == -1) {
                    dfs(to);
                    lowlink[v] = min(lowlink[v], lowlink[to]);
                } else {
                    lowlink[v] = min(lowlink[v], order[to]);
                }
            }
            if (lowlink[v] == order[v]) {
                while (true) {
                    int u = pendingStack.back();
                    pendingStack.pop_back();
                    order[u] = N;
                    groupId[u] = groupNum;
                    if (u == v) break;
                }
                groupNum++;
            }
        };
        for (int v = 0; v < N; v++) if (order[v] == -1) dfs(v);
        for (int v = 0; v < N; v++) groupId[v] = groupNum - 1 - groupId[v];
        return {groupNum, groupId};
    }

    vector<vector<int>> build_scc() const {
        auto [groupNum, groupId] = decomposeToSCC();
        vector<vector<int>> groups(groupNum);
        for (int v = 0; v < N; v++) groups[groupId[v]].push_back(v);
        return groups;
    }

    vector<vector<int>> build_dag() const {
        auto [groupNum, groupId] = decomposeToSCC();
        vector<vector<int>> dag(groupNum);
        for (auto [u, v] : graphEdges) {
            if (groupId[u] != groupId[v]) dag[groupId[u]].push_back(groupId[v]);
        }
        return dag;
    }
};
