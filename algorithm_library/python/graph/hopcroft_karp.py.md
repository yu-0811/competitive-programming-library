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
  code: "from array import array\n\n\ndef hopcroft_karp(g, m):\n    # g[u] \u306F\u5DE6\
    \u9802\u70B9 u \u306E\u96A3\u63A5\u5148\u3002\u53F3\u9802\u70B9\u306F 0 \u4EE5\
    \u4E0A m \u672A\u6E80\u3002\n    # \u5DE6\u9802\u70B9\u3054\u3068\u306E\u76F8\u624B\
    \u3092\u8FD4\u3059\u3002\u672A\u30DE\u30C3\u30C1\u306F -1\u3002O((V+E)\u221A(V))\n\
    \    n = len(g)\n    neg, zero = array(\"i\", [-1]), array(\"i\", [0])\n    left,\
    \ right = neg * n, neg * m\n    end = zero * (m + 1)\n    for row in g:\n    \
    \    for v in row:\n            end[v] += 1\n    size = 0\n    for v in range(m):\n\
    \        end[v], size = size, size + end[v]\n    rev = zero * size\n    for u,\
    \ row in enumerate(g):\n        for v in row:\n            rev[end[v]] = u\n \
    \           end[v] += 1\n    free = [u for u in range(n) if g[u]]\n    src = [v\
    \ for v in range(m) if end[v - 1] < end[v]]\n\n    def augment(s):\n        stack\
    \ = [(s, iter(g[s]))]\n        while stack:\n            u, it = stack[-1]\n \
    \           d = dist[u] - 1\n            for v in it:\n                w = right[v]\n\
    \                if dist[w] != d:\n                    continue\n            \
    \    if w == -1:\n                    for x, _ in reversed(stack):\n         \
    \               right[v], left[x], v = x, v, left[x]\n                    return\
    \ True\n                stack.append((w, iter(g[w])))\n                break\n\
    \            else:\n                dist[u] = -1\n                stack.pop()\n\
    \        return False\n\n    while free:\n        dist = neg * n + zero\n    \
    \    src = [v for v in src if right[v] < 0]\n        que = src\n        d = 1\n\
    \        while que:\n            nxt = []\n            for v in que:\n       \
    \         for k in range(end[v - 1], end[v]):\n                    u = rev[k]\n\
    \                    if dist[u] < 0:\n                        dist[u] = d\n  \
    \                      w = left[u]\n                        if w >= 0:\n     \
    \                       nxt.append(w)\n            que = nxt\n            d +=\
    \ 1\n        free = [u for u in free if dist[u] > 0 and not augment(u)]\n    return\
    \ list(left)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/hopcroft_karp.py
  requiredBy: []
  timestamp: '2026-11-26 00:04:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/hopcroft_karp.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/hopcroft_karp.py
- /library/algorithm_library/python/graph/hopcroft_karp.py.html
title: algorithm_library/python/graph/hopcroft_karp.py
---
