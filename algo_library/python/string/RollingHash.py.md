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
  code: "class RollingHash:\n  def __init__(self, S, base = 1237, mod = (1<<61)-1):\n\
    \    N = len(S)\n    ord_base = ord('a')\n    self.base = base\n    self.mod =\
    \ mod \n    self.hash = [0] * (N + 1)\n    self.base_pow = [1] * (N + 1)\n   \
    \ for i in range(N):\n      self.base_pow[i+1] = self.base_pow[i] * base % mod\n\
    \    for idx, s in enumerate(S):\n      tmp = ord(s) - ord_base + 1 # 0 \u3092\
    \u5272\u308A\u5F53\u3066\u3066\u306F\u3044\u3051\u306A\u3044\n      self.hash[idx+1]\
    \ = (self.hash[idx] * self.base + tmp) % mod\n\n  def get_hash(self, l, r): #[l,\
    \ r)\n    return (self.hash[r] - self.hash[l] * self.base_pow[r - l]) % self.mod"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/string/RollingHash.py
  requiredBy: []
  timestamp: '2024-11-24 09:52:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/string/RollingHash.py
layout: document
redirect_from:
- /library/algo_library/python/string/RollingHash.py
- /library/algo_library/python/string/RollingHash.py.html
title: algo_library/python/string/RollingHash.py
---
