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
    \u30B9\u30C8\n    \"\"\"\n    from math import sqrt, ceil\n    n = len(data)\n\
    \    b = ceil(sqrt(n))  # bukect\u306E\u30B5\u30A4\u30BA\u53CA\u3073\u500B\u6570\
    \n    # [l,r)\u306E\u534A\u958B\u533A\u9593\u3067\u8003\u3048\u308B\n    L = 0\n\
    \    R = 0\n    # query\u3092\u683C\u7D0D\u3059\u308B\u7528\n    bucket = [list()\
    \ for _ in range((b + 1))]\n\n    ########################################\n \
    \   # \u72B6\u614B\u3092\u521D\u671F\u5316\u3059\u308B\u51E6\u7406\u3092\u66F8\
    \u304F\n    ans = 0\n    ########################################\n\n    def _add(i,\
    \ ans):\n        # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u542B\u3081\u3066\u8003\
    \u3048\u308B\u3068\u304D\u3078states\u3092\u66F4\u65B0\n        ########################################\n\
    \n        return ans\n        ########################################\n\n   \
    \ def _delete(i, ans):\n        # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u9664\u3044\
    \u3066\u8003\u3048\u308B\u3068\u304D\u3078states\u3092\u66F4\u65B0\n        ########################################\n\
    \n        return ans\n        ########################################\n\n   \
    \ upper = len(queries)\n    upper_upper = upper * (n + 1)\n\n    for idx, (l,\
    \ r) in enumerate(queries):  # query\u3092bucket\u306B\u683C\u7D0D\n        bucket[l\
    \ // b].append(idx + l*upper + r*upper_upper)\n\n    for i in range(len(bucket)):\n\
    \        if i%2==0: bucket[i].sort()\n        else: bucket[i].sort(reverse=True)\n\
    \n    ret = [-1] * len(queries)\n    for b in bucket:\n        for lri in b: \
    \ # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\u3066\u3044\u304F\n            i = lri\
    \ % upper\n            r = lri // upper_upper\n            l = (lri % upper_upper)\
    \ // upper\n            \n            # \u30AF\u30A8\u30EA[l,r)\u306B\u5BFE\u3057\
    \u3066states\u3092\u66F4\u65B0\u3059\u308B\n            while R < r:  # r\u307E\
    \u3067\u4F38\u9577\n                ans = _add(R,ans)\n                R += 1\n\
    \            while R > r:  # r\u307E\u3067\u77ED\u7E2E\n                R -= 1\n\
    \                ans = _delete(R,ans)\n                \n            while L <\
    \ l:  # l\u307E\u3067\u77ED\u7E2E\n                ans = _delete(L,ans)\n    \
    \            L += 1\n            while L > l:  # l\u307E\u3067\u4F38\u9577\n \
    \               L -= 1\n                ans = _add(L,ans)\n            \n    \
    \        ########################################\n            # \u30AF\u30A8\u30EA\
    \u306B\u7B54\u3048\u308B\u4F5C\u696D\u3092\u3053\u3053\u3067\u66F8\u304F\n   \
    \         # ret[i] \u306B i \u756A\u76EE\u306E\u30AF\u30A8\u30EA\u306E\u7B54\u3048\
    \u3092\u683C\u7D0D\u3059\u308B\n            ret[i] = ans\n            ########################################\n\
    \    return ret"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/Mos_algorithm.py
  requiredBy: []
  timestamp: '2024-12-08 13:03:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/Mos_algorithm.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/Mos_algorithm.py
- /library/algorithm_library/python/data-structure/Mos_algorithm.py.html
title: algorithm_library/python/data-structure/Mos_algorithm.py
---
