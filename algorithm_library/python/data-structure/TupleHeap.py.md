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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"2 \u8981\u7D20\u30BF\u30D7\u30EB\u7528\u30D2\u30FC\u30D7\u3002\u8AAC\
    \u660E: documents/algo_library/data_structure/TupleHeap.md\"\"\"\n\nfrom heapq\
    \ import heapify, heappop, heappush, heappushpop, heapreplace\n\n\nclass TupleHeap:\n\
    \    \"\"\"\u6210\u5206\u3092\u5225\u3005\u306E\u30EA\u30B9\u30C8\u306B\u4FDD\u5B58\
    \u3059\u308B\u3002\u6210\u5206\u306F\u5168\u9806\u5E8F\u3092\u6301\u3064\u5024\
    \u3092\u4F7F\u3046\u3002\"\"\"\n\n    __slots__ = (\"_a\", \"_b\")\n\n    def\
    \ __init__(self, values=()):\n        a, b = self._a, self._b = [], []\n     \
    \   for x, y in values:\n            a.append(x)\n            b.append(y)\n  \
    \      for pos in range(len(a) // 2 - 1, -1, -1):\n            self._sift_down(pos,\
    \ a[pos], b[pos])\n\n    def __len__(self):\n        return len(self._a)\n\n \
    \   def peek(self):\n        return self._a[0], self._b[0]\n\n    def push(self,\
    \ item):\n        x, y = item\n        a, b = self._a, self._b\n        pos =\
    \ len(a)\n        a.append(x)\n        b.append(y)\n        while pos:\n     \
    \       parent = (pos - 1) >> 1\n            u, v = a[parent], b[parent]\n   \
    \         if not (x < u or (x == u and y < v)):\n                break\n     \
    \       a[pos], b[pos] = u, v\n            pos = parent\n        a[pos], b[pos]\
    \ = x, y\n\n    def pop(self):\n        a, b = self._a, self._b\n        result\
    \ = a[0], b[0]\n        x, y = a.pop(), b.pop()\n        if a:\n            self._sift_down(0,\
    \ x, y)\n        return result\n\n    def replace(self, item):\n        \"\"\"\
    \u6700\u5C0F\u5024\u3092\u53D6\u308A\u51FA\u3057\u3066 item \u3092\u633F\u5165\
    \u3059\u308B\u3002\u7A7A\u306A\u3089 IndexError\u3002\"\"\"\n        x, y = item\n\
    \        result = self.peek()\n        self._sift_down(0, x, y)\n        return\
    \ result\n\n    def pushpop(self, item):\n        \"\"\"\u633F\u5165\u3057\u3066\
    \u6700\u5C0F\u5024\u3092\u53D6\u308A\u51FA\u3059\u3002\u7A7A\u306A\u3089 item\
    \ \u306E\u5024\u3092\u8FD4\u3059\u3002\"\"\"\n        x, y = item\n        a,\
    \ b = self._a, self._b\n        if a and (a[0] < x or (a[0] == x and b[0] < y)):\n\
    \            result = a[0], b[0]\n            self._sift_down(0, x, y)\n     \
    \       return result\n        return x, y\n\n    def _sift_down(self, pos, x,\
    \ y):\n        a, b = self._a, self._b\n        n = len(a)\n        start = pos\n\
    \        child = 2 * pos + 1\n        # \u5C0F\u3055\u3044\u65B9\u306E\u5B50\u3092\
    \u8449\u307E\u3067\u5F15\u304D\u4E0A\u3052\u3001\u7A7A\u3044\u305F\u4F4D\u7F6E\
    \u304B\u3089 x, y \u3092\u623B\u3059\u3002\n        while child < n:\n       \
    \     right = child + 1\n            u, v = a[child], b[child]\n            if\
    \ right < n:\n                r, s = a[right], b[right]\n                if r\
    \ < u or (r == u and s < v):\n                    child = right\n            \
    \        u, v = r, s\n            a[pos], b[pos] = u, v\n            pos = child\n\
    \            child = 2 * pos + 1\n        while pos > start:\n            parent\
    \ = (pos - 1) >> 1\n            u, v = a[parent], b[parent]\n            if not\
    \ (x < u or (x == u and y < v)):\n                break\n            a[pos], b[pos]\
    \ = u, v\n            pos = parent\n        a[pos], b[pos] = x, y\n\n\nclass PackedTupleHeap:\n\
    \    \"\"\"(\u6574\u6570 key, 0 <= value < 2**bits \u306E\u6574\u6570) \u3092\
    \ 1 \u6574\u6570\u306B\u7B26\u53F7\u5316\u3059\u308B\u3002\"\"\"\n\n    __slots__\
    \ = (\"_heap\", \"_bits\", \"_mask\")\n\n    def __init__(self, values=(), bits=20):\n\
    \        if not isinstance(bits, int) or bits < 0:\n            raise ValueError(\"\
    bits must be a nonnegative integer\")\n        self._bits = bits\n        self._mask\
    \ = (1 << bits) - 1\n        self._heap = [self._pack(item) for item in values]\n\
    \        heapify(self._heap)\n\n    def _pack(self, item):\n        x, y = item\n\
    \        if not 0 <= y <= self._mask:\n            raise ValueError(\"second component\
    \ must satisfy 0 <= value < 2**bits\")\n        return (x << self._bits) | y\n\
    \n    def _unpack(self, value):\n        return value >> self._bits, value & self._mask\n\
    \n    def __len__(self):\n        return len(self._heap)\n\n    def peek(self):\n\
    \        return self._unpack(self._heap[0])\n\n    def push(self, item):\n   \
    \     heappush(self._heap, self._pack(item))\n\n    def pop(self):\n        return\
    \ self._unpack(heappop(self._heap))\n\n    def replace(self, item):\n        return\
    \ self._unpack(heapreplace(self._heap, self._pack(item)))\n\n    def pushpop(self,\
    \ item):\n        return self._unpack(heappushpop(self._heap, self._pack(item)))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/TupleHeap.py
  requiredBy: []
  timestamp: '2026-10-25 21:47:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/TupleHeap.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/TupleHeap.py
- /library/algorithm_library/python/data-structure/TupleHeap.py.html
title: algorithm_library/python/data-structure/TupleHeap.py
---
