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
  code: "from collections import deque\n\nclass LCA:\n    def __init__(self, N, G,\
    \ root):  \n        # \u6839\u304B\u3089\u306E\u8DDD\u96E2\u3068\u89AA\u3092\u6C42\
    \u3081\u308B\n        self.N = N\n        self.bit = N.bit_length() + 2\n    \
    \    self.parent = [[-1]*(N+1) for _ in range(self.bit)]\n        self.parent[0][root]\
    \ = -1\n        self.depth = [-1]*(N+1) # \u6839\u304B\u3089\u306E\u8DDD\u96E2\
    \n        self.depth[root] = 0\n        que = deque()\n        que.append(root)\n\
    \        while que:\n            v = que.popleft()\n            for v2 in G[v]:\n\
    \                if self.depth[v2]==-1:\n                    self.depth[v2] =\
    \ self.depth[v]+1\n                    self.parent[0][v2] = v\n              \
    \      que.append(v2)\n\n        # \u30C0\u30D6\u30EA\u30F3\u30B0\u3059\u308B\n\
    \        for i in range(1,self.bit):\n            for j in range(N+1):\n     \
    \           if self.parent[i-1][j]!=-1: \n                    self.parent[i][j]\
    \ = self.parent[i-1][self.parent[i-1][j]]\n\n    # u \u3068 v \u306E LCA \u3092\
    \u8FD4\u3059\n    # O(log N)\n    def lca(self,u,v):\n        # \u6DF1\u3055\u3092\
    \u540C\u3058\u306B\u3059\u308B\n        if self.depth[u]<self.depth[v]: u,v =\
    \ v,u\n        for k in range(self.bit):\n            if ((self.depth[u]-self.depth[v])\
    \ >> k) & 1:\n                u = self.parent[k][u]\n        # \u4E8C\u5206\u63A2\
    \u7D22\u3059\u308B\n        if u==v: return u\n        for k in reversed(range(self.bit)):\n\
    \            if self.parent[k][u] != self.parent[k][v]:\n                u = self.parent[k][u]\n\
    \                v = self.parent[k][v]\n        return self.parent[0][u]\n\n \
    \   # u \u3068 v \u306E\u8DDD\u96E2\u3092\u8FD4\u3059\n    def get_distance(self,u,v):\n\
    \        return self.depth[u] + self.depth[v] - 2*self.depth[self.lca(u,v)]\n\
    \    \n    # u-v \u306E\u30D1\u30B9\u4E0A\u306B a \u304C\u5B58\u5728\u3059\u308B\
    \u304B\n    def is_on_path(self,u,v,a):\n        return self.get_distance(u,a)\
    \ + self.get_distance(v,u) == self.get_distance(u,v)"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/LCA.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/LCA.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/LCA.py
- /library/algorithm_library/python/graph/LCA.py.html
title: algorithm_library/python/graph/LCA.py
---
