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
    - https://atcoder.jp/contests/abc344/editorial/9487
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u53CC\u65B9\u5411\u9023\u7D50\u30EA\u30B9\u30C8 https://atcoder.jp/contests/abc344/editorial/9487\n\
    # \u633F\u5165\u30FB\u524A\u9664 O(1)\n# \u8981\u7D20\u306E\u91CD\u8907\u4E0D\u53EF\
    \n\n\nclass TwoWayList:\n    def __init__(self, L):\n        self.head = -1\n\
    \        self.tail = pow(10, 18)\n        self.L = [self.head] + L + [self.tail]\n\
    \        self.front, self.back = dict(), dict()\n        for i in range(len(self.L)\
    \ - 1):\n            self.back[self.L[i]] = self.L[i + 1]  # x\u306E\u5F8C\u308D\
    \n            self.front[self.L[i + 1]] = self.L[i]  # x\u306E\u524D\n\n    def\
    \ insert_front(self, x, y):  # x\u306E\u524D\u306By\u3092\u633F\u5165\u3059\u308B\
    \n        # \u73FE\u5728 a -> x\n        # a -> y -> x\n        a = self.front[x]\n\
    \        self.back[a] = y\n        self.front[x] = y\n        self.back[y] = x\n\
    \        self.front[y] = a\n\n    def insert_back(self, x, y):  # x\u306E\u76F4\
    \u5F8C\u306By\u3092\u633F\u5165\u3059\u308B\n        # \u73FE\u5728 x -> b\n \
    \       # x -> y -> b\n        b = self.back[x]\n        self.back[x] = y\n  \
    \      self.front[y] = x\n        self.back[y] = b\n        self.front[b] = y\n\
    \n    def del_x(self, x):  # x\u3092\u524A\u9664\u3059\u308B\n        a = self.front[x]\n\
    \        b = self.back[x]\n        self.back[a] = b\n        self.front[b] = a\n\
    \        del self.front[x]\n        del self.back[x]\n\n    def res_LIST(self):\
    \  # \u30EA\u30B9\u30C8\u3092\u8FD4\u3059\n        ans = list()\n        crr =\
    \ self.back[self.head]\n        while crr != self.tail:\n            ans.append(crr)\n\
    \            crr = self.back[crr]\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/TwoWayList.py
  requiredBy: []
  timestamp: '2025-12-05 15:36:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/TwoWayList.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/TwoWayList.py
- /library/algorithm_library/python/data-structure/TwoWayList.py.html
title: algorithm_library/python/data-structure/TwoWayList.py
---
