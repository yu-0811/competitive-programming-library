---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: algorithm_library/python/graph/EulerTour.py
    title: algorithm_library/python/graph/EulerTour.py
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
  code: "class BIT:\n    def __init__(self, n):\n        self.n = n\n        self.bit\
    \ = [[0] * self.n for _ in range(2)]\n\n    def add(self, l, r, x):  # [l,r)\u306B\
    x\u3092\u52A0\u7B97\n        bit0, bit1 = self.bit\n        n = self.n\n     \
    \   c = -x * l\n        while l < n:\n            bit0[l] += c\n            bit1[l]\
    \ += x\n            l |= l + 1\n        c = x * r\n        while r < n:\n    \
    \        bit0[r] += c\n            bit1[r] -= x\n            r |= r + 1\n\n  \
    \  # \u533A\u9593 [0, i) \u306E\u548C\u3092\u53D6\u5F97\n    def SUM(self, i):\n\
    \        bit0, bit1 = self.bit\n        s0 = s1 = 0\n        idx = i - 1\n   \
    \     while idx >= 0:\n            s0 += bit0[idx]\n            s1 += bit1[idx]\n\
    \            idx = (idx & (idx + 1)) - 1\n        return s0 + s1 * i\n\n    #\
    \ \u533A\u9593 [l, r) \u306E\u548C\u3092\u53D6\u5F97\n    def range_sum(self,\
    \ l, r):\n        return self.SUM(r) - self.SUM(l)\n\n    # a[0] + ... + a[x]\
    \ >= w \u3068\u306A\u308B\u6700\u5C0F\u306E x \u3092 O(log n) \u3067\u6C42\u3081\
    \u308B\n    # \u5404\u8981\u7D20\u306F\u975E\u8CA0\u3067\u3042\u308B\u3053\u3068\
    \u3002w <= 0 \u306A\u3089 0\u3001\u898B\u3064\u304B\u3089\u306A\u3051\u308C\u3070\
    \ n\n    def lower_bound(self, w):\n        if w <= 0:\n            return 0\n\
    \n        bit0, bit1 = self.bit\n        n = self.n\n        x = -1\n        s0\
    \ = s1 = 0\n        step = 1 << n.bit_length()\n        while step:\n        \
    \    nxt = x + step\n            if nxt < n:\n                t0 = s0 + bit0[nxt]\n\
    \                t1 = s1 + bit1[nxt]\n                # SUM(nxt + 1) \u30922\u672C\
    \u306EBIT\u306E\u7D2F\u7A4D\u5024\u304B\u3089\u5FA9\u5143\u3059\u308B\n      \
    \          if t0 + t1 * (nxt + 1) < w:\n                    x, s0, s1 = nxt, t0,\
    \ t1\n            step >>= 1\n        return x + 1\n\n\nclass fenwick_tree:\n\
    \    def __init__(self, n):\n        self.n = n\n        self.data = [0] * n\n\
    \n    def add(self, p, x):\n        assert 0 <= p < self.n\n        data = self.data\n\
    \        while p < self.n:\n            data[p] += x\n            p |= p + 1\n\
    \n    def sum0(self, r):\n        s = 0\n        while r:\n            s += self.data[r\
    \ - 1]\n            r &= r - 1\n        return s\n\n    def sum(self, l, r):\n\
    \        assert 0 <= l <= r <= self.n\n        return self.sum0(r) - self.sum0(l)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/BIT.py
  requiredBy:
  - algorithm_library/python/graph/EulerTour.py
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/BIT.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/BIT.py
- /library/algorithm_library/python/data_structure/BIT.py.html
title: algorithm_library/python/data_structure/BIT.py
---
