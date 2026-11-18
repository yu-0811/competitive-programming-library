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
    \n\ndef main():\n    N, A, B = map(int, readline().split())\n    # bool \u306E\
    \u8868\u3092\u8FD4\u3059\u7248\u306F\u5C0F\u3055\u3044\u30B1\u30FC\u30B9\u3001\
    \u5947\u6570\u3060\u3051\u306E\u7BE9\u306F\u5927\u304D\u3044\u30B1\u30FC\u30B9\
    \u306B\u4F7F\u3046\u3002\n    if N <= 1_000_000:\n        primes, isprime = eratosthenes(N)\n\
    \        count = sum(isprime)\n    else:\n        primes = res_primeList(N)\n\
    \        count = len(primes)\n    selected = primes[B::A]\n    print(count, len(selected))\n\
    \    print(*selected)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/enumerate_primes_eratosthenes.py
  requiredBy: []
  timestamp: '2026-11-17 18:24:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/enumerate_primes_eratosthenes.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/enumerate_primes_eratosthenes.py
- /library/library-checker-submitcode/src/math/enumerate_primes_eratosthenes.py.html
title: library-checker-submitcode/src/math/enumerate_primes_eratosthenes.py
---
