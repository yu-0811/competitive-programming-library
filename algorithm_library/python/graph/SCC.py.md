---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: tests/graph/test_graph_optimizations.py
    title: tests/graph/test_graph_optimizations.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/graph/scc_yosupo.test.py
    title: tests/graph/scc_yosupo.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SCC:\n    def __init__(self, N: int):\n        self.N = N  # \u9802\
    \u70B9\u6570\n        self.edges = []  # \u8FBA\n\n    def addEdge(self, frm:\
    \ int, to: int):\n        assert 0 <= frm <= self.N\n        assert 0 <= to <=\
    \ self.N\n        self.edges.append([frm, to])\n\n    # \u8FBA\u3092 CSR \u5F62\
    \u5F0F\u306B\u3059\u308B(\u5225\u306BCSR\u3058\u3083\u306A\u304F\u3066\u3082\u3067\
    \u304D\u308B\u304C\u9AD8\u901F\u5316\u306E\u305F\u3081)\n    def _csr(self, N:\
    \ int, edges: list[list]):\n        start = [0] * (N + 1)\n        # dst := \u8FBA\
    \u3092\u59CB\u70B9\u306E\u6607\u9806\u306B\u30BD\u30FC\u30C8\u3057\u305F\u6642\
    \u306E\u7D42\u70B9\u306E\u30EA\u30B9\u30C8\n        dst = [0] * len(edges)\n\n\
    \        # start[i+1] := \u9802\u70B9 i \u3092\u59CB\u70B9\u3068\u3059\u308B\u8FBA\
    \u306E\u6570 \u3068\u306A\u308B\u3088\u3046\u306B\u69CB\u7BC9\n        for u,\
    \ _ in edges:  # u \u3092\u59CB\u70B9\u3068\u3059\u308B\u8FBA\n            start[u\
    \ + 1] += 1\n        # start[i] := \u59CB\u70B9\u306E\u9802\u70B9\u756A\u53F7\u304C\
    \ i \u672A\u6E80\u3067\u3042\u308B\u8FBA\u306E\u6570 \u306B\u306A\u308B\u3088\u3046\
    \u306B\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\n        # \u3053\u306E\u3068\u304D\
    \u3001start[i] = dst \u3067\u9802\u70B9 i \u304C\u59CB\u70B9\u3068\u306A\u308B\
    \u6700\u5C0F\u306E index (0-index)\n        for i in range(1, N + 1):\n      \
    \      start[i] += start[i - 1]\n\n        # pos[i] := \u59CB\u70B9\u3092 i \u3068\
    \u3059\u308B\u8FBA\u306E dst \u3078\u306E\u633F\u5165\u4F4D\u7F6E\n        pos\
    \ = start[:]\n        for u, v in edges:\n            dst[pos[u]] = v\n      \
    \      pos[u] += 1\n\n        return start, dst\n\n    # \u5F37\u9023\u7D50\u6210\
    \u5206\u5206\u89E3\u3092\u3059\u308B\n    def _scc_ids(self):\n        N = self.N\n\
    \        start, dst = self._csr(N, self.edges)\n        it = start[:-1]  # \u5404\
    \u9802\u70B9\u3067\u6B21\u306B\u8ABF\u3079\u308B\u8FBA\u306E\u4F4D\u7F6E\n   \
    \     timer = 0  # \u8A2A\u308C\u305F\u9802\u70B9\u6570\n        count = 0  #\
    \ \u898B\u3064\u304B\u3063\u305F\u5F37\u9023\u7D50\u6210\u5206\u306E\u6570\n \
    \       active = []  # \u63A2\u7D22\u6E08\u307F\u304B\u3064\u6240\u5C5E\u6210\u5206\
    \u304C\u672A\u78BA\u5B9A\u306E\u9802\u70B9\n        lowlink = [0] * N\n      \
    \  order = [-1] * N  # \u9802\u70B9\u306E\u884C\u304D\u304C\u3051\u9806\n    \
    \    parent = [-1] * N\n        comp = [0] * N\n\n        for root in range(N):\n\
    \            if order[root] != -1:\n                continue\n            stack\
    \ = [root]\n            lowlink[root] = order[root] = timer\n            timer\
    \ += 1\n            active.append(root)\n            while stack:\n          \
    \      v = stack[-1]\n                i = it[v]\n                if i < start[v\
    \ + 1]:\n                    it[v] = i + 1\n                    to = dst[i]\n\
    \                    if order[to] == -1:\n                        parent[to] =\
    \ v\n                        lowlink[to] = order[to] = timer\n               \
    \         timer += 1\n                        active.append(to)\n            \
    \            stack.append(to)\n                    elif lowlink[v] > order[to]:\n\
    \                        lowlink[v] = order[to]\n                else:  # \u5E30\
    \u308A\u304C\u3051\n                    stack.pop()\n                    if lowlink[v]\
    \ == order[v]:\n                        while True:\n                        \
    \    u = active.pop()\n                            order[u] = N  # \u78BA\u5B9A\
    \u3057\u305F\u6210\u5206\u3092 lowlink \u306E\u8A08\u7B97\u304B\u3089\u9664\u304F\
    \n                            comp[u] = count\n                            if\
    \ u == v:\n                                break\n                        count\
    \ += 1\n                    pv = parent[v]\n                    if pv != -1 and\
    \ lowlink[pv] > lowlink[v]:\n                        lowlink[pv] = lowlink[v]\n\
    \        # \u7E2E\u7D04\u5F8C\u306E\u30B0\u30E9\u30D5\u3067 comp \u3092\u30C8\u30DD\
    \u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u9806\u306B\u3059\u308B\n        for\
    \ v in range(N):\n            comp[v] = count - 1 - comp[v]\n\n        return\
    \ count, comp\n\n    # groups[i] = \u30B0\u30EB\u30FC\u30D7ID i \u306B\u5C5E\u3059\
    \u308B\u9802\u70B9\u306E\u96C6\u5408\u3092 \u8FD4\u3059\n    def build_scc(self)\
    \ -> list[list[int]]:\n        count, comp = self._scc_ids()\n        groups =\
    \ [[] for _ in range(count)]\n        for v in range(self.N):\n            groups[comp[v]].append(v)\n\
    \        return groups\n\n    # \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3\u5F8C\
    \u306E\u30B0\u30E9\u30D5\u3092\u69CB\u7BC9\u3059\u308B(\u540C\u4E00\u306E\u5F37\
    \u9023\u7D50\u6210\u5206\u5185\u306E\u9802\u70B9\u306F\u7E2E\u7D04)\n    def build_dag(self)\
    \ -> list[list[int]]:\n        # comp[i] = \u9802\u70B9 i \u304C\u5C5E\u3059\u308B\
    \u5F37\u9023\u7D50\u6210\u5206\u306E ID\n        count, comp = self._scc_ids()\n\
    \        # dag[i] = \u5F37\u9023\u7D50\u6210\u5206 i \u304B\u3089\u51FA\u308B\u8FBA\
    \u306E\u884C\u304D\u5148\u306E\u5F37\u9023\u7D50\u6210\u5206\u306E ID\n      \
    \  dag = [[] for _ in range(count)]\n        for u, v in self.edges:\n       \
    \     if comp[u] != comp[v]:\n                dag[comp[u]].append(comp[v])\n \
    \       return dag\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/SCC.py
  requiredBy:
  - tests/graph/test_graph_optimizations.py
  timestamp: '2026-10-20 12:13:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/graph/scc_yosupo.test.py
documentation_of: algorithm_library/python/graph/SCC.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/SCC.py
- /library/algorithm_library/python/graph/SCC.py.html
title: algorithm_library/python/graph/SCC.py
---
