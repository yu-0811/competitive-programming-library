---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: algorithm_library/python/graph/SCC.py
    title: algorithm_library/python/graph/SCC.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\nimport\
    \ sys\n\ninput = sys.stdin.buffer.readline\n\nfrom algorithm_library.python.graph.SCC\
    \ import SCC\n\nN, M = map(int, input().split())\nscc = SCC(N)\nfor _ in range(M):\n\
    \    a, b = map(int, input().split())\n    scc.addEdge(a, b)\n\ngroups = scc.build_scc()\n\
    print(len(groups))\nfor ans in groups:\n    print(len(ans), *ans)\n"
  dependsOn:
  - algorithm_library/python/graph/SCC.py
  isVerificationFile: true
  path: tests/graph/scc_yosupo.test.py
  requiredBy: []
  timestamp: '2026-10-20 12:13:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/graph/scc_yosupo.test.py
layout: document
redirect_from:
- /verify/tests/graph/scc_yosupo.test.py
- /verify/tests/graph/scc_yosupo.test.py.html
title: tests/graph/scc_yosupo.test.py
---
