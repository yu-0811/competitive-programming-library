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
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/static_range_inversions_query\n\
    # include: algorithm_library/python/data_structure/BIT.py\n\n\ndef mos_inversions(data,\
    \ que):\n    \"\"\"Mos_algorithm.py \u306E\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\
    \u3092\u533A\u9593\u8EE2\u5012\u6570\u7528\u306B\u5177\u4F53\u5316\u3059\u308B\
    \u3002\"\"\"\n    from math import ceil, sqrt\n\n    n = len(data)\n    q = len(que)\n\
    \    if q == 0:\n        return []\n    B = max(1, ceil(sqrt(1.5) * n / sqrt(q)))\n\
    \n    ranks = {value: i for i, value in enumerate(sorted(set(data)))}\n    data\
    \ = [ranks[value] for value in data]\n    bit = fenwick_tree(len(ranks))\n   \
    \ add = bit.add\n    prefix = bit.sum0\n    inversions = size = 0\n\n    # \u5DE6\
    \u7AEF\u3067\u306F\u81EA\u5206\u3088\u308A\u5C0F\u3055\u3044\u8981\u7D20\u3001\
    \u53F3\u7AEF\u3067\u306F\u81EA\u5206\u3088\u308A\u5927\u304D\u3044\u8981\u7D20\
    \u3092\u6570\u3048\u308B\u3002\n    def add_left(left, right):\n        nonlocal\
    \ inversions, size\n        for i in range(right - 1, left - 1, -1):\n       \
    \     x = data[i]\n            inversions += prefix(x)\n            add(x, 1)\n\
    \            size += 1\n\n    def add_right(left, right):\n        nonlocal inversions,\
    \ size\n        for i in range(left, right):\n            x = data[i]\n      \
    \      inversions += size - prefix(x + 1)\n            add(x, 1)\n           \
    \ size += 1\n\n    def del_left(left, right):\n        nonlocal inversions, size\n\
    \        for i in range(left, right):\n            x = data[i]\n            inversions\
    \ -= prefix(x)\n            add(x, -1)\n            size -= 1\n\n    def del_right(left,\
    \ right):\n        nonlocal inversions, size\n        for i in range(right - 1,\
    \ left - 1, -1):\n            x = data[i]\n            inversions -= size - prefix(x\
    \ + 1)\n            add(x, -1)\n            size -= 1\n\n    # \u30E9\u30A4\u30D6\
    \u30E9\u30EA\u306E\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\u3068\u540C\u3058\u30D6\
    \u30ED\u30C3\u30AF\u5E45\u30FB\u6574\u6570\u30D1\u30C3\u30AF\u30FB\u86C7\u884C\
    \u9806\u3002\n    shift = q.bit_length()\n    lshift = n.bit_length()\n    mask\
    \ = (1 << shift) - 1\n    bucs = [[] for _ in range(n // B + 1)]\n    for idx,\
    \ (l, r) in enumerate(que):\n        bucs[l // B].append((((r << lshift) | l)\
    \ << shift) | idx)\n    order = []\n    for b, buc in enumerate(bucs):\n     \
    \   buc.sort(reverse=bool(b & 1))\n        order.extend(buc)\n\n    L = R = 0\n\
    \    ret = [-1] * q\n    for lri in order:\n        i = lri & mask\n        l,\
    \ r = que[i]\n        if L > l:\n            add_left(l, L)\n        if R < r:\n\
    \            add_right(R, r)\n        if L < l:\n            del_left(L, l)\n\
    \        if R > r:\n            del_right(r, R)\n        L, R = l, r\n       \
    \ ret[i] = inversions\n    return ret\n\n\ndef main():\n    N, Q = map(int, readline().split())\n\
    \    data = list(map(int, readline().split()))\n    que = [tuple(map(int, readline().split()))\
    \ for _ in range(Q)]\n    ans = mos_inversions(data, que)\n    sys.stdout.write(\"\
    \\n\".join(map(str, ans)) + (\"\\n\" if ans else \"\"))\n\n\nif __name__ == \"\
    __main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/techniques/static_range_inversions_query.py
  requiredBy: []
  timestamp: '2026-11-08 10:24:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/techniques/static_range_inversions_query.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/techniques/static_range_inversions_query.py
- /library/library-checker-submitcode/src/techniques/static_range_inversions_query.py.html
title: library-checker-submitcode/src/techniques/static_range_inversions_query.py
---
