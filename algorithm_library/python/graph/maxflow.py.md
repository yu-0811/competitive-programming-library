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
  code: "class maxflow_edge:\n  def __init__(self, to, cap, rev_idx):\n    self.to\
    \ = to # \u884C\u304D\u5148\n    self.cap = cap # \u5BB9\u91CF\n    self.rev_idx\
    \ = rev_idx # \u9006\u5411\u304D\u306E\u8FBA\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\
    \u30B9\n\nclass maximum_flow():\n  def __init__(self,N):\n    self.G = [[] for\
    \ _ in range(N+1)]\n    self.N = N\n    import pypyjit\n    pypyjit.set_param('max_unroll_recursion=-1')\n\
    \    sys.setrecursionlimit(10**7)\n  \n  def add_edge(self,a,b,c):\n    self.G[a].append(maxflow_edge(b,c,len(self.G[b])))\n\
    \    self.G[b].append(maxflow_edge(a,0,len(self.G[a])-1)) # \u9006\u5411\u304D\
    \n  \n  def dfs(self,v,goal,f):\n    if v==goal: return f\n    self.vis[v] = True\n\
    \    for edge in self.G[v]:\n      if edge.cap > 0 and self.vis[edge.to] == False:\n\
    \        flow = self.dfs(edge.to, goal, min(f, edge.cap))\n        # \u30D5\u30ED\
    \u30FC\u3092\u6D41\u305B\u308B\u306A\u3089\u3001\u6B8B\u4F59\u30B0\u30E9\u30D5\
    \u306E\u5BB9\u91CF\u3092 flow \u5897\u6E1B\u3055\u305B\u308B\n        if flow\
    \ >= 1:\n          edge.cap -= flow\n          self.G[edge.to][edge.rev_idx].cap\
    \ += flow\n          return flow\n    # \u6D41\u305B\u306A\u3044\u306A\u3089\n\
    \    return 0\n\n  def maxflow(self,start,goal):\n    total_flow = 0\n    inf\
    \ = pow(10,18)\n    while True:\n      self.vis = [False]*(self.N+1)\n      res\
    \ = self.dfs(start, goal, inf)\n      if res > 0: total_flow += res\n      else:\
    \ break\n    return total_flow"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/maxflow.py
  requiredBy: []
  timestamp: '2025-03-04 22:47:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/maxflow.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/maxflow.py
- /library/algorithm_library/python/graph/maxflow.py.html
title: algorithm_library/python/graph/maxflow.py
---
