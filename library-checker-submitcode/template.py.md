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
    - https://github.com/yu-0811/competitive-programming-library
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# library: https://github.com/yu-0811/competitive-programming-library

    import sys,math;sys.setrecursionlimit(10**9)

    # import pypyjit

    # pypyjit.set_param(''max_unroll_recursion=-1'')

    from collections import defaultdict,deque

    from bisect import bisect_left,bisect_right

    from heapq import heappop,heappush,heapify

    #from more_itertools import distinct_permutations,distinct_combinations

    readline = sys.stdin.buffer.readline

    def input():return sys.stdin.readline().rstrip()

    def ii(): return int(input())

    def ms(): return map(int, input().split())

    def li(): return list(map(int,input().split()))

    inf = pow(10,18)

    mod = 998244353

    #//////////////////////////

    '
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/template.py
  requiredBy: []
  timestamp: '2026-10-20 13:36:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/template.py
layout: document
redirect_from:
- /library/library-checker-submitcode/template.py
- /library/library-checker-submitcode/template.py.html
title: library-checker-submitcode/template.py
---
