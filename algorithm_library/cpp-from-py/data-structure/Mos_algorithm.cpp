#include <bits/stdc++.h>
using namespace std;

template <class Add, class Del, class Answer>
auto mos_algorithm(int n, const vector<pair<int, int>>& queries, Add add, Del del, Answer answer) {
    int q = (int)queries.size();
    int B = max(1, (int)ceil(sqrt(3.0) * n / (sqrt(2.0) * sqrt(max(1, q)))));
    vector<int> order(q);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int i, int j) {
        auto [li, ri] = queries[i];
        auto [lj, rj] = queries[j];
        int bi = li / B, bj = lj / B;
        if (bi != bj) return bi < bj;
        return (bi & 1) ? ri < rj : ri > rj;
    });
    using R = decltype(answer(0));
    vector<R> ret(q);
    int L = 0, Rr = 0;
    for (int i : order) {
        auto [l, r] = queries[i];
        while (Rr < r) add(Rr++);
        while (Rr > r) del(--Rr);
        while (L < l) del(L++);
        while (L > l) add(--L);
        ret[i] = answer(i);
    }
    return ret;
}
