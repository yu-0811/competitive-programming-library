#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// S: Disjoint Sparse Table で扱うデータ型
// op: 演算関数 (S op(S, S))
template <class S, S (*op)(S, S)>
class DisjointSparseTable {
    int n;
    vector<vector<S>> table;
    vector<int> log_table;

public:
    DisjointSparseTable() {}
    DisjointSparseTable(const vector<S>& v) {
        n = v.size();
        
        // bit_length相当のテーブルサイズ確保
        int b = 1;
        while (b <= n) b <<= 1;
        log_table.resize(b + 1);
        log_table[1] = 0;
        for (int i = 2; i <= b; i++) log_table[i] = log_table[i >> 1] + 1;

        int max_k = (n == 0) ? 0 : log_table[n] + 1;
        // 配列のサイズが2の累乗でない場合のために少し余裕をもたせる計算
        if ((1 << (max_k - 1)) < n) max_k++;

        table.assign(max_k, vector<S>(n));

        for (int k = 0; k < max_k; k++) {
            int block_size = 1 << (k + 1);
            int half = 1 << k;

            for (int start = 0; start < n; start += block_size) {
                int mid = min(start + half, n);
                int end = min(start + block_size, n);

                // 左側 [start, mid)
                if (start < mid) {
                    table[k][mid - 1] = v[mid - 1];
                    for (int i = mid - 2; i >= start; i--) {
                        table[k][i] = op(v[i], table[k][i + 1]);
                    }
                }

                // 右側 [mid, end)
                if (mid < end) {
                    table[k][mid] = v[mid];
                    for (int i = mid + 1; i < end; i++) {
                        table[k][i] = op(table[k][i - 1], v[i]);
                    }
                }
            }
        }
    }

    S query(int l, int r) {
        if (l == r - 1) return table[0][l];
        int k = log_table[l ^ (r - 1)];
        return op(table[k][l], table[k][r - 1]);
    }
};