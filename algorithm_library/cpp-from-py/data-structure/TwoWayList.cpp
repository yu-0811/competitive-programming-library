#include <bits/stdc++.h>
using namespace std;

struct TwoWayList {
    static constexpr long long HEAD = -1;
    static constexpr long long TAIL = (long long)1e18;
    unordered_map<long long, long long> front, back;

    TwoWayList(const vector<long long>& L) {
        vector<long long> v;
        v.push_back(HEAD);
        v.insert(v.end(), L.begin(), L.end());
        v.push_back(TAIL);
        for (int i = 0; i + 1 < (int)v.size(); i++) {
            back[v[i]] = v[i + 1];
            front[v[i + 1]] = v[i];
        }
    }

    void insert_front(long long x, long long y) {
        long long a = front[x];
        back[a] = y;
        front[x] = y;
        back[y] = x;
        front[y] = a;
    }

    void insert_back(long long x, long long y) {
        long long b = back[x];
        back[x] = y;
        front[y] = x;
        back[y] = b;
        front[b] = y;
    }

    void del_x(long long x) {
        long long a = front[x], b = back[x];
        back[a] = b;
        front[b] = a;
        front.erase(x);
        back.erase(x);
    }

    vector<long long> res_LIST() const {
        vector<long long> ans;
        long long cur = back.at(HEAD);
        while (cur != TAIL) {
            ans.push_back(cur);
            cur = back.at(cur);
        }
        return ans;
    }
};
