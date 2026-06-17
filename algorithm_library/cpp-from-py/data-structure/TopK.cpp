#include <bits/stdc++.h>
using namespace std;

struct SumTopK {
    int N, K;
    vector<long long> A;
    multiset<long long> ok, ng;
    long long ans = 0;

    SumTopK(int N_, vector<long long> A_, int K_) : N(N_), K(K_), A(move(A_)) {
        for (int i = 0; i < K; i++) ok.insert(0);
        for (int i = 0; i < N - K; i++) ng.insert(0);
    }

    void add(long long y) {
        ok.insert(y);
        ans += y;
        long long yy = *ok.begin();
        ans -= yy;
        ok.erase(ok.begin());
        ng.insert(yy);
    }

    void DEL(long long y) {
        if (K > 0 && !ok.empty() && y >= *ok.begin()) {
            auto it = ok.find(y);
            if (it != ok.end()) {
                ok.erase(it);
                ans -= y;
                if (!ng.empty()) {
                    auto jt = prev(ng.end());
                    long long yy = *jt;
                    ng.erase(jt);
                    ok.insert(yy);
                    ans += yy;
                }
            }
        } else {
            auto it = ng.find(y);
            if (it != ng.end()) ng.erase(it);
        }
    }

    long long update(int x, long long y) {
        add(y);
        DEL(A[x]);
        A[x] = y;
        return ans;
    }
};
