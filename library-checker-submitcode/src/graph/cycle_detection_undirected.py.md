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
    - https://judge.yosupo.jp/problem/cycle_detection_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/cycle_detection_undirected\n#\
    \ include: algorithm_library/python/graph/cycle_detect.py\n\n\ndef main():\n \
    \   N, M = map(int, readline().split())\n    edges = [tuple(map(int, readline().split()))\
    \ for _ in range(M)]\n    vertices, edge_ids = cycle_detect(N, edges)\n    if\
    \ not vertices:\n        print(-1)\n        return\n    print(len(vertices))\n\
    \    print(*vertices)\n    print(*edge_ids)\n\n\nif __name__ == \"__main__\":\n\
    \    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/cycle_detection_undirected.py
  requiredBy: []
  timestamp: '2026-10-29 14:17:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/cycle_detection_undirected.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/cycle_detection_undirected.py
- /library/library-checker-submitcode/src/graph/cycle_detection_undirected.py.html
title: library-checker-submitcode/src/graph/cycle_detection_undirected.py
---
