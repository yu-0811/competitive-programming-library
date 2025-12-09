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
  code: "class SumTopK:\n  # \u9577\u3055 N \u306E\u914D\u5217 A \u306E\u5927\u304D\
    \u3044\u65B9\u304B\u3089K\u500B\u306E\u548C\u3092\u9AD8\u901F\u306B\u7BA1\u7406\
    \u3059\u308B\n  def __init__(self,N,A,K):\n    self.A = A\n    self.ok = SortedMultiset([0]*K)\
    \ # \u4F7F\u3046\u3084\u3064\n    self.ng = SortedMultiset([0]*(N-K)) # \u4F7F\
    \u308F\u306A\u3044\u3084\u3064\n    self.ans = 0 # \u5927\u304D\u3044\u65B9\u304B\
    \u3089K\u500B\u306E\u548C\n  \n  def add(self,y): # \u3069\u3053\u304B\u306E\u5024\
    \u304Cy\u306B\u5909\u308F\u308B\n    self.ok.add(y)\n    self.ans += y\n    yy\
    \ = self.ok[0]\n    self.ans -= yy\n    self.ok.discard(yy)\n    self.ng.add(yy)\n\
    \    \n  def DEL(self,y): # y\u3092\u524A\u9664\u3059\u308B\n    if y>=self.ok[0]:\n\
    \      self.ok.discard(y)\n      self.ans -= y\n      yy = self.ng[-1]\n     \
    \ self.ng.discard(yy)\n      self.ok.add(yy)\n      self.ans += yy\n    else:\n\
    \      self.ng.discard(y)\n  \n  def update(self,x,y): # A[x]\u3092y\u306B\u66F4\
    \u65B0\u3057\u3001K\u500B\u306E\u548C\u3092\u8FD4\u3059\n    self.add(y)\n   \
    \ self.DEL(self.A[x])\n    self.A[x] = y\n    return self.ans"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/TopK.py
  requiredBy: []
  timestamp: '2025-12-09 12:08:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/TopK.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/TopK.py
- /library/algorithm_library/python/data-structure/TopK.py.html
title: algorithm_library/python/data-structure/TopK.py
---
