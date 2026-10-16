---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://info.atcoder.jp/entry/algorithm_lectures/lex_min_string_concatenation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# O(|S|)\n# Z[i] := S[0:|S|) \u3068 S[i:|S|) \u306E\u6700\u9577\u5171\u901A\
    \u63A5\u982D\u8F9E\u306E\u9577\u3055\ndef z_algo(S):\n    Z = [0] * len(S)\n \
    \   Z[0] = len(S)\n    i, j = 1, 0\n    while i < len(S):\n        # \u4E00\u81F4\
    \u3059\u308B\u9650\u308A\u5EF6\u9577\u3059\u308B\n        while i + j < len(S)\
    \ and S[j] == S[i + j]:\n            j += 1\n        Z[i] = j\n\n        # \u4E00\
    \u6587\u5B57\u3082\u4E00\u81F4\u3057\u306A\u3044\u306A\u3089\u30B3\u30D4\u30FC\
    \u3067\u304D\u306A\u3044\u306E\u3067\u6B21\u306B\u9032\u3080\n        if j ==\
    \ 0:\n            i += 1\n            continue\n\n        k = 1\n        # k+Z[k]>j\
    \ \u306A\u30891\u56DE\u76EE\u306E\u767B\u5834\u306E\u969B\u306B\u306F\u307F\u51FA\
    \u3057\u3066\u3057\u307E\u3063\u3066\u3044\u308B\n        # k+Z[k]=j \u306A\u3089\
    2\u56DE\u76EE\u306E\u767B\u5834\u306E\u969B\u306B\u306F\u307F\u51FA\u3059\u53EF\
    \u80FD\u6027\u304C\u3042\u308B\n        while k < j and k + Z[k] < j:\n      \
    \      Z[i + k] = Z[k]\n            k += 1\n        # \u307E\u3060\u672A\u78BA\
    \u5B9A\u306A\u3068\u3053\u308D\u307E\u3067 i \u3092\u9032\u3081\u308B\n      \
    \  i += k\n        # j \u3092 i \u306B\u5408\u308F\u305B\u308B\n        j -= k\n\
    \n    return Z\n\n\n# reference: https://info.atcoder.jp/entry/algorithm_lectures/lex_min_string_concatenation\n\
    def sort_by_concat(T: list[str]) -> list[str]:\n    \"\"\"\n    \u6587\u5B57\u5217\
    \u914D\u5217 T = [S_1, S_2, ...] \u306E\u4E26\u3079\u66FF\u3048\u3067\u3042\u308A\
    \u3001\u6587\u5B57\u5217\u3092\u7D50\u5408 S_1 + S_2 + ... \u3057\u305F\u3068\u304D\
    \u8F9E\u66F8\u9806\u6700\u5C0F\u306B\u306A\u308B\u9806\u756A\u306B\u4E26\u3079\
    \u66FF\u3048\u3066\u8FD4\u3059\n    T \u306E\u8F9E\u66F8\u9806\u30BD\u30FC\u30C8\
    \u3067\u306F\u306A\u3044\n    \"\"\"\n\n    # a, b \u306E\u8F9E\u66F8\u9806\u3092\
    \u8FD4\u3059\n    def lexcmp(a: str, b: str) -> int:\n        return (a > b) -\
    \ (a < b)\n\n    def cmp(x: tuple[str, list[int]], y: tuple[str, list[int]]) ->\
    \ int:\n        \"\"\"\n        a+b < b+a \u306A\u3089 -1, a+b == b+a \u306A\u3089\
    \ 0, a+b > b+a \u306A\u3089 1\n        \"\"\"\n        a, za = x\n        b, zb\
    \ = y\n        isrev = len(a) > len(b)\n        if isrev:\n            a, b =\
    \ b, a\n            za, zb = zb, za\n        n, m = len(a), len(b)\n\n       \
    \ # 1. a \u3068 b[:n]\n        f = lexcmp(a, b[:n])\n\n        # 2, b[:m-n] \u3068\
    \ b[n:m]\n        if f == 0 and n < m:\n            k = m - n\n            lcp\
    \ = min(zb[n], k)\n            # b[:m-n] != b[n:m] \u306A\u3089 lcp \u306E\u76F4\
    \u5F8C\u306E\u6587\u5B57\u3067\u8F9E\u66F8\u9806\u6C7A\u307E\u308B\n         \
    \   if lcp < k:\n                f = lexcmp(b[lcp], b[n + lcp])\n\n        # 3.\
    \ b[m-n:] \u3068 a\n        if f == 0:\n            f = lexcmp(b[m - n :], a)\n\
    \n        return -f if isrev else f\n\n    def merge_sort(arr: list[tuple[str,\
    \ list[int]]]):\n        # arr \u306E\u8981\u7D20\u306F (\u6587\u5B57\u5217, Z-array)\n\
    \        if len(arr) <= 1:\n            return arr\n\n        mid = len(arr) //\
    \ 2\n        left = merge_sort(arr[:mid])\n        right = merge_sort(arr[mid:])\n\
    \n        res = []\n        i = j = 0\n\n        while i < len(left) and j < len(right):\n\
    \            if cmp(left[i], right[j]) <= 0:\n                res.append(left[i])\n\
    \                i += 1\n            else:\n                res.append(right[j])\n\
    \                j += 1\n\n        res.extend(left[i:])\n        res.extend(right[j:])\n\
    \        return res\n\n    Z = [z_algo(t) for t in T]\n    TZ = list(zip(T, Z))\n\
    \    return [s for s, z in merge_sort(TZ)]\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/string/sort_by_concat.py
  requiredBy: []
  timestamp: '2026-10-16 13:28:30+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/string/sort_by_concat.py
layout: document
redirect_from:
- /library/algorithm_library/python/string/sort_by_concat.py
- /library/algorithm_library/python/string/sort_by_concat.py.html
title: algorithm_library/python/string/sort_by_concat.py
---
