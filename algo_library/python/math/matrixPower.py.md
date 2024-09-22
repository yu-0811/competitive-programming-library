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
  code: "# \u884C\u5217\u7D2F\u4E57\nmod = 998244353\n\n# \u884C\u5217 A \u3068 \u884C\
    \u5217 B \u306E\u7A4D\u3092\u8FD4\u3059\n# mod \u304C\u3044\u3089\u306A\u3044\u6642\
    \u306F\u6D88\u3057\u3066\ndef mat_mul(A: list[list[int]], B: list[list[int]]):\n\
    \  assert len(A[0])==len(B)\n  res = [[0]*len(B[0]) for _ in range(len(A))]\n\
    \  for i in range(len(A)):\n    for j in range(len(B[0])):\n      for k in range(len(B)):\n\
    \        res[i][j] += A[i][k] * B[k][j]\n        res[i][j] %= mod\n  return res\n\
    \n# \u884C\u5217\u7D2F\u4E57\n# \u884C\u5217 M^K\n# \u30C0\u30D6\u30EA\u30F3\u30B0\
    \u307F\u305F\u3044\u306B\u3059\u308B(\u7E70\u308A\u8FD4\u3057\u4E8C\u4E57\u6CD5\
    )\ndef mat_pow(M: list[list[int]], K: int):\n  res = [[0]*len(M) for _ in range(len(M))]\n\
    \  # \u5358\u4F4D\u884C\u5217\u3067\u521D\u671F\u5316\u3059\u308B\n  for i in\
    \ range(len(M)): res[i][i] = 1\n  \n  while (K>0):\n    if (K&1==1): res = mat_mul(M,res)\n\
    \    M = mat_mul(M,M)\n    K >>= 1\n  return res\n\n# \u4F7F\u7528\u4F8B////////////////////\n\
    \n# \u9077\u79FB\u884C\u5217\nM = [[0]*52 for _ in range(52)]\n# M^K\nM_K = mat_pow(M,K)\n\
    \n# \u521D\u671F\u30D9\u30AF\u30C8\u30EB(\u521D\u671F\u72B6\u614B)\nV = [0]*52\n\
    # \u521D\u671F\u5316 ex. V[0] = 1\n\n# K \u56DE\u306E\u79FB\u52D5\u5F8C\u306E\u72B6\
    \u614B\n# M_K * V\nresult = [0]*52\nfor i in range(52):\n  for j in range(52):\n\
    \    result[i] += M_K[i][j]*V[j]\n    result[i] %= mod"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/math/matrixPower.py
  requiredBy: []
  timestamp: '2024-09-22 23:32:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/math/matrixPower.py
layout: document
redirect_from:
- /library/algo_library/python/math/matrixPower.py
- /library/algo_library/python/math/matrixPower.py.html
title: algo_library/python/math/matrixPower.py
---
