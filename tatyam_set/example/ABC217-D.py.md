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
    - https://atcoder.jp/contests/abc217/submissions/46930432
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc217/submissions/46930432\n\n# paste SortedSet\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nL, Q = map(int, input().split())\n\
    s = SortedSet([0, L])\nfor i in range(Q):\n    c, x = map(int, input().split())\n\
    \    if c == 1:\n        s.add(x)\n    else:\n        print(s.gt(x) - s.lt(x))\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC217-D.py
  requiredBy: []
  timestamp: '2026-06-17 12:46:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC217-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC217-D.py
- /library/tatyam_set/example/ABC217-D.py.html
title: tatyam_set/example/ABC217-D.py
---
