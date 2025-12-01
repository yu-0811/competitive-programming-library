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
  code: "import math\n\ndef range_eratosthenes(L : int, R : int) -> list[bool]:\n\
    \    \"\"\"\n    [L,R] \u306E\u7D20\u6570\u306E\u30EA\u30B9\u30C8[bool]\u3092\u8FD4\
    \u3059\n    O(sqrt(R) log log R + (R-L) log log R)\n    \"\"\"\n    assert L <=\
    \ R\n    sqrtR = int(math.sqrt(R)) + 1\n    # sqrtR \u4EE5\u4E0B\u306E\u7D20\u6570\
    \u30EA\u30B9\u30C8\n    is_prime_base = [True] * (sqrtR + 1)\n    # [L,R] \u306E\
    \u7D20\u6570\u30EA\u30B9\u30C8\n    is_prime = [True] * (R - L + 1)\n    \n  \
    \  for p in range(2, sqrtR + 1):\n        if not is_prime_base[p]:\n         \
    \   continue\n        \n        # \u4EE5\u4E0B p \u306F\u7D20\u6570\n        #\
    \ sqrtR \u4EE5\u4E0B\u306E\u7D20\u6570\u30EA\u30B9\u30C8\u3092\u66F4\u65B0\n \
    \       q = p * 2\n        while q <= sqrtR:\n            is_prime_base[q] = False\n\
    \            q += p\n        \n        # L \u4EE5\u4E0A\u306E\u6700\u5C0F\u306E\
    \ p \u306E\u500D\u6570\n        start = L + ((-L) % p)\n        if start == p:\
    \ start = p * 2\n        \n        # [L,R] \u306E\u7D20\u6570\u30EA\u30B9\u30C8\
    \u3092\u66F4\u65B0\n        q = start\n        while q <= R:\n            is_prime[q\
    \ - L] = False\n            q += p\n            \n    return is_prime"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/math/RangeEratosthenes.py
  requiredBy: []
  timestamp: '2025-12-01 14:37:39+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/math/RangeEratosthenes.py
layout: document
redirect_from:
- /library/algorithm_library/python/math/RangeEratosthenes.py
- /library/algorithm_library/python/math/RangeEratosthenes.py.html
title: algorithm_library/python/math/RangeEratosthenes.py
---
