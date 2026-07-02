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
  code: "# \u533A\u9593 [l,r] \u306B i \\in [l,r] \u306B\u4E00\u6B21\u95A2\u6570 a*i\
    \ + b \u3092\u52A0\u7B97\u3067\u304D\u308B\u30E9\u30A4\u30D6\u30E9\u30EA\n# \u30AF\
    \u30A8\u30EA l, r, a, b\uFF1A\u5404 i \u2208 [l, r] \u306B a*i + b \u3092\u52A0\
    \u7B97\u3059\u308B\nclass LinearImos:\n    def __init__(self, n, mod=None):\n\
    \        self.n = n\n        self.mod = mod\n        self.coef = [0] * (n + 1)\
    \  # i \u306E\u4FC2\u6570\n        self.cons = [0] * (n + 1)  # \u5B9A\u6570\u9805\
    \n\n    def add_linear(self, l, r, a, b):\n        \"\"\"\n        \u9589\u533A\
    \u9593 [l, r] \u306B a*i + b \u3092\u52A0\u7B97\u3059\u308B\n        \"\"\"\n\
    \        if l > r:\n            return\n\n        if self.mod is None:\n     \
    \       self.coef[l] += a\n            self.coef[r + 1] -= a\n            self.cons[l]\
    \ += b\n            self.cons[r + 1] -= b\n        else:\n            mod = self.mod\n\
    \            self.coef[l] = (self.coef[l] + a) % mod\n            self.coef[r\
    \ + 1] = (self.coef[r + 1] - a) % mod\n            self.cons[l] = (self.cons[l]\
    \ + b) % mod\n            self.cons[r + 1] = (self.cons[r + 1] - b) % mod\n\n\
    \    def add_arithmetic(self, l, r, start, diff):\n        \"\"\"\n        \u521D\
    \u9805 start \u516C\u5DEE diff \u306E\u7B49\u5DEE\u6570\u5217\u3092 [l,r] \u306B\
    \u8DB3\u3059\n        \u9589\u533A\u9593 [l, r] \u306B\n        start, start+diff,\
    \ start+2*diff, ...\n        \u3092\u52A0\u7B97\u3059\u308B\n\n        \u4F4D\u7F6E\
    \ i \u306B\u8DB3\u3059\u5024\u306F\n        start + diff*(i-l)\n        = diff*i\
    \ + (start - diff*l)\n        \"\"\"\n        a = diff\n        b = start - diff\
    \ * l\n        self.add_linear(l, r, a, b)\n\n    def build(self):\n        res\
    \ = [0] * self.n\n        c = 0\n        s = 0\n\n        if self.mod is None:\n\
    \            for i in range(self.n):\n                c += self.coef[i]\n    \
    \            s += self.cons[i]\n                res[i] = c * i + s\n        else:\n\
    \            mod = self.mod\n            for i in range(self.n):\n           \
    \     c = (c + self.coef[i]) % mod\n                s = (s + self.cons[i]) % mod\n\
    \                res[i] = (c * i + s) % mod\n\n        return res"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/LinearImos.py
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/LinearImos.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/LinearImos.py
- /library/algorithm_library/python/data-structure/LinearImos.py.html
title: algorithm_library/python/data-structure/LinearImos.py
---
