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
    - https://judge.yosupo.jp/problem/unionfind_with_potential
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/unionfind_with_potential\n# include:\
    \ algorithm_library/python/graph/PotentialUnionFind.py\n\n\ndef main():\n    N,\
    \ Q = map(int, readline().split())\n    uf = PotentialUnionFind(N)\n    ans =\
    \ []\n    for _ in range(Q):\n        t, u, v, *rest = map(int, readline().split())\n\
    \        # Library Checker asks for a[u] - a[v]; dist(x, y) returns a[y] - a[x].\n\
    \        distance = uf.dist(v, u)\n        if t == 0:\n            x = rest[0]\n\
    \            if distance == uf.inf:\n                uf.union(v, u, x)\n     \
    \           ans.append(\"1\")\n            else:\n                ans.append(\"\
    1\" if distance % mod == x else \"0\")\n        else:\n            ans.append(str(-1\
    \ if distance == uf.inf else distance % mod))\n    sys.stdout.write(\"\\n\".join(ans)\
    \ + \"\\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/unionfind_with_potential.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/unionfind_with_potential.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/unionfind_with_potential.py
- /library/library-checker-submitcode/src/graph/unionfind_with_potential.py.html
title: library-checker-submitcode/src/graph/unionfind_with_potential.py
---
