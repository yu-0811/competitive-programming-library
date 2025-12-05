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
  code: "from warnings import warn\n\n\nclass segtree:  # \u3059\u3079\u3066 0-index\n\
    \    def __init__(self, V, OP, E):\n        self.n = len(V)\n        self.op =\
    \ OP\n        self.e = E\n        self.log = (self.n - 1).bit_length()\n     \
    \   self.size = 1 << self.log\n        self.data = [E for i in range(2 * self.size)]\n\
    \        for i in range(self.n):\n            self.data[self.size + i] = V[i]\n\
    \        for i in range(self.size - 1, 0, -1):\n            self._update(i)\n\n\
    \    # 1 \u70B9\u66F4\u65B0\n    def set(self, p, x):\n        assert 0 <= p and\
    \ p < self.n\n        p += self.size\n        self.data[p] = x\n        for i\
    \ in range(1, self.log + 1):\n            self._update(p >> i)\n\n    # 1 \u70B9\
    \u52A0\u7B97\n    def add(self, p, x):\n        assert 0 <= p and p < self.n\n\
    \        p += self.size\n        self.data[p] += x\n        for i in range(1,\
    \ self.log + 1):\n            self._update(p >> i)\n\n    # \u5143\u306E\u914D\
    \u5217\u306E p \u756A\u76EE\u306E\u8981\u7D20\u3092\u53D6\u5F97\n    def get(self,\
    \ p):\n        assert 0 <= p and p < self.n\n        return self.data[p + self.size]\n\
    \n    # [l,r) \u306E\u6F14\u7B97\u7D50\u679C\u3092\u8FD4\u3059\n    def prod(self,\
    \ l, r):\n        assert 0 <= l and l <= r and r <= self.n\n        if l == r:\n\
    \            warn(\"l=r in prod(l,r)\")\n            return self.e\n        sml\
    \ = self.e\n        smr = self.e\n        l += self.size\n        r += self.size\n\
    \        while l < r:\n            if l & 1:\n                sml = self.op(sml,\
    \ self.data[l])\n                l += 1\n            if r & 1:\n             \
    \   smr = self.op(self.data[r - 1], smr)\n                r -= 1\n           \
    \ l >>= 1\n            r >>= 1\n        return self.op(sml, smr)\n\n    # \u5168\
    \u533A\u9593\u306E\u6F14\u7B97\u7D50\u679C\u3092\u8FD4\u3059\n    def all_prod(self):\n\
    \        return self.data[1]\n\n    # check(operate(data[l],data[l+1],...,data[r-1]))\
    \ = True\n    # \u3092\u6E80\u305F\u3059\u6700\u5927\u306E r \u3092\u8FD4\u3059\
    \n    def max_right(self, l, check):\n        assert 0 <= l and l <= self.n\n\
    \        assert check(self.e)\n        if l == self.n:\n            return self.n\n\
    \        l += self.size\n        sm = self.e\n        while True:\n          \
    \  while l % 2 == 0:\n                l >>= 1\n            if not (check(self.op(sm,\
    \ self.data[l]))):\n                while l < self.size:\n                   \
    \ l = 2 * l\n                    if check(self.op(sm, self.data[l])):\n      \
    \                  sm = self.op(sm, self.data[l])\n                        l +=\
    \ 1\n                return l - self.size\n            sm = self.op(sm, self.data[l])\n\
    \            l += 1\n            if (l & -l) == l:\n                break\n  \
    \      return self.n\n\n    # check(operate(data[l],data[l+1],...,data[r-1]))\
    \ = True\n    # \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E l \u3092\u8FD4\u3059\
    \n    def min_left(self, r, check):\n        assert 0 <= r and r <= self.n\n \
    \       assert check(self.e)\n        if r == 0:\n            return 0\n     \
    \   r += self.size\n        sm = self.e\n        while True:\n            r -=\
    \ 1\n            while r > 1 and (r % 2):\n                r >>= 1\n         \
    \   if not (check(self.op(self.data[r], sm))):\n                while r < self.size:\n\
    \                    r = 2 * r + 1\n                    if check(self.op(self.data[r],\
    \ sm)):\n                        sm = self.op(self.data[r], sm)\n            \
    \            r -= 1\n                return r + 1 - self.size\n            sm\
    \ = self.op(self.data[r], sm)\n            if (r & -r) == r:\n               \
    \ break\n        return 0\n\n    def _update(self, k):\n        self.data[k] =\
    \ self.op(self.data[2 * k], self.data[2 * k + 1])\n\n    def __str__(self):\n\
    \        return str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/Segtree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/Segtree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/Segtree.py
- /library/algorithm_library/python/data-structure/Segtree.py.html
title: algorithm_library/python/data-structure/Segtree.py
---
