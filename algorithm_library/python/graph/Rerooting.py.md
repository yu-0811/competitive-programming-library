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
  code: "# \u5168\u65B9\u4F4D\u6728DP\nclass rerooting:\n    def __init__(\n     \
    \   self,\n        n: int,\n        edges: list[tuple[int, int]],\n        e:\
    \ int,\n        merge: callable,\n        calc_node_value: callable,\n       \
    \ calc_ans: callable,\n    ):\n        self.n = n\n        self.e = e\n      \
    \  self.merge = merge\n        self.calc_node_value = calc_node_value\n      \
    \  self.calc_ans = calc_ans\n        # g[i] = i \u3068\u96A3\u63A5\u3059\u308B\
    \u9802\u70B9\u306E\u30EA\u30B9\u30C8\n        g = self.g = [[] for _ in range(n\
    \ + 1)]\n        # rev[i][j] = g[i][j](i\u306Ej\u756A\u76EE\u306E\u96A3\u63A5\u9802\
    \u70B9)\u306B\u3068\u3063\u3066\u3001i\u304C\u4F55\u756A\u76EE\u306E\u96A3\u63A5\
    \u9802\u70B9\u304B\n        # g[g[i][j]][rev[i][j]] == i \u3067\u3042\u308B\n\
    \        rev = self.rev = [[] for _ in range(n + 1)]\n        for a, b in edges:\n\
    \            rev[a].append(len(g[b]))\n            rev[b].append(len(g[a]))\n\
    \            g[a].append(b)\n            g[b].append(a)\n        # dp[i] = i\u306E\
    \u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\n        # dp[i][j] = i \u3092\u89AA\
    \u3068\u3057\u3001g[i][j]\u3092\u6839\u3068\u3057\u305F\u90E8\u5206\u6728\u306E\
    \u5024\n        self.dp = [[e] * len(row) for row in g]\n        # ans[i] = i\
    \ \u3092\u6839\u3068\u3057\u305F\u3068\u304D\u306E\u6C42\u3081\u305F\u3044\u5024\
    \n        self.ans = [e] * (n + 1)\n\n    # root \u304B\u3089 DFS \u3057\u3066\
    \u3001\u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\u3092\u8A08\u7B97\n    def _dfs1(self,\
    \ root):\n        g, rev, dp = self.g, self.rev, self.dp\n        e, merge, add\
    \ = self.e, self.merge, self.calc_node_value\n        par = self.par = [-1] *\
    \ (self.n + 1)\n        order = self.order = []  # DFS\u3067\u306E\u8A2A\u554F\
    \u9806\n        stack = [root]\n        while stack:\n            v = stack.pop()\n\
    \            order.append(v)\n            for u in g[v]:\n                if u\
    \ != par[v]:\n                    par[u] = v\n                    stack.append(u)\n\
    \        # \u8A2A\u554F\u9806\u3092\u9006\u9806\u306B\u3057\u3066\u3001\u5B50\u304B\
    \u3089\u5024\u3092\u8A08\u7B97\u3057\u3066\u3044\u304F\n        for v in reversed(order[1:]):\n\
    \            p, x = par[v], e\n            for i, u in enumerate(g[v]):\n    \
    \            if u == p:\n                    j = rev[v][i]\n                else:\n\
    \                    x = merge(x, dp[v][i])\n            # v \u3092\u6839\u3068\
    \u3057\u305F\u90E8\u5206\u6728\u306E\u5024\u3092\u89AA\u5074\u306B\u8A18\u9332\
    \n            dp[p][j] = add(x, v)\n\n    # \u89AA\u306E\u90E8\u5206\u6728\u306E\
    \u5024\u3092\u4F7F\u3063\u3066\u3001\u81EA\u5206\u3092\u6839\u3068\u3057\u305F\
    \u90E8\u5206\u6728\u306E\u5024\u3092\u8A08\u7B97\n    def _dfs2(self):\n     \
    \   g, rev, dp = self.g, self.rev, self.dp\n        e, merge, add = self.e, self.merge,\
    \ self.calc_node_value\n        par, ans, answer = self.par, self.ans, self.calc_ans\n\
    \        for v in self.order:\n            val, idx, p = dp[v], rev[v], par[v]\n\
    \            # \u5B50\u306E\u90E8\u5206\u6728\u306E\u5024\u306E\u5DE6\u304B\u3089\
    \u306E\u7D2F\u7A4D\n            left = e\n            # \u5B50\u306E\u90E8\u5206\
    \u6728\u306E\u5024\u306E\u53F3\u304B\u3089\u306E\u7D2F\u7A4D\n            # right[i]\
    \ = merge(dp[v][i+1], dp[v][i+2], ..., dp[v][len(g[v])-1])\n            right\
    \ = [e] * len(val)\n            for i in range(len(val) - 2, -1, -1):\n      \
    \          right[i] = merge(val[i + 1], right[i + 1])\n            for j, u in\
    \ enumerate(g[v]):\n                if u != p:\n                    # u \u304C\
    \u89AA\u3001v \u304C\u6839\u306E\u90E8\u5206\u6728\u306E\u5024\u3092\u8A08\u7B97\
    (u \u3092\u8003\u616E\u3057\u306A\u3044\u3068\u304D\u306E\u5024)\n           \
    \         # maerge(left, right[j]) \u3067 u \u4EE5\u5916\u306E v \u306E\u5B50\u306E\
    \u5024\u3092\u8A08\u7B97\n                    res = add(merge(left, right[j]),\
    \ v)\n                    # \u3044\u307E\u89AA\u3068\u3057\u305F\u9802\u70B9\u306E\
    \u914D\u5217\u306B\u8A18\u9332\n                    dp[u][idx[j]] = res\n    \
    \            # left \u3092\u66F4\u65B0\n                left = merge(left, val[j])\n\
    \            # v \u3092\u6839\u3068\u3057\u305F\u3068\u304D\u306E\u6C42\u3081\u305F\
    \u3044\u5024\u3092\u8A08\u7B97\n            ans[v] = answer(left, v)\n\n    def\
    \ run(self, root=1):\n        self._dfs1(root)\n        self._dfs2()\n       \
    \ return self.ans\n\n\n\"\"\"\ne = \u9802\u70B9\u306B\u6301\u305F\u305B\u308B\u5024\
    (\u95A2\u6570\u306Ea\u306B\u6E21\u3055\u308C\u308B)\u306E\u5358\u4F4D\u5143\n\
    merge(a, b) = \u90E8\u5206\u6728\u306E\u5024 a, b \u3092\u30DE\u30FC\u30B8\u3059\
    \u308B\u95A2\u6570\ncalc_node_value(a, v) = \u3059\u3079\u3066\u306E\u5B50\u90E8\
    \u5206\u6728\u306E\u5024\u3092\u30DE\u30FC\u30B8\u3057\u305F\u5024 a \u304B\u3089\
    \u9802\u70B9 v \u3092\u6839\u3068\u3057\u305F\u3068\u304D\u306E\u8A08\u7B97\u306B\
    \u4F7F\u3046\u5024(DP\u306E\u5024)\u3092\u8A08\u7B97\u3059\u308B\u95A2\u6570\n\
    calc_ans(a, v) = \u3059\u3079\u3066\u306E\u5B50\u90E8\u5206\u6728\u306E\u5024\u3092\
    \u30DE\u30FC\u30B8\u3057\u305F\u5024 a \u304B\u3089\u9802\u70B9 v \u3092\u6839\
    \u3068\u3057\u305F\u3068\u304D\u306E\u6C42\u3081\u305F\u3044\u3082\u306E\u3092\
    \u8A08\u7B97\u3059\u308B\u95A2\u6570\n\"\"\"\n\n# e =\n# def merge(a,b):\n#  \
    \ return\n# def calc_node_value(a,v):\n#   return\n# def calc_ans(a,v):\n#   \
    \  return\n\n\n# rr = rerooting(N, edges, e, merge, calc_node_value, calc_ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/Rerooting.py
  requiredBy: []
  timestamp: '2026-11-06 23:09:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/Rerooting.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/Rerooting.py
- /library/algorithm_library/python/graph/Rerooting.py.html
title: algorithm_library/python/graph/Rerooting.py
---
