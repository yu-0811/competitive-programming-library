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
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/shortest_path\n# include: algorithm_library/python/data_structure/TupleHeap.py\n\
    \n\ndef main():\n    N, M, start, goal = map(int, readline().split())\n    graph\
    \ = [[] for _ in range(N)]\n    for _ in range(M):\n        u, v, w = map(int,\
    \ readline().split())\n        graph[u].append((v, w))\n\n    dist = [inf] * N\n\
    \    prev = [-1] * N\n    dist[start] = 0\n    heap = TupleHeap(1, [(0, start)])\n\
    \    while heap:\n        d, v = heap.pop()\n        if d != dist[v]:\n      \
    \      continue\n        if v == goal:\n            break\n        for u, w in\
    \ graph[v]:\n            nd = d + w\n            if nd < dist[u]:\n          \
    \      dist[u] = nd\n                prev[u] = v\n                heap.push((nd,\
    \ u))\n\n    if dist[goal] == inf:\n        print(-1)\n        return\n    path\
    \ = []\n    v = goal\n    while v != start:\n        u = prev[v]\n        path.append(f\"\
    {u} {v}\")\n        v = u\n    print(dist[goal], len(path))\n    sys.stdout.write(\"\
    \\n\".join(reversed(path)) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/shortest_path_tuple_heap.py
  requiredBy: []
  timestamp: '2026-11-18 22:17:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/shortest_path_tuple_heap.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/shortest_path_tuple_heap.py
- /library/library-checker-submitcode/src/graph/shortest_path_tuple_heap.py.html
title: library-checker-submitcode/src/graph/shortest_path_tuple_heap.py
---
