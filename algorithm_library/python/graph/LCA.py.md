---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/400748
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# HLD\u3002\u53C2\u8003: https://judge.yosupo.jp/submission/400748\nclass\
    \ LCA:\n    # n: \u9802\u70B9\u6570\u3001E: \u8FBA\u96C6\u5408, root: \u6728\u306E\
    \u6839\n    def __init__(self, n, E, root=0):\n        par = self.par = [0] *\
    \ (n + 1)\n        dep = self.dep = [-1] * (n + 1)\n        siz = self.siz = [1]\
    \ * (n + 1)\n        jmp = self.jmp = [-1] * (n + 1)\n        tin = self.tin =\
    \ [0] * (n + 1)\n        deg = [0] * (n + 1)\n\n        for u, v in E:\n     \
    \       deg[u] += 1\n            deg[v] += 1\n            par[u] ^= v\n      \
    \      par[v] ^= u\n        que = []\n        for u in range(n + 1):\n       \
    \     if deg[u] == 1 and u != root:\n                que.append(u)\n         \
    \   elif deg[u] == 0:\n                par[u] = -1\n        for u in que:\n  \
    \          v = par[u]\n            siz[v] += siz[u]\n            if siz[u] > tin[v]:\n\
    \                tin[v] = siz[u]\n                jmp[v] = u\n            par[v]\
    \ ^= u\n            deg[v] -= 1\n            if deg[v] == 1 and v != root:\n \
    \               que.append(v)\n        par[root] = -1\n\n        if jmp[root]\
    \ >= 0:\n            siz[jmp[root]] = -siz[jmp[root]]\n        jmp[root] = -1\n\
    \        siz[root] = tin[root] + 1\n        dep[root] = tin[root] = 0\n      \
    \  for u in reversed(que):\n            v = par[u]\n            dep[u] = dep[v]\
    \ + 1\n            h, b = jmp[u], tin[u] + 1\n            if h >= 0:\n       \
    \         siz[h] = -siz[h]\n            if siz[u] < 0:\n                tin[u]\
    \ = tin[v] + 1\n                jmp[u] = jmp[v]\n            else:\n         \
    \       tin[u] = tin[v] + siz[v]\n                siz[v] += siz[u]\n         \
    \       jmp[u] = v\n            siz[u] = b\n\n    # u \u3068 v \u306E LCA \u3092\
    \u8FD4\u3059 O(log N)\n    def lca(self, u, v):\n        tin, jmp = self.tin,\
    \ self.jmp\n        l, r = tin[u], tin[v]\n        if l > r:\n            l, r\
    \ = r, l\n            u, v = v, u\n        if r < l + self.siz[u]:\n         \
    \   return u\n        v = jmp[v]\n        while l < tin[v]:\n            v = jmp[v]\n\
    \        return v\n\n    # \u69CB\u7BC9\u6642\u306E\u6839\u3092\u57FA\u6E96\u306B\
    \u3001u \u306E\u90E8\u5206\u6728\u306B v \u304C\u542B\u307E\u308C\u308B\u304B\
    \ O(1)\n    def is_in_subtree(self, u, v):\n        tin = self.tin\n        return\
    \ tin[u] <= tin[v] < tin[u] + self.siz[u]\n\n    # u \u3068 v \u306E\u8DDD\u96E2\
    \u3092\u8FD4\u3059\n    def get_distance(self, u, v):\n        dep = self.dep\n\
    \        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]\n\n    # u-v \u306E\u30D1\
    \u30B9\u304Cvia\u3092\u901A\u308B\u304B\uFF08\u7AEF\u70B9\u3082\u542B\u3080\uFF09\
    \n    def is_on_path(self, u, v, via):\n        anc_u = self.is_in_subtree(via,\
    \ u)\n        anc_v = self.is_in_subtree(via, v)\n        return anc_u != anc_v\
    \ or anc_u and self.lca(u, v) == via\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/LCA.py
  requiredBy: []
  timestamp: '2026-10-27 19:55:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/LCA.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/LCA.py
- /library/algorithm_library/python/graph/LCA.py.html
title: algorithm_library/python/graph/LCA.py
---
