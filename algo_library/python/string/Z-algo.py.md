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
  code: "# Z[i] := S[0:|S|) \u3068 S[i:|S|) \u306E\u6700\u9577\u5171\u901A\u63A5\u982D\
    \u8F9E\u306E\u9577\u3055\ndef z_algo(S):\n  Z = [0]*len(S)\n  Z[0] = len(S)\n\
    \  i,j = 1,0\n  while i<len(S):\n    # \u4E00\u81F4\u3059\u308B\u9650\u308A\u5EF6\
    \u9577\u3059\u308B\n    while (i+j<len(S) and S[j]==S[i+j]): j += 1\n    Z[i]\
    \ = j\n    \n    # \u4E00\u6587\u5B57\u3082\u4E00\u81F4\u3057\u306A\u3044\u306A\
    \u3089\u30B3\u30D4\u30FC\u3067\u304D\u306A\u3044\u306E\u3067\u6B21\u306B\u9032\
    \u3080\n    if j==0: \n      i += 1\n      continue\n    \n    k = 1\n    # k+Z[k]>j\
    \ \u306A\u30891\u56DE\u76EE\u306E\u767B\u5834\u306E\u969B\u306B\u306F\u307F\u51FA\
    \u3057\u3066\u3057\u307E\u3063\u3066\u3044\u308B\n    # k+Z[k]=j \u306A\u3089\
    2\u56DE\u76EE\u306E\u767B\u5834\u306E\u969B\u306B\u306F\u307F\u51FA\u3059\u53EF\
    \u80FD\u6027\u304C\u3042\u308B\n    while (k<j and k+Z[k]<j):\n      Z[i+k] =\
    \ Z[k]\n      k += 1\n    # \u307E\u3060\u672A\u78BA\u5B9A\u306A\u3068\u3053\u308D\
    \u307E\u3067 i \u3092\u9032\u3081\u308B\n    i += k\n    # j \u3092 i \u306B\u5408\
    \u308F\u305B\u308B\n    j -= k\n    \n  return Z"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/string/Z-algo.py
  requiredBy: []
  timestamp: '2024-11-26 23:23:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/string/Z-algo.py
layout: document
redirect_from:
- /library/algo_library/python/string/Z-algo.py
- /library/algo_library/python/string/Z-algo.py.html
title: algo_library/python/string/Z-algo.py
---
