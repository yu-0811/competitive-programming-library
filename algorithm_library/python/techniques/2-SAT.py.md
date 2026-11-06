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
  code: "# n: \u5909\u6570\u6570\n# clause: \u8981\u7D20 (i, f, j, g) \u306F (x[i]\
    \ == f) or (x[j] == g) 0-indexed\n# \u6E80\u305F\u3059T/F\u306E\u7D44\u304C\u3042\
    \u308C\u3070\u305D\u308C\u3092\u3001\u306A\u3051\u308C\u3070None\u3092\u8FD4\u3059\
    \ndef two_sat(n: int, clause: list[tuple[int, bool, int, bool]]) -> list[bool]:\n\
    \    N = 2 * n\n    s = [0] * (N + 1)\n    e = []  # \u542B\u610F\u306E\u59CB\u70B9\
    \u3092\u7BC0\u3054\u3068\u306B2\u3064\u305A\u3064\u4FDD\u5B58\u3002\u5BFE\u306E\
    \u4ED6\u65B9\u3092\u53CD\u8EE2\u3059\u308B\u3068\u7D42\u70B9\u3002\n    for i,\
    \ f, j, g in clause:\n        a, b = 2 * i + (not f), 2 * j + (not g)\n      \
    \  e.extend((a, b))\n        s[a] += 1\n        s[b] += 1\n    for i in range(N):\n\
    \        s[i + 1] += s[i]\n    to = [0] * len(e)\n    for i, v in enumerate(e):\n\
    \        s[v] -= 1\n        to[s[v]] = e[i ^ 1] ^ 1\n    d = [-1] * N  # \u672A\
    \u8A2A\u554F: -1\u3001\u63A2\u7D22\u4E2D: S \u5185\u306E\u4F4D\u7F6E\u3001\u78BA\
    \u5B9A\u6E08\u307F: N \u4EE5\u4E0A\n    S, P = [], []  # S: \u672A\u78BA\u5B9A\
    \u306E\u9802\u70B9\u3001P: \u6210\u5206\u306E\u6839\u5019\u88DC\u306E\u4F4D\u7F6E\
    \n    k = N\n    for r in range(N):\n        if d[r] != -1:\n            continue\n\
    \        st = [r]\n        while st:\n            v = st.pop()\n            if\
    \ v < 0:  # ~v \u306F\u5E30\u308A\u304C\u3051\n                if P[-1] == d[~v]:\n\
    \                    b = P.pop()\n                    while len(S) > b:\n    \
    \                    u = S.pop()\n                        d[u] = k\n         \
    \               if d[u ^ 1] == k:\n                            return None\n \
    \                   k += 1\n            elif d[v] == -1:\n                d[v]\
    \ = len(S)\n                S.append(v)\n                P.append(d[v])\n    \
    \            st.append(~v)\n                st.extend(to[s[v]:s[v + 1]])\n   \
    \         else:\n                while P[-1] > d[v]:\n                    P.pop()\n\
    \    return [d[2 * i] > d[2 * i + 1] for i in range(n)]"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/2-SAT.py
  requiredBy: []
  timestamp: '2026-11-06 22:27:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/2-SAT.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/2-SAT.py
- /library/algorithm_library/python/techniques/2-SAT.py.html
title: algorithm_library/python/techniques/2-SAT.py
---
