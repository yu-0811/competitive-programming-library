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
    - https://judge.yosupo.jp/problem/enumerate_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/enumerate_primes\n# include: algorithm_library/python/math/factorization.py\n\
    \n\ndef main():\n    N, A, B = map(int, readline().split())\n    primes = res_primeList(N)\n\
    \    selected = primes[B::A]\n    print(len(primes), len(selected))\n    print(*selected)\n\
    \n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/enumerate_primes.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/enumerate_primes.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/enumerate_primes.py
- /library/library-checker-submitcode/src/math/enumerate_primes.py.html
title: library-checker-submitcode/src/math/enumerate_primes.py
---
