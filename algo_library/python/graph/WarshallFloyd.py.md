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
  code: "# \u30BF\u30A4\u30D7\u6570\u524A\u6E1B\u3001\u4F59\u8A08\u306A\u3053\u3068\
    \u3092\u8003\u3048\u306A\u304F\u3066\u3044\u3044\u3088\u3046\u306B\u3001inf,N,G\
    \ \u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\n# \u30B0\u30E9\u30D5\u306F\
    \ 1-index\n\ndef WarshallFloyd():\n  dist = [[inf]*(N+1) for _ in range(N+1)]\n\
    \  for i in range(1,N+1): dist[i][i] = 0\n  for i in range(1,N+1):\n    for c,j\
    \ in G[i]:\n      if dist[i][j]>c: dist[i][j] = c\n      if dist[j][i]>c: dist[i][j]\
    \ = c\n  \n  for k in range(1,N+1):\n    for i in range(1,N+1):\n      for j in\
    \ range(1,N+1):\n        if i==j: continue\n        if dist[i][j]>dist[i][k]+dist[k][j]:\n\
    \          dist[i][j] = dist[i][k]+dist[k][j]\n  \n  return dist"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/graph/WarshallFloyd.py
  requiredBy: []
  timestamp: '2024-09-24 23:23:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/graph/WarshallFloyd.py
layout: document
redirect_from:
- /library/algo_library/python/graph/WarshallFloyd.py
- /library/algo_library/python/graph/WarshallFloyd.py.html
title: algo_library/python/graph/WarshallFloyd.py
---
