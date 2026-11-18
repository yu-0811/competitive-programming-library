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
    \n\ndef main():\n    N, A, B = map(int, readline().split())\n    # \u6700\u5C0F\
    \u7D20\u56E0\u6570\u8868\u306F N \u4EE5\u4E0B\u306E\u6574\u6570\u3092\u3059\u3079\
    \u3066\u6301\u3064\u3002\u5927\u304D\u3044\u30B1\u30FC\u30B9\u306F\u5947\u6570\
    \u3060\u3051\u306E\u7BE9\u3092\u4F7F\u3046\u3002\n    if N <= 1_000_000:\n   \
    \     factors = init_factorization(N)\n        primes = [i for i in range(2, N\
    \ + 1) if factors[i] == i]\n    else:\n        primes = res_primeList(N)\n   \
    \ selected = primes[B::A]\n    print(len(primes), len(selected))\n    print(*selected)\n\
    \n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/enumerate_primes_spf.py
  requiredBy: []
  timestamp: '2026-11-17 18:24:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/enumerate_primes_spf.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/enumerate_primes_spf.py
- /library/library-checker-submitcode/src/math/enumerate_primes_spf.py.html
title: library-checker-submitcode/src/math/enumerate_primes_spf.py
---
