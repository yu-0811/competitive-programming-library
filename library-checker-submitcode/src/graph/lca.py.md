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
  code: "# problem: https://judge.yosupo.jp/problem/lca\n# include: algorithm_library/python/graph/LCA.py\n\
    \n\ndef main():\n    readline = sys.stdin.buffer.readline\n    N, Q = map(int,\
    \ readline().split())\n    edges = ((p, v) for v, p in enumerate(map(int, readline().split()),\
    \ 1))\n    tree = LCA(N, edges)\n    ans = [0] * Q\n    for i in range(Q):\n \
    \       u, v = map(int, readline().split())\n        ans[i] = tree.lca(u, v)\n\
    \    sys.stdout.write(\"\\n\".join(map(str, ans)) + \"\\n\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/lca.py
  requiredBy: []
  timestamp: '2026-10-27 19:55:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/lca.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/lca.py
- /library/library-checker-submitcode/src/graph/lca.py.html
title: library-checker-submitcode/src/graph/lca.py
---
