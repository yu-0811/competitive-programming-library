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
    - https://atcoder.jp/contests/abc140/submissions/46930364
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc140/submissions/46930364\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nN = int(input())\nP = list(map(int,\
    \ input().split()))\nQ = [0] * N\nfor i in range(N):\n    Q[P[i] - 1] = i\n\n\
    s = SortedMultiset([-1, -1, N, N])\nans = 0\ncnt = 0\nfor x in reversed(Q):\n\
    \    s.add(x)\n    i = s.index(x)\n    v = s[i - 2]\n    w = s[i - 1]\n    y =\
    \ s[i + 1]\n    z = s[i + 2]\n    cnt += (z - y) * (x - w) + (y - x) * (w - v)\n\
    \    ans += cnt\n\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC140-E.py
  requiredBy: []
  timestamp: '2026-06-17 22:16:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC140-E.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC140-E.py
- /library/tatyam_set/example/ABC140-E.py.html
title: tatyam_set/example/ABC140-E.py
---
