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
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/vertex_add_path_sum\n# include:\
    \ algorithm_library/python/graph/EulerTour.py\n\n\ndef main():\n    N, Q = map(int,\
    \ readline().split())\n    values = list(map(int, readline().split()))\n    tree\
    \ = EulerTour(N)\n    for _ in range(N - 1):\n        u, v = map(int, readline().split())\n\
    \        tree.add_edge(u, v, -(values[u] + values[v]))\n    # \u30D1\u30B9\u548C\
    \u306F\u6839\u306B\u3088\u3089\u306A\u3044\u306E\u3067\u3001\u9802\u70B9 0 \u4EE5\
    \u5916\u3092\u6839\u306B\u3057\u3066\u3082\u540C\u3058\u3088\u3046\u306B\u6271\
    \u3048\u308B\u3002\n    root = N - 1\n    tree.build(root)\n    bit = tree.fen\n\
    \    ans = []\n    for _ in range(Q):\n        t, u, v = map(int, readline().split())\n\
    \        if t == 0:\n            values[u] += v\n            if u == root:\n \
    \               if N > 1:\n                    bit.add(1, -v)\n            else:\n\
    \                # \u6839\u304B\u3089\u306E\u8DDD\u96E2\u306E\u5897\u5206\u306F\
    \ u \u3067 -v\u3001\u771F\u306E\u5B50\u5B6B\u3067 -2v\u3001\u90E8\u5206\u6728\u5916\
    \u3067 0\u3002\n                l, r = tree._in[u], tree._out[u] + 1\n       \
    \         bit.add(l, -v)\n                bit.add(l + 1, -v)\n               \
    \ bit.add(r, 2 * v)\n        else:\n            # \u8FBA\u91CD\u307F -(a[u]+a[v])\
    \ \u3092\u4F7F\u3044\u3001\u8CA0\u306E\u8FBA\u91CD\u307F\u306B\u3082\u5BFE\u5FDC\
    \u3059\u308B\u3002\n            ans.append((-tree.get_distance(u, v) + values[u]\
    \ + values[v]) // 2)\n    for i in range(0, len(ans), 8192):\n        sys.stdout.write(\"\
    \\n\".join(map(str, ans[i:i + 8192])) + \"\\n\")\n\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/vertex_add_path_sum_euler_tour.py
  requiredBy: []
  timestamp: '2026-10-29 16:19:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/vertex_add_path_sum_euler_tour.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/vertex_add_path_sum_euler_tour.py
- /library/library-checker-submitcode/src/graph/vertex_add_path_sum_euler_tour.py.html
title: library-checker-submitcode/src/graph/vertex_add_path_sum_euler_tour.py
---
