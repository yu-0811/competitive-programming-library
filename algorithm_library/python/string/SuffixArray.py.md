---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from itertools import accumulate\n\n\n# SA \u306E\u69CB\u7BC9\uFF1AO(|S|)\n\
    # SA[i]: int \u3067 S \u306E SA[i] \u304B\u3089\u59CB\u307E\u308B suffix \u304C\
    \u30BD\u30FC\u30C8\u3055\u308C\u3066\u308B\n\n\ndef sa_is(s, upper):\n    n =\
    \ len(s)\n    if n < 2:\n        return list(range(n))\n    ls = bytearray(n)\n\
    \    for i in range(n - 2, -1, -1):\n        ls[i] = ls[i + 1] if s[i] == s[i\
    \ + 1] else s[i] < s[i + 1]\n    count = [0] * (upper + 1)\n    for x in s:\n\
    \        count[x] += 1\n    # \u6587\u5B57 x \u306E\u30D0\u30B1\u30C3\u30C8\u306F\
    \ [bounds[x], bounds[x + 1])\u3002\n    bounds = list(accumulate(count, initial=0))\n\
    \n    def induce(lms):\n        sa = [-1] * n\n        buf = bounds[1:]\n    \
    \    for i in reversed(lms):\n            c = s[i]\n            buf[c] -= 1\n\
    \            sa[buf[c]] = i\n        buf = bounds[:-1]\n        sa[buf[s[-1]]]\
    \ = n - 1\n        buf[s[-1]] += 1\n        for v in sa:\n            i = v -\
    \ 1\n            if i >= 0 and not ls[i]:\n                c = s[i]\n        \
    \        sa[buf[c]] = i\n                buf[c] += 1\n        buf = bounds[1:]\n\
    \        for v in reversed(sa):\n            i = v - 1\n            if i >= 0\
    \ and ls[i]:\n                c = s[i]\n                buf[c] -= 1\n        \
    \        sa[buf[c]] = i\n        return sa\n\n    lms = [i for i in range(1, n)\
    \ if not ls[i - 1] and ls[i]]\n    m = len(lms)\n    sa = induce(lms)\n    if\
    \ m:\n        ids = [-1] * n\n        for i, v in enumerate(lms):\n          \
    \  ids[v] = i\n        order = [v for v in sa if ids[v] != -1]\n        lms.append(n)\n\
    \        rec = [0] * m\n        rank = 0\n        # LMS \u90E8\u5206\u6587\u5B57\
    \u5217\u306F\u6B21\u306E LMS \u4F4D\u7F6E\u306E\u6587\u5B57\u307E\u3067\u542B\u3081\
    \u3066\u6BD4\u8F03\u3059\u308B\u3002\n        # \u5404\u533A\u9593\u306E\u6BD4\
    \u8F03\u306F\u9AD8\u3005 2 \u56DE\u306A\u306E\u3067\u3001\u30B9\u30E9\u30A4\u30B9\
    \u306E\u5408\u8A08\u9577\u3082 O(n)\u3002\n        for l, r in zip(order, order[1:]):\n\
    \            el, er = lms[ids[l] + 1], lms[ids[r] + 1]\n            rank += s[l\
    \ : el + 1] != s[r : er + 1]\n            rec[ids[r]] = rank\n        if rank\
    \ + 1 < m:\n            order = [lms[i] for i in sa_is(rec, rank)]\n        sa\
    \ = induce(order)\n    return sa\n\n\ndef suffix_array_upper(s, upper):\n    assert\
    \ 0 <= upper\n    for d in s:\n        assert 0 <= d <= upper\n    return sa_is(s,\
    \ upper)\n\n\ndef suffix_array(s) -> list[int]:\n    n = len(s)\n    # 1 \u6587\
    \u5B57 1 \u30D0\u30A4\u30C8\u306B\u3067\u304D\u308B\u3068\u304D\u306F\u5EA7\u6A19\
    \u5727\u7E2E\u3092\u7701\u304F\u3002\n    if isinstance(s, str) and max(s, default=\"\
    \") <= \"\\xff\":\n        s = s.encode(\"latin1\")\n    if isinstance(s, (bytes,\
    \ bytearray)):\n        return sa_is(s, 255)\n    idx = sorted(range(n), key=s.__getitem__)\n\
    \    s2 = [0] * n\n    now = 0\n    for i, j in zip(idx, idx[1:]):\n        now\
    \ += s[i] != s[j]\n        s2[j] = now\n    return sa_is(s2, now)\n\n\n# lcp[i]\
    \ = S \u306E SA[i] \u6587\u5B57\u76EE\u304B\u3089\u59CB\u307E\u308B suffix \u3068\
    \ S \u306E SA[i+1] \u6587\u5B57\u76EE\u304B\u3089\u59CB\u307E\u308B suffix \u306E\
    \u5171\u901A\u63A5\u982D\u8F9E\u306E\u9577\u3055\ndef lcp_array(s: str, sa: list[int])\
    \ -> list[int]:\n    n = len(s)\n    assert n >= 1\n    rnk = [0] * n\n    for\
    \ i, v in enumerate(sa):\n        rnk[v] = i\n    lcp = [0] * (n - 1)\n    h =\
    \ 0\n    for i in range(n):\n        if h:\n            h -= 1\n        if rnk[i]\
    \ == 0:\n            continue\n        j = sa[rnk[i] - 1]\n        while j + h\
    \ < n and i + h < n and s[j + h] == s[i + h]:\n            h += 1\n        lcp[rnk[i]\
    \ - 1] = h\n    return lcp\n\n\n# suffix \u3092\u30BD\u30FC\u30C8\u3057\u3066\
    \ T <= x \u306A\u308B suffix x \u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u3092\
    \u8FD4\u3059\n# T <= S[SA[i] : SA[i] + len(T)] \u3092\u6E80\u305F\u3059\u6700\u5C0F\
    \u306E i\ndef suffix_array_bisect(S, SA, T):\n    ng, ok = -1, len(S)\n    while\
    \ ok - ng > 1:\n        mid = (ok + ng) // 2\n        idx = SA[mid]\n        if\
    \ T <= S[idx : idx + len(T)]:\n            ok = mid\n        else:\n         \
    \   ng = mid\n    return ok\n\n\n# SA = suffix_array(S)\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/string/SuffixArray.py
  requiredBy: []
  timestamp: '2026-11-26 00:25:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/string/SuffixArray.py
layout: document
redirect_from:
- /library/algorithm_library/python/string/SuffixArray.py
- /library/algorithm_library/python/string/SuffixArray.py.html
title: algorithm_library/python/string/SuffixArray.py
---
