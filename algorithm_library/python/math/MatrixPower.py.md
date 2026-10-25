---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: tests/math/test_matrix_power.py
    title: tests/math/test_matrix_power.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def vec_mul(v: list[int], M: list[list[int]], mod: int):\n    n = len(v)\n\
    \    assert n == len(M)\n    res = [0] * n\n    for i in range(n):\n        x,\
    \ row = v[i], M[i]\n        for j in range(n):\n            res[j] = (res[j] +\
    \ x * row[j]) % mod\n    return res\n\n\n# \u884C\u5217 A \u3068 \u884C\u5217\
    \ B \u306E\u7A4D\u3092\u8FD4\u3059\ndef mat_mul(A: list[list[int]], B: list[list[int]],\
    \ mod):\n    assert len(A[0]) == len(B)\n    K = len(B)\n    end = K & -8\n  \
    \  BT = list(zip(*B))\n    res = []\n    for row in A:\n        out = []\n   \
    \     for col in BT:\n            total = 0\n            # \u591A\u500D\u9577\u6574\
    \u6570\u306E\u6210\u9577\u3092\u6291\u3048\u308B\u305F\u3081\u30018\u9805\u3054\
    \u3068\u306B\u5270\u4F59\u3092\u53D6\u308B\n            for k in range(0, end,\
    \ 8):\n                total = (\n                    total\n                \
    \    + row[k] * col[k]\n                    + row[k + 1] * col[k + 1]\n      \
    \              + row[k + 2] * col[k + 2]\n                    + row[k + 3] * col[k\
    \ + 3]\n                    + row[k + 4] * col[k + 4]\n                    + row[k\
    \ + 5] * col[k + 5]\n                    + row[k + 6] * col[k + 6]\n         \
    \           + row[k + 7] * col[k + 7]\n                ) % mod\n            for\
    \ k in range(end, K):\n                total += row[k] * col[k]\n            out.append(total\
    \ % mod)\n        res.append(out)\n    return res\n\n\n# \u884C\u5217\u7D2F\u4E57\
    \ M^K\ndef mat_pow(M: list[list[int]], K: int, mod: int):\n    res = []\n    while\
    \ K > 0:\n        if K & 1:\n            if not res:\n                # \u6700\
    \u521D\u306E\u5358\u4F4D\u884C\u5217\u3068\u306E\u7A4D\u306F\u3001\u5270\u4F59\
    \u3092\u53D6\u3063\u305F\u30B3\u30D4\u30FC\u3067\u7F6E\u304D\u63DB\u3048\u308B\
    \n                res = [[x % mod for x in row] for row in M]\n            else:\n\
    \                res = mat_mul(M, res, mod)\n        K >>= 1\n        if K:\n\
    \            M = mat_mul(M, M, mod)\n\n    if not res:\n        res = [[0] * len(M)\
    \ for _ in range(len(M))]\n        for i in range(len(M)):\n            res[i][i]\
    \ = 1\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/MatrixPower.py
  requiredBy:
  - tests/math/test_matrix_power.py
  timestamp: '2026-10-25 10:02:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/MatrixPower.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/MatrixPower.py
- /library/algorithm_library/python/math/MatrixPower.py.html
title: algorithm_library/python/math/MatrixPower.py
---
