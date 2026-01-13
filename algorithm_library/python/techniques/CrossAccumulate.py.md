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
  code: "class CrossAccumulate:\n    def __init__(self, grid: list[list[int]]):\n\
    \        self.H = len(grid)\n        self.W = len(grid[0])\n        self.s = [[0]\
    \ * (self.W + 1) for _ in range(self.H + 1)]\n\n        for i in range(self.H):\n\
    \            for j in range(self.W):\n                self.s[i + 1][j + 1] = (\n\
    \                    self.s[i][j + 1] + self.s[i + 1][j] - self.s[i][j] + grid[i][j]\n\
    \                )\n\n    def query(self, r1: int, c1: int, r2: int, c2: int)\
    \ -> int:\n        \"\"\"\n        \u5DE6\u4E0A(r1,c1), \u53F3\u4E0B(r2,c2) \u306E\
    \u9589\u533A\u9593\u77E9\u5F62\u306E\u548C\u3092\u8FD4\u3059\n        \"\"\"\n\
    \        assert 0 <= r1 <= r2 < self.H and 0 <= c1 <= c2 < self.W\n        return\
    \ (\n            self.s[r2 + 1][c2 + 1]\n            - self.s[r1][c2 + 1]\n  \
    \          - self.s[r2 + 1][c1]\n            + self.s[r1][c1]\n        )\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/CrossAccumulate.py
  requiredBy: []
  timestamp: '2026-01-13 11:58:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/CrossAccumulate.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/CrossAccumulate.py
- /library/algorithm_library/python/techniques/CrossAccumulate.py.html
title: algorithm_library/python/techniques/CrossAccumulate.py
---
