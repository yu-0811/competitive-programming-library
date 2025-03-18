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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5\
    , \u4E00\u6B21\u5408\u540C\u5F0F\n\n# ax + by = gcd(a,b) \u3092\u6E80\u305F\u3059\
    \ (x,y) \u3092\u6C42\u3081\u308B\n# \u8FD4\u308A\u5024\uFF1Agcd(a,b), x, y\ndef\
    \ extGCD(a,b) -> tuple[int,int,int]:\n    if b == 0:\n        return a, 1, 0\n\
    \    g,s,t = extGCD(b, a%b)\n    # g = b * s + (a%b) * t\n    #   = b * s + (a\
    \ - a//b * b) * t\n    #   = a * t + b * s + (-a//b * b * t)\n    #   = a * t\
    \ + b * (s - a//b * t)\n    x = t\n    y = s - a//b * t\n    return g, x, y\n\n\
    # ax \u2261 1 (mod m) \u3092\u6E80\u305F\u3059 x (a^-1) \u3092\u6C42\u3081\u308B\
    \ndef modinv(a,m) -> int:\n    g,x,y = extGCD(a,m)\n    assert g == 1, \"a \u3068\
    \ m \u304C\u4E92\u3044\u306B\u7D20\u3067\u306A\u3044\"\n    return x % m\n\n#\
    \ ax \u2261 b (mod m) \u3092\u6E80\u305F\u3059 x \u3092\u6C42\u3081\u308B\ndef\
    \ modlin(a,b,m) -> int:\n    g,x,y = extGCD(a,m)\n    if b % g != 0:\n       \
    \ return None # \u89E3\u306A\u3057\n    a //= g; b //= g; m //= g\n    inv_a =\
    \ modinv(a,m)\n    return (inv_a * b) % m\n\n# \u4E2D\u56FD\u5270\u4F59\u5B9A\u7406\
    \n# x \u2261 B[i] (mod M[i]) \u3092\u6E80\u305F\u3059 x \u2261 r (mod lcm(M))\
    \ \u3092\u6C42\u3081\u308B\n# \u8FD4\u308A\u5024\uFF1A\u89E3 r, lcm(M)\ndef chineseRem(B\
    \ : list[int], M : list[int]) -> tuple[int,int]:\n    assert len(B) == len(M)\n\
    \    n = len(B)\n    r = 0; m = 1\n    for i in range(n):\n        d, p, q = extGCD(m,\
    \ M[i])\n        if (B[i] - r) % d != 0:\n            return None, None # \u89E3\
    \u306A\u3057\n        tmp = (B[i] - r) // d * p % (M[i] // d)\n        r += m\
    \ * tmp\n        m *= M[i] // d\n    return r % m, m"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/extGCD.py
  requiredBy: []
  timestamp: '2025-03-18 19:06:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/extGCD.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/extGCD.py
- /library/algorithm_library/python/math/extGCD.py.html
title: algorithm_library/python/math/extGCD.py
---
