---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"algo_library/cpp/doubing.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define\
    \ ll long long\nconst int MOD = 998244353;\nconst int INF = 1000000000;\nconst\
    \ ll INFll = 9223372036854775807;\n\nvector<vector<int>> doubling(vector<vector<int>>\
    \ &dp, int LEN, ll POW){\n    for (int i=1; i<POW; i++){\n        for (int j=0;\
    \ j<LEN; j++){\n            dp[i][j] = dp[i-1][dp[i-1][j]];\n        }\n    }\n\
    \    return dp;\n}\n\nint query(vector<vector<int>> &dp, int j, ll k){\n    int\
    \ tmp = j; int i=0;\n    while (k>0){\n        if (k&1){\n            tmp = dp[i][tmp];\n\
    \        }\n        k >>= 1;\n        i += 1;\n    }\n    return tmp;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n#define rep(i, n) for (int\
    \ i = 0; i < (int)(n); i++)\n#define ll long long\nconst int MOD = 998244353;\n\
    const int INF = 1000000000;\nconst ll INFll = 9223372036854775807;\n\nvector<vector<int>>\
    \ doubling(vector<vector<int>> &dp, int LEN, ll POW){\n    for (int i=1; i<POW;\
    \ i++){\n        for (int j=0; j<LEN; j++){\n            dp[i][j] = dp[i-1][dp[i-1][j]];\n\
    \        }\n    }\n    return dp;\n}\n\nint query(vector<vector<int>> &dp, int\
    \ j, ll k){\n    int tmp = j; int i=0;\n    while (k>0){\n        if (k&1){\n\
    \            tmp = dp[i][tmp];\n        }\n        k >>= 1;\n        i += 1;\n\
    \    }\n    return tmp;\n}"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/cpp/doubing.cpp
  requiredBy: []
  timestamp: '2024-11-24 09:52:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/cpp/doubing.cpp
layout: document
redirect_from:
- /library/algo_library/cpp/doubing.cpp
- /library/algo_library/cpp/doubing.cpp.html
title: algo_library/cpp/doubing.cpp
---
