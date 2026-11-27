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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import randint\n\n\nclass MultisetHash:\n    # \u6BD4\u8F03\u3057\
    \u305F\u3044\u914D\u5217\u3092\u5F15\u6570\u306B\u6E21\u3059\n    def __init__(self,\
    \ A: list, B: list) -> None:\n        mod = self.mod = (1 << 61) - 1\n       \
    \ h = self.hash = {}\n        self.hashA, self.hashB = [0], [0]\n        for values,\
    \ prefix in ((A, self.hashA), (B, self.hashB)):\n            for x in values:\n\
    \                v = h.get(x)\n                if v is None:\n               \
    \     v = h[x] = randint(1, mod - 1)\n                prefix.append((prefix[-1]\
    \ + v) % mod)\n\n    # 0-index \u306E\u534A\u958B\u533A\u9593 A[al:ar] \u3068\
    \ B[bl:br] \u306E\u591A\u91CD\u96C6\u5408\u3092\u6BD4\u8F03\u3059\u308B\u3002\n\
    \    def isEqual(self, al, ar, bl, br):\n        diff = self.hashA[ar] - self.hashA[al]\
    \ - self.hashB[br] + self.hashB[bl]\n        return diff % self.mod == 0\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/hash/MultisetHash.py
  requiredBy: []
  timestamp: '2026-11-25 22:52:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/hash/MultisetHash.py
layout: document
redirect_from:
- /library/algorithm_library/python/hash/MultisetHash.py
- /library/algorithm_library/python/hash/MultisetHash.py.html
title: algorithm_library/python/hash/MultisetHash.py
---
