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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from warnings import warn\n\n\nclass segtree:  # \u3059\u3079\u3066 0-index\n\
    \    def __init__(s, v, op, e):\n        s.n = len(v)\n        s.op = op\n   \
    \     s.e = e\n        s.z = 1 << (s.n - 1).bit_length()\n        d = s.d = [e]\
    \ * (2 * s.z)\n        d[s.z : s.z + s.n] = v\n        for i in range(s.z - 1,\
    \ 0, -1):\n            d[i] = op(d[2 * i], d[2 * i + 1])\n\n    # 1 \u70B9\u66F4\
    \u65B0\n    def set(s, p, x):\n        assert 0 <= p and p < s.n\n        d, op\
    \ = s.d, s.op\n        p += s.z\n        d[p] = x\n        p >>= 1\n        while\
    \ p:\n            d[p] = op(d[2 * p], d[2 * p + 1])\n            p >>= 1\n\n \
    \   # 1 \u70B9\u52A0\u7B97\n    def add(s, p, x):\n        assert 0 <= p and p\
    \ < s.n\n        d, op = s.d, s.op\n        p += s.z\n        d[p] += x\n    \
    \    p >>= 1\n        while p:\n            d[p] = op(d[2 * p], d[2 * p + 1])\n\
    \            p >>= 1\n\n    # \u5143\u306E\u914D\u5217\u306E p \u756A\u76EE\u306E\
    \u8981\u7D20\u3092\u53D6\u5F97\n    def get(s, p):\n        assert 0 <= p and\
    \ p < s.n\n        return s.d[p + s.z]\n\n    # [l,r) \u306E\u6F14\u7B97\u7D50\
    \u679C\u3092\u8FD4\u3059\n    def prod(s, l, r):\n        assert 0 <= l and l\
    \ <= r and r <= s.n\n        if l == r:\n            warn(\"l=r in prod(l,r)\"\
    )\n            return s.e\n        d, op = s.d, s.op\n        sml = smr = s.e\n\
    \        l += s.z\n        r += s.z\n        while l < r:\n            if l &\
    \ 1:\n                sml = op(sml, d[l])\n                l += 1\n          \
    \  if r & 1:\n                smr = op(d[r - 1], smr)\n            l >>= 1\n \
    \           r >>= 1\n        return op(sml, smr)\n\n    # \u5168\u533A\u9593\u306E\
    \u6F14\u7B97\u7D50\u679C\u3092\u8FD4\u3059\n    def all_prod(s):\n        return\
    \ s.d[1]\n\n    # check(operate(data[l],data[l+1],...,data[r-1])) = True\n   \
    \ # \u3092\u6E80\u305F\u3059\u6700\u5927\u306E r \u3092\u8FD4\u3059\n    def max_right(s,\
    \ l, check):\n        assert 0 <= l and l <= s.n\n        assert check(s.e)\n\
    \        if l == s.n:\n            return s.n\n        l += s.z\n        sm =\
    \ s.e\n        while True:\n            while l % 2 == 0:\n                l >>=\
    \ 1\n            if not (check(s.op(sm, s.d[l]))):\n                while l <\
    \ s.z:\n                    l = 2 * l\n                    if check(s.op(sm, s.d[l])):\n\
    \                        sm = s.op(sm, s.d[l])\n                        l += 1\n\
    \                return l - s.z\n            sm = s.op(sm, s.d[l])\n         \
    \   l += 1\n            if (l & -l) == l:\n                break\n        return\
    \ s.n\n\n    # check(operate(data[l],data[l+1],...,data[r-1])) = True\n    # \u3092\
    \u6E80\u305F\u3059\u6700\u5C0F\u306E l \u3092\u8FD4\u3059\n    def min_left(s,\
    \ r, check):\n        assert 0 <= r and r <= s.n\n        assert check(s.e)\n\
    \        if r == 0:\n            return 0\n        r += s.z\n        sm = s.e\n\
    \        while True:\n            r -= 1\n            while r > 1 and (r % 2):\n\
    \                r >>= 1\n            if not (check(s.op(s.d[r], sm))):\n    \
    \            while r < s.z:\n                    r = 2 * r + 1\n             \
    \       if check(s.op(s.d[r], sm)):\n                        sm = s.op(s.d[r],\
    \ sm)\n                        r -= 1\n                return r + 1 - s.z\n  \
    \          sm = s.op(s.d[r], sm)\n            if (r & -r) == r:\n            \
    \    break\n        return 0\n\n    # print(seg) \u3067\u8449\u306E\u5024\uFF08\
    \u5143\u306E\u914D\u5217\uFF09\u3092\u8868\u793A\u3059\u308B\n    def __str__(s):\n\
    \        return str([s.get(i) for i in range(s.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/Segtree.py
  requiredBy: []
  timestamp: '2026-10-25 10:02:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/Segtree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/Segtree.py
- /library/algorithm_library/python/data-structure/Segtree.py.html
title: algorithm_library/python/data-structure/Segtree.py
---
