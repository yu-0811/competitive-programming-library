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
    - https://atcoder.jp/contests/abc392/submissions/62566441
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc392/submissions/62566441\n\nimport sys\n\
    input = sys.stdin.readline\n\n# paste BucketList here\n\nN = int(input())\nA =\
    \ BucketList()\nP = list(map(int, input().split()))\n\nfor i, p in enumerate(P):\n\
    \    A.insert(p-1, i+1)\n\nprint(*A)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC392-F.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC392-F.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC392-F.py
- /library/tatyam_set/example/ABC392-F.py.html
title: tatyam_set/example/ABC392-F.py
---
