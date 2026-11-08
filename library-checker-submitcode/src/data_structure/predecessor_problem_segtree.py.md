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
    - https://judge.yosupo.jp/problem/predecessor_problem
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/predecessor_problem\n# include:\
    \ algorithm_library/python/data_structure/Segtree.py\n\n\ndef is_zero(x):\n  \
    \  return x == 0\n\n\ndef main():\n    N, Q = map(int, readline().split())\n \
    \   tree = segtree([c - 48 for c in readline().strip()], lambda a, b: a + b, 0)\n\
    \    ans = []\n    for _ in range(Q):\n        t, k = map(int, readline().split())\n\
    \        if t < 2:\n            tree.set(k, 1 - t)\n        elif t == 2:\n   \
    \         ans.append(str(tree.get(k)))\n        elif t == 3:\n            x =\
    \ tree.max_right(k, is_zero)\n            ans.append(str(x if x < N else -1))\n\
    \        else:\n            ans.append(str(tree.min_left(k + 1, is_zero) - 1))\n\
    \    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/predecessor_problem_segtree.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/predecessor_problem_segtree.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/predecessor_problem_segtree.py
- /library/library-checker-submitcode/src/data_structure/predecessor_problem_segtree.py.html
title: library-checker-submitcode/src/data_structure/predecessor_problem_segtree.py
---
