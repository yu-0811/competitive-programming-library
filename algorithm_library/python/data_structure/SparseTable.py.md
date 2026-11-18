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
  code: "class SparseTable:\n    def __init__(s, arr, op):\n        \"\"\"\n     \
    \   arr: \u914D\u5217\n        op: \u6F14\u7B97 (\u7D50\u5408\u5247\u3001\u51AA\
    \u7B49\u5247\u3092\u6E80\u305F\u3059\u3053\u3068)\n        \u6642\u9593\u8A08\u7B97\
    \u91CF: O(n log n) \u69CB\u7BC9, O(1) \u30AF\u30A8\u30EA\n        \"\"\"\n   \
    \     s.op = op\n        s.n = n = len(arr)\n        # table[k][i] = i \u304B\u3089\
    \u9577\u3055 2^k \u306E\u533A\u9593\u306B\u5BFE\u3059\u308B\u6F14\u7B97\u7D50\u679C\
    \n        s.tab = tab = [arr[:]]\n\n        for k in range(n.bit_length() - 1):\n\
    \            prev = tab[-1]\n            row = prev[1 << k :]\n            for\
    \ i in range(len(row)):\n                row[i] = op(prev[i], row[i])\n      \
    \      tab.append(row)\n\n    def query(s, l, r):\n        assert 0 <= l < r <=\
    \ s.n\n        # 2^k <= r - l \u3092\u6E80\u305F\u3059\u6700\u5927\u306E k \u3092\
    \u6C42\u3081\u308B\n        k = (r - l).bit_length() - 1\n        # [l, l + 2^k)\
    \ \u3068 [r - 2^k, r) \u306E\u533A\u9593\u306B\u5206\u5272\u3057\u3066\u8A08\u7B97\
    \n        return s.op(s.tab[k][l], s.tab[k][r - (1 << k)])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/SparseTable.py
  requiredBy: []
  timestamp: '2026-11-17 18:24:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/SparseTable.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/SparseTable.py
- /library/algorithm_library/python/data_structure/SparseTable.py.html
title: algorithm_library/python/data_structure/SparseTable.py
---
