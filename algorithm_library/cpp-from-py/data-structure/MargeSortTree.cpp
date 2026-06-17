#include <bits/stdc++.h>
using namespace std;

template <class T>
struct MergeSortTree {
    int n, size;
    vector<vector<T>> tree;

    MergeSortTree(const vector<T>& data) {
        n = (int)data.size();
        size = 1;
        while (size < n) size <<= 1;
        tree.assign(2 * size, {});
        for (int i = 0; i < n; i++) tree[size + i] = {data[i]};
        for (int i = size - 1; i > 0; i--) {
            tree[i].resize(tree[2 * i].size() + tree[2 * i + 1].size());
            merge(tree[2 * i].begin(), tree[2 * i].end(), tree[2 * i + 1].begin(), tree[2 * i + 1].end(), tree[i].begin());
        }
    }

    int query_leq(int l, int r, const T& x) const {
        l += size;
        r += size;
        int res = 0;
        while (l < r) {
            if (l & 1) res += upper_bound(tree[l].begin(), tree[l].end(), x) - tree[l].begin(), l++;
            if (r & 1) --r, res += upper_bound(tree[r].begin(), tree[r].end(), x) - tree[r].begin();
            l >>= 1;
            r >>= 1;
        }
        return res;
    }

    int query_range(int l, int r, const T& a, const T& b) const {
        l += size;
        r += size;
        int res = 0;
        while (l < r) {
            if (l & 1) {
                res += lower_bound(tree[l].begin(), tree[l].end(), b) - lower_bound(tree[l].begin(), tree[l].end(), a);
                l++;
            }
            if (r & 1) {
                --r;
                res += lower_bound(tree[r].begin(), tree[r].end(), b) - lower_bound(tree[r].begin(), tree[r].end(), a);
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
};
