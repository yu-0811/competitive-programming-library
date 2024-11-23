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
  code: "# 0-index \u3067\u6570\u5217\u3092\u6271\u3046\u3053\u3068\u306B\u6CE8\u610F\
    \n\nclass Mo:\n    def __init__(self, data): # data \u306F\u6570\u5217\n     \
    \   from math import sqrt, ceil\n        self.data = data\n        self.n = len(data)\n\
    \        self.b = ceil(sqrt(self.n))  # bukect\u306E\u30B5\u30A4\u30BA\u53CA\u3073\
    \u500B\u6570\n        # [l,r)\u306E\u534A\u958B\u533A\u9593\u3067\u8003\u3048\u308B\
    \n        self.l = 0\n        self.r = 0\n        # query\u3092\u683C\u7D0D\u3059\
    \u308B\u7528\n        self.bucket = [list() for _ in range((self.b + 1))]\n\n\
    \        ########################################\n        # \u3053\u3053\u306B\
    \u7BA1\u7406\u3057\u305F\u3044\u72B6\u614B\u3092\u521D\u671F\u5316\u3059\u308B\
    \u51E6\u7406\u3092\u66F8\u304F\n\n        ########################################\n\
    \n    def _add(self, i):\n        # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u542B\
    \u3081\u3066\u8003\u3048\u308B\u3068\u304D\u3078states\u3092\u66F4\u65B0\n   \
    \     ########################################\n        pass\n        ########################################\n\
    \n    def _delete(self, i):\n        # i\u756A\u76EE\u306E\u8981\u7D20\u3092\u9664\
    \u3044\u3066\u8003\u3048\u308B\u3068\u304D\u3078states\u3092\u66F4\u65B0\n   \
    \     ########################################\n        pass\n        ########################################\n\
    \n    def _one_process(self, l, r):\n        # \u30AF\u30A8\u30EA[l,r)\u306B\u5BFE\
    \u3057\u3066states\u3092\u66F4\u65B0\u3059\u308B\n        while self.r < r:  #\
    \ r\u307E\u3067\u4F38\u9577\n            self._add(self.r)\n            self.r\
    \ += 1\n        while self.r > r:  # r\u307E\u3067\u77ED\u7E2E\n            self.r\
    \ -= 1\n            self._delete(self.r)\n            \n        while self.l <\
    \ l:  # l\u307E\u3067\u77ED\u7E2E\n            self._delete(self.l)\n        \
    \    self.l += 1\n        while self.l > l:  # l\u307E\u3067\u4F38\u9577\n   \
    \         self.l -= 1\n            self._add(self.l)\n\n    def process(self,\
    \ queries):\n        upper = len(queries)\n        upper_upper = upper * (self.n\
    \ + 1)\n\n        for idx, (l, r) in enumerate(queries):  # query\u3092bucket\u306B\
    \u683C\u7D0D\n            self.bucket[l // self.b].append(idx + l*upper + r*upper_upper)\n\
    \n        for i in range(len(self.bucket)):\n            self.bucket[i].sort()\n\
    \n        ret = [-1] * len(queries)\n        for b in self.bucket:\n         \
    \   for lri in b:  # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\u3066\u3044\u304F\n\
    \                i = lri % upper\n                r = lri // upper_upper\n   \
    \             l = (lri % upper_upper) // upper\n               # \u30AF\u30A8\u30EA\
    [l,r)\u306B\u5BFE\u3057\u3066states\u3092\u66F4\u65B0\u3059\u308B\n          \
    \      while self.r < r:  # r\u307E\u3067\u4F38\u9577\n                    self._add(self.r)\n\
    \                    self.r += 1\n                while self.r > r:  # r\u307E\
    \u3067\u77ED\u7E2E\n                    self.r -= 1\n                    self._delete(self.r)\n\
    \                    \n                while self.l < l:  # l\u307E\u3067\u77ED\
    \u7E2E\n                    self._delete(self.l)\n                    self.l +=\
    \ 1\n                while self.l > l:  # l\u307E\u3067\u4F38\u9577\n        \
    \            self.l -= 1\n                    self._add(self.l)\n            \
    \    \n                ########################################\n            \
    \    # \u30AF\u30A8\u30EA\u306B\u7B54\u3048\u308B\u4F5C\u696D\u3092\u3053\u3053\
    \u3067\u66F8\u304F\n                # ret[i] \u306B i \u756A\u76EE\u306E\u30AF\
    \u30A8\u30EA\u306E\u7B54\u3048\u3092\u683C\u7D0D\u3059\u308B\n               \
    \ ret[i] = self.ans\n                ########################################\n\
    \        return ret"
  dependsOn: []
  isVerificationFile: false
  path: algo_library/python/data-structure/Mos_algorithm.py
  requiredBy: []
  timestamp: '2024-11-23 20:37:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algo_library/python/data-structure/Mos_algorithm.py
layout: document
redirect_from:
- /library/algo_library/python/data-structure/Mos_algorithm.py
- /library/algo_library/python/data-structure/Mos_algorithm.py.html
title: algo_library/python/data-structure/Mos_algorithm.py
---
