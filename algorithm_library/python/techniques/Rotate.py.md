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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def two_dimension_list_rotate_R90(L: list[list[int]]) -> list[list[int]]:\n\
    \    # 2\u6B21\u5143\u30EA\u30B9\u30C8\u3092\u53F3\u306B90\u5EA6\u56DE\u8EE2\u3055\
    \u305B\u308B\n    return [list(col) for col in zip(*L[::-1])]\n\n\ndef two_dimension_list_rotate_L90(L:\
    \ list[list[int]]) -> list[list[int]]:\n    # 2\u6B21\u5143\u30EA\u30B9\u30C8\u3092\
    \u5DE6\u306B90\u5EA6\u56DE\u8EE2\u3055\u305B\u308B\n    return [list(col) for\
    \ col in zip(*L)][::-1]\n\n\ndef tention(L: list[list[int]]) -> list[list[int]]:\n\
    \    # 2\u6B21\u5143\u30EA\u30B9\u30C8\u3092\u8EE2\u7F6E\u3059\u308B\n    return\
    \ [list(col) for col in zip(*L)]\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Rotate.py
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Rotate.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Rotate.py
- /library/algorithm_library/python/techniques/Rotate.py.html
title: algorithm_library/python/techniques/Rotate.py
---
