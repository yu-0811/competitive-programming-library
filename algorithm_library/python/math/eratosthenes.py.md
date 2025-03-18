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
  code: "# \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\n# O (N log log\
    \ N)\ndef eratosthenes(N: int): \n  prime_number = list() # \u7D20\u6570\n  isprime\
    \ = [True] * (N+1) # isprime[i]==True \u306A\u3089 i \u306F\u7D20\u6570\n  isprime[0],\
    \ isprime[1] = False, False\n  for p in range(2, N+1):\n      if not isprime[p]:\
    \ continue\n      q = p * 2\n      while q <= N:\n          isprime[q] = False\n\
    \          q += p\n  for p in range(2,N+1):\n      if isprime[p]: prime_number.append(p)\n\
    \  return prime_number, isprime\n\n# M \u4EE5\u4E0B\u306E\u7D20\u6570\u30EA\u30B9\
    \u30C8\u3092\u8FD4\u3059\n# O(M log log M)\ndef res_primeList(M):\n    isprime\
    \ = [True] * (M+1)\n    isprime[0], isprime[1] = False, False\n    for i in range(2,\
    \ M+1):\n        if i*i > M: break\n        if isprime[i]:\n            for j\
    \ in range(i*i, M+1, i):\n                isprime[j] = False\n    return [i for\
    \ i in range(2, M+1) if isprime[i]]"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/eratosthenes.py
  requiredBy: []
  timestamp: '2025-03-18 19:06:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/eratosthenes.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/eratosthenes.py
- /library/algorithm_library/python/math/eratosthenes.py.html
title: algorithm_library/python/math/eratosthenes.py
---
