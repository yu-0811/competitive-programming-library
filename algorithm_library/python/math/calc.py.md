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
    - https://atcoder.jp/contests/abc367/editorial/10712
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u5207\u308A\u4E0A\u3052\u9664\u7B97\ndef ceilDiv(p: int, q: int) -> int:\n\
    \    return (p + q - 1) // q\n\n\n# \u7B49\u5DEE\u6570\u5217\u306E\u548C\n# \u521D\
    \u9805 a1, \u9805\u6570 n, \u516C\u5DEE d\ndef cal(a1, n, d):\n    return (n *\
    \ (2 * a1 + (n - 1) * d)) // 2\n\n\n# https://atcoder.jp/contests/abc367/editorial/10712\n\
    def c_is_buween_a_to_b(a, b, c):\n    return (a - b) * (b - c) * (c - a) > 0"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/calc.py
  requiredBy: []
  timestamp: '2026-11-22 20:55:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/calc.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/calc.py
- /library/algorithm_library/python/math/calc.py.html
title: algorithm_library/python/math/calc.py
---
