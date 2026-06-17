#include <bits/stdc++.h>
using namespace std;

struct PotentialUnionFind {
    int N;
    vector<int> parents;
    vector<long long> potential;
    vector<bool> inconsistent;
    const long long inf = (long long)1e18;

    PotentialUnionFind(int N_) : N(N_), parents(N + 1, -1), potential(N + 1, 0), inconsistent(N + 1, false) {}

    int root(int x) {
        if (parents[x] < 0) return x;
        int p = parents[x];
        int r = root(p);
        potential[x] += potential[p];
        parents[x] = r;
        return r;
    }

    long long dist(int x, int y) {
        int rx = root(x), ry = root(y);
        if (rx == ry) return potential[y] - potential[x];
        return inf;
    }

    bool union_(int x, int y, long long w) {
        int rx = root(x), ry = root(y);
        if (rx == ry) {
            if (potential[y] - potential[x] != w) inconsistent[rx] = true;
            return potential[y] - potential[x] == w;
        }
        if (parents[ry] > parents[rx]) {
            parents[rx] += parents[ry];
            potential[ry] = potential[x] + w - potential[y];
            parents[ry] = rx;
        } else {
            parents[ry] += parents[rx];
            potential[rx] = potential[y] - w - potential[x];
            parents[rx] = ry;
        }
        return true;
    }

    int size(int x) { return -parents[root(x)]; }
    bool isSame(int x, int y) { return root(x) == root(y); }
    vector<int> members(int x) {
        int r = root(x);
        vector<int> res;
        for (int i = 1; i <= N; i++) if (root(i) == r) res.push_back(i);
        return res;
    }
    vector<int> roots() {
        vector<int> res;
        for (int i = 1; i <= N; i++) if (parents[i] < 0) res.push_back(i);
        return res;
    }
    int group_count() { return (int)roots().size(); }
};
