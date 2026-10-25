---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: tests/graph/test_graph_optimizations.py
    title: tests/graph/test_graph_optimizations.py
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
  code: "# Dinic\u6CD5 O(V^2 E)\nclass maxflow_edge:\n    def __init__(self, to, cap,\
    \ rev_idx):\n        self.to = to  # \u884C\u304D\u5148\n        self.cap = cap\
    \  # \u5BB9\u91CF\n        self.rev_idx = rev_idx  # \u9006\u5411\u304D\u306E\u8FBA\
    \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n\n\nclass maximum_flow:\n    def __init__(self,\
    \ N):\n        self.G = [[] for _ in range(N + 1)]\n        self.N = N\n\n   \
    \ def add_edge(self, a, b, c):\n        self.G[a].append(maxflow_edge(b, c, len(self.G[b])))\n\
    \        self.G[b].append(maxflow_edge(a, 0, len(self.G[a]) - 1))  # \u9006\u5411\
    \u304D\n\n    def dfs(self, v, goal, f):\n        graph, level, it = self.G, self.level,\
    \ self.it\n        vertices = [v]\n        path = []\n        limits = [f]\n \
    \       while vertices:\n            v = vertices[-1]\n            if v == goal:\n\
    \                flow = limits[-1]\n                for edge in path:\n      \
    \              edge.cap -= flow\n                    graph[edge.to][edge.rev_idx].cap\
    \ += flow\n                return flow\n\n            row = graph[v]\n       \
    \     i = it[v]\n            while i < len(row):\n                edge = row[i]\n\
    \                if edge.cap > 0 and level[edge.to] == level[v] + 1:\n       \
    \             it[v] = i\n                    vertices.append(edge.to)\n      \
    \              path.append(edge)\n                    limits.append(min(limits[-1],\
    \ edge.cap))\n                    break\n                i += 1\n            else:\n\
    \                it[v] = i\n                level[v] = -1  # \u3053\u306E\u9802\
    \u70B9\u304B\u3089\u306F\u3053\u308C\u4EE5\u4E0A\u6D41\u305B\u306A\u3044\n   \
    \             vertices.pop()\n                limits.pop()\n                if\
    \ path:\n                    path.pop()\n                    it[vertices[-1]]\
    \ += 1\n        return 0\n\n    def maxflow(self, start, goal):\n        assert\
    \ start != goal\n        graph = self.G\n        total_flow = 0\n        inf =\
    \ sum(edge.cap for edge in graph[start])\n        while True:\n            level\
    \ = self.level = [-1] * (self.N + 1)\n            level[start] = 0\n         \
    \   que = [start]\n            for v in que:\n                for edge in graph[v]:\n\
    \                    if edge.cap > 0 and level[edge.to] == -1:\n             \
    \           level[edge.to] = level[v] + 1\n                        que.append(edge.to)\n\
    \            if level[goal] == -1:\n                return total_flow\n\n    \
    \        self.it = [0] * (self.N + 1)\n            while True:\n             \
    \   res = self.dfs(start, goal, inf)\n                if res == 0:\n         \
    \           break\n                total_flow += res\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/maxflow.py
  requiredBy:
  - tests/graph/test_graph_optimizations.py
  timestamp: '2026-10-20 12:07:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/maxflow.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/maxflow.py
- /library/algorithm_library/python/graph/maxflow.py.html
title: algorithm_library/python/graph/maxflow.py
---
