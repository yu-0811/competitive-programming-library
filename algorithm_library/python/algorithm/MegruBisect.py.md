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
  path: algorithm_library/python/algorithm/MegruBisect.py
  requiredBy: []
  timestamp: '2024-12-08 13:07:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/algorithm/MegruBisect.py
layout: document
redirect_from:
- /library/algorithm_library/python/algorithm/MegruBisect.py
- /library/algorithm_library/python/algorithm/MegruBisect.py.html
title: algorithm_library/python/algorithm/MegruBisect.py
---
