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
  code: "inf = pow(10,18)\n\ndef bellman_ford(Edges : list[tuple[int,int,int]], N\
    \ : int, s : int) -> tuple[list[int], bool]:\n  \"\"\"\n  Edges : \u6709\u5411\
    \u8FBA(\u7121\u5411\u306E\u3068\u304D\u306F\u4E21\u65B9\u5165\u308C\u308B)\n \
    \ N : \u9802\u70B9\u6570\n  s : \u59CB\u70B9 \n  \u8FD4\u308A\u5024 : (\u6700\u77ED\
    \u8DDD\u96E2\u914D\u5217, \u8CA0\u9589\u8DEF\u306E\u6709\u7121)\n  \"\"\"\n  dist\
    \ = [inf] * (N+1)\n  dist[s] = 0\n  cnt = 0\n  while (cnt < N):\n    end = True\n\
    \    for fro, to, cost in Edges:\n      if dist[to] > dist[fro] + cost:\n    \
    \    dist[to] = dist[fro] + cost\n        end = False\n    if end: break\n   \
    \ cnt += 1\n  \n  return dist, cnt == N"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/Bellman_ford.py
  requiredBy: []
  timestamp: '2025-07-29 17:33:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/Bellman_ford.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/Bellman_ford.py
- /library/algorithm_library/python/graph/Bellman_ford.py.html
title: algorithm_library/python/graph/Bellman_ford.py
---
