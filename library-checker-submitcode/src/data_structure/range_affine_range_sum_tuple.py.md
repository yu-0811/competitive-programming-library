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
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/range_affine_range_sum\n# include:\
    \ algorithm_library/python/data-structure/TupleLazySegtree.py\n\n\ndef combine(left,\
    \ right):\n    return (left[0] + right[0]) % mod, left[1] + right[1]\n\n\ndef\
    \ mapping(f, value):\n    a, b = f\n    total, length = value\n    return (a *\
    \ total + b * length) % mod, length\n\n\ndef composition(f, g):\n    a, b = f\n\
    \    c, d = g\n    return a * c % mod, (a * d + b) % mod\n\n\ndef main():\n  \
    \  N, Q = map(int, readline().split())\n    values = [(a, 1) for a in map(int,\
    \ readline().split())]\n    tree = TupleLazySegtree(values, combine, (0, 0), mapping,\
    \ composition, (1, 0))\n    ans = []\n    for _ in range(Q):\n        t, l, r,\
    \ *rest = map(int, readline().split())\n        if t == 0:\n            tree.apply(l,\
    \ r, tuple(rest))\n        else:\n            ans.append(str(tree.prod(l, r)[0]))\n\
    \    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/range_affine_range_sum_tuple.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/range_affine_range_sum_tuple.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/range_affine_range_sum_tuple.py
- /library/library-checker-submitcode/src/data_structure/range_affine_range_sum_tuple.py.html
title: library-checker-submitcode/src/data_structure/range_affine_range_sum_tuple.py
---
