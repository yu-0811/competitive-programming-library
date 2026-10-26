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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys;\ndef input():return sys.stdin.readline().rstrip()\n\n# \u5165\
    \u529B\u306A\u3069\ndef ii(): return int(input())\ndef ms(): return map(int, input().split())\n\
    def li(): return list(map(int,input().split()))\ninf = pow(10,18)\nmod = 998244353\n\
    \n# \u30E9\u30A4\u30D6\u30E9\u30EA\u7CFB\n# import pypyjit\n# pypyjit.set_param('max_unroll_recursion=-1')\n\
    sys.setrecursionlimit(10**9)\nfrom collections import defaultdict,deque\nfrom\
    \ itertools import combinations,permutations,accumulate,product\nfrom bisect import\
    \ bisect_left,bisect_right\nfrom heapq import heappop,heappush,heapify\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/ICPCtemplate.py
  requiredBy: []
  timestamp: '2026-10-26 10:59:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/ICPCtemplate.py
layout: document
redirect_from:
- /library/algorithm_library/python/ICPCtemplate.py
- /library/algorithm_library/python/ICPCtemplate.py.html
title: algorithm_library/python/ICPCtemplate.py
---
