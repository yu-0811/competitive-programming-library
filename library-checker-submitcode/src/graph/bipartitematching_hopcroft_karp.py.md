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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/bipartitematching\n# include:\
    \ algorithm_library/python/graph/hopcroft_karp.py\n\n\ndef main():\n    n, m,\
    \ e = map(int, readline().split())\n    g = [[] for _ in range(n)]\n    for _\
    \ in range(e):\n        u, v = map(int, readline().split())\n        g[u].append(v)\n\
    \    p = hopcroft_karp(g, m)\n    ans = [f\"{u} {v}\" for u, v in enumerate(p)\
    \ if v >= 0]\n    print(len(ans))\n    sys.stdout.write(\"\\n\".join(ans) + \"\
    \\n\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/graph/bipartitematching_hopcroft_karp.py
  requiredBy: []
  timestamp: '2026-11-25 22:52:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/graph/bipartitematching_hopcroft_karp.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/graph/bipartitematching_hopcroft_karp.py
- /library/library-checker-submitcode/src/graph/bipartitematching_hopcroft_karp.py.html
title: library-checker-submitcode/src/graph/bipartitematching_hopcroft_karp.py
---
