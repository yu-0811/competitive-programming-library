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
  code: "class CartesianTree:\n    def __init__(self, A):\n        n = len(A)\n  \
    \      self.root = 0\n        self.left = [-1] * n\n        self.right = [-1]\
    \ * n\n        self.parent = [-1] * n\n        st = [-1] * n\n        st[0] =\
    \ 0\n        st_top = 0\n        for i in range(1, n):\n            if A[st[st_top]]\
    \ > A[i]:  # pop \u3057\u3066\u304B\u3089 push\n                while st_top >=\
    \ 1 and A[st[st_top - 1]] > A[i]:\n                    st_top -= 1\n         \
    \       # st_top > 0 \u306A\u3089 A[st[top-1]] <= A[i] < A[st[top]]\n        \
    \        # st[st_top] \u3092\u5DE6\u306E\u5B50\u3001st[st_top-1] \u3092\u89AA\u306B\
    \u3059\u308B\n                self.left[i] = st[st_top]\n                self.parent[self.left[i]]\
    \ = i\n                if st_top == 0:\n                    self.root = i\n  \
    \              else:\n                    self.parent[i] = st[st_top - 1]\n  \
    \                  self.right[self.parent[i]] = i\n                st[st_top]\
    \ = i\n            else:  # push \u3059\u308B\u3060\u3051\n                self.parent[i]\
    \ = st[st_top]\n                self.right[self.parent[i]] = i\n             \
    \   st_top += 1\n                st[st_top] = i\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/CartesianTree.py
  requiredBy: []
  timestamp: '2025-12-09 12:08:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/CartesianTree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/CartesianTree.py
- /library/algorithm_library/python/data-structure/CartesianTree.py.html
title: algorithm_library/python/data-structure/CartesianTree.py
---
