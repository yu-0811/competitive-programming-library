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
  code: "class SparseTable:\n    def __init__(self, arr, op):\n        \"\"\"\n  \
    \      arr: \u914D\u5217\n        op: \u6F14\u7B97 (\u7D50\u5408\u5247\u3001\u51AA\
    \u7B49\u5247\u3092\u6E80\u305F\u3059\u3053\u3068)\n        \u6642\u9593\u8A08\u7B97\
    \u91CF: O(n log n) \u69CB\u7BC9, O(1) \u30AF\u30A8\u30EA\n        \u7A7A\u9593\
    \u8A08\u7B97\u91CF: O(n log n)\n        \"\"\"\n        self.op = op\n       \
    \ self.n = len(arr)\n        self.max_k = self.n.bit_length()\n        # table[k][i]\
    \ = i \u304B\u3089\u9577\u3055 2^k \u306E\u533A\u9593\u306B\u5BFE\u3059\u308B\u6F14\
    \u7B97\u7D50\u679C\n        self.table = [[0] * self.n for _ in range(self.max_k)]\n\
    \n        for i in range(self.n):\n            self.table[0][i] = arr[i]\n   \
    \     for k in range(1, self.max_k):\n            range_ = 1 << (k - 1)\n    \
    \        for i in range(self.n - (1 << k) + 1):\n                self.table[k][i]\
    \ = op(\n                    self.table[k - 1][i], self.table[k - 1][i + range_]\n\
    \                )\n\n    def query(self, l, r):\n        \"\"\"\n        [l,\
    \ r) \u306E\u533A\u9593\u306B\u5BFE\u3059\u308B\u6F14\u7B97\u7D50\u679C\u3092\u8FD4\
    \u3059 O(1)\n        \"\"\"\n        assert 0 <= l < r <= self.n\n        # 2^k\
    \ <= r - l \u3092\u6E80\u305F\u3059\u6700\u5927\u306E k \u3092\u6C42\u3081\u308B\
    \n        k = (r - l).bit_length() - 1\n        # [l, l + 2^k) \u3068 [r - 2^k,\
    \ r) \u306E\u533A\u9593\u306B\u5206\u5272\u3057\u3066\u8A08\u7B97\n        return\
    \ self.op(self.table[k][l], self.table[k][r - (1 << k)])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/SparseTable.py
  requiredBy: []
  timestamp: '2025-12-09 12:08:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/SparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/SparseTable.py
- /library/algorithm_library/python/data-structure/SparseTable.py.html
title: algorithm_library/python/data-structure/SparseTable.py
---
