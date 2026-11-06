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
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n# include:\
    \ algorithm_library/python/graph/VertexAddSubtreeSum.py\n\n\ndef main():\n   \
    \ n, q = map(int, readline().split())\n    # \u5024\u3068\u30AF\u30A8\u30EA\u306F\
    \u975E\u8CA0\u6574\u6570\u306A\u306E\u3067\u3001split \u3067\u5C0F\u3055\u306A\
    \ bytes \u3092\u5927\u91CF\u306B\u4F5C\u3089\u305A\u8AAD\u3080\u3002\n    data\
    \ = sys.stdin.buffer.read()\n    i = 0\n    values = [0] * n\n    for v in range(n):\n\
    \        x = 0\n        c = data[i]\n        while c >= 48:\n            x = x\
    \ * 10 + c - 48\n            i += 1\n            c = data[i]\n        i += 1\n\
    \        values[v] = x\n    parents = [-1] * n\n    for v in range(1, n):\n  \
    \      x = 0\n        c = data[i]\n        while c >= 48:\n            x = x *\
    \ 10 + c - 48\n            i += 1\n            c = data[i]\n        i += 1\n \
    \       parents[v] = x\n    if n == 1:\n        i += 1  # N = 1 \u306E\u3068\u304D\
    \u306E\u7A7A\u306E\u89AA\u914D\u5217\u306E\u884C\n    tree = VertexAddSubtreeSum(parents,\
    \ values)\n    add = tree.add\n    subtree_sum = tree.subtree_sum\n    ans = []\n\
    \    for _ in range(q):\n        t = data[i]\n        i += 2\n        v = 0\n\
    \        c = data[i]\n        while c >= 48:\n            v = v * 10 + c - 48\n\
    \            i += 1\n            c = data[i]\n        i += 1\n        if t ==\
    \ 48:\n            x = 0\n            c = data[i]\n            while c >= 48:\n\
    \                x = x * 10 + c - 48\n                i += 1\n               \
    \ c = data[i]\n            i += 1\n            add(v, x)\n        else:\n    \
    \        ans.append(subtree_sum(v))\n    # \u56DE\u7B54\u306F\u6574\u6570\u306E\
    \u307E\u307E\u6301\u3061\u3001\u6587\u5B57\u5217\u5316\u306E\u4E00\u6642\u9818\
    \u57DF\u3092\u5C0F\u3055\u304F\u4FDD\u3064\u3002\n    for i in range(0, len(ans),\
    \ 8192):\n        sys.stdout.write(\"\\n\".join(map(str, ans[i:i + 8192])) + \"\
    \\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/vertex_add_subtree_sum.py
  requiredBy: []
  timestamp: '2026-10-29 16:19:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/vertex_add_subtree_sum.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/vertex_add_subtree_sum.py
- /library/library-checker-submitcode/src/graph/vertex_add_subtree_sum.py.html
title: library-checker-submitcode/src/graph/vertex_add_subtree_sum.py
---
