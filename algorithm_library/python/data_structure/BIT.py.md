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
  code: "from operator import gt, lt\n\n\nclass RangeAddBIT: # \u533A\u9593\u52A0\u7B97\
    \u533A\u9593\u548C\n    def __init__(s, n):\n        s.n = n\n        s.bit =\
    \ [[0] * s.n for _ in range(2)]\n\n    # \u521D\u671F\u914D\u5217 a \u304B\u3089\
    \ O(n) \u3067\u69CB\u7BC9\u3059\u308B\u5834\u5408\u306F __init__ \u3092\u3053\u3061\
    \u3089\u306B\u5DEE\u3057\u66FF\u3048\u308B\u3002\n    # def __init__(s, a):\n\
    \    #     n = s.n = len(a)\n    #     b0, b1 = s.bit = [[0] * n, [0] * n]\n \
    \   #     p = 0\n    #     for i, x in enumerate(a):\n    #         d = x - p\n\
    \    #         p = x\n    #         b0[i] -= i * d\n    #         b1[i] += d\n\
    \    #         j = i | (i + 1)\n    #         if j < n:\n    #             b0[j]\
    \ += b0[i]\n    #             b1[j] += b1[i]\n\n    def rangeadd(s, l, r, x):\
    \  # [l,r)\u306Bx\u3092\u52A0\u7B97\n        b0, b1 = s.bit\n        n = s.n\n\
    \        c = -x * l\n        while l < n:\n            b0[l] += c\n          \
    \  b1[l] += x\n            l |= l + 1\n        c = x * r\n        while r < n:\n\
    \            b0[r] += c\n            b1[r] -= x\n            r |= r + 1\n\n  \
    \  def _sum(s, i): # \u533A\u9593 [0, i) \u306E\u548C\n        b0, b1 = s.bit\n\
    \        s0 = s1 = 0\n        idx = i - 1\n        while idx >= 0:\n         \
    \   s0 += b0[idx]\n            s1 += b1[idx]\n            idx = (idx & (idx +\
    \ 1)) - 1\n        return s0 + s1 * i\n\n    def sum(s, l, r): # \u533A\u9593\
    \ [l, r) \u306E\u548C\n        return s._sum(r) - s._sum(l)\n\n    # a[0] + ...\
    \ + a[x] >= w \u3068\u306A\u308B\u6700\u5C0F\u306E x \u3092 O(log n) \u3067\u6C42\
    \u3081\u308B\n    # \u5404\u8981\u7D20\u306F\u975E\u8CA0\u3067\u3042\u308B\u3053\
    \u3068\u3002w <= 0 \u306A\u3089 0\u3001\u898B\u3064\u304B\u3089\u306A\u3051\u308C\
    \u3070 n\n    def lower_bound(s, w):\n        if w <= 0:\n            return 0\n\
    \n        b0, b1 = s.bit\n        n = s.n\n        x = -1\n        s0 = s1 = 0\n\
    \        step = 1 << n.bit_length()\n        while step:\n            nxt = x\
    \ + step\n            if nxt < n:\n                t0 = s0 + b0[nxt]\n       \
    \         t1 = s1 + b1[nxt]\n                if t0 + t1 * (nxt + 1) < w:\n   \
    \                 x, s0, s1 = nxt, t0, t1\n            step >>= 1\n        return\
    \ x + 1\n\n\nclass BIT:  # 1\u70B9\u52A0\u7B97\u533A\u9593\u548C\n    def __init__(s,\
    \ a):\n        d = s.d = a\n        n = s.n = len(d)\n        for i in range(n):\n\
    \            j = i | (i + 1)\n            if j < n:\n                d[j] += d[i]\n\
    \n    def add(s, p, x):\n        assert 0 <= p < s.n\n        d = s.d\n      \
    \  while p < s.n:\n            d[p] += x\n            p |= p + 1\n\n    def set(s,\
    \ p, x):\n        s.add(p, x - s.get(p))\n\n    def get(s, p):\n        return\
    \ s.prod(p, p + 1)\n\n    def prod0(s, r):\n        res = 0\n        while r:\n\
    \            res += s.d[r - 1]\n            r &= r - 1\n        return res\n\n\
    \    def prod(s, l, r):\n        assert 0 <= l <= r <= s.n\n        return s.prod0(r)\
    \ - s.prod0(l)\n\n\nclass XorBIT:  # 1\u70B9XOR\u533A\u9593XOR\n    def __init__(s,\
    \ a):\n        d = s.d = a\n        n = s.n = len(d)\n        for i in range(n):\n\
    \            j = i | (i + 1)\n            if j < n:\n                d[j] ^= d[i]\n\
    \n    def add(s, p, x):  # a[p] ^= x\n        assert 0 <= p < s.n\n        d =\
    \ s.d\n        while p < s.n:\n            d[p] ^= x\n            p |= p + 1\n\
    \n    def set(s, p, x):\n        s.add(p, x ^ s.get(p))\n\n    def get(s, p):\n\
    \        return s.prod(p, p + 1)\n\n    def prod0(s, r):\n        res = 0\n  \
    \      while r:\n            res ^= s.d[r - 1]\n            r &= r - 1\n     \
    \   return res\n\n    def prod(s, l, r):\n        assert 0 <= l <= r <= s.n\n\
    \        return s.prod0(r) ^ s.prod0(l)\n    \n\nclass MinBIT:  # 1\u70B9\u4EE3\
    \u5165\uFF08\u6E1B\u5C11\u306E\u307F\uFF09\u30FB1\u70B9\u53D6\u5F97\u30FB\u533A\
    \u9593\u6700\u5C0F\u5024\n    op = min\n    cmp = lt\n    e = 10**18  # \u5024\
    \u57DF\u306F -10**18 \u4EE5\u4E0A 10**18 \u4EE5\u4E0B\u3002\n\n    def __init__(s,\
    \ a):\n        s.a = a\n        n = s.n = len(a)\n        op = s.op\n        #\
    \ \u5185\u90E8\u306F 1-indexed\u3002b0[i] \u306F i \u304C\u53F3\u7AEF\u3001b1[i]\
    \ \u306F i \u304C\u5DE6\u7AEF\u3002\n        b0 = s.b0 = [s.e] + a\n        b1\
    \ = s.b1 = b0[:]\n        for i in range(1, n + 1):\n            j = i + (i &\
    \ -i)\n            if j <= n:\n                b0[j] = op(b0[j], b0[i])\n    \
    \    for i in range(n, 0, -1):\n            j = i & (i - 1)\n            if j:\n\
    \                b1[j] = op(b1[j], b1[i])\n\n    def set(s, p, x):\n        n\
    \ = s.n\n        assert 0 <= p < n\n        a, b0, b1, cmp = s.a, s.b0, s.b1,\
    \ s.cmp\n        y = a[p]\n        assert cmp(x, y) or x == y\n        a[p] =\
    \ x\n        # \u89AA\u306F\u5B50\u306E\u533A\u9593\u3092\u542B\u3080\u306E\u3067\
    \u3001\u6975\u5024\u304C\u5909\u308F\u3089\u306A\u3044\u6642\u70B9\u3067\u6B62\
    \u3081\u308B\u3002\n        i = p + 1\n        while i <= n and cmp(x, b0[i]):\n\
    \            b0[i] = x\n            i += i & -i\n        i = p + 1\n        while\
    \ i and cmp(x, b1[i]):\n            b1[i] = x\n            i &= i - 1\n\n    def\
    \ get(s, p):\n        assert 0 <= p < s.n\n        return s.a[p]\n\n    def prod0(s,\
    \ r):\n        return s.prod(0, r)\n\n    def prod(s, l, r):\n        assert 0\
    \ <= l <= r <= s.n\n        res = s.e\n        if l == r:\n            return\
    \ res\n        b0, b1, op = s.b0, s.b1, s.op\n        l += 1\n        while l\
    \ < r:\n            j = l + (l & -l)\n            if j > r:\n                break\n\
    \            res = op(res, b1[l])\n            l = j\n        while l < r:\n \
    \           res = op(res, b0[r])\n            r &= r - 1\n        return op(res,\
    \ s.a[l - 1])\n\n\nclass MaxBIT(MinBIT):  # 1\u70B9\u4EE3\u5165\uFF08\u5897\u52A0\
    \u306E\u307F\uFF09\u30FB1\u70B9\u53D6\u5F97\u30FB\u533A\u9593\u6700\u5927\u5024\
    \n    op = max\n    cmp = gt\n    e = -10**18\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/BIT.py
  requiredBy:
  - algorithm_library/python/graph/EulerTour.py
  timestamp: '2026-11-19 23:50:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/BIT.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/BIT.py
- /library/algorithm_library/python/data_structure/BIT.py.html
title: algorithm_library/python/data_structure/BIT.py
---
