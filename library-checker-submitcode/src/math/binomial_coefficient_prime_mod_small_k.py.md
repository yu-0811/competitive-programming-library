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
    - https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    # include: algorithm_library/python/math/modComb.py:Comb:1\n\nCombTable = Comb\n\
    \n# include: algorithm_library/python/math/modComb.py:Comb:2\n\n\ndef main():\n\
    \    T, mod = map(int, readline().split())\n    queries = [tuple(map(int, readline().split()))\
    \ for _ in range(T)]\n    N = max(n for n, _ in queries)\n    limit = min(N, 64)\n\
    \    small = Comb(limit, mod)\n    table = CombTable(N, mod)\n    answers = []\n\
    \    for n, k in queries:\n        # \u5C0F\u3055\u3044 k \u306E\u7248\u306F O(k)\u3002\
    \u5927\u304D\u3044 k \u306E\u516C\u5F0F\u30B1\u30FC\u30B9\u306B\u306F\u968E\u4E57\
    \u8868\u3092\u4F7F\u3046\u3002\n        if not 0 <= k <= n or min(k, n - k) <=\
    \ limit:\n            answer = small.nCk(n, k)\n        else:\n            answer\
    \ = table.H(n - k + 1, k)\n        answers.append(str(answer))\n    print(\"\\\
    n\".join(answers))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/binomial_coefficient_prime_mod_small_k.py
  requiredBy: []
  timestamp: '2026-11-17 17:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/binomial_coefficient_prime_mod_small_k.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/binomial_coefficient_prime_mod_small_k.py
- /library/library-checker-submitcode/src/math/binomial_coefficient_prime_mod_small_k.py.html
title: library-checker-submitcode/src/math/binomial_coefficient_prime_mod_small_k.py
---
