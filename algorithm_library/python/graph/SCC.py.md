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
  code: "# edges \u306F (\u59CB\u70B9, \u7D42\u70B9) \u306E\u30EA\u30B9\u30C8\n# \u8FD4\
    \u308A\u5024: groups, dag\n# groups[i] \u306F\u6210\u5206 i \u306E\u9802\u70B9\
    \u30EA\u30B9\u30C8\u3001dag[i] \u306F\u6210\u5206 i \u304B\u3089\u51FA\u308B\u8FBA\
    \u306E\u884C\u304D\u5148\u3002\ndef scc_dag(n, edges):\n    start = [0] * (n +\
    \ 1)\n    for u, _ in edges:\n        start[u] += 1\n    for u in range(n):\n\
    \        start[u + 1] += start[u]\n    to = [0] * len(edges)\n    # \u5404\u9802\
    \u70B9\u306E\u8FBA\u3092\u5F8C\u308D\u304B\u3089\u683C\u7D0D\u3059\u308B\u3068\
    \ start \u304C\u958B\u59CB\u4F4D\u7F6E\u306B\u306A\u308B\u3002\n    for u, v in\
    \ reversed(edges):\n        start[u] -= 1\n        to[start[u]] = v\n\n    pos\
    \ = [-1] * n  # \u672A\u8A2A\u554F\u306F -1\u3001\u63A2\u7D22\u4E2D\u306F active\
    \ \u5185\u306E\u4F4D\u7F6E\u3001\u78BA\u5B9A\u6E08\u307F\u306F n \u4EE5\u4E0A\n\
    \    # roots \u306B\u306F\u6210\u5206\u306E\u6839\u5019\u88DC\u306E active \u5185\
    \u306E\u4F4D\u7F6E\u3092\u7A4D\u3080\u3002\n    active, roots, groups = [], [],\
    \ []\n    k = n\n    for r in range(n):\n        if pos[r] >= 0:\n           \
    \ continue\n        if start[r] == start[r + 1]:\n            pos[r] = k\n   \
    \         k += 1\n            groups.append([r])\n            continue\n     \
    \   st = [r]\n        while st:\n            v = st.pop()\n            if v <\
    \ 0:  # ~v \u306F\u5E30\u308A\u304C\u3051\n                v = ~v\n          \
    \      if roots[-1] == pos[v]:\n                    i = roots.pop()\n        \
    \            group = active[i:]\n                    del active[i:]\n        \
    \            for u in group:\n                        pos[u] = k\n           \
    \         k += 1\n                    groups.append(group)\n            elif pos[v]\
    \ == -1:\n                p = pos[v] = len(active)\n                active.append(v)\n\
    \                roots.append(p)\n                st.append(~v)\n            \
    \    st.extend(to[start[v]:start[v + 1]])\n            else:\n               \
    \ p = pos[v]\n                while roots[-1] > p:\n                    roots.pop()\n\
    \    groups.reverse()\n    dag = [[] for _ in range(k - n)]\n    # \u78BA\u5B9A\
    \u9806\u306E\u756A\u53F7\u3092\u53CD\u8EE2\u3057\u3001groups \u3068\u540C\u3058\
    \u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u9806\u306B\u3059\u308B\u3002\n    last =\
    \ k - 1\n    if len(dag) > 1:\n        for u, v in edges:\n            a, b =\
    \ pos[u], pos[v]\n            if a != b:\n                dag[last - a].append(last\
    \ - b)\n    return groups, dag\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/SCC.py
  requiredBy: []
  timestamp: '2026-11-27 15:22:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/SCC.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/SCC.py
- /library/algorithm_library/python/graph/SCC.py.html
title: algorithm_library/python/graph/SCC.py
---
