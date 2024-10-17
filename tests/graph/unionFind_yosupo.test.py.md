---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: algo_library/python/graph/unionFind.py
    title: algo_library/python/graph/unionFind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom algo_library.python.graph.unionFind\
    \ import UnionFind\n\n\ndef main() -> None:\n    N, Q = map(int, input().split())\n\
    \    uft = UnionFind(N)\n    for _ in range(Q):\n        t, u, v = map(int, input().split())\n\
    \        if t == 0:\n            uft.union(u, v)\n        else:\n            print(int(uft.isSame(u,\
    \ v)))\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - algo_library/python/graph/unionFind.py
  isVerificationFile: true
  path: tests/graph/unionFind_yosupo.test.py
  requiredBy: []
  timestamp: '2024-10-17 17:29:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/graph/unionFind_yosupo.test.py
layout: document
redirect_from:
- /verify/tests/graph/unionFind_yosupo.test.py
- /verify/tests/graph/unionFind_yosupo.test.py.html
title: tests/graph/unionFind_yosupo.test.py
---
