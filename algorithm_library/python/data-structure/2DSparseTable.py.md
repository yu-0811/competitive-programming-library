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
  code: "# \u672Averified\n# \u30E1\u30E2\u30EA\u4F7F\u7528\u91CF\u306B\u6CE8\u610F\
    \n\n\nclass SparseTable2D:\n    def __init__(self, grid, op):\n        \"\"\"\n\
    \        grid: 2\u6B21\u5143\u914D\u5217\n        op: \u6F14\u7B97 (\u7D50\u5408\
    \u5247\u3001\u51AA\u7B49\u6027\u304C\u5FC5\u8981)\n        \"\"\"\n        self.op\
    \ = op\n        self.H = len(grid)\n        self.W = len(grid[0])\n        self.K\
    \ = self.H.bit_length()\n        self.L = self.W.bit_length()\n\n        # table[k][l][i][j]:\
    \ \u5DE6\u4E0A (i, j)\u3001\u9AD8\u3055 2^k\u3001\u5E45 2^l \u306E\u77E9\u5F62\
    \u306B op \u3092\u9069\u7528\u3057\u305F\u7D50\u679C\n        self.table = [\n\
    \            [[[0] * self.W for _ in range(self.H)] for _ in range(self.L)]\n\
    \            for _ in range(self.K)\n        ]\n\n        for i in range(self.H):\n\
    \            for j in range(self.W):\n                self.table[0][0][i][j] =\
    \ grid[i][j]\n\n        # \u884C\u65B9\u5411\u306E\u69CB\u7BC9 (\u9AD8\u3055 1\
    \ \u56FA\u5B9A\u3067\u5E45\u3092\u62E1\u5927)\n        for l in range(1, self.L):\n\
    \            width = 1 << l\n            half = width >> 1\n            for i\
    \ in range(self.H):\n                # j \u304B\u3089\u5E45 2^l \u306E\u533A\u9593\
    \u304C\u53CE\u307E\u308B\u7BC4\u56F2\u3060\u3051\u8A08\u7B97\n               \
    \ for j in range(self.W - width + 1):\n                    self.table[0][l][i][j]\
    \ = op(\n                        self.table[0][l - 1][i][j], self.table[0][l -\
    \ 1][i][j + half]\n                    )\n        # \u5217\u65B9\u5411\u306E\u69CB\
    \u7BC9 (\u4EFB\u610F\u306E\u5E45 l \u306B\u5BFE\u3057\u3066\u9AD8\u3055\u3092\u62E1\
    \u5927)\n        for k in range(1, self.K):\n            height = 1 << k\n   \
    \         half = height >> 1\n            for l in range(self.L):\n          \
    \      width = 1 << l\n                for i in range(self.H - height + 1):\n\
    \                    for j in range(self.W - width + 1):\n                   \
    \     self.table[k][l][i][j] = op(\n                            self.table[k -\
    \ 1][l][i][j],\n                            self.table[k - 1][l][i + half][j],\n\
    \                        )\n\n    def query(self, r1, c1, r2, c2):\n        \"\
    \"\"\n        (r1, c1) \u3092\u5DE6\u4E0A, (r2, c2) \u3092\u53F3\u4E0B\u3068\u3059\
    \u308B\u9589\u533A\u9593\u77E9\u5F62\u306E\u6F14\u7B97\u7D50\u679C\u3092\u8FD4\
    \u3059\n        0 <= r1 <= r2 < R, 0 <= c1 <= c2 < C\n        \"\"\"\n       \
    \ assert 0 <= r1 <= r2 < self.H\n        assert 0 <= c1 <= c2 < self.W\n\n   \
    \     height = r2 - r1 + 1\n        width = c2 - c1 + 1\n        k = height.bit_length()\
    \ - 1\n        l = width.bit_length() - 1\n\n        # 4\u3064\u306E\u9577\u65B9\
    \u5F62\u3067\u30AB\u30D0\u30FC\u3059\u308B\n        bottom_row = r2 - (1 << k)\
    \ + 1\n        right_col = c2 - (1 << l) + 1\n\n        rl = self.table[k][l][r1][c1]\n\
    \        tr = self.table[k][l][r1][right_col]\n        bl = self.table[k][l][bottom_row][c1]\n\
    \        br = self.table[k][l][bottom_row][right_col]\n\n        return self.op(self.op(rl,\
    \ tr), self.op(bl, br))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/2DSparseTable.py
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/2DSparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/2DSparseTable.py
- /library/algorithm_library/python/data-structure/2DSparseTable.py.html
title: algorithm_library/python/data-structure/2DSparseTable.py
---
