---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: algorithm_library/python/graph/PotentialUnionFind.py
    title: algorithm_library/python/graph/PotentialUnionFind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential\n\
    \nfrom algorithm_library.python.graph.PotentialUnionFind import PotentialUnionFind\n\
    \nimport sys\ndef input():return sys.stdin.readline().rstrip()\nmod = 998244353\n\
    \nN,Q = map(int,input().split())\nuf = PotentialUnionFind(N)\nfor _ in range(Q):\n\
    \  t,*P = map(int,input().split())\n  if t==0:\n    u,v,x = P\n    res = uf.dist(v,u)\n\
    \    if res!=uf.inf and res%mod!=x:\n      print(0)\n    else:\n      print(1)\n\
    \      uf.union(v,u,x)\n  else:\n    u,v = P\n    res = uf.dist(v,u)\n    if res!=uf.inf:\
    \ print(res%mod)\n    else: print(-1)"
  dependsOn:
  - algorithm_library/python/graph/PotentialUnionFind.py
  isVerificationFile: true
  path: tests/graph/PotentialUnionFind_yosupo.test.py
  requiredBy: []
  timestamp: '2025-05-04 17:49:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/graph/PotentialUnionFind_yosupo.test.py
layout: document
redirect_from:
- /verify/tests/graph/PotentialUnionFind_yosupo.test.py
- /verify/tests/graph/PotentialUnionFind_yosupo.test.py.html
title: tests/graph/PotentialUnionFind_yosupo.test.py
---
