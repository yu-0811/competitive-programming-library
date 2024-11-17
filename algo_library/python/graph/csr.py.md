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
  code: "# \u7121\u5411\u30B0\u30E9\u30D5\u306E\u5834\u5408\u306F graphEdges \u306B\
    \u3044\u3064\u3082\u901A\u308A u -> v \u3068 v -> u \u306E\u4E21\u65B9\u3092\u52A0\
    \u3048\u308B\n# \u91CD\u307F\u4ED8\u304D\u30B0\u30E9\u30D5\u306E\u5834\u5408\u306F\
    \ endList \u306B\u683C\u7D0D\u3059\u308B\u5024\u3092 (\u7D42\u70B9, \u91CD\u307F\
    ) \u306B\u3059\u308C\u3070\u3088\u3044\n\n# \u6709\u5411\u30B0\u30E9\u30D5\u306E\
    \u3068\u304D\n\n# N := \u9802\u70B9\u6570\n# graphEdges[i] := [\u8FBA i \u306E\
    \u59CB\u70B9, \u8FBA i \u306E\u7D42\u70B9]\ndef csr(N: int, graphEdges: list[list[int]]):\n\
    \  start = [0]*(N+1)\n  # endList := \u8FBA\u3092\u59CB\u70B9\u306E\u6607\u9806\
    \u306B\u30BD\u30FC\u30C8\u3057\u305F\u6642\u306E\u7D42\u70B9\u306E\u30EA\u30B9\
    \u30C8\n  endList = [0]*len(graphEdges)\n\n  # start[i+1] := \u9802\u70B9 i \u3092\
    \u59CB\u70B9\u3068\u3059\u308B\u8FBA\u306E\u6570 \u3068\u306A\u308B\u3088\u3046\
    \u306B\u69CB\u7BC9\n  for u,v in graphEdges: # u -> v \u3078\u306E\u8FBA\n   \
    \ start[u+1] += 1\n  # start[i] := \u59CB\u70B9\u306E\u9802\u70B9\u756A\u53F7\u304C\
    \ i \u672A\u6E80\u3067\u3042\u308B\u8FBA\u306E\u6570 \u306B\u306A\u308B\u3088\u3046\
    \u306B\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\n  # \u3053\u306E\u3068\u304D\u3001\
    start[i] = endList \u3067\u9802\u70B9 i \u304C\u59CB\u70B9\u3068\u306A\u308B\u6700\
    \u5C0F\u306E index (0-index)\n  for i in range(1,N+1):\n    start[i] += start[i-1]\n\
    \n  # pointer[i] := \u59CB\u70B9\u3092 i \u3068\u3059\u308B\u8FBA\u306E endList\
    \ \u3078\u306E\u633F\u5165\u4F4D\u7F6E\n  pointer = start[:]\n  for u,v in graphEdges:\n\
    \    endList[pointer[u]] = v\n    pointer[u] += 1\n    \n  return start, endList\n\
    \nfrom itertools import accumulate\nclass Graph:\n  def __init__(self,n,m):\n\
    \    self.N = n+1\n    self.M = m\n    self.start = [0]*(self.N+1)\n    self.buf\
    \ = list()\n    self.endList = [None] * m \n    \n  def add_edge(self,u,v,cost=None):\n\
    \    self.buf.append((u,v,cost))\n    self.start[u] += 1\n    if len(self.buf)==self.M:\
    \ self.build()\n  \n  def build(self):\n    self.start = list(accumulate(self.start))\n\
    \    for u,v,c in self.buf:\n      self.start[u] -= 1\n      if c==None: self.endList[self.start[u]]\
    \ = v\n      else: self.endList[self.start[u]] = (v,c)\n  \n  def get_edges(self,u):\n\
    \    return self.endList[self.start[u]:self.start[u+1]]"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/graph/csr.py
  requiredBy: []
  timestamp: '2024-11-17 11:08:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/graph/csr.py
layout: document
redirect_from:
- /library/algo_library/python/graph/csr.py
- /library/algo_library/python/graph/csr.py.html
title: algo_library/python/graph/csr.py
---
