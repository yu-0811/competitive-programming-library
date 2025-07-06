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
  code: "def mos_algorithm(data, queries):\n    \"\"\"\n    data : list of int : \u5143\
    \u306E\u914D\u5217\n    queries : list of tuple : \u30AF\u30A8\u30EA\u306E\u30EA\
    \u30B9\u30C8\n    \u30AF\u30A8\u30EA\u306F 0-indexed \u3067\u534A\u958B\u533A\u9593\
    [l,r)\n    \"\"\"\n    from math import sqrt, ceil\n    n = len(data)\n    q =\
    \ len(queries)\n    B = ceil(sqrt(3)*n / (sqrt(2)*sqrt(q))) # bukect\u306E\u30B5\
    \u30A4\u30BA(nyaan\u3055\u3093\u306E\u8A18\u4E8B\u3088\u308A)\n    L,R = 0,0\n\
    \    # query\u306E\u9806\u756A\u3092\u683C\u7D0D\u3059\u308B\u7528\n    order\
    \ = [-1] * q\n\n    ########################################\n    # \u72B6\u614B\
    \u3092\u521D\u671F\u5316\u3059\u308B\u51E6\u7406\u3092\u66F8\u304F\n\n    ########################################\n\
    \n    def _add(i, ans):\n        # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u542B\
    \u3081\u3066\u8003\u3048\u308B\u3068\u304D\u3078states\u3092\u66F4\u65B0\n   \
    \     ########################################\n\n        return ans\n       \
    \ ########################################\n\n    def _delete(i, ans):\n     \
    \   # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u9664\u3044\u3066\u8003\u3048\u308B\
    \u3068\u304D\u3078states\u3092\u66F4\u65B0\n        ########################################\n\
    \n        return ans\n        ########################################\n\n   \
    \ # \u30AF\u30A8\u30EA\u306E\u89E3\u7B54\u9806\n    # (ceil(l/B), r*-1^{ceil(l/B)})\
    \ \u306E\u6607\u9806\u306B\u3059\u308B\u306E\u304C\u6700\u901F\u307D\u3044\n \
    \   for idx, (l,r) in enumerate(queries):\n        order[idx] = ((l//B)<<40)+((r\
    \ if (l//B)&1 else -r)<<20)+idx\n    order.sort()\n\n    mask = (1<<20)-1\n  \
    \  ret = [-1] * q\n    for lri in order:  # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\
    \u3066\u3044\u304F\n        i = lri & mask\n        l,r = queries[i]\n       \
    \ \n        # \u30AF\u30A8\u30EA[l,r)\u306B\u5BFE\u3057\u3066states\u3092\u66F4\
    \u65B0\u3059\u308B\n        while R < r:  # r\u307E\u3067\u4F38\u9577\n      \
    \      ans = _add(R,ans)\n            R += 1\n        while R > r:  # r\u307E\u3067\
    \u77ED\u7E2E\n            R -= 1\n            ans = _delete(R,ans)\n         \
    \   \n        while L < l:  # l\u307E\u3067\u77ED\u7E2E\n            ans = _delete(L,ans)\n\
    \            L += 1\n        while L > l:  # l\u307E\u3067\u4F38\u9577\n     \
    \       L -= 1\n            ans = _add(L,ans)\n        \n        ########################################\n\
    \        # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\u308B\u4F5C\u696D\u3092\u3053\u3053\
    \u3067\u66F8\u304F\n        # ret[i] \u306B i \u756A\u76EE\u306E\u30AF\u30A8\u30EA\
    \u306E\u7B54\u3048\u3092\u683C\u7D0D\u3059\u308B\n        ret[i] = ans\n     \
    \   ########################################\n        \n    return ret"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/Mos_algorithm.py
  requiredBy: []
  timestamp: '2025-07-06 10:57:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/Mos_algorithm.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/Mos_algorithm.py
- /library/algorithm_library/python/data-structure/Mos_algorithm.py.html
title: algorithm_library/python/data-structure/Mos_algorithm.py
---
