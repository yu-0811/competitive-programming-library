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
    # include: algorithm_library/python/data_structure/TupleHeap.py\n\n\ndef main():\n\
    \    N, Q = map(int, readline().split())\n    records = [{\"value\": x, \"alive\"\
    : True} for x in map(int, readline().split())]\n    lo = TupleHeap(1, ((r[\"value\"\
    ], r) for r in records))\n    # -value \u3092\u4E0A\u4F4D\u30FB\u4E0B\u4F4D\u306B\
    \u5206\u3051\u3001\u5148\u982D2\u6210\u5206\u306E\u8F9E\u66F8\u9806\u3067\u6700\
    \u5927\u5024\u3092\u63A2\u3059\u3002\n    # \u672B\u5C3E\u306E dict \u306F\u3001\
    \u540C\u3058\u5024\u304C\u8907\u6570\u3042\u3063\u3066\u3082\u6BD4\u8F03\u3057\
    \u306A\u3044\u3002\n    hi = TupleHeap(2, ((*divmod(-r[\"value\"], 1 << 16), r)\
    \ for r in records))\n    ans = []\n    for _ in range(Q):\n        query = list(map(int,\
    \ readline().split()))\n        if query[0] == 0:\n            x = query[1]\n\
    \            record = {\"value\": x, \"alive\": True}\n            lo.push((x,\
    \ record))\n            hi.push((*divmod(-x, 1 << 16), record))\n        else:\n\
    \            heap = lo if query[0] == 1 else hi\n            while not heap.top()[-1][\"\
    alive\"]:\n                heap.pop()\n            record = heap.pop()[-1]\n \
    \           record[\"alive\"] = False\n            ans.append(str(record[\"value\"\
    ]))\n    sys.stdout.write(\"\\n\".join(ans) + (\"\\n\" if ans else \"\"))\n\n\n\
    if __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/data_structure/double_ended_priority_queue_tuple_heap.py
  requiredBy: []
  timestamp: '2026-11-18 22:17:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/data_structure/double_ended_priority_queue_tuple_heap.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/data_structure/double_ended_priority_queue_tuple_heap.py
- /library/library-checker-submitcode/src/data_structure/double_ended_priority_queue_tuple_heap.py.html
title: library-checker-submitcode/src/data_structure/double_ended_priority_queue_tuple_heap.py
---
