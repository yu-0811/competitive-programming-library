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
  code: "def megru_bisect(ng,ok):\n  def judge(mid):\n  \n  while abs(ok-ng)>1:\n\
    \    mid = (ok+ng)//2\n    if judge(mid): # \u6761\u4EF6\u3092\u6E80\u305F\u3059\
    \u306A\u3089\n      ok = mid\n    else:\n      ng = mid\n\n  return ng,ok"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/megruBisect.py
  requiredBy: []
  timestamp: '2024-10-24 08:22:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/megruBisect.py
layout: document
redirect_from:
- /library/algo_library/python/megruBisect.py
- /library/algo_library/python/megruBisect.py.html
title: algo_library/python/megruBisect.py
---
