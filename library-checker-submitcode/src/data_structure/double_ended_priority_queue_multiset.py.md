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
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    # include: algorithm_library/python/data_structure/SortedMultiset.py\n\n\ndef\
    \ main():\n    N, Q = map(int, readline().split())\n    s = SortedMultiset(map(int,\
    \ readline().split()))\n    ans = []\n    for _ in range(Q):\n        query =\
    \ list(map(int, readline().split()))\n        if query[0] == 0:\n            s.add(query[1])\n\
    \        else:\n            ans.append(str(s.pop(0 if query[0] == 1 else -1)))\n\
    \    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/double_ended_priority_queue_multiset.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/double_ended_priority_queue_multiset.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/double_ended_priority_queue_multiset.py
- /library/library-checker-submitcode/src/data_structure/double_ended_priority_queue_multiset.py.html
title: library-checker-submitcode/src/data_structure/double_ended_priority_queue_multiset.py
---
