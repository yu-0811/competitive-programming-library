#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
    int n;
    vector<int> parents;

    UnionFind(int n_) : n(n_), parents(n, -1) {}

    int root(int x) {
        if (parents[x] < 0) return x;
        return parents[x] = root(parents[x]);
    }

    int union_(int x, int y) {
        x = root(x);
        y = root(y);
        if (x == y) return x;
        if (parents[x] > parents[y]) swap(x, y);
        parents[x] += parents[y];
        parents[y] = x;
        return x;
    }

    int size(int x) { return -parents[root(x)]; }
    bool isSame(int x, int y) { return root(x) == root(y); }
    vector<int> members(int x) {
        int r = root(x);
        vector<int> res;
        for (int i = 0; i < n; i++) if (root(i) == r) res.push_back(i);
        return res;
    }
    vector<int> roots() const {
        vector<int> res;
        for (int i = 0; i < n; i++) if (parents[i] < 0) res.push_back(i);
        return res;
    }
    int group_count() const { return (int)roots().size(); }
    vector<vector<int>> all_group_members() {
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < n; i++) mp[root(i)].push_back(i);
        vector<vector<int>> res;
        for (auto& [_, v] : mp) res.push_back(v);
        return res;
    }
};
