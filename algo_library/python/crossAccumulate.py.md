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
  code: "# \u30AF\u30E9\u30B9\u306B\u3057\u305F\u3044\u304C\u3001\u901F\u5EA6\u7684\
    \u306B\u9045\u3044\u306E\u3067\u95A2\u6570\u3067\nfrom itertools import accumulate\n\
    \n# \u5DE6\u4E0A\u3092(i0,j0), \u53F3\u4E0A\u3092(i1,j1)\u3068\u3059\u308B\u9577\
    \u65B9\u5F62\u9818\u57DF\u306B d \u52A0\u7B97\u3059\u308B\n# \u3042\u3048\u3066\
    \u8FD4\u308A\u5024\u3092 None \u306B\u3057\u3066\u3044\u308B(\u76F4\u63A5\u66F8\
    \u304D\u63DB\u3048\u305F\u65B9\u304C\u901F\u305D\u3046)\ndef applyRangeAddition(grid:\
    \ list[list[int]], i0: int, j0: int, i1: int, j1: int, increment: int) -> None:\n\
    \  assert i0<=i1 and j0<=j1\n  grid[i0][j0] += increment\n  if i1+1<len(grid):\
    \ grid[i1+1][j0] -= increment\n  if j1+1<len(grid[0]): grid[i0][j1+1] -= increment\n\
    \  if i1+1<len(grid) and j1+1<len(grid[0]):\n    grid[i1+1][j1+1] += increment\n\
    \    \n# \u4E8C\u6B21\u5143\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\ndef crossAccumulate(grid:\
    \ list[list[int]]) -> list[list[int]]:\n  for i in range(len(grid)):\n    grid[i]\
    \ = list(accumulate(grid[i]))\n  for j in range(len(grid[0])):\n    for i in range(1,len(grid)):\n\
    \      grid[i][j] += grid[i-1][j]\n  return grid\n    \n# \u5DE6\u4E0A\u3092(i0,j0),\
    \ \u53F3\u4E0A\u3092(i1,j1)\u3059\u308B\u9577\u65B9\u5F62\u9818\u57DF\u306E\u5408\
    \u8A08\u3092\u8FD4\u3059\ndef imos(grid: list[list[int]], i0: int, j0: int, i1:\
    \ int, j1: int) -> int:\n  res = 0\n  if 0<=i0-1 and 0<=j0-1: res += grid[i0-1][j0-1]\n\
    \  if 0<=i0-1: res -= grid[i0-1][j1]\n  if 0<=j0-1: res -= grid[i1][j0-1]\n  res\
    \ += grid[i1][j1]\n  return res"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/crossAccumulate.py
  requiredBy: []
  timestamp: '2024-11-24 09:52:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/crossAccumulate.py
layout: document
redirect_from:
- /library/algo_library/python/crossAccumulate.py
- /library/algo_library/python/crossAccumulate.py.html
title: algo_library/python/crossAccumulate.py
---
