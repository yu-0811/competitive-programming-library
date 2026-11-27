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
    \ = s.parent = [-1] * n\n        s.root = -1\n        for i, x in enumerate(A):\n\
    \            p = i - 1\n            while p >= 0 and A[p] > x:\n             \
    \   left[i] = p\n                p = parent[p]\n            if left[i] >= 0:\n\
    \                parent[left[i]] = i\n            if p >= 0:\n               \
    \ right[p] = i\n                parent[i] = p\n            else:\n           \
    \     s.root = i\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/CartesianTree.py
  requiredBy: []
  timestamp: '2026-11-26 13:10:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/CartesianTree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/CartesianTree.py
- /library/algorithm_library/python/data_structure/CartesianTree.py.html
title: algorithm_library/python/data_structure/CartesianTree.py
---
