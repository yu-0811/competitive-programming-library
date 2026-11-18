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
  code: "# \u5148\u982D k \u6210\u5206\u3060\u3051\u3092\u8F9E\u66F8\u9806\u3067\u6BD4\
    \u8F03\u3059\u308B\u6700\u5C0F\u30D2\u30FC\u30D7\u3002k >= 1\u3001\u5404\u30BF\
    \u30D7\u30EB\u306E\u9577\u3055 >= k\u3002\n# h = TupleHeap(1, [(0, start)])  #\
    \ (\u8DDD\u96E2, \u9802\u70B9) \u3092\u8DDD\u96E2\u3060\u3051\u3067\u6BD4\u8F03\
    \n# h.push((d, v)); d, v = h.pop(); h.top(); len(h)\n# while h: d, v = h.pop()\n\
    # k=2 \u306A\u3089 (\u512A\u5148\u5EA61, \u512A\u5148\u5EA62, \u30C7\u30FC\u30BF\
    , ...) \u306E\u5148\u982D2\u6210\u5206\u3067\u6BD4\u8F03\u3002\n# \u5F8C\u7D9A\
    \u6210\u5206\u306F\u6BD4\u8F03\u3057\u306A\u3044\u3002\u540C\u3058\u30AD\u30FC\
    \u306E\u53D6\u308A\u51FA\u3057\u9806\u306F\u4E0D\u5B9A\u3002\u7A7A\u306E pop/top\
    \ \u306F IndexError\u3002\n\n\nclass TupleHeap:\n    def __init__(s, k=1, values=()):\n\
    \        s.k = k\n        s.q = list(values)\n        s.keys = [x[0] if k == 1\
    \ else x[:k] for x in s.q]\n        for i in range(len(s.q) // 2 - 1, -1, -1):\n\
    \            s._down(i)\n\n    def __len__(s):\n        return len(s.q)\n\n  \
    \  def top(s):\n        return s.q[0]\n\n    def push(s, x):\n        a, q = s.keys,\
    \ s.q\n        key = x[0] if s.k == 1 else x[:s.k]\n        i = len(q)\n     \
    \   a.append(key)\n        q.append(x)\n        while i:\n            p = (i -\
    \ 1) // 2\n            if not key < a[p]:\n                break\n           \
    \ a[i], q[i] = a[p], q[p]\n            i = p\n        a[i], q[i] = key, x\n\n\
    \    def _down(s, i):\n        a, q = s.keys, s.q\n        n = len(q)\n      \
    \  key, x = a[i], q[i]\n        while 2 * i + 1 < n:\n            j = 2 * i +\
    \ 1\n            if j + 1 < n and a[j + 1] < a[j]:\n                j += 1\n \
    \           if not a[j] < key:\n                break\n            a[i], q[i]\
    \ = a[j], q[j]\n            i = j\n        a[i], q[i] = key, x\n\n    def pop(s):\n\
    \        a, q = s.keys, s.q\n        result = q[0]\n        key, x = a.pop(),\
    \ q.pop()\n        if q:\n            a[0], q[0] = key, x\n            s._down(0)\n\
    \        return result\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/TupleHeap.py
  requiredBy: []
  timestamp: '2026-11-18 22:17:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/TupleHeap.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/TupleHeap.py
- /library/algorithm_library/python/data_structure/TupleHeap.py.html
title: algorithm_library/python/data_structure/TupleHeap.py
---
