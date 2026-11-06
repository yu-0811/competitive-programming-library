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
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/two_sat\n# include: algorithm_library/python/techniques/2-SAT.py\n\
    \n\ndef main():\n    _, _, n, m = readline().split()\n    n, m = int(n), int(m)\n\
    \n    def clauses():\n        for _ in range(m):\n            a, b, _ = map(int,\
    \ readline().split())\n            yield abs(a) - 1, a > 0, abs(b) - 1, b > 0\n\
    \n    answer = two_sat(n, clauses())\n    if answer is None:\n        print(\"\
    s UNSATISFIABLE\")\n    else:\n        print(\"s SATISFIABLE\")\n        print(\"\
    v\", \" \".join(str(i if x else -i) for i, x in enumerate(answer, 1)), 0)\n\n\n\
    if __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/techniques/two_sat.py
  requiredBy: []
  timestamp: '2026-11-06 22:27:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/techniques/two_sat.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/techniques/two_sat.py
- /library/library-checker-submitcode/src/techniques/two_sat.py.html
title: library-checker-submitcode/src/techniques/two_sat.py
---
