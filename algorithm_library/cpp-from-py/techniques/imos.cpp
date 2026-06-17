#include <bits/stdc++.h>
using namespace std;

struct imos {
    vector<vector<long long>> grid;

    imos(int H, int W) : grid(H, vector<long long>(W, 0)) {}

    void add(int i0, int j0, int i1, int j1, long long increment) {
        assert(0 <= i0 && i0 <= i1 && i1 < (int)grid.size());
        assert(0 <= j0 && j0 <= j1 && j1 < (int)grid[0].size());
        grid[i0][j0] += increment;
        if (i1 + 1 < (int)grid.size()) grid[i1 + 1][j0] -= increment;
        if (j1 + 1 < (int)grid[0].size()) grid[i0][j1 + 1] -= increment;
        if (i1 + 1 < (int)grid.size() && j1 + 1 < (int)grid[0].size()) grid[i1 + 1][j1 + 1] += increment;
    }

    vector<vector<long long>> cross_accumulate() {
        for (auto& row : grid) {
            for (int j = 1; j < (int)row.size(); j++) row[j] += row[j - 1];
        }
        for (int j = 0; j < (int)grid[0].size(); j++) {
            for (int i = 1; i < (int)grid.size(); i++) grid[i][j] += grid[i - 1][j];
        }
        return grid;
    }
};
