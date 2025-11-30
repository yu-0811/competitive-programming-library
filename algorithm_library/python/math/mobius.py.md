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
  code: "def mobius(A):\n    \"\"\"\n    \u9AD8\u901F\u30E1\u30D3\u30A6\u30B9\u5909\
    \u63DB\n    N = log_2 |A| \u3068\u3057\u3066 O(N 2^N)\n    Args:\n        A: \u30B5\
    \u30A4\u30BA\u304C 2^N \u306E\u30EA\u30B9\u30C8\n           A[mask] \u306B\u306F\
    \u300C\u6761\u4EF6 mask \u3092\u5C11\u306A\u304F\u3068\u3082\u6E80\u305F\u3059\
    \u7D44\u5408\u305B\u306E\u7DCF\u548C\u300D\u304C\u5165\u3063\u3066\u3044\u308B\
    \n    Returns:\n        A: \u5909\u63DB\u5F8C\u306E\u30EA\u30B9\u30C8 (\u7834\u58CA\
    \u7684\u5909\u66F4)\n           A[mask] \u306B\u306F\u300C\u3061\u3087\u3046\u3069\
    \u6761\u4EF6 mask \u3060\u3051\u3092\u6E80\u305F\u3059\u7D44\u5408\u305B\u300D\
    \u304C\u5165\u308B\n    \"\"\"\n    n = len(A).bit_length() - 1\n    assert len(A)\
    \ == (1 << n), \"\u914D\u5217\u306E\u9577\u3055\u306F 2^N \u3067\u3042\u308B\u5FC5\
    \u8981\u304C\u3042\u308A\u307E\u3059\"\n\n    for i in range(n):\n        bit\
    \ = 1 << i\n        for mask in range(1 << n):\n            if not (mask & bit):\n\
    \                A[mask] -= A[mask | bit]\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/mobius.py
  requiredBy: []
  timestamp: '2025-11-30 11:50:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/mobius.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/mobius.py
- /library/algorithm_library/python/math/mobius.py.html
title: algorithm_library/python/math/mobius.py
---
