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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def doubling(dp, LEN, POW):\n    for i in range(1, POW):\n        prev, cur\
    \ = dp[i - 1], dp[i]\n        for j in range(LEN):\n            cur[j] = prev[prev[j]]\n\
    \    return dp\n\n\ndef query(dp, j, k):\n    \"\"\"\n    j \u304B\u3089\u59CB\
    \u3081\u3066 k \u56DE\u79FB\u52D5\u3059\u308B\n    \"\"\"\n    tmp = j\n    while\
    \ k:\n        i = k.bit_length() - 1\n        tmp = dp[i][tmp]\n        k ^= 1\
    \ << i\n    return tmp\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Doubling.py
  requiredBy: []
  timestamp: '2026-10-20 11:41:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Doubling.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Doubling.py
- /library/algorithm_library/python/techniques/Doubling.py.html
title: algorithm_library/python/techniques/Doubling.py
---
