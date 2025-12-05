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
  code: "# \u7D44\u5408\u305B\u7DCF\u6570\u30E9\u30A4\u30D6\u30E9\u30EA\nclass Comb:\n\
    \  def __init__(self,n,mod):\n    self.mod = mod\n    self.n = n\n    self.fact\
    \ = [1, 1] \n    self.factinv = [1, 1]  \n    self.inv = [0, 1] \n    for i in\
    \ range(2,self.n+1):\n        self.fact.append((self.fact[i-1] * i) % self.mod)\n\
    \        self.inv.append((self.mod-self.inv[self.mod % i] * (self.mod // i)) %\
    \ self.mod)\n        self.factinv.append((self.factinv[i-1] * self.inv[i]) % self.mod)\n\
    \        \n  def C(self,n,k): # nCk % mod\u3092\u8FD4\u3059\n    assert n <= self.n\n\
    \    if (k < 0 or n < 0) or (n < k):return 0\n    if k==1: return n\n    k = min(k,n-k)\n\
    \    return self.fact[n]*self.factinv[k]%self.mod*self.factinv[n-k]%self.mod\n\
    \n  # \u91CD\u8907\u7D44\u5408\u305B nHr % mod\u3092\u8FD4\u3059\n  def H(self,n,r):\n\
    \      return self.C(n+r-1,r)"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/modComb.py
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/modComb.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/modComb.py
- /library/algorithm_library/python/math/modComb.py.html
title: algorithm_library/python/math/modComb.py
---
