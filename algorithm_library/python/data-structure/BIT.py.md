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
  code: "class BIT: \n  def __init__(self, n):\n    self.n = n + 1\n    self.bit =\
    \ [[0] * self.n for _ in range(2)]\n\n  def _add_sub(self, p, i, x):\n    idx\
    \ = i\n    while idx < self.n:\n      self.bit[p][idx] += x\n      idx += idx\
    \ & -idx\n\n  def add(self, l, r, x): # [l,r)\u306Bx\u3092\u52A0\u7B97\n    self._add_sub(0,\
    \ l, -x * (l - 1))\n    self._add_sub(0, r, x * (r - 1))\n    self._add_sub(1,\
    \ l, x)\n    self._add_sub(1, r, -x)\n\n  def _sum_sub(self, p, i):\n    s = 0\n\
    \    idx = i\n    while idx > 0:\n      s += self.bit[p][idx]\n      idx -= idx\
    \ & -idx\n    return s\n\n  def SUM(self, i):\n    return self._sum_sub(0, i)\
    \ + self._sum_sub(1, i) * i\n\n  # \u4EFB\u610F\u306E\u533A\u9593[l,r)\u306E\u533A\
    \u9593\u3092\u3092\u53D6\u5F97\n  def range_sum(self,l,r): \n    return self.SUM(r-1)\
    \ -self.SUM(l-1)\n  \n  # \u4E8C\u5206\u63A2\u7D22\n  ## a_1 + a_2 + ... + a_x\
    \ >= w \u3068\u306A\u308B\u6700\u5C0F\u306E x \u3092\u6C42\u3081\u308B\n  def\
    \ lower_bound(self,w):\n    if w<=0: return 0\n    else:\n      x,LEN = 0,1\n\
    \      # \u6700\u5927\u306E\u533A\u9593\u9577\u3092 LEN \u306B\u5165\u308C\u308B\
    \n      while LEN<self.size: LEN <<= 1\n      while LEN>0:\n        # \u533A\u9593\
    [x+1,x+LEN]\u304C w \u4EE5\u4E0B\u306E\u3068\u304D = \u63A1\u7528\u3059\u308B\u6642\
    \n        if x+LEN<self.size and self.tree[x+LEN]<w:\n          w -= self.tree[x+LEN]\n\
    \          x += LEN\n        LEN >>= 1\n    \n    return x+1"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/BIT.py
  requiredBy: []
  timestamp: '2025-11-24 14:08:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/BIT.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/BIT.py
- /library/algorithm_library/python/data-structure/BIT.py.html
title: algorithm_library/python/data-structure/BIT.py
---
