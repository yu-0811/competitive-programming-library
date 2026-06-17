#include <bits/stdc++.h>
using namespace std;

vector<pair<char, int>> run_length_compression(const string& S) {
    vector<pair<char, int>> res;
    if (S.empty()) return res;
    char tmp = S[0];
    int cnt = 1;
    for (int i = 1; i < (int)S.size(); i++) {
        if (S[i] == tmp) cnt++;
        else {
            res.emplace_back(tmp, cnt);
            tmp = S[i];
            cnt = 1;
        }
    }
    res.emplace_back(tmp, cnt);
    return res;
}
