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
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/pow_of_matrix\n# include: algorithm_library/python/math/MatrixPower.py\n\
    \n\ndef main():\n    N, K = map(int, readline().split())\n    A = [list(map(int,\
    \ readline().split())) for _ in range(N)]\n    result = [[int(i == j) for j in\
    \ range(N)] for i in range(N)]\n    while K:\n        if K & 1:\n            result\
    \ = [vec_mul(row, A, mod) for row in result]\n        K >>= 1\n        if K:\n\
    \            A = [vec_mul(row, A, mod) for row in A]\n    sys.stdout.write(\"\\\
    n\".join(\" \".join(map(str, row)) for row in result) + \"\\n\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/pow_of_matrix_vec.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/pow_of_matrix_vec.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/pow_of_matrix_vec.py
- /library/library-checker-submitcode/src/math/pow_of_matrix_vec.py.html
title: library-checker-submitcode/src/math/pow_of_matrix_vec.py
---
