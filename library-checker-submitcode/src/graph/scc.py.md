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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/scc\n# include: algorithm_library/python/graph/SCC.py\n\
    \n\ndef main():\n    N, M = map(int, readline().split())\n    edges = []\n   \
    \ for _ in range(M):\n        u, v = map(int, readline().split())\n        edges.append((u,\
    \ v))\n    groups, _ = scc_dag(N, edges)\n    ans = [str(len(groups))]\n    ans.extend(f\"\
    {len(group)} \" + \" \".join(map(str, group)) for group in groups)\n    sys.stdout.write(\"\
    \\n\".join(ans) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/scc.py
  requiredBy: []
  timestamp: '2026-11-27 15:22:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/scc.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/scc.py
- /library/library-checker-submitcode/src/graph/scc.py.html
title: library-checker-submitcode/src/graph/scc.py
---
