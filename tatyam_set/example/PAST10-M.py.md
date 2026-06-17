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
    - https://atcoder.jp/contests/past202203-open/submissions/46930650
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/past202203-open/submissions/46930650\n\n# paste\
    \ SortedSet here\n\nimport sys\ninput = sys.stdin.readline\n\nN, Q = map(int,\
    \ input().split())\nP = list(map(int, input().split()))\n\nrank = SortedSet(P[i]\
    \ << 20 | i for i in range(N))\n\nfor _ in range(Q):\n    query = input()\n  \
    \  t = query[0]\n    query = query[2:]\n    if t == '1':\n        i, x = map(int,\
    \ query.split())\n        i -= 1\n        rank.discard(P[i] << 20 | i)\n     \
    \   P[i] = x\n        rank.add(x << 20 | i)\n    elif t == '2':\n        i = int(query)\n\
    \        i -= 1\n        print(N - rank.index(P[i] << 20))\n    else:\n      \
    \  r = int(query)\n        print((rank[-r] & 0xfffff) + 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/PAST10-M.py
  requiredBy: []
  timestamp: '2026-06-17 13:03:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/PAST10-M.py
layout: document
redirect_from:
- /library/tatyam_set/example/PAST10-M.py
- /library/tatyam_set/example/PAST10-M.py.html
title: tatyam_set/example/PAST10-M.py
---
