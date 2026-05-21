#include <bits/stdc++.h>
using namespace std;

// combinations: n 個から r 個選ぶ
template <class T>
vector<vector<T>> combinations(const vector<T>& a, int r) {
    int n = (int)a.size();
    vector<vector<T>> res;

    if (r < 0 || r > n) return res;

    vector<T> cur;

    auto dfs = [&](auto&& dfs, int start) -> void {
        if ((int)cur.size() == r) {
            res.push_back(cur);
            return;
        }

        int need = r - (int)cur.size();

        for (int i = start; i <= n - need; i++) {
            cur.push_back(a[i]);
            dfs(dfs, i + 1);
            cur.pop_back();
        }
    };

    dfs(dfs, 0);
    return res;
}

// permutations: 長さ r の順列
template <class T>
vector<vector<T>> permutations(const vector<T>& a, int r = -1) {
    int n = (int)a.size();
    if (r == -1) r = n;

    vector<vector<T>> res;
    if (r < 0 || r > n) return res;

    vector<T> cur;
    vector<int> used(n, 0);

    auto dfs = [&](auto&& dfs) -> void {
        if ((int)cur.size() == r) {
            res.push_back(cur);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (used[i]) continue;

            used[i] = 1;
            cur.push_back(a[i]);

            dfs(dfs);

            cur.pop_back();
            used[i] = 0;
        }
    };

    dfs(dfs);
    return res;
}


// product(a, repeat): Python の itertools.product(a, repeat=k)
template <class T>
vector<vector<T>> product(const vector<T>& a, int repeat) {
    vector<vector<T>> pools(repeat, a);
    return product(pools);
}