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
  code: "def mos_algorithm(data, que):\n    \"\"\"\n    data : list of int : \u5143\
    \u306E\u914D\u5217\n    que : list of tuple : \u30AF\u30A8\u30EA\u306E\u30EA\u30B9\
    \u30C8\n    \u30AF\u30A8\u30EA\u306F 0-indexed \u3067\u534A\u958B\u533A\u9593\
    [l,r)\n    \u66F4\u65B0\u95A2\u6570\u306B\u306F\u534A\u958B\u533A\u9593\u3092\u6E21\
    \u3057\u3001\u56DE\u7B54\u306E\u53D6\u5F97\u306F\u30AF\u30A8\u30EA\u3054\u3068\
    \u306B1\u56DE\u3060\u3051\u884C\u3046\u3002\n    \u5DE6\u53F3\u306E\u8FFD\u52A0\
    \u30FB\u524A\u9664\u3092\u5225\u3005\u306B\u5B9A\u7FA9\u3057\u3001\u5404\u8981\
    \u7D20\u3092\u7AEF\u304B\u3089\u9806\u306B\u51E6\u7406\u3059\u308B\u3002\n   \
    \ \"\"\"\n    from math import sqrt, ceil\n\n    n = len(data)\n    q = len(que)\n\
    \    if q == 0:\n        return []\n    B = max(1, ceil(sqrt(1.5) * n / sqrt(q)))\n\
    \n    # \u72B6\u614B\u3092\u521D\u671F\u5316\u3059\u308B\u51E6\u7406\u3092\u66F8\
    \u304F\n    # ans = ?\n\n    def _add_left(left, right):\n        # \u5DE6\u7AEF\
    \u306B [left, right) \u3092\u8FFD\u52A0\u3059\u308B\uFF08\u53F3\u304B\u3089\u5DE6\
    \u306E\u9806\uFF09\n        for i in range(right - 1, left - 1, -1):\n       \
    \     pass\n\n    def _add_right(left, right):\n        # \u53F3\u7AEF\u306B [left,\
    \ right) \u3092\u8FFD\u52A0\u3059\u308B\uFF08\u5DE6\u304B\u3089\u53F3\u306E\u9806\
    \uFF09\n        for i in range(left, right):\n            pass\n\n    def _del_left(left,\
    \ right):\n        # \u5DE6\u7AEF\u306E [left, right) \u3092\u524A\u9664\u3059\
    \u308B\uFF08\u5DE6\u304B\u3089\u53F3\u306E\u9806\uFF09\n        for i in range(left,\
    \ right):\n            pass\n\n    def _del_right(left, right):\n        # \u53F3\
    \u7AEF\u306E [left, right) \u3092\u524A\u9664\u3059\u308B\uFF08\u53F3\u304B\u3089\
    \u5DE6\u306E\u9806\uFF09\n        for i in range(right - 1, left - 1, -1):\n \
    \           pass\n\n    shift = q.bit_length()\n    lshift = n.bit_length()\n\
    \    mask = (1 << shift) - 1\n    bucs = [[] for _ in range(n // B + 1)]\n   \
    \ for idx, (l, r) in enumerate(que):\n        bucs[l // B].append((((r << lshift)\
    \ | l) << shift) | idx)\n    order = []\n    for b, buc in enumerate(bucs):\n\
    \        buc.sort(reverse=bool(b & 1))\n        order.extend(buc)\n\n    L = R\
    \ = 0\n    ret = [-1] * q\n    for lri in order:\n        i = lri & mask\n   \
    \     l, r = que[i]\n\n        if L > l:\n            _add_left(l, L)\n      \
    \  if R < r:\n            _add_right(R, r)\n        if L < l:\n            _del_left(L,\
    \ l)\n        if R > r:\n            _del_right(r, R)\n        L, R = l, r\n\n\
    \        # \u66F4\u65B0\u3055\u308C\u305F\u72B6\u614B\u304B\u3089\u30AF\u30A8\u30EA\
    \u306E\u7B54\u3048\u3092\u6C42\u3081\u308B\n        ret[i] = \n\n    return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Mos_algorithm.py
  requiredBy: []
  timestamp: '2026-11-08 10:24:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Mos_algorithm.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Mos_algorithm.py
- /library/algorithm_library/python/techniques/Mos_algorithm.py.html
title: algorithm_library/python/techniques/Mos_algorithm.py
---
