#include <bits/stdc++.h>
using namespace std;

struct CrossAccumulate {
    int H, W;
    vector<vector<long long>> s;

    CrossAccumulate(const vector<vector<long long>>& grid) {
        H = (int)grid.size();
        W = (int)grid[0].size();
        s.assign(H + 1, vector<long long>(W + 1, 0));
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + grid[i][j];
            }
        }
    }

    long long query(int r1, int c1, int r2, int c2) const {
        assert(0 <= r1 && r1 <= r2 && r2 < H && 0 <= c1 && c1 <= c2 && c2 < W);
        return s[r2 + 1][c2 + 1] - s[r1][c2 + 1] - s[r2 + 1][c1] + s[r1][c1];
    }
};
