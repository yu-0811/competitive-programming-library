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
  code: "# \u53CC\u65B9\u5411\u9023\u7D50\u30EA\u30B9\u30C8 \n# \u8981\u7D20\u306F\
    \u30CF\u30C3\u30B7\u30E5\u53EF\u80FD\u30FB\u91CD\u8907\u4E0D\u53EF\u3002\u633F\
    \u5165\u30FB\u524A\u9664\u306F\u5E73\u5747 O(1)\u3002\n\n\nclass TwoWayList:\n\
    \    def __init__(self, L=()):\n        self.head, self.tail = object(), object()\n\
    \        self.front = {self.tail: self.head}\n        self.back = {self.head:\
    \ self.tail}\n        for x in L:\n            self.insert_front(self.tail, x)\n\
    \n    def insert_front(self, x, y):  # \u5024x\u306E\u524D\u306By\u3092\u633F\u5165\
    \u3059\u308B\n        self.insert_back(self.front[x], y)\n\n    def insert_back(self,\
    \ x, y):  # \u5024x\u306E\u76F4\u5F8C\u306By\u3092\u633F\u5165\u3059\u308B\n \
    \       b = self.back[x]\n        self.back[x] = self.front[b] = y\n        self.front[y],\
    \ self.back[y] = x, b\n\n    def del_x(self, x):  # \u5024x\u3092\u524A\u9664\u3059\
    \u308B\n        a, b = self.front.pop(x), self.back.pop(x)\n        self.back[a],\
    \ self.front[b] = b, a\n\n    def res_LIST(self):  # \u30EA\u30B9\u30C8\u3092\u8FD4\
    \u3059\n        ans = []\n        x = self.back[self.head]\n        while x is\
    \ not self.tail:\n            ans.append(x)\n            x = self.back[x]\n  \
    \      return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/TwoWayList.py
  requiredBy: []
  timestamp: '2026-11-15 12:34:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/TwoWayList.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/TwoWayList.py
- /library/algorithm_library/python/data_structure/TwoWayList.py.html
title: algorithm_library/python/data_structure/TwoWayList.py
---
