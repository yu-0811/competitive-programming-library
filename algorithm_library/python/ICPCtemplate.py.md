---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: 'import sys

    def input():return sys.stdin.readline().rstrip()

    def ii(): return int(input())

    def ms(): return map(int, input().split())

    def li(): return list(map(int,input().split()))

    inf = pow(10,18)

    mod = 998244353


    # import pypyjit

    # pypyjit.set_param(''max_unroll_recursion=-1'')

    sys.setrecursionlimit(10**9)

    from collections import defaultdict,deque

    from itertools import combinations,permutations,accumulate,product

    from bisect import bisect_left,bisect_right

    from heapq import heappop,heappush,heapify

    from functools import cache

    # @cache'
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/ICPCtemplate.py
  requiredBy: []
  timestamp: '2026-11-22 20:55:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/ICPCtemplate.py
layout: document
redirect_from:
- /library/algorithm_library/python/ICPCtemplate.py
- /library/algorithm_library/python/ICPCtemplate.py.html
title: algorithm_library/python/ICPCtemplate.py
---
