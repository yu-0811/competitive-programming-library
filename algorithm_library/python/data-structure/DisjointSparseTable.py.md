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
  code: "class DisjointSparseTable:\n    def __init__(self, arr, op):\n        \"\"\
    \"\n        arr: \u914D\u5217\n        op: \u6F14\u7B97 (\u7D50\u5408\u5F8B\u3092\
    \u6E80\u305F\u3059\u3053\u3068)\n        \"\"\"\n        self.n = len(arr)\n \
    \       self.arr = arr[:]\n        self.op = op\n\n        self.max_k = self.n.bit_length()\n\
    \        self.table = [[0] * self.n for _ in range(self.max_k)]\n\n        for\
    \ k in range(self.max_k):\n            block_size = 1 << (k + 1)  # \u30D6\u30ED\
    \u30C3\u30AF\u5168\u4F53\u306E\u9577\u3055\n            half = 1 << k  # \u534A\
    \u5206\u306E\u9577\u3055\n\n            for start in range(0, self.n, block_size):\n\
    \                mid = min(start + half, self.n)\n                end = min(start\
    \ + block_size, self.n)\n\n                # \u5DE6\u5074 [start, mid) \u306E\u7D2F\
    \u7A4D\u3092\u8A08\u7B97\n                if start < mid:\n                  \
    \  cur = arr[mid - 1]\n                    self.table[k][mid - 1] = cur\n    \
    \                for i in range(mid - 2, start - 1, -1):\n                   \
    \     cur = op(arr[i], cur)\n                        self.table[k][i] = cur\n\n\
    \                # \u53F3\u5074 [mid, end) \u306E\u7D2F\u7A4D\u3092\u8A08\u7B97\
    \n                if mid < end:\n                    cur = arr[mid]\n        \
    \            self.table[k][mid] = cur\n                    for i in range(mid\
    \ + 1, end):\n                        cur = op(cur, arr[i])\n                \
    \        self.table[k][i] = cur\n\n    def query(self, l, r):\n        assert\
    \ 0 <= l < r <= self.n\n        if r - l == 1:\n            return self.arr[l]\n\
    \n        # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\u308B\u305F\u3081\u306B\u4F7F\
    \u3046\u30EC\u30D9\u30EB k \u3092\u6C42\u3081\u308B\n        k = (l ^ (r - 1)).bit_length()\
    \ - 1\n        return self.op(self.table[k][l], self.table[k][r - 1])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/DisjointSparseTable.py
  requiredBy: []
  timestamp: '2025-12-05 18:59:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/DisjointSparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/DisjointSparseTable.py
- /library/algorithm_library/python/data-structure/DisjointSparseTable.py.html
title: algorithm_library/python/data-structure/DisjointSparseTable.py
---
