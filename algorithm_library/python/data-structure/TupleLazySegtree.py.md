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
  code: "class Columns2:\n    __slots__ = (\"a\", \"b\")\n\n    def __init__(s, n,\
    \ e):\n        s.a = [e[0]] * n\n        s.b = [e[1]] * n\n\n    def __getitem__(s,\
    \ i):\n        return s.a[i], s.b[i]\n\n    def __setitem__(s, i, x):\n      \
    \  s.a[i], s.b[i] = x\n\n\nclass Columns3:\n    __slots__ = (\"a\", \"b\", \"\
    c\")\n\n    def __init__(s, n, e):\n        s.a = [e[0]] * n\n        s.b = [e[1]]\
    \ * n\n        s.c = [e[2]] * n\n\n    def __getitem__(s, i):\n        return\
    \ s.a[i], s.b[i], s.c[i]\n\n    def __setitem__(s, i, x):\n        s.a[i], s.b[i],\
    \ s.c[i] = x\n\n\n# 4\u6210\u5206\u4EE5\u4E0A\u306F\u540C\u3058\u5F62\u306E\u30AF\
    \u30E9\u30B9\u3092\u7528\u610F\u3057\u3001\u3053\u306E\u8F9E\u66F8\u306B\u8FFD\
    \u52A0\u3059\u308B\u3002\nCOLUMN_TYPES = {2: Columns2, 3: Columns3}\n\n\nclass\
    \ TupleLazySegtree:\n    # \u30BF\u30D7\u30EB\u3092\u305D\u306E\u307E\u307E\u8F09\
    \u305B\u308B\u3060\u3051\u3067\u3044\u3044\n    def __init__(s, v, op, e, mp,\
    \ comp, ide):\n        s.n = len(v)\n        s.log = (max(1, s.n) - 1).bit_length()\n\
    \        z = s.z = 1 << s.log\n        s.e = e = tuple(e)\n        s.ide = ide\
    \ = tuple(ide)\n        s.op = op\n        s.mp = mp\n        s.comp = comp\n\
    \        assert len(e) in COLUMN_TYPES and len(ide) in COLUMN_TYPES\n        d\
    \ = s.d = COLUMN_TYPES[len(e)](2 * z, e)\n        s.lz = COLUMN_TYPES[len(ide)](z,\
    \ ide)\n        s.pend = [False] * z\n        for i, value in enumerate(v, z):\n\
    \            d[i] = value\n        for i in range(z - 1, 0, -1):\n           \
    \ d[i] = op(d[2 * i], d[2 * i + 1])\n\n    def _push(s, k):\n        pend = s.pend\n\
    \        if not pend[k]:\n            return\n        d, lz, mp, comp = s.d, s.lz,\
    \ s.mp, s.comp\n        f = lz[k]\n        c = 2 * k\n        d[c] = mp(f, d[c])\n\
    \        d[c + 1] = mp(f, d[c + 1])\n        if c < s.z:\n            lz[c] =\
    \ comp(f, lz[c]) if pend[c] else f\n            lz[c + 1] = comp(f, lz[c + 1])\
    \ if pend[c + 1] else f\n            pend[c] = pend[c + 1] = True\n        pend[k]\
    \ = False\n\n    def set(s, p, x):\n        \"\"\"p \u756A\u76EE\u306E\u5024\u3092\
    \u30BF\u30D7\u30EB x \u306B\u66F4\u65B0\u3059\u308B\u3002\"\"\"\n        assert\
    \ 0 <= p < s.n\n        d, op, push = s.d, s.op, s._push\n        p += s.z\n \
    \       for i in range(s.log, 0, -1):\n            push(p >> i)\n        d[p]\
    \ = x\n        p >>= 1\n        while p:\n            d[p] = op(d[2 * p], d[2\
    \ * p + 1])\n            p >>= 1\n\n    def get(s, p):\n        assert 0 <= p\
    \ < s.n\n        push = s._push\n        p += s.z\n        for i in range(s.log,\
    \ 0, -1):\n            push(p >> i)\n        return s.d[p]\n\n    def prod(s,\
    \ l, r):\n        assert 0 <= l <= r <= s.n\n        if l == r:\n            return\
    \ s.e\n        d, op, push = s.d, s.op, s._push\n        l += s.z\n        r +=\
    \ s.z\n        left = (l & -l).bit_length()\n        right = (r & -r).bit_length()\n\
    \        for i in range(s.log, 0, -1):\n            if i >= left:\n          \
    \      push(l >> i)\n            if i >= right:\n                push(r >> i)\n\
    \        sml = smr = s.e\n        while l < r:\n            if l & 1:\n      \
    \          sml = op(sml, d[l])\n                l += 1\n            if r & 1:\n\
    \                smr = op(d[r - 1], smr)\n            l >>= 1\n            r >>=\
    \ 1\n        return op(sml, smr)\n\n    def all_prod(s):\n        return s.d[1]\n\
    \n    def apply_point(s, p, f):\n        assert 0 <= p < s.n\n        d, op, push\
    \ = s.d, s.op, s._push\n        p += s.z\n        for i in range(s.log, 0, -1):\n\
    \            push(p >> i)\n        d[p] = s.mp(f, d[p])\n        p >>= 1\n   \
    \     while p:\n            d[p] = op(d[2 * p], d[2 * p + 1])\n            p >>=\
    \ 1\n\n    def apply(s, l, r, f):\n        assert 0 <= l <= r <= s.n\n       \
    \ if l == r:\n            return\n        d, lz, pend = s.d, s.lz, s.pend\n  \
    \      op, mp, comp = s.op, s.mp, s.comp\n        push, z = s._push, s.z\n   \
    \     l += z\n        r += z\n        left = (l & -l).bit_length()\n        right\
    \ = (r & -r).bit_length()\n        for i in range(s.log, 0, -1):\n           \
    \ if i >= left:\n                push(l >> i)\n            if i >= right:\n  \
    \              push(r >> i)\n        l2, r2 = l, r\n        while l < r:\n   \
    \         if l & 1:\n                d[l] = mp(f, d[l])\n                if l\
    \ < z:\n                    lz[l] = comp(f, lz[l]) if pend[l] else f\n       \
    \             pend[l] = True\n                l += 1\n            if r & 1:\n\
    \                r -= 1\n                d[r] = mp(f, d[r])\n                if\
    \ r < z:\n                    lz[r] = comp(f, lz[r]) if pend[r] else f\n     \
    \               pend[r] = True\n            l >>= 1\n            r >>= 1\n   \
    \     for i in range(1, s.log + 1):\n            if i >= left:\n             \
    \   k = l2 >> i\n                d[k] = op(d[2 * k], d[2 * k + 1])\n         \
    \   if i >= right:\n                k = r2 >> i\n                d[k] = op(d[2\
    \ * k], d[2 * k + 1])\n\n    def max_right(s, l, check):\n        \"\"\"check(prod(l,\
    \ r)) \u3092\u6E80\u305F\u3059\u6700\u5927\u306E r\u3002check(e) \u304C\u771F\u3067\
    \u5358\u8ABF\u3067\u3042\u308B\u3053\u3068\u3002\"\"\"\n        assert 0 <= l\
    \ <= s.n\n        assert check(s.e)\n        if l == s.n:\n            return\
    \ s.n\n        d, op, push = s.d, s.op, s._push\n        z = s.z\n        l +=\
    \ z\n        for i in range(s.log, 0, -1):\n            push(l >> i)\n       \
    \ sm = s.e\n        while True:\n            while l % 2 == 0:\n             \
    \   l >>= 1\n            nxt = op(sm, d[l])\n            if not check(nxt):\n\
    \                while l < z:\n                    push(l)\n                 \
    \   l *= 2\n                    nxt = op(sm, d[l])\n                    if check(nxt):\n\
    \                        sm = nxt\n                        l += 1\n          \
    \      return l - z\n            sm = nxt\n            l += 1\n            if\
    \ (l & -l) == l:\n                return s.n\n\n    def min_left(s, r, check):\n\
    \        \"\"\"check(prod(l, r)) \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E l\u3002\
    check(e) \u304C\u771F\u3067\u5358\u8ABF\u3067\u3042\u308B\u3053\u3068\u3002\"\"\
    \"\n        assert 0 <= r <= s.n\n        assert check(s.e)\n        if r == 0:\n\
    \            return 0\n        d, op, push = s.d, s.op, s._push\n        z = s.z\n\
    \        r += z\n        for i in range(s.log, 0, -1):\n            push((r -\
    \ 1) >> i)\n        sm = s.e\n        while True:\n            r -= 1\n      \
    \      while r > 1 and r % 2:\n                r >>= 1\n            nxt = op(d[r],\
    \ sm)\n            if not check(nxt):\n                while r < z:\n        \
    \            push(r)\n                    r = 2 * r + 1\n                    nxt\
    \ = op(d[r], sm)\n                    if check(nxt):\n                       \
    \ sm = nxt\n                        r -= 1\n                return r + 1 - z\n\
    \            sm = nxt\n            if (r & -r) == r:\n                return 0\n\
    \n    def __str__(s):\n        return str([s.get(i) for i in range(s.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/data-structure/TupleLazySegtree.py
  requiredBy: []
  timestamp: '2026-10-25 10:12:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/data-structure/TupleLazySegtree.py
layout: document
redirect_from:
- /library/algorithm_library/python/data-structure/TupleLazySegtree.py
- /library/algorithm_library/python/data-structure/TupleLazySegtree.py.html
title: algorithm_library/python/data-structure/TupleLazySegtree.py
---
