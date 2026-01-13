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
  code: "# \u5207\u308A\u4E0A\u3052\u9664\u7B97\ndef ceilDiv(p: int, q: int) -> int:\n\
    \    return (p + q - 1) // q\n\n\ndef max_leq_congruent(R: int, r: int, m: int)\
    \ -> int:\n    \"\"\"R \u4EE5\u4E0B\u3067 r \u2261 x (mod m) \u3092\u6E80\u305F\
    \u3059\u6700\u5927\u306E\u6574\u6570 x \u3092\u6C42\u3081\u308B\"\"\"\n    r %=\
    \ m\n    return R - ((R - r) % m)\n\n\ndef min_geq_congruent(L: int, r: int, m:\
    \ int) -> int:\n    \"\"\"L \u4EE5\u4E0A\u3067 r \u2261 x (mod m) \u3092\u6E80\
    \u305F\u3059\u6700\u5C0F\u306E\u6574\u6570 x \u3092\u6C42\u3081\u308B\"\"\"\n\
    \    if m <= 0:\n        raise ValueError(\"m must be positive\")\n    r %= m\n\
    \    return L + ((r - L) % m)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/calc.py
  requiredBy: []
  timestamp: '2026-01-13 11:58:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/calc.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/calc.py
- /library/algorithm_library/python/math/calc.py.html
title: algorithm_library/python/math/calc.py
---
