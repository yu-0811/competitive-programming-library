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
  code: "from itertools import accumulate\n\n# \u4E8C\u6B21\u5143\u914D\u5217\u306E\
    \u9577\u65B9\u5F62\u9818\u57DF\u306E\u5024\u306E\u548C\u3092\u8A08\u7B97\u3067\
    \u304D\u308B\nclass cross_accumulate:\n  # \u4E8C\u6B21\u5143\u914D\u5217\u3092\
    \u6E21\u3059\n  def __init__(self, grid : list[list[int]]):\n    self.grid = self._crossAccumulate(grid)\n\
    \n  # \u4E8C\u6B21\u5143\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\n  def _crossAccumulate(self,\
    \ grid):\n    for i in range(len(grid)):\n      grid[i] = list(accumulate(grid[i]))\n\
    \    for j in range(len(grid[0])):\n      for i in range(1,len(grid)):\n     \
    \   grid[i][j] += grid[i-1][j]\n    return grid\n      \n  def query(self, i0:\
    \ int, j0: int, i1: int, j1: int) -> int:\n    \"\"\"\n    \u5DE6\u4E0A\u3092\
    (i0,j0), \u53F3\u4E0B\u3092(i1,j1)\u3059\u308B\u9577\u65B9\u5F62\u9818\u57DF\u306E\
    \u5408\u8A08\u3092\u8FD4\u3059\n    \n    grid[i0][j0], grid[i0][j0+1], ..., grid[i0][j1]\n\
    \    grid[i0+1][j0], grid[i0+1][j0+1], ..., grid[i0+1][j1]\n    ...\n    grid[i1][j0],\
    \ grid[i1][j0+1], ..., grid[i1][j1]\n    \"\"\"\n    assert 0<=i0<=i1<len(self.grid)\
    \ and 0<=j0<=j1<len(self.grid[0])\n  \n    res = 0\n    if 0<=i0-1 and 0<=j0-1:\
    \ res += self.grid[i0-1][j0-1]\n    if 0<=i0-1: res -= self.grid[i0-1][j1]\n \
    \   if 0<=j0-1: res -= self.grid[i1][j0-1]\n    res += self.grid[i1][j1]\n   \
    \ return res"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/CrossAccumulate.py
  requiredBy: []
  timestamp: '2025-05-04 17:49:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/CrossAccumulate.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/CrossAccumulate.py
- /library/algorithm_library/python/techniques/CrossAccumulate.py.html
title: algorithm_library/python/techniques/CrossAccumulate.py
---
