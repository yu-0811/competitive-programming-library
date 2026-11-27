---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: algorithm_library/python/string/sort_by_concat.py
    title: algorithm_library/python/string/sort_by_concat.py
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
  code: "# O(|S|)\u3002Z[i] \u306F S \u3068 S[i:] \u306E\u6700\u9577\u5171\u901A\u63A5\
    \u982D\u8F9E\u306E\u9577\u3055\u3002\ndef z_algo(S):\n    n = len(S)\n    Z =\
    \ [n] * n\n    l = r = 0  # S[l:r] \u306F\u63A5\u982D\u8F9E\u3068\u4E00\u81F4\u3059\
    \u308B\u533A\u9593\u3002r \u306F\u3053\u3053\u307E\u3067\u3067\u6700\u5927\n \
    \   for i in range(1, n):\n        if i < r and Z[i - l] < r - i:\n          \
    \  Z[i] = Z[i - l]\n            continue\n        l, r = i, max(i, r)\n      \
    \  while r < n and S[r - l] == S[r]:\n            r += 1\n        Z[i] = r - l\n\
    \    return Z\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/string/Z_algo.py
  requiredBy:
  - algorithm_library/python/string/sort_by_concat.py
  timestamp: '2026-11-26 00:25:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/string/Z_algo.py
layout: document
redirect_from:
- /library/algorithm_library/python/string/Z_algo.py
- /library/algorithm_library/python/string/Z_algo.py.html
title: algorithm_library/python/string/Z_algo.py
---
