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
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/jump_on_tree\n# include: algorithm_library/python/graph/LCA.py\n\
    # include: algorithm_library/python/techniques/Doubling.py\n\n\ndef main():\n\
    \    N, Q = map(int, readline().split())\n    graph = [[] for _ in range(N)]\n\
    \    for _ in range(N - 1):\n        u, v = map(int, readline().split())\n   \
    \     graph[u].append(v)\n        graph[v].append(u)\n    tree = LCA(N, graph,\
    \ 0)\n    # Build the jump table through Doubling.py as well as testing LCA.py.\n\
    \    dp = [[0] * N for _ in range(N.bit_length())]\n    dp[0] = [max(0, parent)\
    \ for parent in tree.parent[0][:N]]\n    doubling(dp, N, len(dp))\n    ans = []\n\
    \    for _ in range(Q):\n        u, v, k = map(int, readline().split())\n    \
    \    ancestor = tree.lca(u, v)\n        up = tree.depth[u] - tree.depth[ancestor]\n\
    \        distance = up + tree.depth[v] - tree.depth[ancestor]\n        if k >\
    \ distance:\n            ans.append(\"-1\")\n        elif k <= up:\n         \
    \   ans.append(str(query(dp, u, k)))\n        else:\n            ans.append(str(query(dp,\
    \ v, distance - k)))\n    sys.stdout.write(\"\\n\".join(ans) + \"\\n\")\n\n\n\
    if __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/jump_on_tree.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/jump_on_tree.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/jump_on_tree.py
- /library/library-checker-submitcode/src/graph/jump_on_tree.py.html
title: library-checker-submitcode/src/graph/jump_on_tree.py
---
