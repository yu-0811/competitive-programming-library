---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\nimport\
    \ sys\ninput = sys.stdin.buffer.readline\n\nfrom algorithm_library.python.graph.SCC\
    \ import SCC\n\nN,M = map(int,input().split())\nscc = SCC(N)\nfor _ in range(M):\n\
    \  a,b = map(int,input().split())\n  scc.addEdge(a,b)\n\ngroups = scc.doSCC()\n\
    print(len(groups))\nfor ans in groups:\n  print(len(ans),*ans)"
  dependsOn: []
  isVerificationFile: true
  path: tests/graph/scc_yosupo.test.py
  requiredBy: []
  timestamp: '2024-12-08 12:22:34+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: tests/graph/scc_yosupo.test.py
layout: document
redirect_from:
- /verify/tests/graph/scc_yosupo.test.py
- /verify/tests/graph/scc_yosupo.test.py.html
title: tests/graph/scc_yosupo.test.py
---
