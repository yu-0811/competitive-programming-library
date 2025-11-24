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
  code: "vis = [False]*(N+1)\nfin = [False]*(N+1)\nhistory = deque()\n\n# \u9802\u70B9\
    \ v \u306E\u9023\u7D50\u6210\u5206\u5185\u306E\u9589\u8DEF\u3092\u8FD4\u3059\n\
    def cycle_detect(v):\n  sta = deque()\n  sta.append((v,0))\n  cycle_start = -1\n\
    \  while sta and cycle_start == -1:\n    v,prev = sta.pop()\n    if prev == -1:\n\
    \      history.pop()\n      fin[v] = True\n      continue\n    if vis[v]: continue\n\
    \    vis[v] = True\n    history.append(v)\n    for v2 in G[v]:\n      if v2==prev:\
    \ continue\n      if fin[v2]: continue\n      if vis[v2]: # \u9589\u8DEF\u691C\
    \u51FA\n        cycle_start = v2\n        break\n      sta.append((v2,-1))\n \
    \     sta.append((v2,v))\n  \n  cycle = list()\n  if cycle_start == -1: return\
    \ cycle\n  while history:\n    v = history.pop()\n    cycle.append(v)\n    if\
    \ v == cycle_start: break\n  return cycle"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/cycle_detect.py
  requiredBy: []
  timestamp: '2025-11-24 14:08:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/cycle_detect.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/cycle_detect.py
- /library/algorithm_library/python/graph/cycle_detect.py.html
title: algorithm_library/python/graph/cycle_detect.py
---
