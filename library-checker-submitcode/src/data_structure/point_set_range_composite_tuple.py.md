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
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/point_set_range_composite\n# include:\
    \ algorithm_library/python/data-structure/TupleSegtree.py\n\n\ndef compose(left,\
    \ right):\n    a, b = left\n    c, d = right\n    return a * c % mod, (b * c +\
    \ d) % mod\n\n\ndef main():\n    N, Q = map(int, readline().split())\n    functions\
    \ = [tuple(map(int, readline().split())) for _ in range(N)]\n    tree = TupleSegtree(functions,\
    \ compose, (1, 0))\n    ans = []\n    for _ in range(Q):\n        t, *values =\
    \ map(int, readline().split())\n        if t == 0:\n            p, a, b = values\n\
    \            tree.set(p, (a, b))\n        else:\n            l, r, x = values\n\
    \            a, b = tree.prod(l, r)\n            ans.append(str((a * x + b) %\
    \ mod))\n    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\
    \n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/point_set_range_composite_tuple.py
  requiredBy: []
  timestamp: '2026-10-25 10:09:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/point_set_range_composite_tuple.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/point_set_range_composite_tuple.py
- /library/library-checker-submitcode/src/data_structure/point_set_range_composite_tuple.py.html
title: library-checker-submitcode/src/data_structure/point_set_range_composite_tuple.py
---
