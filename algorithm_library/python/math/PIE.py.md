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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u7D04\u6570\u7CFB\u5305\u9664\u306B\u4F7F\u3046\u3084\u3064\u7CFB\n\n\n\
    class eratosthenes:\n    def __init__(self, MAX: int):\n        \"\"\"\n     \
    \   \u521D\u671F\u5316 : O(MAX)\n        \"\"\"\n        self.MAX = MAX\n    \
    \    isprime = self.isprime = [False] * (MAX + 1)\n        mebius = self.mebius\
    \ = [1] * (MAX + 1)  # \u30E1\u30D3\u30A6\u30B9\u95A2\u6570\n        min_factor\
    \ = self.min_factor = [0] * (MAX + 1)  # \u6700\u5C0F\u306E\u7D20\u56E0\u6570\n\
    \        min_factor[1] = 1\n        primes = []\n\n        for i in range(2, MAX\
    \ + 1):\n            if min_factor[i] == 0:\n                min_factor[i] = i\n\
    \                isprime[i] = True\n                mebius[i] = -1\n         \
    \       primes.append(i)\n\n            smallest, mu = min_factor[i], mebius[i]\n\
    \            for prime in primes:\n                j = i * prime\n           \
    \     if j > MAX:\n                    break\n                min_factor[j] =\
    \ prime\n                if prime == smallest:\n                    mebius[j]\
    \ = 0\n                    break\n                mebius[j] = -mu\n\n    def prime_factors(self,\
    \ n: int) -> list[tuple[int, int]]:\n        \"\"\"\n        \u7D20\u56E0\u6570\
    \u5206\u89E3: (\u7D20\u56E0\u6570, \u6307\u6570) \u306E\u30EA\u30B9\u30C8\u3092\
    \u8FD4\u3059\n        O(log n)\n        \"\"\"\n        res = []\n        while\
    \ n != 1:\n            prime = self.min_factor[n]\n            exp = 0\n     \
    \       while self.min_factor[n] == prime:\n                exp += 1\n       \
    \         n //= prime\n            res.append((prime, exp))\n        return res\n\
    \n    def divisors(self, n: int) -> list[int]:\n        \"\"\"\n        \u7D04\
    \u6570\u5217\u6319: n \u306E\u7D04\u6570\u3092\u3059\u3079\u3066\u30EA\u30B9\u30C8\
    \u3067\u8FD4\u3059\n        O(d(n)) (d(n): n \u306E\u7D04\u6570\u306E\u500B\u6570\
    , d(n) < O(n^(1/3)))\n        \"\"\"\n        res = [1]\n        for prime, exp\
    \ in self.prime_factors(n):\n            current_size = len(res)\n           \
    \ for i in range(current_size):\n                value = 1\n                for\
    \ _ in range(exp):\n                    value *= prime\n                    res.append(res[i]\
    \ * value)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/PIE.py
  requiredBy: []
  timestamp: '2026-10-20 11:51:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/PIE.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/PIE.py
- /library/algorithm_library/python/math/PIE.py.html
title: algorithm_library/python/math/PIE.py
---
