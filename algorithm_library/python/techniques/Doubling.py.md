---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def doubling(dp,LEN,POW):\n  for i in range(1,POW):\n    for j in range(LEN):\n\
    \      dp[i][j] = dp[i-1][dp[i-1][j]]\n  return dp\n\ndef query(dp,j,k):\n  tmp\
    \ = j\n  i = 0\n  while k:\n    if k&1: tmp = dp[i][tmp]\n    k >>= 1\n    i +=\
    \ 1\n  return tmp"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Doubling.py
  requiredBy: []
  timestamp: '2025-02-07 14:18:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Doubling.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Doubling.py
- /library/algorithm_library/python/techniques/Doubling.py.html
title: algorithm_library/python/techniques/Doubling.py
---
