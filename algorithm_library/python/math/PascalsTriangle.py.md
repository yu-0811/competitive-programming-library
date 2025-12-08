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
  code: "class PascalsTriangle:\n    \"\"\"\n    \u30D1\u30B9\u30AB\u30EB\u306E\u4E09\
    \u89D2\u5F62\u3067 nCk \u3092\u6C42\u3081\u308B\n    \u8A08\u7B97\u91CF: O(N^2)\n\
    \    mod \u304C\u7D20\u6570\u3067\u306A\u304F\u3066\u3082\u4F7F\u7528\u53EF\u80FD\
    \n    \"\"\"\n    def __init__(self, N, mod):\n        self.mod = mod\n      \
    \  self.binom = [[0] * (N + 1) for _ in range(N + 1)]\n        for i in range(N\
    \ + 1):\n            self.binom[i][0] = 1\n            for j in range(1, i + 1):\n\
    \                self.binom[i][j] = (self.binom[i - 1][j - 1] + self.binom[i -\
    \ 1][j]) % mod\n\n    def C(self, n, k):\n        assert 0 <= k <= n\n       \
    \ return self.binom[n][k]\n\n    def H(self, n, k):\n        \"\"\" \u91CD\u8907\
    \u7D44\u5408\u305B nHk \"\"\"\n        assert n >= 0 and k >= 0\n        return\
    \ self.C(n + k - 1, k)"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/PascalsTriangle.py
  requiredBy: []
  timestamp: '2025-12-08 11:04:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/PascalsTriangle.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/PascalsTriangle.py
- /library/algorithm_library/python/math/PascalsTriangle.py.html
title: algorithm_library/python/math/PascalsTriangle.py
---
