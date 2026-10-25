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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def run_length_compression(S: str):\n    res = []\n    tmp = S[0]\n    it\
    \ = iter(S)\n    next(it)\n    cnt = 1\n    for s in it:\n        if s == tmp:\n\
    \            cnt += 1\n        else:\n            res.append((tmp, cnt))\n   \
    \         tmp = s\n            cnt = 1\n    res.append((tmp, cnt))\n    return\
    \ res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/RunLengthCompression.py
  requiredBy: []
  timestamp: '2026-10-20 11:41:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/RunLengthCompression.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/RunLengthCompression.py
- /library/algorithm_library/python/techniques/RunLengthCompression.py.html
title: algorithm_library/python/techniques/RunLengthCompression.py
---
