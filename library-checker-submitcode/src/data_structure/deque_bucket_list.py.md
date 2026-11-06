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
    - https://judge.yosupo.jp/problem/deque
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/deque\n# include: algorithm_library/python/data_structure/BucketList.py\n\
    \n\ndef main():\n    Q = int(readline())\n    a = BucketList()\n    ans = []\n\
    \    for _ in range(Q):\n        query = list(map(int, readline().split()))\n\
    \        t = query[0]\n        if t == 0:\n            a.insert(0, query[1])\n\
    \        elif t == 1:\n            a.append(query[1])\n        elif t == 2:\n\
    \            a.pop(0)\n        elif t == 3:\n            a.pop()\n        else:\n\
    \            ans.append(str(a[query[1]]))\n    sys.stdout.write(\"\\n\".join(ans)\
    \ + (\"\\n\" if ans else \"\"))\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/deque_bucket_list.py
  requiredBy: []
  timestamp: '2026-11-06 23:20:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/deque_bucket_list.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/deque_bucket_list.py
- /library/library-checker-submitcode/src/data_structure/deque_bucket_list.py.html
title: library-checker-submitcode/src/data_structure/deque_bucket_list.py
---
