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
  code: "# \u7D44\u5408\u305B\u7DCF\u6570\u30E9\u30A4\u30D6\u30E9\u30EA\nmod = 998244353\n\
    \nMAX = pow(10,6) # n \u306E\u6700\u5927\u5024\nfact = [1, 1] \nfactinv = [1,\
    \ 1]  \ninv = [0, 1] \nfor i in range(2, MAX+1):\n    fact.append((fact[i-1] *\
    \ i) % mod)\n    inv.append((mod-inv[mod % i] * (mod // i)) % mod)\n    factinv.append((factinv[i-1]\
    \ * inv[i]) % mod)\n    \ndef modComb(n,k): # nCk % mod\u3092\u8FD4\u3059\n  if\
    \ (k < 0 or n<0) or (n < k):return 0\n  if k==1: return n\n  k = min(k,n-k)\n\
    \  return fact[n]*factinv[k]%mod*factinv[n-k]%mod"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/math/modComb.py
  requiredBy: []
  timestamp: '2024-11-16 18:16:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/math/modComb.py
layout: document
redirect_from:
- /library/algo_library/python/math/modComb.py
- /library/algo_library/python/math/modComb.py.html
title: algo_library/python/math/modComb.py
---
