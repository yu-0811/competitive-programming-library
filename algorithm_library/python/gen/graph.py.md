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
  code: "# \u5358\u7D14\u9023\u7D50\u7121\u5411\u30B0\u30E9\u30D5\u306E\u751F\u6210\
    \uFF081-indexed\uFF09\nfrom random import randint, shuffle\n\nN = randint(3, 10)\n\
    V = list(range(1, N + 1))\nshuffle(V)\nM = []\nfor i in range(1, N):\n    p =\
    \ randint(0, i - 1)  # \u524D\u306E\u9802\u70B9\u304B\u3089\u5FC5\u305A1\u3064\
    \u3064\u306A\u3050\n    for j in range(i):\n        if j == p or randint(0, 1):\n\
    \            M.append((V[j], V[i]))\n\nprint(N, len(M))\nfor e in M:\n    print(*e)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/gen/graph.py
  requiredBy: []
  timestamp: '2026-10-29 10:58:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/gen/graph.py
layout: document
redirect_from:
- /library/algorithm_library/python/gen/graph.py
- /library/algorithm_library/python/gen/graph.py.html
title: algorithm_library/python/gen/graph.py
---
