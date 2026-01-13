
// S: Sparse Table で扱うデータ型
// op: 演算関数 (S op(S, S))
template <class S, S (*op)(S, S)>
class SparseTable {
    int n;
    vector<vector<S>> table;
    vector<int> log_table;

public:
    SparseTable() {}
    SparseTable(const vector<S>& v) {
        n = v.size();
        log_table.resize(n + 1);
        log_table[1] = 0;
        for (int i = 2; i <= n; i++) log_table[i] = log_table[i >> 1] + 1;

        int max_k = log_table[n] + 1;
        table.assign(max_k, vector<S>(n));

        for (int i = 0; i < n; i++) table[0][i] = v[i];

        for (int k = 1; k < max_k; k++) {
            int half = 1 << (k - 1);
            for (int i = 0; i + (1 << k) <= n; i++) {
                table[k][i] = op(table[k - 1][i], table[k - 1][i + half]);
            }
        }
    }

    S prod(int l, int r) {
        int b = r - l;
        int k = log_table[b];
        return op(table[k][l], table[k][r - (1 << k)]);
    }
};