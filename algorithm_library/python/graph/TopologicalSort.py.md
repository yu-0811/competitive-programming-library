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
  code: "from collections import deque\n\ndef TopologicalSort(N,G):\n  sortedVertices\
    \ = list()\n  indegree = [0]*(N+1)\n  for v in range(1,N+1):\n    for v2 in G[v]:\n\
    \      indegree[v2] += 1\n  \n  que = deque()\n  for v in range(1,N+1):\n    if\
    \ indegree[v]==0: que.append(v)\n    \n  # \u5165\u6B21\u6570 0 \u306E\u9802\u70B9\
    \u3068\u305D\u306E\u9802\u70B9\u304B\u3089\u51FA\u308B\u8FBA\u3092\u524A\u9664\
    \u3059\u308B\n  while que:\n    v = que.popleft()\n    sortedVertices.append(v)\n\
    \    for v2 in G[v]:\n      indegree[v2] -= 1\n      if indegree[v2]==0: que.append(v2)\n\
    \  \n  # \u9589\u8DEF\u304C\u3042\u308B\u306A\u3089\u7A7A\u306E\u914D\u5217\u3092\
    \u8FD4\u3059\n  if len(sortedVertices)!=N: return []\n  else: return sortedVertices"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/TopologicalSort.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/TopologicalSort.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/TopologicalSort.py
- /library/algorithm_library/python/graph/TopologicalSort.py.html
title: algorithm_library/python/graph/TopologicalSort.py
---
