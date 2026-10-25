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
    - https://judge.yosupo.jp/problem/matrix_product
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/matrix_product\n# include: algorithm_library/python/math/MatrixPower.py\n\
    \n\ndef main():\n    N, M, K = map(int, readline().split())\n    A = [list(map(int,\
    \ readline().split())) for _ in range(N)]\n    B = [list(map(int, readline().split()))\
    \ for _ in range(M)]\n    result = mat_mul(A, B, mod)\n    sys.stdout.write(\"\
    \\n\".join(\" \".join(map(str, row)) for row in result) + \"\\n\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/matrix_product.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/matrix_product.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/matrix_product.py
- /library/library-checker-submitcode/src/math/matrix_product.py.html
title: library-checker-submitcode/src/math/matrix_product.py
---
