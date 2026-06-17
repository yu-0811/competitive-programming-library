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
    - https://atcoder.jp/contests/past202112-open/submissions/46930630
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/past202112-open/submissions/46930630\n\n# paste\
    \ SortedSet here\n\nimport sys\ninput = sys.stdin.readline\n\nN, Q = map(int,\
    \ input().split())\nS = input().split()\nS = SortedSet((S[i], i) for i in range(N))\n\
    for i in range(Q):\n    X, T = input().split()\n    X = S[int(X) - 1]\n    S.discard(X)\n\
    \    S.add((T, X[1]))\n\nans = [\"\"] * N\nfor name, id in S:\n    ans[id] = name\n\
    for i in ans:\n    print(i)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/PAST9-M.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/PAST9-M.py
layout: document
redirect_from:
- /library/tatyam_set/example/PAST9-M.py
- /library/tatyam_set/example/PAST9-M.py.html
title: tatyam_set/example/PAST9-M.py
---
