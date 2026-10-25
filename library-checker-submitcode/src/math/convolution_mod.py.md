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
    - https://judge.yosupo.jp/problem/convolution_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/convolution_mod\n# include: algorithm_library/python/math/FFT.py\n\
    \n\ndef main():\n    N, M = map(int, readline().split())\n    A = list(map(int,\
    \ readline().split()))\n    B = list(map(int, readline().split()))\n    print(*FFT(mod).convolution(A,\
    \ B))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/convolution_mod.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/convolution_mod.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/convolution_mod.py
- /library/library-checker-submitcode/src/math/convolution_mod.py.html
title: library-checker-submitcode/src/math/convolution_mod.py
---
