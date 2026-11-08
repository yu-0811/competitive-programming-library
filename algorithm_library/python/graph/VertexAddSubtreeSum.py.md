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
  code: "class VertexAddSubtreeSum:\n    \"\"\"\u89AA\u756A\u53F7\u304C\u5B50\u756A\
    \u53F7\u3088\u308A\u5C0F\u3055\u3044\u6839\u4ED8\u304D\u6728\u306E\u9802\u70B9\
    \u52A0\u7B97\u30FB\u90E8\u5206\u6728\u548C\u3002\n\n    parents[0] = -1, 0 <=\
    \ parents[v] < v \u3068\u3059\u308B\u3002\n    \u69CB\u7BC9 O(N)\u3001\u7A7A\u9593\
    \ O(N)\u3002\u9AD8\u3055\u304C 2 * N.bit_length() \u4EE5\u4E0B\u306A\u3089\u7956\
    \u5148\u306E\u548C\u3092\u76F4\u63A5\u66F4\u65B0\u3057\u3001\n    \u305D\u308C\
    \u4EE5\u5916\u306F\u5E30\u308A\u304C\u3051\u9806\u306E\u90E8\u5206\u6728\u533A\
    \u9593\u3068 Fenwick Tree \u3092\u4F7F\u3046\u3002\n    \"\"\"\n\n    def __init__(s,\
    \ parents, values):\n        n = s.n = len(parents)\n        s.parents = parents\n\
    \        sums = s.sums = list(values)\n        depth = [0] * n\n        for v\
    \ in range(1, n):\n            depth[v] = depth[parents[v]] + 1\n        s.shallow\
    \ = max(depth) <= 2 * n.bit_length()\n        if s.shallow:\n            for v\
    \ in range(n - 1, 0, -1):\n                sums[parents[v]] += sums[v]\n     \
    \   else:\n            size = s.size = [1] * n\n            for v in range(n -\
    \ 1, 0, -1):\n                p = parents[v]\n                sums[p] += sums[v]\n\
    \                size[p] += size[v]\n            # end[v] \u306F\u5E30\u308A\u304C\
    \u3051\u9806\u3067\u306E v \u306E\u4F4D\u7F6E + 1\u3002\n            # \u5B50\u306E\
    \u533A\u9593\u3092\u89AA\u306E\u624B\u524D\u306B\u7F6E\u304F\u3002\u96A3\u63A5\
    \u30EA\u30B9\u30C8\u3084 DFS \u306F\u4E0D\u8981\u3002\n            end = s.end\
    \ = [1] * n\n            for v in range(1, n):\n                p = parents[v]\n\
    \                end[v] = end[p]\n                end[p] += size[v]\n        \
    \    # \u521D\u671F\u5024\u306F sums \u306B\u6301\u3061\u3001BIT \u306B\u306F\u69CB\
    \u7BC9\u5F8C\u306E\u52A0\u7B97\u3060\u3051\u3092\u8F09\u305B\u308B\u3002\n   \
    \         s.bit = [0] * (n + 1)\n\n    def add(s, v, x):\n        \"\"\"\u9802\
    \u70B9 v \u306B x \u3092\u52A0\u7B97\u3002O(log N)\u3002\"\"\"\n        if s.shallow:\n\
    \            sums = s.sums\n            parents = s.parents\n            while\
    \ v >= 0:\n                sums[v] += x\n                v = parents[v]\n    \
    \    else:\n            bit = s.bit\n            n = s.n\n            v = s.end[v]\n\
    \            while v <= n:\n                bit[v] += x\n                v +=\
    \ v & -v\n\n    def subtree_sum(s, v):\n        \"\"\"v \u3092\u6839\u3068\u3059\
    \u308B\u90E8\u5206\u6728\u306E\u548C\u3002O(1)\u3001\u6DF1\u3044\u6728\u3067\u306F\
    \ O(log N)\u3002\"\"\"\n        total = s.sums[v]\n        if not s.shallow:\n\
    \            bit = s.bit\n            r = s.end[v]\n            l = r - s.size[v]\n\
    \            # \u5171\u901A\u3059\u308B\u7D2F\u7A4D\u548C\u306E\u9805\u306F\u76F8\
    \u6BBA\u3055\u308C\u308B\u306E\u3067\u8AAD\u307E\u306A\u3044\u3002\n         \
    \   while l != r:\n                if l < r:\n                    total += bit[r]\n\
    \                    r &= r - 1\n                else:\n                    total\
    \ -= bit[l]\n                    l &= l - 1\n        return total\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/graph/VertexAddSubtreeSum.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/graph/VertexAddSubtreeSum.py
layout: document
redirect_from:
- /library/algorithm_library/python/graph/VertexAddSubtreeSum.py
- /library/algorithm_library/python/graph/VertexAddSubtreeSum.py.html
title: algorithm_library/python/graph/VertexAddSubtreeSum.py
---
