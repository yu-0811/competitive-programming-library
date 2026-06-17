#include <bits/stdc++.h>
using namespace std;

template <class T, class Op>
struct SparseTable2D {
    int H, W, K, L;
    Op op;
    vector<vector<vector<vector<T>>>> table;

    SparseTable2D(const vector<vector<T>>& grid, Op op) : op(op) {
        H = (int)grid.size();
        W = (int)grid[0].size();
        K = 32 - __builtin_clz(H);
        L = 32 - __builtin_clz(W);
        table.assign(K, vector<vector<vector<T>>>(L, vector<vector<T>>(H, vector<T>(W))));
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) table[0][0][i][j] = grid[i][j];
        }
        for (int l = 1; l < L; l++) {
            int width = 1 << l, half = width >> 1;
            for (int i = 0; i < H; i++) {
                for (int j = 0; j + width <= W; j++) {
                    table[0][l][i][j] = op(table[0][l - 1][i][j], table[0][l - 1][i][j + half]);
                }
            }
        }
        for (int k = 1; k < K; k++) {
            int height = 1 << k, half = height >> 1;
            for (int l = 0; l < L; l++) {
                int width = 1 << l;
                for (int i = 0; i + height <= H; i++) {
                    for (int j = 0; j + width <= W; j++) {
                        table[k][l][i][j] = op(table[k - 1][l][i][j], table[k - 1][l][i + half][j]);
                    }
                }
            }
        }
    }

    T query(int r1, int c1, int r2, int c2) const {
        assert(0 <= r1 && r1 <= r2 && r2 < H);
        assert(0 <= c1 && c1 <= c2 && c2 < W);
        int height = r2 - r1 + 1, width = c2 - c1 + 1;
        int k = 31 - __builtin_clz(height);
        int l = 31 - __builtin_clz(width);
        int r2_start = r2 - (1 << k) + 1;
        int c2_start = c2 - (1 << l) + 1;
        T tl = table[k][l][r1][c1];
        T tr = table[k][l][r1][c2_start];
        T bl = table[k][l][r2_start][c1];
        T br = table[k][l][r2_start][c2_start];
        return op(op(tl, tr), op(bl, br));
    }
};
