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
  code: "from bisect import bisect_right\n\nclass MergeSortTree:\n    def __init__(self,\
    \ data):\n        self.n = len(data)\n        self.size = 1 << self.n.bit_length()\n\
    \        self.tree = [[] for _ in range(2 * self.size)]\n        self._build(data)\n\
    \n    def _build(self, data):\n        for i in range(self.n):\n            self.tree[self.size\
    \ + i] = [data[i]]\n        # \u5B50\u30CE\u30FC\u30C9\u306E\u8981\u7D20\u3092\
    \u30BD\u30FC\u30C8\u3057\u3066\u3059\u3079\u3066\u6301\u3064\u3088\u3046\u306B\
    \u69CB\u7BC9\n        for i in range(self.size - 1, 0, -1):\n           # \u30DE\
    \u30FC\u30B8\u30BD\u30FC\u30C8\u306E\u8981\u9818\u3067\u30DE\u30FC\u30B8\n   \
    \         left_child = self.tree[2 * i]\n            right_child = self.tree[2\
    \ * i + 1]\n            l,r = 0,0\n            while l < len(left_child) and r\
    \ < len(right_child):\n                if left_child[l] < right_child[r]:\n  \
    \                  self.tree[i].append(left_child[l])\n                    l +=\
    \ 1\n                else:\n                    self.tree[i].append(right_child[r])\n\
    \                    r += 1\n            while l < len(left_child):\n        \
    \        self.tree[i].append(left_child[l])\n                l += 1\n        \
    \    while r < len(right_child):\n                self.tree[i].append(right_child[r])\n\
    \                r += 1\n            \n    # \u533A\u9593 [l, r) \u3067\u5024\u304C\
    \ x \u4EE5\u4E0B\u306E\u8981\u7D20\u6570\u3092\u6C42\u3081\u308B\n    def query(self,\
    \ l, r, x):\n        l += self.size \n        r += self.size \n        res = 0\n\
    \        while l < r:\n            if (l&1):\n                res += self._count_less_equal(self.tree[l],\
    \ x)\n                l += 1\n            if (r&1):\n                res += self._count_less_equal(self.tree[r-1],\
    \ x)\n                r -= 1\n            l >>= 1\n            r >>= 1\n     \
    \   return res\n\n    def _count_less_equal(self,array, x):\n        return bisect_right(array,\
    \ x)"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/data-structure/MargeSortTree.py
  requiredBy: []
  timestamp: '2024-11-10 12:05:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/data-structure/MargeSortTree.py
layout: document
redirect_from:
- /library/algo_library/python/data-structure/MargeSortTree.py
- /library/algo_library/python/data-structure/MargeSortTree.py.html
title: algo_library/python/data-structure/MargeSortTree.py
---
