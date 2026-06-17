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
    - https://atcoder.jp/contests/abc234/submissions/46930540
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc234/submissions/46930540\n\n# paste SortedSet\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nN, K = map(int, input().split())\n\
    P = list(map(int, input().split()))\nK -= 1\ns = SortedSet(P[:K])\n\nfor i in\
    \ range(K, N):\n    s.add(P[i])\n    print(s[~K])\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC234-D.py
  requiredBy: []
  timestamp: '2026-06-17 22:16:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC234-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC234-D.py
- /library/tatyam_set/example/ABC234-D.py.html
title: tatyam_set/example/ABC234-D.py
---
