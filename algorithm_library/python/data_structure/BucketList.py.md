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
  code: "# \u4EFB\u610F\u306E\u5834\u6240\u306B\u633F\u5165\u3057\u305F\u308A\u524A\
    \u9664\u3068\u304B\u304C\u3067\u304D\u308B\nimport math\n\n\nclass BucketList:\n\
    \    br = 16\n    sr = 24\n\n    def __init__(s, a=[]):\n        a = list(a)\n\
    \        n = s.size = len(a)\n        k = math.ceil(math.sqrt(n / s.br))\n   \
    \     s.a = [\n            a[n * i // k : n * (i + 1) // k]\n            for i\
    \ in range(k)\n        ]\n\n    def __iter__(s):\n        for a in s.a:\n    \
    \        yield from a\n\n    def __contains__(s, x):\n        \"x \u304C\u542B\
    \u307E\u308C\u3066\u3044\u308C\u3070 True \u3092\u8FD4\u3059\u3002 / O(N)\"\n\
    \        for y in s:\n            if x == y:\n                return True\n  \
    \      return False\n\n    def _insert(s, a, b, i, x):\n        a.insert(i, x)\n\
    \        s.size += 1\n        if len(a) > len(s.a) * s.sr:\n            mid =\
    \ len(a) >> 1\n            s.a[b : b + 1] = [a[:mid], a[mid:]]\n\n    def insert(s,\
    \ i, x):\n        \"i \u756A\u76EE\u306E\u4F4D\u7F6E\u306B x \u3092\u633F\u5165\
    \u3059\u308B\u3002 / O(\u221AN)\"\n        if s.size == 0:\n            if i !=\
    \ 0 and i != -1:\n                raise IndexError\n            s.a = [[x]]\n\
    \            s.size = 1\n            return\n        if i < 0:\n            for\
    \ b, a in enumerate(reversed(s.a)):\n                i += len(a)\n           \
    \     if i >= 0:\n                    return s._insert(a, len(s.a) + ~b, i, x)\n\
    \        else:\n            for b, a in enumerate(s.a):\n                if i\
    \ <= len(a):\n                    return s._insert(a, b, i, x)\n             \
    \   i -= len(a)\n        raise IndexError\n\n    def append(s, x):\n        \"\
    \u672B\u5C3E\u306B x \u3092\u8FFD\u52A0\u3059\u308B\u3002 / \u511F\u5374 O(1)\"\
    \n        if s.size == 0:\n            s.a = [[x]]\n            s.size = 1\n \
    \           return\n        a = s.a[-1]\n        return s._insert(a, len(s.a)\
    \ - 1, len(a), x)\n\n    def extend(s, a):\n        for x in a:\n            s.append(x)\n\
    \n    def __getitem__(s, i):\n        if i < 0:\n            for a in reversed(s.a):\n\
    \                i += len(a)\n                if i >= 0:\n                   \
    \ return a[i]\n        else:\n            for a in s.a:\n                if i\
    \ < len(a):\n                    return a[i]\n                i -= len(a)\n  \
    \      raise IndexError\n\n    def _pop(s, a, b, i):\n        ans = a.pop(i)\n\
    \        s.size -= 1\n        if not a:\n            del s.a[b]\n        return\
    \ ans\n\n    def pop(s, i=-1):\n        \"i \u756A\u76EE\u306E\u8981\u7D20\u3092\
    \u524A\u9664\u3057\u3066\u8FD4\u3059\u3002 / O(\u221AN) / i < 0 \u306A\u3089 O(-i)\"\
    \n        if i < 0:\n            for b, a in enumerate(reversed(s.a)):\n     \
    \           i += len(a)\n                if i >= 0:\n                    return\
    \ s._pop(a, ~b, i)\n        else:\n            for b, a in enumerate(s.a):\n \
    \               if i < len(a):\n                    return s._pop(a, b, i)\n \
    \               i -= len(a)\n        raise IndexError\n\n    def count(s, x):\n\
    \        \"x \u306E\u51FA\u73FE\u56DE\u6570\u3092\u8FD4\u3059\u3002 / O(N)\"\n\
    \        return sum(1 for y in s if x == y)\n\n    def index(s, x):\n        \"\
    \u6700\u521D\u306B\u73FE\u308C\u308B x \u306E\u6DFB\u5B57\u3092\u8FD4\u3059\u3002\
    \u898B\u3064\u304B\u3089\u306A\u3051\u308C\u3070 ValueError \u3092\u9001\u51FA\
    \u3059\u308B\u3002 / O(N)\"\n        for i, y in enumerate(s):\n            if\
    \ x == y:\n                return i\n        raise ValueError\n\n    def remove(s,\
    \ x):\n        \"\u6700\u521D\u306B\u73FE\u308C\u308B x \u3092\u524A\u9664\u3059\
    \u308B\u3002\u898B\u3064\u304B\u3089\u306A\u3051\u308C\u3070 ValueError \u3092\
    \u9001\u51FA\u3059\u308B\u3002 / O(N)\"\n        s.pop(s.index(x))\n\n    def\
    \ clear(s):\n        s.a = []\n        s.size = 0\n\n    def reverse(s):\n   \
    \     s.a.reverse()\n        for a in s.a:\n            a.reverse()\n\n    def\
    \ copy(s):\n        return BucketList(s)\n\n    def __len__(s):\n        return\
    \ s.size\n\n    def __str__(s):\n        return str(list(s))\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data_structure/BucketList.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data_structure/BucketList.py
layout: document
redirect_from:
- /library/algorithm_library/python/data_structure/BucketList.py
- /library/algorithm_library/python/data_structure/BucketList.py.html
title: algorithm_library/python/data_structure/BucketList.py
---
