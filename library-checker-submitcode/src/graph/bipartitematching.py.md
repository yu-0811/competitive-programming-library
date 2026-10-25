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
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/bipartitematching\n# include:\
    \ algorithm_library/python/graph/maxflow.py\n\n\ndef main():\n    L, R, M = map(int,\
    \ readline().split())\n    source, sink = L + R, L + R + 1\n    flow = maximum_flow(L\
    \ + R + 2)\n    edges = []\n    for _ in range(M):\n        u, v = map(int, readline().split())\n\
    \        flow.add_edge(u, L + v, 1)\n        edges.append((u, v, flow.G[u][-1]))\n\
    \    for u in range(L):\n        flow.add_edge(source, u, 1)\n    for v in range(R):\n\
    \        flow.add_edge(L + v, sink, 1)\n    ans = [str(flow.maxflow(source, sink))]\n\
    \    ans.extend(f\"{u} {v}\" for u, v, edge in edges if edge.cap == 0)\n    sys.stdout.write(\"\
    \\n\".join(ans) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/bipartitematching.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/bipartitematching.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/bipartitematching.py
- /library/library-checker-submitcode/src/graph/bipartitematching.py.html
title: library-checker-submitcode/src/graph/bipartitematching.py
---
