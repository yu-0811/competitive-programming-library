---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u884C\u30D9\u30AF\u30C8\u30EB v \u3068\u884C\u5217 M \u306E\u7A4D\u3002\
    M \u306F\u9577\u65B9\u5F62\u3067\u3082\u3088\u3044\u3002\ndef vec_mul(v: list[int],\
    \ M: list[list[int]], mod: int):\n    k = len(v)\n    assert k == len(M)\n   \
    \ n = len(M[0]) if M else 0\n    res = [0] * n\n    rem = k % 4\n    for x, row\
    \ in zip(v[:rem], M):\n        res = [(t + x*y) % mod for t, y in zip(res, row)]\n\
    \    # 4 \u884C\u305A\u3064\u307E\u3068\u3081\u3001\u5404\u5217\u306E\u8AAD\u307F\
    \u66F8\u304D\u3068\u5270\u4F59\u306E\u56DE\u6570\u3092\u6E1B\u3089\u3059\u3002\
    \n    for i in range(rem, k, 4):\n        a, b, c, d = v[i:i + 4]\n        if\
    \ a or b or c or d:\n            A, B, C, D = M[i:i + 4]\n            for j in\
    \ range(n):\n                res[j] = (res[j] + a*A[j] + b*B[j]\n            \
    \              + c*C[j] + d*D[j]) % mod\n    return res\n\n\n# \u884C\u5217 A\
    \ \u3068\u884C\u5217 B \u306E\u7A4D\u3092\u8FD4\u3059\ndef mat_mul(A: list[list[int]],\
    \ B: list[list[int]], mod):\n    return [vec_mul(row, B, mod) for row in A]\n\n\
    \n# \u884C\u5217\u7D2F\u4E57 M^K\ndef mat_pow(M: list[list[int]], K: int, mod:\
    \ int):\n    res = []\n    while K > 0:\n        if K & 1:\n            if not\
    \ res:\n                # \u6700\u521D\u306E\u5358\u4F4D\u884C\u5217\u3068\u306E\
    \u7A4D\u306F\u3001\u5270\u4F59\u3092\u53D6\u3063\u305F\u30B3\u30D4\u30FC\u3067\
    \u7F6E\u304D\u63DB\u3048\u308B\n                res = [[x % mod for x in row]\
    \ for row in M]\n            else:\n                res = mat_mul(M, res, mod)\n\
    \        K >>= 1\n        if K:\n            M = mat_mul(M, M, mod)\n\n    if\
    \ not res:\n        res = [[0] * len(M) for _ in range(len(M))]\n        for i\
    \ in range(len(M)):\n            res[i][i] = 1\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/MatrixPower.py
  requiredBy: []
  timestamp: '2026-11-26 00:25:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/MatrixPower.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/MatrixPower.py
- /library/algorithm_library/python/math/MatrixPower.py.html
title: algorithm_library/python/math/MatrixPower.py
---
