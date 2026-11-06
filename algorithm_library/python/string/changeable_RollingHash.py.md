---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/data_structure/Segtree.py
    title: algorithm_library/python/data_structure/Segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from algorithm_library.python.data_structure.Segtree import segtree\n\n\n\
    class changeable_RollingHash:\n    def __init__(self, S, base=1237, mod=(1 <<\
    \ 61) - 1):\n        N = len(S)\n        self.N = N\n        self.ord_base = ord(\"\
    a\")\n        self.base = base\n        self.mod = mod\n        self.base_pow\
    \ = [1] * (N + 1)\n        self.base_inv = [1] * (N + 1)\n        self.inv = pow(base,\
    \ mod - 2, mod)\n        for i in range(N):\n            self.base_pow[i + 1]\
    \ = (self.base_pow[i] * base) % mod\n            self.base_inv[i + 1] = (self.base_inv[i]\
    \ * self.inv) % mod\n        hash = [\n            ((ord(s) - self.ord_base +\
    \ 1) * self.base_pow[N - idx - 1]) % mod\n            for idx, s in enumerate(S)\n\
    \        ]\n        e = 0\n\n        def operate(a, b):\n            return (a\
    \ + b) % mod\n\n        self.seg = segtree(hash, operate, e)\n\n    # \u30A4\u30F3\
    \u30C7\u30C3\u30AF\u30B9 x \u306E\u8981\u7D20\u3092 c \u306B\u5909\u3048\u308B\
    \n    def change(self, x, c):\n        self.seg.set(\n            x, ((ord(c)\
    \ - self.ord_base + 1) * self.base_pow[self.N - x - 1]) % self.mod\n        )\n\
    \n    def get_hash(self, l, r):  # [l, r),0-index\n        return (self.seg.prod(l,\
    \ r) * self.base_inv[self.N - r]) % self.mod\n"
  dependsOn:
  - algorithm_library/python/data_structure/Segtree.py
  isVerificationFile: false
  path: algorithm_library/python/string/changeable_RollingHash.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/string/changeable_RollingHash.py
layout: document
redirect_from:
- /library/algorithm_library/python/string/changeable_RollingHash.py
- /library/algorithm_library/python/string/changeable_RollingHash.py.html
title: algorithm_library/python/string/changeable_RollingHash.py
---
