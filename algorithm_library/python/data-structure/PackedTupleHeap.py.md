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
  code: "\"\"\"\nPackedTupleHeap(arity=2, bits=20, values=None): \u6574\u6570\u30BF\
    \u30D7\u30EB\u306E\u8F9E\u66F8\u9806\u6700\u5C0F\u30D2\u30FC\u30D7\u3002\narity:\
    \ \u30BF\u30D7\u30EB\u306E\u9577\u3055\nvalues: list[tuple[int, ...]]\uFF08\u4F8B\
    : [(1, 2, 3)]\uFF09\u3002\u7701\u7565\u6642\u306E None \u306F\u7A7A\u3002\nbits:\
    \ \u7B2C2\u6210\u5206\u4EE5\u964D\u306E\u7BC4\u56F2\u3092\u8868\u3059 int \u307E\
    \u305F\u306F\u6574\u6570\u306E\u5217\u30023\u8981\u7D20 (a, b, c) \u306E\u5834\
    \u5408:\n  bits=8       \u2192 b, c \u306F\u5404 0\uFF5E255\u3002\n  bits=(8,\
    \ 12) \u2192 b \u306F 0\uFF5E255\u3001c \u306F 0\uFF5E4095\u3002\n\u5148\u982D\
    \u306E a \u306F\u6307\u5B9A\u3057\u306A\u3044\u3001\u8CA0\u6570\u3082\u53EF\u3002\
    \u5404\u6210\u5206\u306E\u6700\u5927\u5024\u304C M\uFF080\u4EE5\u4E0A\uFF09\u306A\
    \u3089\u3001\u5FC5\u8981\u306A\u30D3\u30C3\u30C8\u6570\u306F M.bit_length()\u3002\
    \nh = PackedTupleHeap(3, bits=(8, 12), values=[(-1, 2, 3)])\nh.push((0, 4, 5))\
    \     # \u8FFD\u52A0\u3002\u6E21\u3059\u30BF\u30D7\u30EB\u306E\u9577\u3055\u306F\
    \u5E38\u306B arity\nh.top(); h.pop()      # \u6700\u5C0F\u5024\u306E\u53C2\u7167\
    \ / \u53D6\u308A\u51FA\u3057\uFF08\u7A7A\u306A\u3089 IndexError\uFF09\nlen(h);\
    \ bool(h)       # \u8981\u7D20\u6570 / \u975E\u7A7A\u304B\nwhile h: print(h.pop())\
    \  # \u7A7A\u306B\u306A\u308B\u307E\u3067\u53D6\u308A\u51FA\u3059\n\"\"\"\n\n\
    from heapq import heapify, heappop, heappush\n\n\nclass PackedTupleHeap:\n   \
    \ def __init__(\n        s,\n        arity: int = 2,\n        bits: int | list[int]\
    \ = 20,\n        values: list[tuple[int, ...]] | None = None,\n    ) -> None:\n\
    \        s.bits = (bits,) * (arity - 1) if isinstance(bits, int) else tuple(bits)\n\
    \        s.q = [s._pack(x) for x in values or ()]\n        heapify(s.q)\n\n  \
    \  def __len__(s):\n        return len(s.q)\n\n    def _pack(s, x):\n        x\
    \ = tuple(x)\n        v = x[0]\n        for a, b in zip(x[1:], s.bits):\n    \
    \        v = (v << b) | a\n        return v\n\n    def _unpack(s, v):\n      \
    \  x = []\n        for b in reversed(s.bits):\n            x.append(v & ((1 <<\
    \ b) - 1))\n            v >>= b\n        return (v, *reversed(x))\n\n    def top(s):\n\
    \        return s._unpack(s.q[0])\n\n    def push(s, x):\n        heappush(s.q,\
    \ s._pack(x))\n\n    def pop(s):\n        return s._unpack(heappop(s.q))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/PackedTupleHeap.py
  requiredBy: []
  timestamp: '2026-10-25 23:05:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/PackedTupleHeap.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/PackedTupleHeap.py
- /library/algorithm_library/python/data-structure/PackedTupleHeap.py.html
title: algorithm_library/python/data-structure/PackedTupleHeap.py
---
