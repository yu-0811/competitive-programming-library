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
  code: "# \u5168\u65B9\u4F4D\u6728DP\nclass rerooting:\n  def __init__(self, n:int,\
    \ edges:list[tuple[int,int]], identity:int, merge:callable, calc_node_value:callable,\
    \ calc_ans:callable):\n    self.n = n\n    self.identity = identity\n    self.merge\
    \ = merge\n    self.calc_node_value = calc_node_value\n    self.calc_ans = calc_ans\n\
    \    # adjacents[i] = i \u3068\u96A3\u63A5\u3059\u308B\u9802\u70B9\u306E\u30EA\
    \u30B9\u30C8\n    self.adjacents = [[] for _ in range(n+1)]\n    # indexForAdjacents[i][j]\
    \ = adjacents[i][j](i\u306Ej\u756A\u76EE\u306E\u96A3\u63A5\u9802\u70B9)\u306B\u3068\
    \u3063\u3066\u3001i\u304C\u4F55\u756A\u76EE\u306E\u96A3\u63A5\u9802\u70B9\u304B\
    \n    # adjacents[adjacents[i][j]][indexForAdjacents[i][j]] == i \u3067\u3042\u308B\
    \n    self.indexForAdjacents = [[] for _ in range(n+1)]\n    for a, b in edges:\n\
    \      self.indexForAdjacents[a].append(len(self.adjacents[b]))\n      self.indexForAdjacents[b].append(len(self.adjacents[a]))\n\
    \      self.adjacents[a].append(b)\n      self.adjacents[b].append(a)\n    # childSubTreeValue[i]\
    \ = i\u306E\u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\n    # childSubTreeValue[i][j]\
    \ = i \u3092\u89AA\u3068\u3057\u3001adjacents[i][j]\u3092\u6839\u3068\u3057\u305F\
    \u90E8\u5206\u6728\u306E\u5024\n    self.childSubTreeValue = [[self.identity]\
    \ * len(self.adjacents[i]) for i in range(n+1)]\n    # ans[i] = i \u3092\u6839\
    \u3068\u3057\u305F\u3068\u304D\u306E\u6C42\u3081\u305F\u3044\u5024\n    self.ans\
    \ = [self.identity] * (n+1)\n    \n  # root \u304B\u3089 DFS \u3057\u3066\u3001\
    \u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\u3092\u8A08\u7B97\n  def _dfs1(self,\
    \ root):\n    self.parent = [-1] * (self.n+1)\n    self.order = [-1] * self.n\
    \ # DFS\u3067\u306E\u8A2A\u554F\u9806\n    stack = [root]\n    idx = 0\n    while\
    \ stack:\n      v = stack.pop()\n      self.order[idx] = v\n      idx += 1\n \
    \     for u in self.adjacents[v]:\n        if u == self.parent[v]:\n         \
    \ continue\n        self.parent[u] = v\n        stack.append(u)\n    # \u8A2A\u554F\
    \u9806\u3092\u9006\u9806\u306B\u3057\u3066\u3001\u5B50\u304B\u3089\u5024\u3092\
    \u8A08\u7B97\u3057\u3066\u3044\u304F\n    for v in reversed(self.order[1:]):\n\
    \      pv = self.parent[v]\n      result = self.identity\n      parentIndex =\
    \ -1\n      for i, u in enumerate(self.adjacents[v]):\n        if u == pv:\n \
    \         parentIndex = i\n          continue\n        result = self.merge(result,\
    \ self.childSubTreeValue[v][i])\n      # v \u3092\u6839\u3068\u3057\u305F\u90E8\
    \u5206\u6728\u306E\u5024\u3092\u89AA\u5074\u306B\u8A18\u9332\n      self.childSubTreeValue[pv][self.indexForAdjacents[v][parentIndex]]\
    \ = self.calc_node_value(result, v)\n  \n  # \u89AA\u306E\u90E8\u5206\u6728\u306E\
    \u5024\u3092\u4F7F\u3063\u3066\u3001\u81EA\u5206\u3092\u6839\u3068\u3057\u305F\
    \u90E8\u5206\u6728\u306E\u5024\u3092\u8A08\u7B97\n  def _dfs2(self):\n    for\
    \ v in self.order:\n      # \u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\u306E\u5DE6\
    \u304B\u3089\u306E\u7D2F\u7A4D\n      accFromLeft = self.identity\n      # \u5B50\
    \u306E\u90E8\u5206\u6728\u306E\u5024\u306E\u53F3\u304B\u3089\u306E\u7D2F\u7A4D\
    \n      # accFromRight[i] = merge(childSubTreeValue[v][i+1], childSubTreeValue[v][i+2],\
    \ ..., childSubTreeValue[v][len(adjacents[v])-1])\n      accFromRight = [self.identity]\
    \ * len(self.adjacents[v])\n      for i in reversed(range(len(self.adjacents[v])-1)):\n\
    \        accFromRight[i] = self.merge(self.childSubTreeValue[v][i+1], accFromRight[i+1])\n\
    \      \n      for j in range(len(self.adjacents[v])):\n        u = self.adjacents[v][j]\n\
    \        # u \u304C\u89AA\u3001v \u304C\u6839\u306E\u90E8\u5206\u6728\u306E\u5024\
    \u3092\u8A08\u7B97(u \u3092\u8003\u616E\u3057\u306A\u3044\u3068\u304D\u306E\u5024\
    )\n        # maerge(accFromLeft, accFromRight[j]) \u3067 u \u4EE5\u5916\u306E\
    \ v \u306E\u5B50\u306E\u5024\u3092\u8A08\u7B97\n        result = self.calc_node_value(self.merge(accFromLeft,\
    \ accFromRight[j]), v)\n        # \u3044\u307E\u89AA\u3068\u3057\u305F\u9802\u70B9\
    \u306E\u914D\u5217\u306B\u8A18\u9332\n        self.childSubTreeValue[u][self.indexForAdjacents[v][j]]\
    \ = result\n        # accFromLeft \u3092\u66F4\u65B0\n        accFromLeft = self.merge(accFromLeft,\
    \ self.childSubTreeValue[v][j])\n      # v \u3092\u6839\u3068\u3057\u305F\u3068\
    \u304D\u306E\u6C42\u3081\u305F\u3044\u5024\u3092\u8A08\u7B97\n      self.ans[v]\
    \ = self.calc_ans(accFromLeft, v)\n  \n  def run(self, root=1):\n    self._dfs1(root)\n\
    \    self._dfs2()\n    return self.ans\n\n\"\"\"\nidentity = \u9802\u70B9\u306B\
    \u6301\u305F\u305B\u308B\u5024(\u95A2\u6570\u306Ea\u306B\u6E21\u3055\u308C\u308B\
    )\u306E\u5358\u4F4D\u5143\nmerge(a, b) = \u90E8\u5206\u6728\u306E\u5024 a, b \u3092\
    \u30DE\u30FC\u30B8\u3059\u308B\u95A2\u6570\ncalc_node_value(a, v) = \u3059\u3079\
    \u3066\u306E\u5B50\u90E8\u5206\u6728\u306E\u5024\u3092\u30DE\u30FC\u30B8\u3057\
    \u305F\u5024 a \u304B\u3089\u9802\u70B9 v \u3092\u6839\u3068\u3057\u305F\u3068\
    \u304D\u306E\u8A08\u7B97\u306B\u4F7F\u3046\u5024(DP\u306E\u5024)\u3092\u8A08\u7B97\
    \u3059\u308B\u95A2\u6570\ncalc_ans(a, v) = \u3059\u3079\u3066\u306E\u5B50\u90E8\
    \u5206\u6728\u306E\u5024\u3092\u30DE\u30FC\u30B8\u3057\u305F\u5024 a \u304B\u3089\
    \u9802\u70B9 v \u3092\u6839\u3068\u3057\u305F\u3068\u304D\u306E\u6C42\u3081\u305F\
    \u3044\u3082\u306E\u3092\u8A08\u7B97\u3059\u308B\u95A2\u6570\n\"\"\"\n\n# identity\
    \ = \n# def merge(a,b):\n#   return \n# def calc_node_value(a,v):\n#   return\
    \ \n# def calc_ans(a,v):\n#     return \n\n\n# rr = rerooting(N, edges, identity,\
    \ merge, calc_node_value, calc_ans)"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/Rerooting.py
  requiredBy: []
  timestamp: '2025-11-13 20:32:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/Rerooting.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/Rerooting.py
- /library/algorithm_library/python/graph/Rerooting.py.html
title: algorithm_library/python/graph/Rerooting.py
---
