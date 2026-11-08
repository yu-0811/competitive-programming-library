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
  code: "class CartesianTree:\n    def __init__(s, A):\n        n = len(A)\n     \
    \   left = s.left = [-1] * n\n        right = s.right = [-1] * n\n        parent\
    \ = s.parent = [-1] * n\n        stack = []\n        for i in range(n):\n    \
    \        last = -1\n            while stack and A[stack[-1]] > A[i]:\n       \
    \         last = stack.pop()\n            if stack:\n                p = parent[i]\
    \ = stack[-1]\n                right[p] = i\n            if last >= 0:\n     \
    \           left[i] = last\n                parent[last] = i\n            stack.append(i)\n\
    \        s.root = stack[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/CartesianTree.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/CartesianTree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/CartesianTree.py
- /library/algorithm_library/python/data_structure/CartesianTree.py.html
title: algorithm_library/python/data_structure/CartesianTree.py
---
