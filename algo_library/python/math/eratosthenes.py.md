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
    \ N) (\u307B\u307C\u7DDA\u5F62)\ndef eratosthenes(N: int): \n  prime_number =\
    \ list() # \u7D20\u6570\n  isprime = [True] * (N+1) # isprime[i]==True \u306A\u3089\
    \ i \u306F\u7D20\u6570\n  isprime[0], isprime[1] = False, False\n  for p in range(2,\
    \ N+1):\n      if not isprime[p]: continue\n      q = p * 2\n      while q <=\
    \ N:\n          isprime[q] = False\n          q += p\n  for p in range(2,N+1):\n\
    \      if isprime[p]: prime_number.append(p)\n  return prime_number, isprime"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/math/eratosthenes.py
  requiredBy: []
  timestamp: '2024-11-26 23:09:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/math/eratosthenes.py
layout: document
redirect_from:
- /library/algo_library/python/math/eratosthenes.py
- /library/algo_library/python/math/eratosthenes.py.html
title: algo_library/python/math/eratosthenes.py
---
