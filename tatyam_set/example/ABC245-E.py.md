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
    - https://atcoder.jp/contests/abc245/submissions/46930576
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc245/submissions/46930576\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nN, M = map(int, input().split())\n\
    A = list(map(int, input().split()))\nB = list(map(int, input().split()))\nC =\
    \ list(map(int, input().split()))\nD = list(map(int, input().split()))\n\nA =\
    \ [A[i] << 30 | B[i] for i in range(N)]\nC = [C[i] << 30 | D[i] for i in range(M)]\n\
    A.sort(reverse=True)\nC.sort()\nC.insert(0, 0)\n\ns = SortedMultiset()\nMASK =\
    \ (1 << 30) - 1\n\nfor xy in A:\n    while C[-1] >= xy:\n        s.add(C.pop()\
    \ & MASK)\n    a = s.ge(xy & MASK)\n    if a is None:\n        exit(print(\"No\"\
    ))\n    s.discard(a)\n\nprint(\"Yes\")\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC245-E.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC245-E.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC245-E.py
- /library/tatyam_set/example/ABC245-E.py.html
title: tatyam_set/example/ABC245-E.py
---
