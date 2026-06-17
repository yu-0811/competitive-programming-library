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
    - https://atcoder.jp/contests/abc241/submissions/46930547
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc241/submissions/46930547\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nQ = int(input())\nA = SortedMultiset()\n\
    for _ in range(Q):\n    s = input()\n    if s[0] == \"1\":\n        x = int(s[2:])\n\
    \        A.add(x)\n    elif s[0] == \"2\":\n        x, k = map(int, s[2:].split())\n\
    \        i = A.index_right(x) - k\n        print(-1 if i < 0 else A[i])\n    else:\n\
    \        x, k = map(int, s[2:].split())\n        i = A.index(x) + k - 1\n    \
    \    print(-1 if i >= len(A) else A[i])\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC241-D.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC241-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC241-D.py
- /library/tatyam_set/example/ABC241-D.py.html
title: tatyam_set/example/ABC241-D.py
---
