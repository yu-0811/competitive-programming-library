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
  code: "# \u672Averified\n# \u30E1\u30E2\u30EA\u4F7F\u7528\u91CF\u306B\u6CE8\u610F\
    \n\n\nclass SparseTable2D:\n    def __init__(self, grid, op):\n        \"\"\"\n\
    \        grid: \u7A7A\u3067\u306A\u30442\u6B21\u5143\u914D\u5217\n        op:\
    \ \u6F14\u7B97 (\u7D50\u5408\u5247\u3001\u53EF\u63DB\u6027\u3001\u51AA\u7B49\u6027\
    \u304C\u5FC5\u8981)\n        \u69CB\u7BC9\u30FB\u7A7A\u9593: O(H * W * logH *\
    \ logW), \u30AF\u30A8\u30EA: O(1)\n        \"\"\"\n        self.op = op\n    \
    \    self.H = len(grid)\n        self.W = len(grid[0])\n        self.K = self.H.bit_length()\n\
    \        self.L = self.W.bit_length()\n\n        # table[k][l][i][j]: \u5DE6\u4E0A\
    \ (i, j)\u3001\u9AD8\u3055 2^k\u3001\u5E45 2^l \u306E\u77E9\u5F62\n        # \u5404\
    \u6BB5\u306F\u77E9\u5F62\u304C\u53CE\u307E\u308B\u4F4D\u7F6E\u3060\u3051\u4FDD\
    \u6301\u3059\u308B\n        self.table = table = [[[row[:] for row in grid]]]\n\
    \n        for l in range(1, self.L):\n            half = 1 << (l - 1)\n      \
    \      table[0].append([list(map(op, row, row[half:])) for row in table[0][-1]])\n\
    \        for k in range(1, self.K):\n            half = 1 << (k - 1)\n       \
    \     table.append(\n                [\n                    [list(map(op, top,\
    \ bottom)) for top, bottom in zip(prev, prev[half:])]\n                    for\
    \ prev in table[-1]\n                ]\n            )\n\n    def query(self, r1,\
    \ c1, r2, c2):\n        \"\"\"\n        (r1, c1) \u3092\u5DE6\u4E0A, (r2, c2)\
    \ \u3092\u53F3\u4E0B\u3068\u3059\u308B\u9589\u533A\u9593\u77E9\u5F62\u306E\u6F14\
    \u7B97\u7D50\u679C\u3092\u8FD4\u3059\n        0 <= r1 <= r2 < H, 0 <= c1 <= c2\
    \ < W\n        \"\"\"\n        assert 0 <= r1 <= r2 < self.H\n        assert 0\
    \ <= c1 <= c2 < self.W\n\n        k = (r2 - r1 + 1).bit_length() - 1\n       \
    \ l = (c2 - c1 + 1).bit_length() - 1\n        rows = self.table[k][l]\n      \
    \  top = rows[r1]\n        bottom = rows[r2 - (1 << k) + 1]\n        c2 = c2 -\
    \ (1 << l) + 1\n        op = self.op\n        return op(op(top[c1], top[c2]),\
    \ op(bottom[c1], bottom[c2]))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/2DSparseTable.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/2DSparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/2DSparseTable.py
- /library/algorithm_library/python/data_structure/2DSparseTable.py.html
title: algorithm_library/python/data_structure/2DSparseTable.py
---
