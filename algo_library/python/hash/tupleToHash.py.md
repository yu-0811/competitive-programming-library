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
  code: "# 10^6 \u304F\u3089\u3044\u307E\u3067\u306F 22 \u3067\u5927\u4E08\u592B\n\
    # 22 \u3067 3 \u3064\u3068\u304B\u306A\u3089\u3044\u3051\u308B\n# \u30BF\u30A4\
    \u30D7\u6570\u3092\u6E1B\u3089\u3059\u305F\u3081\u306B\u30B0\u30ED\u30FC\u30D0\
    \u30EB\u5909\u6570\n\nSIZE = 3\nLEN = 0\nMASK = (1<<22)-1\n\ndef to_hash(x,y,z):\n\
    \  res = 0\n  res |= x<<44\n  res |= y<<22\n  res |= z\n  return res\n\ndef rev(h):\n\
    \  x = (h>>44) & mask\n  y = (h>>22) & mask\n  z = h & mask\n  return x,y,z"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/hash/tupleToHash.py
  requiredBy: []
  timestamp: '2024-09-29 14:24:30+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/hash/tupleToHash.py
layout: document
redirect_from:
- /library/algo_library/python/hash/tupleToHash.py
- /library/algo_library/python/hash/tupleToHash.py.html
title: algo_library/python/hash/tupleToHash.py
---
