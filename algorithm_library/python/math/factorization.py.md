---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc177/editorial/82
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import defaultdict\n\n\"\"\"\n\u9AD8\u901F\u7D20\u56E0\u6570\
    \u5206\u89E3 https://atcoder.jp/contests/abc177/editorial/82\n\u7D20\u56E0\u6570\
    \u5206\u89E3\u3092\u3057\u305F\u3044\u6700\u5927\u306E\u6570\u3092 N \u3068\u3057\
    \u3066\n\u69CB\u7BC9 O(N log log N)\n\u7D20\u56E0\u6570\u5206\u89E3 O(log N)\n\
    init_factorization \u306E\u5F15\u6570\u306B\u6700\u5927\u306E\u6570 N \u3092\u5165\
    \u308C\u3066\u521D\u671F\u5316\n\"\"\"\ndef init_factorization(N : int) -> list[int]:\n\
    \  # N \u4EE5\u4E0B\u306E\u6574\u6570\u306B\u5BFE\u3057\u3066\u6700\u5C0F\u306E\
    \u7D20\u56E0\u6570\u3092\u6C42\u3081\u308B\n  # D[i] = i \u306E\u6700\u5C0F\u306E\
    \u7D20\u56E0\u6570\n  D = [1]*(N+1)\n  for i in range(2,N+1):\n    if D[i]!=1:\
    \ continue\n    for j in range(i,N+1,i):\n      if D[j]==1: D[j] = i\n  return\
    \ D\n\nD = init_factorization( ) \n\n# \u7D20\u56E0\u6570\u5206\u89E3\ndef factorization(x\
    \ : int) -> dict[int,int]: \n  res = defaultdict(int)\n  while x!=1:\n    res[D[x]]\
    \ += 1\n    x //= D[x]\n  return res"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/factorization.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/factorization.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/factorization.py
- /library/algorithm_library/python/math/factorization.py.html
title: algorithm_library/python/math/factorization.py
---
