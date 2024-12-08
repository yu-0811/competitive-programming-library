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
  code: "from random import randint\nclass ZobristHash:\n  # \u6BD4\u8F03\u3057\u305F\
    \u3044\u914D\u5217\u3092\u5F15\u6570\u306B\u6E21\u3059\n  def __init__(self,A:\
    \ list, B: list) -> None:\n    MAX = (1<<61)-1\n    self.hash = dict()\n    for\
    \ a in A: self.hash[a] = randint(1,MAX)\n    for b in B: self.hash[b] = randint(1,MAX)\n\
    \    # \u30CF\u30C3\u30B7\u30E5\u3092\u53D6\u308B\n    self.hashA,self.hashB =\
    \ [0],[0]\n    setA,setB = set(),set()\n    for a in A: \n      if a in setA:\n\
    \        self.hashA.append(self.hashA[-1])\n      else:\n        self.hashA.append(self.hashA[-1]\
    \ ^ self.hash[a])\n        setA.add(a)\n    for b in B: \n      if b in setB:\n\
    \        self.hashB.append(self.hashB[-1])\n      else:\n        self.hashB.append(self.hashB[-1]\
    \ ^ self.hash[b])\n        setB.add(b)\n    \n  # 1-index(A_1, A_2, ...)\n  #\
    \ (A_al,A_{al+1},...,A_ar) == (B_al,B_{al+1},...,B_ar) \u3092\u8FD4\u3059\n  def\
    \ isEqual(self,al,ar,bl,br):\n    return (self.hashA[ar] - self.hashA[al-1]) ==\
    \ (self.hashB[br] - self.hashB[bl-1])"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/hash/ZobristHash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/hash/ZobristHash.py
layout: document
redirect_from:
- /library/algorithm_library/python/hash/ZobristHash.py
- /library/algorithm_library/python/hash/ZobristHash.py.html
title: algorithm_library/python/hash/ZobristHash.py
---
