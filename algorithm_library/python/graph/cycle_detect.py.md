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
  code: "def cycle_detect(n, edges):\n    \"\"\"\u7121\u5411\u30B0\u30E9\u30D5\u306E\
    \u9589\u8DEF\u3092 (\u9802\u70B9\u5217, \u8FBA ID \u5217) \u3067\u8FD4\u3059\u3002\
    \u306A\u3051\u308C\u3070 ([], [])\u3002\n\n    \u9802\u70B9\u306F 0-indexed\u3001\
    \u8FBA ID \u306F edges \u5185\u306E\u4F4D\u7F6E\u3002\u81EA\u5DF1\u30EB\u30FC\u30D7\
    \u30FB\u591A\u91CD\u8FBA\u306B\u5BFE\u5FDC\u3002\n    \u6642\u9593\u30FB\u7A7A\
    \u9593\u8A08\u7B97\u91CF O(n + m)\u3002\n    \"\"\"\n    g = [[] for _ in range(n)]\n\
    \    to = []\n    for i, (u, v) in enumerate(edges):\n        g[u].append(2 *\
    \ i)\n        g[v].append(2 * i + 1)\n        to.extend((v, u))\n    pos = [-1]\
    \ * n\n    for r in range(n):\n        if pos[r] != -1:\n            continue\n\
    \        vs, es = [r], [-1]\n        pos[r] = 0\n        while vs:\n         \
    \   v = vs[-1]\n            if not g[v]:\n                pos[v] = -2\n      \
    \          vs.pop()\n                es.pop()\n                continue\n    \
    \        j = g[v].pop()\n            i = j >> 1\n            if i == es[-1]:\n\
    \                continue\n            u = to[j]\n            if pos[u] >= 0:\n\
    \                return vs[pos[u]:], es[pos[u] + 1:] + [i]\n            if pos[u]\
    \ == -1:\n                pos[u] = len(vs)\n                vs.append(u)\n   \
    \             es.append(i)\n    return [], []\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/cycle_detect.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/cycle_detect.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/cycle_detect.py
- /library/algorithm_library/python/graph/cycle_detect.py.html
title: algorithm_library/python/graph/cycle_detect.py
---
