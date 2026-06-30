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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nvector<pair<char, int>> run_length_compression(const\
    \ string& S) {\n    vector<pair<char, int>> res;\n    if (S.empty()) return res;\n\
    \    char tmp = S[0];\n    int cnt = 1;\n    for (int i = 1; i < (int)S.size();\
    \ i++) {\n        if (S[i] == tmp) cnt++;\n        else {\n            res.emplace_back(tmp,\
    \ cnt);\n            tmp = S[i];\n            cnt = 1;\n        }\n    }\n   \
    \ res.emplace_back(tmp, cnt);\n    return res;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<pair<char, int>>\
    \ run_length_compression(const string& S) {\n    vector<pair<char, int>> res;\n\
    \    if (S.empty()) return res;\n    char tmp = S[0];\n    int cnt = 1;\n    for\
    \ (int i = 1; i < (int)S.size(); i++) {\n        if (S[i] == tmp) cnt++;\n   \
    \     else {\n            res.emplace_back(tmp, cnt);\n            tmp = S[i];\n\
    \            cnt = 1;\n        }\n    }\n    res.emplace_back(tmp, cnt);\n   \
    \ return res;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp
  requiredBy: []
  timestamp: '2026-06-30 23:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp
- /library/algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp.html
title: algorithm_library/cpp-from-py/techniques/RunLengthCompression.cpp
---
