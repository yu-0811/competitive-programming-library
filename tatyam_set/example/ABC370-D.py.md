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
    - https://atcoder.jp/contests/abc370/submissions/57703551
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc370/submissions/57703551\n\n# paste SortedSet\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nH, W, Q = map(int, input().split())\n\
    rows = [SortedSet(range(W)) for _ in range(H)]\ncols = [SortedSet(range(H)) for\
    \ _ in range(W)]\nans = H * W\n\ndef remove(x, y):\n    if x is None or y is None:\
    \ return\n    rows[x].discard(y)\n    cols[y].discard(x)\n    global ans\n   \
    \ ans -= 1\n    \nfor _ in range(Q):\n    x, y = map(int, input().split())\n \
    \   x -= 1\n    y -= 1\n    if y in rows[x]:\n        remove(x, y)\n    else:\n\
    \        remove(x, rows[x].lt(y))\n        remove(x, rows[x].gt(y))\n        remove(cols[y].lt(x),\
    \ y)\n        remove(cols[y].gt(x), y)\n\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC370-D.py
  requiredBy: []
  timestamp: '2026-06-17 12:46:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC370-D.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC370-D.py
- /library/tatyam_set/example/ABC370-D.py.html
title: tatyam_set/example/ABC370-D.py
---
