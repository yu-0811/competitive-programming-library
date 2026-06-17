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
    - https://atcoder.jp/contests/abc308/submissions/46930610
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc308/submissions/46930610\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nQ = int(input())\nA = SortedMultiset()\n\
    X = SortedMultiset()\n\ndef add(a):\n    A.add(a)\n    i = A.index(a)\n    l =\
    \ A[i - 1] if i else None\n    r = A[i + 1] if i + 1 < len(A) else None\n    if\
    \ l is not None and r is not None:\n        X.discard(l ^ r)\n    if l is not\
    \ None:\n        X.add(l ^ a)\n    if r is not None:\n        X.add(r ^ a)\n\n\
    def erase(a):\n    i = A.index(a)\n    l = A[i - 1] if i else None\n    r = A[i\
    \ + 1] if i + 1 < len(A) else None\n    A.discard(a)\n    if l is not None and\
    \ r is not None:\n        X.add(l ^ r)\n    if l is not None:\n        X.discard(l\
    \ ^ a)\n    if r is not None:\n        X.discard(r ^ a)\n\nfor _ in range(Q):\n\
    \    query = input()\n    if query[0] == \"3\":\n        print(X[0])\n       \
    \ continue\n    t, x = query[0], int(query[2:])\n    if t == '1':\n        add(x)\n\
    \    else:\n        erase(x)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC308-G.py
  requiredBy: []
  timestamp: '2026-06-17 12:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC308-G.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC308-G.py
- /library/tatyam_set/example/ABC308-G.py.html
title: tatyam_set/example/ABC308-G.py
---
