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
  code: "class BIT:\n    def __init__(self, n):\n        self.n = n + 1\n        self.bit\
    \ = [[0] * self.n for _ in range(2)]\n\n    def _add_sub(self, p, i, x):\n   \
    \     idx = i\n        while idx < self.n:\n            self.bit[p][idx] += x\n\
    \            idx += idx & -idx\n\n    def add(self, l, r, x):  # [l,r)\u306Bx\u3092\
    \u52A0\u7B97\n        bit0, bit1 = self.bit\n        n = self.n\n        c = -x\
    \ * (l - 1)\n        while l < n:\n            bit0[l] += c\n            bit1[l]\
    \ += x\n            l += l & -l\n        c = x * (r - 1)\n        while r < n:\n\
    \            bit0[r] += c\n            bit1[r] -= x\n            r += r & -r\n\
    \n    def _sum_sub(self, p, i):\n        s = 0\n        idx = i\n        while\
    \ idx > 0:\n            s += self.bit[p][idx]\n            idx -= idx & -idx\n\
    \        return s\n\n    def SUM(self, i):\n        bit0, bit1 = self.bit\n  \
    \      s0 = s1 = 0\n        idx = i\n        while idx > 0:\n            s0 +=\
    \ bit0[idx]\n            s1 += bit1[idx]\n            idx -= idx & -idx\n    \
    \    return s0 + s1 * i\n\n    # \u4EFB\u610F\u306E\u533A\u9593[l,r)\u306E\u533A\
    \u9593\u3092\u3092\u53D6\u5F97\n    def range_sum(self, l, r):\n        return\
    \ self.SUM(r - 1) - self.SUM(l - 1)\n\n    # a_1 + a_2 + ... + a_x >= w \u3068\
    \u306A\u308B\u6700\u5C0F\u306E x \u3092 O(log n) \u3067\u6C42\u3081\u308B\n  \
    \  # \u5404\u8981\u7D20\u306F\u975E\u8CA0\u3067\u3042\u308B\u3053\u3068\u3002\
    w <= 0 \u306A\u3089 0\u3001\u898B\u3064\u304B\u3089\u306A\u3051\u308C\u3070\u8981\
    \u7D20\u6570 + 1\n    def lower_bound(self, w):\n        if w <= 0:\n        \
    \    return 0\n\n        bit0, bit1 = self.bit\n        n = self.n\n        x\
    \ = s0 = s1 = 0\n        step = 1 << (n.bit_length() - 1)\n        while step:\n\
    \            nxt = x + step\n            if nxt < n:\n                t0 = s0\
    \ + bit0[nxt]\n                t1 = s1 + bit1[nxt]\n                # SUM(nxt)\
    \ \u30922\u672C\u306EBIT\u306E\u7D2F\u7A4D\u5024\u304B\u3089\u5FA9\u5143\u3059\
    \u308B\n                if t0 + t1 * nxt < w:\n                    x, s0, s1 =\
    \ nxt, t0, t1\n            step >>= 1\n        return x + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/BIT.py
  requiredBy: []
  timestamp: '2026-10-20 12:29:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/BIT.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/BIT.py
- /library/algorithm_library/python/data-structure/BIT.py.html
title: algorithm_library/python/data-structure/BIT.py
---
