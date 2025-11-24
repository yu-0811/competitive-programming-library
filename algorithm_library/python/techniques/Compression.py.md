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
  code: "# \u5EA7\u6A19\u5727\u7E2E\n# ex. A=[2,9,9,7,9,2,4]\_-> \u8FD4\u308A\u5024\
    =[1,4,4,3,4,1,2]\ndef compression(A):\n  B = [0]*len(A)\n  Adic = {x:i for i,x\
    \ in enumerate(sorted(list(set(A))))}\n  for i in range(len(A)):\n    B[i] = Adic[A[i]]\n\
    \  return B"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Compression.py
  requiredBy: []
  timestamp: '2025-11-24 14:08:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Compression.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Compression.py
- /library/algorithm_library/python/techniques/Compression.py.html
title: algorithm_library/python/techniques/Compression.py
---
