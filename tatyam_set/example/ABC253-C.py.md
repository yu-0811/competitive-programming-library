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
    - https://atcoder.jp/contests/abc253/submissions/46930587
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc253/submissions/46930587\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nQ = int(input())\na = SortedMultiset()\n\
    for i in range(Q):\n    query = input()\n    if query[0] == \"1\":\n        x\
    \ = int(query[2:])\n        a.add(x)\n    elif query[0] == \"2\":\n        x,\
    \ c = map(int, query[2:].split())\n        for _ in range(c):\n            if\
    \ not a.discard(x):\n                break\n    else:\n        print(a[-1] - a[0])\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC253-C.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC253-C.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC253-C.py
- /library/tatyam_set/example/ABC253-C.py.html
title: tatyam_set/example/ABC253-C.py
---
