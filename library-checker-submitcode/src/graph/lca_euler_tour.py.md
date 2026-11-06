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
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/lca\n# include: algorithm_library/python/graph/EulerTour.py\n\
    \n\ndef main():\n    N, Q = map(int, readline().split())\n    tree = EulerTour(N)\n\
    \    for v, parent in enumerate(map(int, readline().split()), 1):\n        tree.add_edge(parent,\
    \ v, 1)\n    tree.build(0, path_sum=False)\n    ans = [0] * Q\n    for i in range(Q):\n\
    \        u, v = map(int, readline().split())\n        ans[i] = tree.lca(u, v)\n\
    \    for i in range(0, Q, 8192):\n        sys.stdout.write(\"\\n\".join(map(str,\
    \ ans[i:i + 8192])) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/lca_euler_tour.py
  requiredBy: []
  timestamp: '2026-10-29 16:19:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/lca_euler_tour.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/lca_euler_tour.py
- /library/library-checker-submitcode/src/graph/lca_euler_tour.py.html
title: library-checker-submitcode/src/graph/lca_euler_tour.py
---
