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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import getrandbits\n\n\n# \u63A5\u982D\u8F9E\u7248\u3002N = len(A)\
    \ + len(B) \u3068\u3057\u3066\u3001\u524D\u51E6\u7406\u306F\u671F\u5F85 O(N) \u6642\
    \u9593\u30FBO(N) \u9818\u57DF\u3001\u30AF\u30A8\u30EA\u306F O(1)\u3002\n# \u7570\
    \u306A\u308B\u96C6\u5408\u304C\u4E00\u81F4\u3059\u308B\u78BA\u7387\u306F 1 \u30AF\
    \u30A8\u30EA\u3042\u305F\u308A 2^-61\u3002\nclass ZobristHash:\n    def __init__(self,\
    \ A, B):\n        h, a, b = {}, [0], [0]\n        for x in A:\n            v =\
    \ 0\n            if x not in h:\n                h[x] = v = getrandbits(61)\n\
    \            a.append(a[-1] ^ v)\n        for x in B:\n            v = h.get(x)\n\
    \            if v is None:\n                v = getrandbits(61)\n            h[x]\
    \ = 0  # B \u3067 2 \u56DE\u76EE\u4EE5\u964D\u306B\u73FE\u308C\u305F\u3089 XOR\
    \ \u3057\u306A\u3044\n            b.append(b[-1] ^ v)\n        self.a, self.b\
    \ = a, b\n\n    # [0, ar) \u3068 [0, br) \u306E\u96C6\u5408\u3092\u6BD4\u8F03\u3059\
    \u308B\u3002\n    def isEqual(self, ar, br):\n        return self.a[ar] == self.b[br]\n\
    \n\nfrom bisect import bisect_left\n\n\n# \u4EFB\u610F\u533A\u9593\u7248\uFF08\
    \u53B3\u5BC6\uFF09\u3002N = len(A) + len(B)\u3001K = \u7570\u306A\u308B\u5024\u306E\
    \u6570\u3001W = 2 \u533A\u9593\u306E\u9577\u3055\u306E\u548C\u3002\n# \u524D\u51E6\
    \u7406\u306F\u671F\u5F85 O(N) \u6642\u9593\u30FBO(N) \u9818\u57DF\u3001\u30AF\u30A8\
    \u30EA\u306F\u671F\u5F85 O(1 + min(W, K log(N + 2)))\u3002\nclass ZobristHash:\n\
    \    def __init__(self, A, B):\n        self.A, self.B = list(A), list(B)\n  \
    \      self.log = (len(self.A) + len(self.B)).bit_length() + 1\n        pos =\
    \ {}\n        for side, S in enumerate((self.A, self.B)):\n            for i,\
    \ x in enumerate(S):\n                pos.setdefault(x, ([-1], [-1]))[side].append(i)\n\
    \        self.pos = list(pos.values())\n\n    # 0-index \u306E\u534A\u958B\u533A\
    \u9593 [al, ar), [bl, br) \u306E\u96C6\u5408\u3092\u6BD4\u8F03\u3059\u308B\u3002\
    \n    def isEqual(self, al, ar, bl, br):\n        if al == ar or bl == br:\n \
    \           return al == ar and bl == br\n\n        def has(p, l, r, n):\n   \
    \         # \u51FA\u73FE\u304C\u591A\u3044\u5024\u306F\u3001\u533A\u9593\u4E2D\
    \u592E\u4ED8\u8FD1\u306B\u5F53\u305F\u308B\u6DFB\u5B57\u3092\u898B\u7A4D\u3082\
    \u3063\u3066\u5148\u306B\u8A66\u3059\u3002\n            if len(p) > 64 and l <=\
    \ p[(l + r) * len(p) // (2 * n + 1)] < r:\n                return True\n     \
    \       return p[bisect_left(p, r) - 1] >= l\n\n        n, m = len(self.A), len(self.B)\n\
    \        budget = (ar - al + br - bl) // self.log\n        for a, b in self.pos:\n\
    \            if budget == 0:\n                return set(self.A[al:ar]) == set(self.B[bl:br])\n\
    \            budget -= 1\n            if has(a, al, ar, n) != has(b, bl, br, m):\n\
    \                return False\n        return True\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/hash/ZobristHash.py
  requiredBy: []
  timestamp: '2026-11-22 20:43:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/hash/ZobristHash.py
layout: document
redirect_from:
- /library/algorithm_library/python/hash/ZobristHash.py
- /library/algorithm_library/python/hash/ZobristHash.py.html
title: algorithm_library/python/hash/ZobristHash.py
---
