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
    - https://judge.yosupo.jp/problem/ordered_set
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/ordered_set\n# include: algorithm_library/python/data_structure/SortedMultiset.py\n\
    \n\ndef main():\n    N, Q = map(int, readline().split())\n    s = SortedMultiset(map(int,\
    \ readline().split()))\n    ans = []\n    for _ in range(Q):\n        t, x = map(int,\
    \ readline().split())\n        if t == 0:\n            if x not in s:\n      \
    \          s.add(x)\n        elif t == 1:\n            s.discard(x)\n        elif\
    \ t == 2:\n            ans.append(str(s[x - 1] if x <= len(s) else -1))\n    \
    \    elif t == 3:\n            ans.append(str(s.index_right(x)))\n        elif\
    \ t == 4:\n            y = s.lt(x + 1)\n            ans.append(str(y if y is not\
    \ None else -1))\n        else:\n            y = s.gt(x - 1)\n            ans.append(str(y\
    \ if y is not None else -1))\n    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\"\
    \ if ans else \"\"))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/ordered_set_multiset.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/ordered_set_multiset.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/ordered_set_multiset.py
- /library/library-checker-submitcode/src/data_structure/ordered_set_multiset.py.html
title: library-checker-submitcode/src/data_structure/ordered_set_multiset.py
---
