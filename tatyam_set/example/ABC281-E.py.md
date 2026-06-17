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
    - https://atcoder.jp/contests/abc281/submissions/46930602
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc281/submissions/46930602\n\n# paste SortedMultiset\
    \ here\n\nimport sys\ninput = sys.stdin.readline\n\nN, M, K = map(int, input().split())\n\
    A = list(map(int, input().split()))\nfirst = sorted(A[:M])\nlow = SortedMultiset(first[:K])\n\
    high = SortedMultiset(first[K:])\nans = sum(first[:K])\nprint(ans)\n\nfor i in\
    \ range(M, N):\n    x = A[i]\n    if x < low[-1]:\n        ans -= low[-1]\n  \
    \      high.add(low.pop(-1))\n        ans += x\n        low.add(x)\n    else:\n\
    \        high.add(x)\n    x = A[i - M]\n    if x < high[0]:\n        ans -= x\n\
    \        low.discard(x)\n        ans += high[0]\n        low.add(high.pop(0))\n\
    \    else:\n        high.discard(x)\n    print(ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: tatyam_set/example/ABC281-E.py
  requiredBy: []
  timestamp: '2026-06-17 12:46:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tatyam_set/example/ABC281-E.py
layout: document
redirect_from:
- /library/tatyam_set/example/ABC281-E.py
- /library/tatyam_set/example/ABC281-E.py.html
title: tatyam_set/example/ABC281-E.py
---
