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
    - https://atcoder.jp/contests/abc228/submissions/46930446
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc228/submissions/46930446\n\n# paste SortedSet\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nN = 1 << 20\nA = [-1] * N\n\
    Q = int(input())\nmask = N - 1\ns = SortedSet(range(N))\n\nfor i in range(Q):\n\
    \    t, x = map(int, input().split())\n    if t == 1:\n        y = s.ge(x & mask)\n\
    \        if y is None:\n            y = s[0]\n        A[y] = x\n        s.discard(y)\n\
    \    else:\n        print(A[x & mask])\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC228-D.py
  requiredBy: []
  timestamp: '2026-06-17 12:46:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC228-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC228-D.py
- /library/tatyam_set/example/ABC228-D.py.html
title: tatyam_set/example/ABC228-D.py
---
