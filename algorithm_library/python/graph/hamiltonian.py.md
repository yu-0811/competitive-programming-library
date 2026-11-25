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
  code: "# \u6709\u5411\u30B0\u30E9\u30D5\u306E\u30CF\u30DF\u30EB\u30C8\u30F3\u8DEF\
    \u3092\u8FD4\u3059 O(N^2)\ndef hamiltonian_path(G):\n    N = len(G)\n    G = [set(g)\
    \ for g in G]\n    path = []\n\n    for v in range(N):\n        # v\u3092\u65E2\
    \u5B58\u306E\u30CF\u30DF\u30EB\u30C8\u30F3\u8DEF\u306B\u633F\u5165\u3059\u308B\
    \n        for i, u in enumerate(path):\n            # v \u2192 u \u304C\u5B58\u5728\
    \u3059\u308B\u6700\u521D\u306E\u9802\u70B9\u3092\u63A2\u3059\n            if u\
    \ in G[v]:\n                path.insert(i, v)\n                break\n       \
    \ else:\n            # \u898B\u3064\u304B\u3089\u306A\u3051\u308C\u3070\u672B\u5C3E\
    \u306B\u8FFD\u52A0\n            path.append(v)\n\n    return path"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/hamiltonian.py
  requiredBy: []
  timestamp: '2026-11-25 16:54:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/hamiltonian.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/hamiltonian.py
- /library/algorithm_library/python/graph/hamiltonian.py.html
title: algorithm_library/python/graph/hamiltonian.py
---
