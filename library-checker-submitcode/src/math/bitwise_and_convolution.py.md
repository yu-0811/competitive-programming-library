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
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/bitwise_and_convolution\n# include:\
    \ algorithm_library/python/math/mobius.py\n\n\ndef main():\n    N = int(readline())\n\
    \    arrays = [list(map(int, readline().split())) for _ in range(2)]\n    for\
    \ data in arrays:\n        for i in range(N):\n            bit = 1 << i\n    \
    \        for start in range(0, 1 << N, 2 * bit):\n                for mask in\
    \ range(start, start + bit):\n                    data[mask] += data[mask + bit]\n\
    \    result = [(a % mod) * (b % mod) % mod for a, b in zip(*arrays)]\n    mobius(result)\n\
    \    print(*(x % mod for x in result))\n\n\nif __name__ == \"__main__\":\n   \
    \ main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/bitwise_and_convolution.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/bitwise_and_convolution.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/bitwise_and_convolution.py
- /library/library-checker-submitcode/src/math/bitwise_and_convolution.py.html
title: library-checker-submitcode/src/math/bitwise_and_convolution.py
---
