---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: tests/math/test_cmp_sort.py
    title: tests/math/test_cmp_sort.py
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
  code: "def cmp_sort(a, cmp):\n    \"\"\"\u6BD4\u8F03\u95A2\u6570 cmp \u306B\u5F93\
    \u3063\u3066\u30EA\u30B9\u30C8 a \u3092\u7834\u58CA\u7684\u306B\u5B89\u5B9A\u30BD\
    \u30FC\u30C8\u3059\u308B\u3002\n\n    cmp(x, y) \u306F x \u304C\u5148\u306A\u3089\
    \u8CA0\u3001\u540C\u9806\u4F4D\u306A\u3089 0\u3001\u5F8C\u306A\u3089\u6B63\u3092\
    \u8FD4\u3059\u3002\n    \u6BD4\u8F03\u7D50\u679C\u306F\u4E00\u8CAB\u3057\u305F\
    \u9806\u5E8F\u3092\u5B9A\u3081\u308B\u3053\u3068\u3002\u4E26\u3079\u66FF\u3048\
    \u305F\u540C\u3058\u30EA\u30B9\u30C8 a \u3092\u8FD4\u3059\u3002\n    \u6642\u9593\
    \ O(n log n)\u3001\u8FFD\u52A0\u9818\u57DF O(n)\u3002\u6574\u5217\u6E08\u307F\u30FB\
    \u72ED\u7FA9\u9006\u9806\u306A\u3089 O(n)\u3002\n    PyPy \u5411\u3051\u306B\u6BD4\
    \u8F03\u95A2\u6570\u3092\u76F4\u63A5\u547C\u3073\u51FA\u3059\u3001\u975E\u518D\
    \u5E30\u306E\u30DE\u30FC\u30B8\u30BD\u30FC\u30C8\u3002\n    \"\"\"\n    n = len(a)\n\
    \    # \u5168\u4F53\u304C\u6607\u9806\u307E\u305F\u306F\u72ED\u7FA9\u964D\u9806\
    \u306A\u3089 O(n) \u3067\u7D42\u4E86\u3059\u308B\u3002\n    if n > 1:\n      \
    \  d = cmp(a[0], a[1]) > 0\n        r = 2\n        while r < n and (cmp(a[r -\
    \ 1], a[r]) > 0) == d:\n            r += 1\n        if r == n:\n            if\
    \ d:\n                a.reverse()\n            return a\n\n    # \u5E45 w \u306E\
    \u6574\u5217\u6E08\u307F\u533A\u9593\u3092\u96A3\u540C\u58EB\u3067\u30DE\u30FC\
    \u30B8\u3059\u308B\u3002\n    w = 1\n    while w < n:\n        for l in range(0,\
    \ n - w, 2 * w):\n            m, r = l + w, min(l + 2 * w, n)\n            if\
    \ cmp(a[m - 1], a[m]) <= 0:\n                continue\n            b = a[l:m]\
    \  # \u5DE6\u5074\u3060\u3051\u9000\u907F\u3059\u308B\u3002\u9577\u3055\u306F\u5E38\
    \u306B w\u3002\n            i, j, k = 0, m, l\n            while i < w and j <\
    \ r:\n                if cmp(b[i], a[j]) <= 0:\n                    a[k] = b[i]\n\
    \                    i += 1\n                else:\n                    a[k] =\
    \ a[j]\n                    j += 1\n                k += 1\n            a[k:j]\
    \ = b[i:]\n        w *= 2\n    return a\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/CmpSort.py
  requiredBy:
  - tests/math/test_cmp_sort.py
  timestamp: '2026-10-25 21:47:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/CmpSort.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/CmpSort.py
- /library/algorithm_library/python/techniques/CmpSort.py.html
title: algorithm_library/python/techniques/CmpSort.py
---
