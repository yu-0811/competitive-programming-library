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
  code: "from collections import deque\n\nclass SCC:\n  def __init__(self, N: int):\n\
    \    self.N = N # \u9802\u70B9\u6570\n    self.graphEdges = list() # \u8FBA\n\
    \    self.inf = pow(10,9)\n    \n  def addEdge(self, frm: int, to: int):\n   \
    \ assert 0<=frm<=self.N\n    assert 0<=to<=self.N\n    self.graphEdges.append([frm,to])\n\
    \  \n  # \u8FBA\u3092 CSR \u5F62\u5F0F\u306B\u3059\u308B\n  # \u9AD8\u901F\u5316\
    \u306E\u305F\u3081\u3001python \u3067\u306F\u3042\u3093\u307E\u610F\u5473\u306A\
    \u3044\uFF1F\n  def _toCSR(self,N: int, graphEdges: list[list]):\n    start =\
    \ [0]*(N+1)\n    # endList := \u8FBA\u3092\u59CB\u70B9\u306E\u6607\u9806\u306B\
    \u30BD\u30FC\u30C8\u3057\u305F\u6642\u306E\u7D42\u70B9\u306E\u30EA\u30B9\u30C8\
    \n    endList = [0]*len(graphEdges)\n\n    # start[i+1] := \u9802\u70B9 i \u3092\
    \u59CB\u70B9\u3068\u3059\u308B\u8FBA\u306E\u6570 \u3068\u306A\u308B\u3088\u3046\
    \u306B\u69CB\u7BC9\n    for u,v in graphEdges: # u -> v \u3078\u306E\u8FBA\n \
    \     start[u+1] += 1\n    # start[i] := \u59CB\u70B9\u306E\u9802\u70B9\u756A\u53F7\
    \u304C i \u672A\u6E80\u3067\u3042\u308B\u8FBA\u306E\u6570 \u306B\u306A\u308B\u3088\
    \u3046\u306B\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\n    # \u3053\u306E\u3068\u304D\
    \u3001start[i] = endList \u3067\u9802\u70B9 i \u304C\u59CB\u70B9\u3068\u306A\u308B\
    \u6700\u5C0F\u306E index (0-index)\n    for i in range(1,N+1):\n      start[i]\
    \ += start[i-1]\n\n    # pointer[i] := \u59CB\u70B9\u3092 i \u3068\u3059\u308B\
    \u8FBA\u306E endList \u3078\u306E\u633F\u5165\u4F4D\u7F6E\n    pointer = start[:]\n\
    \    for u,v in graphEdges:\n      endList[pointer[u]] = v\n      pointer[u] +=\
    \ 1\n      \n    return start, endList\n  \n  # \u5F37\u9023\u7D50\u6210\u5206\
    \u5206\u89E3\u3092\u3059\u308B\n  def _decomposeToSCC(self):\n    start, endList\
    \ = self._toCSR(self.N, self.graphEdges)\n    nowOrder = 0 # \u8A2A\u308C\u305F\
    \u9802\u70B9\u6570\n    groupNum = 0 # \u898B\u3064\u304B\u3063\u305F\u5F37\u9023\
    \u7D50\u6210\u5206\u306E\u6570\n    pendingStack = deque() # \u63A2\u7D22\u6E08\
    \u307F\u304B\u3064 sccId \u304C\u672A\u78BA\u5B9A\u306E\u9802\u70B9\u3092\u7BA1\
    \u7406\u3059\u308B stack\n    lowlink = [0]*self.N\n    order = [-1]*self.N #\
    \ \u9802\u70B9\u306E\u884C\u304D\u304C\u3051\u9806\n    groupId = [0]*self.N\n\
    \    \n    def dfs(v):\n      nonlocal nowOrder, groupNum, pendingStack, lowlink,\
    \ order, groupId\n      dfsStack = deque()\n      dfsStack.append(-(v+1))\n  \
    \    dfsStack.append(v)\n      while dfsStack:\n        v = dfsStack.pop()\n \
    \       if v<0: # \u5E30\u308A\u304C\u3051\n          # lowlink \u3092\u66F4\u65B0\
    \u3059\u308B\u5FC5\u8981\u304C\u3042\u308B\u306A\u3089\n          v *= -1\n  \
    \        v -= 1\n          if v>=self.inf:\n            frm = v//self.inf - 1\n\
    \            to =  v%self.inf\n            # lowlink[frm] = min(lowlink[frm],\
    \ lowlink[to])\n            if lowlink[frm]>lowlink[to]:\n              lowlink[frm]\
    \ = lowlink[to]\n            v %= self.inf\n            \n          # scc_roote\
    \ \u306A\u3089\n          if lowlink[v] == order[v]:\n            while True:\n\
    \              u = pendingStack.pop()\n              order[u] = self.inf # lowlink\
    \ \u306E\u8A08\u7B97\u306B\u4F7F\u308F\u308C\u306A\u3044\u3088\u3046\u306B order\
    \ \u3092\u66F4\u65B0\n              groupId[u] = groupNum # groupId \u3092\u78BA\
    \u5B9A\n              if u==v: break\n            groupNum += 1\n            \n\
    \        else: # \u884C\u304D\u304C\u3051\n          if order[v]!=-1: continue\n\
    \          lowlink[v] = order[v] = nowOrder\n          nowOrder += 1\n       \
    \   pendingStack.append(v)\n          for i in range(start[v], start[v+1]):\n\
    \            to = endList[i] # v -> to \u306E\u8FBA\n            if order[to]==-1:\
    \ # \u672A\u63A2\u7D22\u306A\u3089\n              dfsStack.append(-((to+1) + (v+1)*self.inf))\
    \ # 0-index \u3067\u58CA\u308C\u306A\u3044\u3088\u3046\u306B v+1 \u306B\n    \
    \          dfsStack.append(to)\n            # \u63A2\u7D22\u6E08\u307F\u306A\u3089\
    \ back edge \u304B cross edge\n            else:\n              # lowlink[v] =\
    \ min(lowlink[v], order[to])\n              if lowlink[v]>order[to]:\n       \
    \         lowlink[v] = order[to]\n          \n    for v in range(self.N):\n  \
    \    if order[v]==-1: dfs(v)\n    # \u7E2E\u7D04\u5F8C\u306E\u30B0\u30E9\u30D5\
    \u3067 groupId \u3092\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u9806\
    \u306B\u3059\u308B\n    for v in range(self.N):\n      groupId[v] = groupNum-1-groupId[v]\n\
    \      \n    return groupNum, groupId\n  \n  # groups[i] = \u30B0\u30EB\u30FC\u30D7\
    ID i \u306B\u5C5E\u3059\u308B\u9802\u70B9\u306E\u96C6\u5408\u3092 \u8FD4\u3059\
    \n  def doSCC(self):\n    groupNum, groupId = self._decomposeToSCC()\n    groups\
    \ = [[] for _ in range(groupNum)]\n    for v in range(self.N):\n      groups[groupId[v]].append(v)\n\
    \    return groups\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/SCC.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/SCC.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/SCC.py
- /library/algorithm_library/python/graph/SCC.py.html
title: algorithm_library/python/graph/SCC.py
---
