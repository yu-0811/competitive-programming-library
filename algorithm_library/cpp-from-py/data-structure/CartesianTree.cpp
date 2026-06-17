#include <bits/stdc++.h>
using namespace std;

template <class T>
struct CartesianTree {
    int root;
    vector<int> left, right, parent;

    CartesianTree(const vector<T>& A) {
        int n = (int)A.size();
        root = 0;
        left.assign(n, -1);
        right.assign(n, -1);
        parent.assign(n, -1);
        vector<int> st(n, -1);
        st[0] = 0;
        int st_top = 0;
        for (int i = 1; i < n; i++) {
            if (A[st[st_top]] > A[i]) {
                while (st_top >= 1 && A[st[st_top - 1]] > A[i]) st_top--;
                left[i] = st[st_top];
                parent[left[i]] = i;
                if (st_top == 0) {
                    root = i;
                } else {
                    parent[i] = st[st_top - 1];
                    right[parent[i]] = i;
                }
                st[st_top] = i;
            } else {
                parent[i] = st[st_top];
                right[parent[i]] = i;
                st_top++;
                st[st_top] = i;
            }
        }
    }
};
