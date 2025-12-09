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
  code: "def ternary_search_float(f, left, right, eps=1e-9, maximize=False):\n   \
    \ \"\"\"\n    f \u304C [left, right] \u4E0A\u3067 \u51F8 or \u51F9 \u3060\u3068\
    \u4EEE\u5B9A\u3057\u3066\u3001\n    \u305D\u306E\u6700\u5C0F\u5024\uFF08\u307E\
    \u305F\u306F\u6700\u5927\u5024\uFF09\u3092 3 \u5206\u63A2\u7D22\u3067\u6C42\u3081\
    \u308B\u3002\n    maximize=False: \u6700\u5C0F\u5024\u3092\u63A2\u3059\n    maximize=True\
    \ : \u6700\u5927\u5024\u3092\u63A2\u3059\n    \u8FD4\u308A\u5024: (\u6700\u9069\
    \u89E3\u306E\u7BC4\u56F2\u306E\u5DE6\u7AEF, \u53F3\u7AEF, f(\u4E2D\u70B9))\n \
    \   \"\"\"\n    while right - left > eps:\n        m1 = (2 * left + right) / 3\n\
    \        m2 = (left + 2 * right) / 3\n        f1 = f(m1)\n        f2 = f(m2)\n\
    \n        if not maximize:\n            if f1 > f2:\n                left = m1\n\
    \            else:\n                right = m2\n        else:\n            if\
    \ f1 < f2:\n                left = m1\n            else:\n                right\
    \ = m2\n\n        if right - left < eps:\n            break\n\n    x = (left +\
    \ right) / 2\n    return left, right, f(x)\n\n\ndef ternary_search_int(f, left,\
    \ right, eps, maximize=False):\n    \"\"\"\n    f: int -> \u5024 \u3092\u8FD4\u3059\
    \u4E00\u5CF0\u6027\u95A2\u6570\uFF08\u5C71 or \u8C37\uFF09\n    [left, right]\
    \ \u306E\u6574\u6570\u7BC4\u56F2\u3067\u3001f \u306E\u6700\u5927\u5024 or \u6700\
    \u5C0F\u5024\u3092\u63A2\u3059\u3002\n    maximize=True  \u306A\u3089\u6700\u5927\
    \u5024\u3092\u63A2\u3059\n    maximize=False \u306A\u3089\u6700\u5C0F\u5024\u3092\
    \u63A2\u3059\n\n    \u623B\u308A\u5024: (arg_opt, f(arg_opt))\n    \"\"\"\n\n\
    \    while right - left > eps:\n        m1 = (2 * left + right) // 3\n       \
    \ m2 = (left + 2 * right) // 3\n\n        f1 = f(m1)\n        f2 = f(m2)\n\n \
    \       if not maximize:\n            if f1 > f2:\n                left = m1\n\
    \            else:\n                right = m2\n        else:\n            if\
    \ f1 < f2:\n                left = m1\n            else:\n                right\
    \ = m2\n\n    # \u6B8B\u3063\u305F [left, right] \u3092\u611A\u76F4\u306B\u898B\
    \u308B\n    best_x = left\n    best_val = f(left)\n    for x in range(left + 1,\
    \ right + 1):\n        val = f(x)\n        if (maximize and val > best_val) or\
    \ (not maximize and val < best_val):\n            best_val = val\n           \
    \ best_x = x\n\n    return best_x, best_val\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/TernarySearch.py
  requiredBy: []
  timestamp: '2025-12-09 13:42:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/TernarySearch.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/TernarySearch.py
- /library/algorithm_library/python/techniques/TernarySearch.py.html
title: algorithm_library/python/techniques/TernarySearch.py
---
