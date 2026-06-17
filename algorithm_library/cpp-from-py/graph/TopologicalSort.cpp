#include <bits/stdc++.h>
using namespace std;

vector<int> TopologicalSort(int N, const vector<vector<int>>& G) {
    vector<int> sortedVertices, indegree(N + 1, 0);
    for (int v = 1; v <= N; v++) for (int v2 : G[v]) indegree[v2]++;
    queue<int> que;
    for (int v = 1; v <= N; v++) if (indegree[v] == 0) que.push(v);
    while (!que.empty()) {
        int v = que.front();
        que.pop();
        sortedVertices.push_back(v);
        for (int v2 : G[v]) {
            indegree[v2]--;
            if (indegree[v2] == 0) que.push(v2);
        }
    }
    if ((int)sortedVertices.size() != N) return {};
    return sortedVertices;
}
