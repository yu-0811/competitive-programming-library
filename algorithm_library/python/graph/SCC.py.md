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
  code: "class SCC:\n    def __init__(self, N: int):\n        self.N = N  # \u9802\
    \u70B9\u6570\n        self.edges = []  # \u8FBA\n\n    def addEdge(self, frm:\
    \ int, to: int):\n        assert 0 <= frm <= self.N\n        assert 0 <= to <=\
    \ self.N\n        self.edges.append((frm, to))\n\n    # \u8FBA\u3092 CSR \u5F62\
    \u5F0F\u306B\u3059\u308B\n    def _csr(self, N: int, edges: list[tuple]):\n  \
    \      start = [0] * (N + 1)\n        # dst := \u8FBA\u3092\u59CB\u70B9\u306E\u6607\
    \u9806\u306B\u30BD\u30FC\u30C8\u3057\u305F\u6642\u306E\u7D42\u70B9\u306E\u30EA\
    \u30B9\u30C8\n        dst = [0] * len(edges)\n\n        # start[i+1] := \u9802\
    \u70B9 i \u3092\u59CB\u70B9\u3068\u3059\u308B\u8FBA\u306E\u6570 \u3068\u306A\u308B\
    \u3088\u3046\u306B\u69CB\u7BC9\n        for u, _ in edges:  # u \u3092\u59CB\u70B9\
    \u3068\u3059\u308B\u8FBA\n            start[u + 1] += 1\n        for i in range(1,\
    \ N + 1):\n            start[i] += start[i - 1]\n\n        # pos[i] := \u59CB\u70B9\
    \u3092 i \u3068\u3059\u308B\u8FBA\u306E dst \u3078\u306E\u633F\u5165\u4F4D\u7F6E\
    \n        pos = start[:]\n        for u, v in edges:\n            dst[pos[u]]\
    \ = v\n            pos[u] += 1\n\n        return start, dst\n\n    # ids=True\
    \ \u306A\u3089\u6210\u5206ID\u3001False \u306A\u3089\u6210\u5206\u3054\u3068\u306E\
    \u9802\u70B9\u30EA\u30B9\u30C8\u3092\u8A08\u7B97\u3059\u308B\n    def _scc(self,\
    \ ids=False):\n        N = self.N\n        start, dst = self._csr(N, self.edges)\n\
    \        order = [-1] * N  # \u672A\u8A2A\u554F: -1\u3001\u63A2\u7D22\u4E2D: active\
    \ \u5185\u306E\u4F4D\u7F6E\u3001\u78BA\u5B9A\u6E08\u307F: N\n        result =\
    \ [0] * N if ids else []\n        active = []  # \u63A2\u7D22\u6E08\u307F\u304B\
    \u3064\u6240\u5C5E\u6210\u5206\u304C\u672A\u78BA\u5B9A\u306E\u9802\u70B9\n   \
    \     roots = []  # \u5F37\u9023\u7D50\u6210\u5206\u306E\u6839\u5019\u88DC\u306E\
    \ active \u5185\u306E\u4F4D\u7F6E\n        count = 0\n        for root in range(N):\n\
    \            if order[root] != -1:\n                continue\n            stack\
    \ = [root]\n            while stack:\n                v = stack.pop()\n      \
    \          if v < 0:  # ~v \u306F\u5E30\u308A\u304C\u3051\u306E\u51E6\u7406\n\
    \                    v = ~v\n                    if roots[-1] == order[v]:\n \
    \                       begin = roots.pop()\n                        group = active[begin:]\n\
    \                        del active[begin:]\n                        for u in\
    \ group:\n                            order[u] = N\n                         \
    \   if ids:\n                                result[u] = count\n             \
    \           if not ids:\n                            result.append(group)\n  \
    \                      count += 1\n                elif order[v] == -1:\n    \
    \                order[v] = len(active)\n                    active.append(v)\n\
    \                    roots.append(order[v])\n                    stack.append(~v)\n\
    \                    stack.extend(dst[start[v]:start[v + 1]])\n              \
    \  else:\n                    while roots[-1] > order[v]:\n                  \
    \      roots.pop()\n        return count, result\n\n    # groups[i] = \u30B0\u30EB\
    \u30FC\u30D7ID i \u306B\u5C5E\u3059\u308B\u9802\u70B9\u306E\u96C6\u5408\u3092\
    \ \u8FD4\u3059\n    def build_scc(self) -> list[list[int]]:\n        return self._scc()[1][::-1]\n\
    \n    # \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3\u5F8C\u306E\u30B0\u30E9\u30D5\
    \u3092\u69CB\u7BC9\u3059\u308B(\u540C\u4E00\u306E\u5F37\u9023\u7D50\u6210\u5206\
    \u5185\u306E\u9802\u70B9\u306F\u7E2E\u7D04)\n    def build_dag(self) -> list[list[int]]:\n\
    \        # comp[i] = \u9802\u70B9 i \u304C\u5C5E\u3059\u308B\u5F37\u9023\u7D50\
    \u6210\u5206\u306E ID\n        count, comp = self._scc(True)\n        comp = [count\
    \ - 1 - c for c in comp]\n        # dag[i] = \u5F37\u9023\u7D50\u6210\u5206 i\
    \ \u304B\u3089\u51FA\u308B\u8FBA\u306E\u884C\u304D\u5148\u306E\u5F37\u9023\u7D50\
    \u6210\u5206\u306E ID\n        dag = [[] for _ in range(count)]\n        for u,\
    \ v in self.edges:\n            if comp[u] != comp[v]:\n                dag[comp[u]].append(comp[v])\n\
    \        return dag\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/SCC.py
  requiredBy: []
  timestamp: '2026-10-29 12:56:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/SCC.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/SCC.py
- /library/algorithm_library/python/graph/SCC.py.html
title: algorithm_library/python/graph/SCC.py
---
