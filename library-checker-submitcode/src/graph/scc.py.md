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
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/scc\n# include: algorithm_library/python/graph/SCC.py\n\
    \n\ndef main():\n    N, M = map(int, readline().split())\n    graph = SCC(N)\n\
    \    for _ in range(M):\n        u, v = map(int, readline().split())\n       \
    \ graph.addEdge(u, v)\n    groups = graph.build_scc()\n    ans = [str(len(groups))]\n\
    \    ans.extend(f\"{len(group)} \" + \" \".join(map(str, group)) for group in\
    \ groups)\n    sys.stdout.write(\"\\n\".join(ans) + \"\\n\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/scc.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/scc.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/scc.py
- /library/library-checker-submitcode/src/graph/scc.py.html
title: library-checker-submitcode/src/graph/scc.py
---
