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
    - https://atcoder.jp/contests/arc155/submissions/38361198
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/arc155/submissions/38361198\n\nimport sys\n\
    input = sys.stdin.readline\n\n# paste SortedSet here\n\nINF = 1 << 60\ns = SortedSet([-INF,\
    \ INF])\ndef add(a, b):\n    s.add(a + b)\n    s.add(a - b)\n\nQ, A, B = map(int,\
    \ input().split())\nadd(A, B)\n\nfor _ in range(Q):\n    t, a, b = map(int, input().split())\n\
    \    if t == 1:\n        add(a, b)\n    else:\n        print(max(0, min(s.ge(a)\
    \ - b, a - s.le(b))))\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ARC155-B.py
  requiredBy: []
  timestamp: '2026-06-17 12:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ARC155-B.py
layout: document
redirect_from:
- /library/tatyam_set/example/ARC155-B.py
- /library/tatyam_set/example/ARC155-B.py.html
title: tatyam_set/example/ARC155-B.py
---
