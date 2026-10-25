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
    - https://judge.yosupo.jp/problem/sort_points_by_argument
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/sort_points_by_argument\n# include:\
    \ algorithm_library/python/math/AngularSort.py\n\nfrom functools import cmp_to_key\n\
    \n\ndef main():\n    N = int(readline())\n    lower, zeros, upper = [], [], []\n\
    \    for _ in range(N):\n        point = tuple(map(int, readline().split()))\n\
    \        if point == (0, 0):\n            zeros.append(point)\n        elif point[1]\
    \ < 0:\n            lower.append(point)\n        else:\n            upper.append(point)\n\
    \    # The library starts at angle 0; the problem uses (-pi, pi], with arg(0)=0.\n\
    \    lower.sort(key=cmp_to_key(compare))\n    upper.sort(key=cmp_to_key(compare))\n\
    \    points = lower + zeros + upper\n    sys.stdout.write(\"\\n\".join(f\"{x}\
    \ {y}\" for x, y in points) + \"\\n\")\n\n\nif __name__ == \"__main__\":\n   \
    \ main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/math/sort_points_by_argument.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/math/sort_points_by_argument.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/math/sort_points_by_argument.py
- /library/library-checker-submitcode/src/math/sort_points_by_argument.py.html
title: library-checker-submitcode/src/math/sort_points_by_argument.py
---
