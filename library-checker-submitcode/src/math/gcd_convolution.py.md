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
    - https://judge.yosupo.jp/problem/gcd_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/gcd_convolution\n# include: algorithm_library/python/math/PIE.py\n\
    \n\ndef main():\n    n = int(readline())\n    a = [0] + list(map(int, readline().split()))\n\
    \    b = [0] + list(map(int, readline().split()))\n    sieve = PIE(n)\n    c =\
    \ [0] * (n + 1)\n    for d in range(1, n + 1):\n        c[d] = sum(a[d::d]) *\
    \ sum(b[d::d]) % mod\n    ans = [0] * (n + 1)\n    for i in range(1, n + 1):\n\
    \        for d in sieve.divisors(i):\n            ans[d] += sieve.mebius[i //\
    \ d] * c[i]\n    print(*(x % mod for x in ans[1:]))\n\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/gcd_convolution.py
  requiredBy: []
  timestamp: '2026-11-14 00:15:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/gcd_convolution.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/gcd_convolution.py
- /library/library-checker-submitcode/src/math/gcd_convolution.py.html
title: library-checker-submitcode/src/math/gcd_convolution.py
---
