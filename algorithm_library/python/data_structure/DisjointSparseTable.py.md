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
  code: "class DisjointSparseTable:\n    def __init__(s, arr, op):\n        \"\"\"\
    \n        arr: \u914D\u5217\n        op: \u6F14\u7B97 (\u7D50\u5408\u5F8B\u3092\
    \u6E80\u305F\u3059\u3053\u3068)\n        \"\"\"\n        s.n = n = len(arr)\n\
    \        s.arr = arr[:]\n        s.op = op\n\n        s.max_k = n.bit_length()\n\
    \        s.table = [[0] * n for _ in range(s.max_k)]\n\n        for k in range(s.max_k):\n\
    \            half = 1 << k\n            row = s.table[k]\n            for start\
    \ in range(0, n, 2 * half):\n                mid = min(start + half, n)\n    \
    \            end = min(start + 2 * half, n)\n                # \u5DE6\u534A\u5206\
    \u306E\u63A5\u5C3E\u8F9E\u3068\u53F3\u534A\u5206\u306E\u63A5\u982D\u8F9E\u3092\
    \u3001\u9806\u5E8F\u3092\u4FDD\u3063\u3066\u7D2F\u7A4D\u3059\u308B\u3002\n   \
    \             cur = row[mid - 1] = arr[mid - 1]\n                for i in range(mid\
    \ - 2, start - 1, -1):\n                    cur = op(arr[i], cur)\n          \
    \          row[i] = cur\n                if mid < end:\n                    cur\
    \ = row[mid] = arr[mid]\n                    for i in range(mid + 1, end):\n \
    \                       cur = op(cur, arr[i])\n                        row[i]\
    \ = cur\n\n    def query(s, l, r):\n        assert 0 <= l < r <= s.n\n       \
    \ if r - l == 1:\n            return s.arr[l]\n\n        # \u30AF\u30A8\u30EA\u306B\
    \u7B54\u3048\u308B\u305F\u3081\u306B\u4F7F\u3046\u30EC\u30D9\u30EB k \u3092\u6C42\
    \u3081\u308B\n        k = (l ^ (r - 1)).bit_length() - 1\n        row = s.table[k]\n\
    \        return s.op(row[l], row[r - 1])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/DisjointSparseTable.py
  requiredBy: []
  timestamp: '2026-11-08 11:01:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/DisjointSparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/DisjointSparseTable.py
- /library/algorithm_library/python/data_structure/DisjointSparseTable.py.html
title: algorithm_library/python/data_structure/DisjointSparseTable.py
---
