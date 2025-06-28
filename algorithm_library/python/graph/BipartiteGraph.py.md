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
  code: "from collections import defaultdict,deque\n\n# \u4E8C\u90E8\u30B0\u30E9\u30D5\
    \u306A\u3089 True \u3068\u8272\u5206\u3051\u3092\u8FD4\u3059\ndef is_bipartite_graph(G\
    \ : list[list[int]], N : int) -> tuple[bool, list[int]]:\n  col = [-1]*(N+1)\n\
    \  def dfs(v):\n    que = deque()\n    que.append(v)\n    while que:\n      v\
    \ = que.pop()\n      for v2 in G[v]:\n        if col[v2]!=-1:\n          if col[v]==col[v2]:\n\
    \            return False\n          continue\n        col[v2] = 1-col[v]\n  \
    \      que.append(v2)\n    return True\n\n  for v in range(1,N+1):\n    if col[v]!=-1:\
    \ continue\n    col[v] = 1\n    if dfs(v) == False:\n      return False, []\n\
    \  \n  return True, col"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/BipartiteGraph.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/BipartiteGraph.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/BipartiteGraph.py
- /library/algorithm_library/python/graph/BipartiteGraph.py.html
title: algorithm_library/python/graph/BipartiteGraph.py
---
