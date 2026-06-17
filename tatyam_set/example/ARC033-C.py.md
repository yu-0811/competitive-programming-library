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
    - https://atcoder.jp/contests/arc033/submissions/46930623
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/arc033/submissions/46930623\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nQ = int(input())\ns = SortedMultiset()\n\
    for _ in range(Q):\n    t, x = map(int, input().split())\n    if t == 1:\n   \
    \     s.add(x)\n    else:\n        x = s[x - 1]\n        print(x)\n        s.discard(x)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ARC033-C.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ARC033-C.py
layout: document
redirect_from:
- /library/tatyam_set/example/ARC033-C.py
- /library/tatyam_set/example/ARC033-C.py.html
title: tatyam_set/example/ARC033-C.py
---
