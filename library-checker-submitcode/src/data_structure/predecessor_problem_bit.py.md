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
    \ algorithm_library/python/data_structure/BIT.py\n\n\ndef main():\n    N, Q =\
    \ map(int, readline().split())\n    T = bytearray(readline().strip())\n    bit\
    \ = BIT(N)\n    l = 0\n    for r in range(N + 1):\n        if r == N or T[r] ==\
    \ 48:\n            if l < r:\n                bit.add(l, r, 1)\n            l\
    \ = r + 1\n    ans = []\n    for _ in range(Q):\n        t, k = map(int, readline().split())\n\
    \        if t < 2:\n            value = 1 - t\n            if T[k] - 48 != value:\n\
    \                bit.add(k, k + 1, 2 * value - 1)\n                T[k] = 48 +\
    \ value\n        elif t == 2:\n            ans.append(str(T[k] - 48))\n      \
    \  elif t == 3:\n            x = bit.lower_bound(bit.SUM(k) + 1)\n           \
    \ ans.append(str(x if x < N else -1))\n        else:\n            w = bit.SUM(k\
    \ + 1)\n            ans.append(str(bit.lower_bound(w) if w else -1))\n    sys.stdout.write(\"\
    \\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/predecessor_problem_bit.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/predecessor_problem_bit.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/predecessor_problem_bit.py
- /library/library-checker-submitcode/src/data_structure/predecessor_problem_bit.py.html
title: library-checker-submitcode/src/data_structure/predecessor_problem_bit.py
---
