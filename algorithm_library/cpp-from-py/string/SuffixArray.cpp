#include <bits/stdc++.h>
using namespace std;

vector<int> sa_is(const vector<int>& s, int upper) {
    int n = (int)s.size();
    if (n == 0) return {};
    if (n == 1) return {0};
    if (n == 2) return s[0] < s[1] ? vector<int>{0, 1} : vector<int>{1, 0};
    vector<int> sa(n), ls(n);
    for (int i = n - 2; i >= 0; i--) ls[i] = (s[i] == s[i + 1]) ? ls[i + 1] : (s[i] < s[i + 1]);
    vector<int> sum_l(upper + 1), sum_s(upper + 1);
    for (int i = 0; i < n; i++) {
        if (!ls[i]) sum_s[s[i]]++;
        else sum_l[s[i] + 1]++;
    }
    for (int i = 0; i <= upper; i++) {
        sum_s[i] += sum_l[i];
        if (i < upper) sum_l[i + 1] += sum_s[i];
    }
    auto induce = [&](const vector<int>& lms) {
        fill(sa.begin(), sa.end(), -1);
        vector<int> buf = sum_s;
        for (int d : lms) {
            if (d == n) continue;
            sa[buf[s[d]]++] = d;
        }
        buf = sum_l;
        sa[buf[s[n - 1]]++] = n - 1;
        for (int i = 0; i < n; i++) {
            int v = sa[i];
            if (v >= 1 && !ls[v - 1]) sa[buf[s[v - 1]]++] = v - 1;
        }
        buf = sum_l;
        for (int i = n - 1; i >= 0; i--) {
            int v = sa[i];
            if (v >= 1 && ls[v - 1]) sa[--buf[s[v - 1] + 1]] = v - 1;
        }
    };
    vector<int> lms_map(n + 1, -1);
    int m = 0;
    for (int i = 1; i < n; i++) if (!ls[i - 1] && ls[i]) lms_map[i] = m++;
    vector<int> lms;
    for (int i = 1; i < n; i++) if (!ls[i - 1] && ls[i]) lms.push_back(i);
    induce(lms);
    if (m) {
        vector<int> sorted_lms;
        for (int v : sa) if (v >= 0 && lms_map[v] != -1) sorted_lms.push_back(v);
        vector<int> rec_s(m);
        int rec_upper = 0;
        rec_s[lms_map[sorted_lms[0]]] = 0;
        for (int i = 1; i < m; i++) {
            int l = sorted_lms[i - 1], r = sorted_lms[i];
            int end_l = (lms_map[l] + 1 < m) ? lms[lms_map[l] + 1] : n;
            int end_r = (lms_map[r] + 1 < m) ? lms[lms_map[r] + 1] : n;
            bool same = true;
            if (end_l - l != end_r - r) same = false;
            else {
                while (l < end_l) {
                    if (s[l] != s[r]) break;
                    l++;
                    r++;
                }
                if (l == n || s[l] != s[r]) same = false;
            }
            if (!same) rec_upper++;
            rec_s[lms_map[sorted_lms[i]]] = rec_upper;
        }
        vector<int> rec_sa = sa_is(rec_s, rec_upper);
        for (int i = 0; i < m; i++) sorted_lms[i] = lms[rec_sa[i]];
        induce(sorted_lms);
    }
    return sa;
}

vector<int> suffix_array_upper(const vector<int>& s, int upper) {
    assert(0 <= upper);
    for (int d : s) assert(0 <= d && d <= upper);
    return sa_is(s, upper);
}

vector<int> suffix_array(const string& s) {
    vector<int> s2(s.size());
    for (int i = 0; i < (int)s.size(); i++) s2[i] = (unsigned char)s[i];
    return sa_is(s2, 255);
}

template <class T>
vector<int> suffix_array(const vector<T>& s) {
    int n = (int)s.size();
    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int i, int j) { return s[i] < s[j]; });
    vector<int> s2(n);
    int now = 0;
    for (int i = 0; i < n; i++) {
        if (i && s[idx[i - 1]] != s[idx[i]]) now++;
        s2[idx[i]] = now;
    }
    return sa_is(s2, now);
}

vector<int> lcp_array(const string& s, const vector<int>& sa) {
    int n = (int)s.size();
    assert(n >= 1);
    vector<int> rnk(n), lcp(n - 1);
    for (int i = 0; i < n; i++) rnk[sa[i]] = i;
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (h > 0) h--;
        if (rnk[i] == 0) continue;
        int j = sa[rnk[i] - 1];
        while (j + h < n && i + h < n && s[j + h] == s[i + h]) h++;
        lcp[rnk[i] - 1] = h;
    }
    return lcp;
}
