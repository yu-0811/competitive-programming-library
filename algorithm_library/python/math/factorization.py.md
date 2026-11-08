---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc177/editorial/82
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import defaultdict\nfrom math import isqrt\n\n\"\"\"\n\u9AD8\
    \u901F\u7D20\u56E0\u6570\u5206\u89E3 https://atcoder.jp/contests/abc177/editorial/82\n\
    \u7D20\u56E0\u6570\u5206\u89E3\u3092\u3057\u305F\u3044\u6700\u5927\u306E\u6570\
    \u3092 N \u3068\u3057\u3066\n\u69CB\u7BC9 O(N log log N)\n\u7D20\u56E0\u6570\u5206\
    \u89E3 O(log N)\ninit_factorization \u306E\u5F15\u6570\u306B\u6700\u5927\u306E\
    \u6570 N \u3092\u5165\u308C\u3066\u521D\u671F\u5316\n\"\"\"\n\n\ndef init_factorization(N:\
    \ int) -> list[int]:\n    # N \u4EE5\u4E0B\u306E\u6574\u6570\u306B\u5BFE\u3057\
    \u3066\u6700\u5C0F\u306E\u7D20\u56E0\u6570\u3092\u6C42\u3081\u308B\n    # D[i]\
    \ = i \u306E\u6700\u5C0F\u306E\u7D20\u56E0\u6570\n    D = [1] * (N + 1)\n    for\
    \ i in range(2, N + 1):\n        if D[i] != 1:\n            continue\n       \
    \ for j in range(i, N + 1, i):\n            if D[j] == 1:\n                D[j]\
    \ = i\n    return D\n\n\nD = []  # \u4F7F\u7528\u524D\u306B D = init_factorization(N)\
    \ \u3067\u521D\u671F\u5316\u3059\u308B\n\n\n# \u7D20\u56E0\u6570\u5206\u89E3\n\
    def factorization(x: int) -> dict[int, int]:\n    res = defaultdict(int)\n   \
    \ while x != 1:\n        res[D[x]] += 1\n        x //= D[x]\n    return res\n\n\
    \n# \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\n# O (N log log N)\n\
    def eratosthenes(N: int):\n    prime_number = list()  # \u7D20\u6570\n    isprime\
    \ = [True] * (N + 1)  # isprime[i]==True \u306A\u3089 i \u306F\u7D20\u6570\n \
    \   isprime[0], isprime[1] = False, False\n    for p in range(2, N + 1):\n   \
    \     if not isprime[p]:\n            continue\n        q = p * 2\n        while\
    \ q <= N:\n            isprime[q] = False\n            q += p\n    for p in range(2,\
    \ N + 1):\n        if isprime[p]:\n            prime_number.append(p)\n    return\
    \ prime_number, isprime\n\n\n# M \u4EE5\u4E0B\u306E\u7D20\u6570\u30EA\u30B9\u30C8\
    \u3092\u8FD4\u3059\n# O(M log log M)\ndef res_primeList(M):\n    if M < 2:\n \
    \       return []\n    s = bytearray(b\"\\1\") * ((M + 1) // 2)  # s[k] \u306F\
    \u5947\u6570 2*k+1 \u306E\u30D5\u30E9\u30B0\n    for i in range(3, isqrt(M) +\
    \ 1, 2):\n        if s[i // 2]:\n            j = i * i // 2\n            s[j::i]\
    \ = bytes((len(s) - 1 - j) // i + 1)\n    res = [i for i in range(1, M + 1, 2)\
    \ if s[i // 2]]\n    res[0] = 2\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/factorization.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/factorization.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/factorization.py
- /library/algorithm_library/python/math/factorization.py.html
title: algorithm_library/python/math/factorization.py
---
