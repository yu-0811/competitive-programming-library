---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: algorithm_library/python/string/Z_algo.py
    title: algorithm_library/python/string/Z_algo.py
  - icon: ':warning:'
    path: algorithm_library/python/techniques/CmpSort.py
    title: algorithm_library/python/techniques/CmpSort.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://info.atcoder.jp/entry/algorithm_lectures/lex_min_string_concatenation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from algorithm_library.python.string.Z_algo import z_algo\nfrom algorithm_library.python.techniques.CmpSort\
    \ import cmp_sort\n\n\n# reference: https://info.atcoder.jp/entry/algorithm_lectures/lex_min_string_concatenation\n\
    def sort_by_concat(T: list[str]) -> list[str]:\n    \"\"\"\n    \u6587\u5B57\u5217\
    \u914D\u5217 T = [S_1, S_2, ...] \u306E\u4E26\u3079\u66FF\u3048\u3067\u3042\u308A\
    \u3001\u6587\u5B57\u5217\u3092\u7D50\u5408 S_1 + S_2 + ... \u3057\u305F\u3068\u304D\
    \u8F9E\u66F8\u9806\u6700\u5C0F\u306B\u306A\u308B\u9806\u756A\u306B\u4E26\u3079\
    \u66FF\u3048\u3066\u8FD4\u3059\n    S_i+S_j \u3092\u57FA\u6E96\u306B\u30BD\u30FC\
    \u30C8\u3059\u308C\u3070\u3044\u3044\n    T \u306E\u8F9E\u66F8\u9806\u30BD\u30FC\
    \u30C8\u3067\u306F\u306A\u3044\n    \"\"\"\n\n    # Z-array \u306F\u6BD4\u8F03\
    \u3067\u5FC5\u8981\u306B\u306A\u3063\u305F\u3068\u304D\u306B\u4E00\u5EA6\u3060\
    \u3051\u69CB\u7BC9\u3059\u308B\n    Z = [None] * len(T)\n\n    # a, b \u306E\u8F9E\
    \u66F8\u9806\u3092\u8FD4\u3059\n    def lexcmp(a: str, b: str) -> int:\n     \
    \   return (a > b) - (a < b)\n\n    def cmp(x: int, y: int) -> int:\n        \"\
    \"\"\n        a+b < b+a \u306A\u3089 -1, a+b == b+a \u306A\u3089 0, a+b > b+a\
    \ \u306A\u3089 1\n        \"\"\"\n        a, b = T[x], T[y]\n        isrev = len(a)\
    \ > len(b)\n        if isrev:\n            a, b = b, a\n            x, y = y,\
    \ x\n        n, m = len(a), len(b)\n\n        # 1. a \u3068 b[:n]\n        f =\
    \ lexcmp(a, b[:n])\n\n        # 2, b[:m-n] \u3068 b[n:m]\n        if f == 0 and\
    \ n < m:\n            zb = Z[y]\n            if zb is None:\n                Z[y]\
    \ = zb = z_algo(b)\n            k = m - n\n            lcp = min(zb[n], k)\n \
    \           # b[:m-n] != b[n:m] \u306A\u3089 lcp \u306E\u76F4\u5F8C\u306E\u6587\
    \u5B57\u3067\u8F9E\u66F8\u9806\u6C7A\u307E\u308B\n            if lcp < k:\n  \
    \              f = lexcmp(b[lcp], b[n + lcp])\n\n        # 3. b[m-n:] \u3068 a\n\
    \        if f == 0:\n            f = lexcmp(b[m - n :], a)\n\n        return -f\
    \ if isrev else f\n\n    return [T[i] for i in cmp_sort(list(range(len(T))), cmp)]\n"
  dependsOn:
  - algorithm_library/python/string/Z_algo.py
  - algorithm_library/python/techniques/CmpSort.py
  isVerificationFile: false
  path: algorithm_library/python/string/sort_by_concat.py
  requiredBy: []
  timestamp: '2026-11-06 23:36:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/string/sort_by_concat.py
layout: document
redirect_from:
- /library/algorithm_library/python/string/sort_by_concat.py
- /library/algorithm_library/python/string/sort_by_concat.py.html
title: algorithm_library/python/string/sort_by_concat.py
---
