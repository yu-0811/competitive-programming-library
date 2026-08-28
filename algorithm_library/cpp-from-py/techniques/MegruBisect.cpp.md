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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/techniques/MegruBisect.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class Judge>\npair<long\
    \ long, long long> megru_bisect(long long ng, long long ok, Judge judge) {\n \
    \   while (abs(ok - ng) > 1) {\n        long long mid = (ok + ng) / 2;\n     \
    \   if (judge(mid)) ok = mid;\n        else ng = mid;\n    }\n    return {ng,\
    \ ok};\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\ntemplate <class Judge>\n\
    pair<long long, long long> megru_bisect(long long ng, long long ok, Judge judge)\
    \ {\n    while (abs(ok - ng) > 1) {\n        long long mid = (ok + ng) / 2;\n\
    \        if (judge(mid)) ok = mid;\n        else ng = mid;\n    }\n    return\
    \ {ng, ok};\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/techniques/MegruBisect.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/techniques/MegruBisect.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/techniques/MegruBisect.cpp
- /library/algorithm_library/cpp-from-py/techniques/MegruBisect.cpp.html
title: algorithm_library/cpp-from-py/techniques/MegruBisect.cpp
---
