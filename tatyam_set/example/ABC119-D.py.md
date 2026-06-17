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
    - https://atcoder.jp/contests/abc119/submissions/46930274
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc119/submissions/46930274\n\n# paste SortedSet\
    \ here\n\nimport sys\ninput = sys.stdin.readline\nINF = 1 << 60\n\nA, B, Q = map(int,\
    \ input().split())\ns = SortedSet([-INF] + [int(input()) for i in range(A)] +\
    \ [INF])\nt = SortedSet([-INF] + [int(input()) for i in range(B)] + [INF])\nfor\
    \ i in range(Q):\n\tx = int(input())\n\ts0 = x - s.le(x)\n\ts1 = s.ge(x) - x\n\
    \tt0 = x - t.le(x)\n\tt1 = t.ge(x) - x\n\tprint(min(max(s0, t0), max(s1, t1),\
    \ s0 + t1 + min(s0, t1), s1 + t0 + min(s1, t0)))\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC119-D.py
  requiredBy: []
  timestamp: '2026-06-17 12:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC119-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC119-D.py
- /library/tatyam_set/example/ABC119-D.py.html
title: tatyam_set/example/ABC119-D.py
---
