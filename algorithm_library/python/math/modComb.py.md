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
  code: "# \u4E8C\u9805\u4FC2\u6570\u30E9\u30A4\u30D6\u30E9\u30EA\n\n# \u524D\u8A08\
    \u7B97 O(n)\n# O(1) \u3067 nCk, nHk \u3092\u8FD4\u3059\nclass Comb:\n    def __init__(self,\
    \ n, mod):\n        self.mod = mod\n        self.n = n\n        self.fact = [1,\
    \ 1]\n        self.factinv = [1, 1]\n        self.inv = [0, 1]\n        for i\
    \ in range(2, self.n + 1):\n            self.fact.append((self.fact[i - 1] * i)\
    \ % self.mod)\n            self.inv.append(\n                (self.mod - self.inv[self.mod\
    \ % i] * (self.mod // i)) % self.mod\n            )\n            self.factinv.append((self.factinv[i\
    \ - 1] * self.inv[i]) % self.mod)\n\n    def C(self, n, k):  # nCk % mod\u3092\
    \u8FD4\u3059\n        assert n <= self.n\n        if (k < 0 or n < 0) or (n <\
    \ k):\n            return 0\n        if k == 1:\n            return n\n      \
    \  k = min(k, n - k)\n        return (\n            self.fact[n] * self.factinv[k]\
    \ % self.mod * self.factinv[n - k] % self.mod\n        )\n\n    # \u91CD\u8907\
    \u7D44\u5408\u305B nHr % mod\u3092\u8FD4\u3059\n    def H(self, n, r):\n     \
    \   return self.C(n + r - 1, r)\n\n\n# O(k) \u524D\u8A08\u7B97\n# O(k) \u3067\
    \ nCk \u3092\u8A08\u7B97\uFF08n \u304C\u5927\u304D\u3044\u3068\u304D\u3067\u3082\
    \u4F7F\u3048\u308B\uFF09\nclass Comb:\n    def __init__(self, k, mod):\n     \
    \   self.k = k\n        self.mod = mod\n        self.fact_inv = [0] * (k + 1)\n\
    \        self.inv = [0] * (k + 1)\n        self.fact_inv[0] = 1\n        if k\
    \ >= 1:\n            self.fact_inv[1] = 1\n            self.inv[1] = 1\n\n   \
    \     for i in range(2, k + 1):\n            self.inv[i] = mod - self.inv[mod\
    \ % i] * (mod // i) % mod\n            self.fact_inv[i] = self.fact_inv[i - 1]\
    \ * self.inv[i] % mod\n\n    def nCk(self, n, k):\n        if k < 0 or k > n:\n\
    \            return 0\n        if k > self.k:\n            raise ValueError(\"\
    precomputed k is too small\")\n        ans = 1\n        for i in range(k):\n \
    \           ans *= n - i\n            ans %= self.mod\n        return ans * self.fact_inv[k]\
    \ % self.mod\n\n\nclass PascalsTriangle:\n    \"\"\"\n    \u30D1\u30B9\u30AB\u30EB\
    \u306E\u4E09\u89D2\u5F62\u3067 nCk \u3092\u6C42\u3081\u308B\n    \u8A08\u7B97\u91CF\
    : O(N^2)\n    mod \u304C\u7D20\u6570\u3067\u306A\u304F\u3066\u3082\u4F7F\u7528\
    \u53EF\u80FD\n    \"\"\"\n\n    def __init__(self, N, mod):\n        self.mod\
    \ = mod\n        self.binom = [[0] * (N + 1) for _ in range(N + 1)]\n        for\
    \ i in range(N + 1):\n            self.binom[i][0] = 1\n            for j in range(1,\
    \ i + 1):\n                self.binom[i][j] = (\n                    self.binom[i\
    \ - 1][j - 1] + self.binom[i - 1][j]\n                ) % mod\n\n    def C(self,\
    \ n, k):\n        assert 0 <= k <= n\n        return self.binom[n][k]\n\n    def\
    \ H(self, n, k):\n        \"\"\"\u91CD\u8907\u7D44\u5408\u305B nHk\"\"\"\n   \
    \     assert n >= 0 and k >= 0\n        return self.C(n + k - 1, k)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/modComb.py
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/modComb.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/modComb.py
- /library/algorithm_library/python/math/modComb.py.html
title: algorithm_library/python/math/modComb.py
---
