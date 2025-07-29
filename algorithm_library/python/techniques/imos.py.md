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
  code: "from itertools import accumulate\n\n# \u4E8C\u6B21\u5143\u306Eimos\u6CD5\n\
    class imos:\n  def __init__(self, H : int, W : int):\n    self.grid = [[0]*W for\
    \ _ in range(H)]\n    \n  def add(self, i0: int, j0: int, i1: int, j1: int, increment:\
    \ int) -> None:\n    \"\"\"\n    \u5DE6\u4E0A\u3092(i0,j0), \u53F3\u4E0B\u3092\
    (i1,j1)\u3068\u3059\u308B\u9577\u65B9\u5F62\u9818\u57DF\u306B increment \u52A0\
    \u7B97\u3059\u308B\n    \n    grid[i0][j0], grid[i0][j0+1], ..., grid[i0][j1]\n\
    \    grid[i0+1][j0], grid[i0+1][j0+1], ..., grid[i0+1][j1]\n    ...\n    grid[i1][j0],\
    \ grid[i1][j0+1], ..., grid[i1][j1]\n    \"\"\"\n    assert 0<=i0<=i1<len(self.grid)\
    \ and 0<=j0<=j1<len(self.grid[0])\n    \n    self.grid[i0][j0] += increment\n\
    \    if i1+1<len(self.grid): self.grid[i1+1][j0] -= increment\n    if j1+1<len(self.grid[0]):\
    \ self.grid[i0][j1+1] -= increment\n    if i1+1<len(self.grid) and j1+1<len(self.grid[0]):\n\
    \      self.grid[i1+1][j1+1] += increment\n      \n  # \u4E8C\u6B21\u5143\u7D2F\
    \u7A4D\u548C\u3092\u53D6\u308B\n  def cross_accumulate(self):\n    self.flag =\
    \ True\n    for i in range(len(self.grid)):\n      self.grid[i] = list(accumulate(self.grid[i]))\n\
    \    for j in range(len(self.grid[0])):\n      for i in range(1,len(self.grid)):\n\
    \        self.grid[i][j] += self.grid[i-1][j]\n    return self.grid"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/imos.py
  requiredBy: []
  timestamp: '2025-07-29 17:33:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/imos.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/imos.py
- /library/algorithm_library/python/techniques/imos.py.html
title: algorithm_library/python/techniques/imos.py
---
