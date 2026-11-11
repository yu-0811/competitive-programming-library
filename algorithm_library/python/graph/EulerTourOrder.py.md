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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def euler_tour(G, r=0):\n    \"\"\"\u6728\u306E\u96A3\u63A5\u30EA\u30B9\u30C8\
    \ G -> (tin, tout, od)\n    \u6642\u9593\u30FB\u7A7A\u9593 O(N)\n    tin: \u5404\
    \u9802\u70B9\u3092\u8A2A\u308C\u305F\u6642\u523B\n    tout: \u5404\u9802\u70B9\
    \u304B\u3089\u5E30\u308B\u6642\u523B\n    od: \u884C\u304D\u304C\u3051\u9806\u306B\
    \u9802\u70B9\u3092\u4E26\u3079\u305F\u5217\n    \u90E8\u5206\u6728 v = od[tin[v]:tout[v]]\uFF08\
    v \u81EA\u8EAB\u3092\u542B\u3080\uFF09\n    \"\"\"\n    tin = [-1] * len(G)\n\
    \    tout = [-1] * len(G)\n    od = []\n    st = [r]\n    while st:\n        v\
    \ = st.pop()\n        if v < 0:  # \u9000\u51FA\u306E\u5370\u3092\u5143\u306E\u9802\
    \u70B9\u306B\u623B\u3059\n            tout[~v] = len(od)\n        else:\n    \
    \        tin[v] = len(od)\n            od.append(v)\n            st.append(~v)\n\
    \            for u in reversed(G[v]):\n                if tin[u] < 0:\n      \
    \              st.append(u)\n    return tin, tout, od\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/EulerTourOrder.py
  requiredBy: []
  timestamp: '2026-11-11 22:38:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/EulerTourOrder.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/EulerTourOrder.py
- /library/algorithm_library/python/graph/EulerTourOrder.py.html
title: algorithm_library/python/graph/EulerTourOrder.py
---
