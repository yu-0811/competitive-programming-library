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
  code: "# \u884C\u5217 A \u3068 \u884C\u5217 B \u306E\u7A4D\u3092\u8FD4\u3059\n#\
    \ mod \u304C\u3044\u3089\u306A\u3044\u6642\u306F\u6D88\u3057\u3066\ndef mat_mul(A:\
    \ list[list[int]], B: list[list[int]], mod):\n  assert len(A[0])==len(B)\n  res\
    \ = [[0]*len(B[0]) for _ in range(len(A))]\n  for i in range(len(A)):\n    for\
    \ j in range(len(B[0])):\n      for k in range(len(B)):\n        res[i][j] +=\
    \ A[i][k] * B[k][j]\n        res[i][j] %= mod\n  return res\n\n# \u884C\u5217\u7D2F\
    \u4E57\n# \u884C\u5217 M^K\n# \u30C0\u30D6\u30EA\u30F3\u30B0\u307F\u305F\u3044\
    \u306B\u3059\u308B(\u7E70\u308A\u8FD4\u3057\u4E8C\u4E57\u6CD5)\ndef mat_pow(M:\
    \ list[list[int]], K: int, mod: int):\n  res = [[0]*len(M) for _ in range(len(M))]\n\
    \  # \u5358\u4F4D\u884C\u5217\u3067\u521D\u671F\u5316\u3059\u308B\n  for i in\
    \ range(len(M)): res[i][i] = 1\n  \n  while (K>0):\n    if (K&1==1): res = mat_mul(M,res,mod)\n\
    \    M = mat_mul(M,M,mod)\n    K >>= 1\n  return res"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/MatrixPower.py
  requiredBy: []
  timestamp: '2025-09-08 21:21:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/MatrixPower.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/MatrixPower.py
- /library/algorithm_library/python/math/MatrixPower.py.html
title: algorithm_library/python/math/MatrixPower.py
---
