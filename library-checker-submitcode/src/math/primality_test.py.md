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
    - https://judge.yosupo.jp/problem/primality_test
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/primality_test\n# include: algorithm_library/python/math/factorization.py\n\
    \n\ndef main():\n    for _ in range(int(readline())):\n        n = int(readline())\n\
    \        prime = is_prime(n) if n < 1024 else is_prime64(n)\n        print(\"\
    Yes\" if prime else \"No\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/primality_test.py
  requiredBy: []
  timestamp: '2026-11-26 13:10:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/primality_test.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/primality_test.py
- /library/library-checker-submitcode/src/math/primality_test.py.html
title: library-checker-submitcode/src/math/primality_test.py
---
