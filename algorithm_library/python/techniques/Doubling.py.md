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
  code: "from array import array\ndef doubling(nxt: list[int], max_steps: int) ->\
    \ list[array]:\n    \"\"\"\n    nxt: \u72B6\u614Bi\u304B\u30891\u56DE\u9077\u79FB\
    \u3057\u305F\u5F8C\u306E\u72B6\u614Bnxt[i]\n    max_steps: \u6700\u5927\u9077\u79FB\
    \u56DE\u6570\n    return dp[i][v] := v \u304B\u3089 2**i \u56DE\u9077\u79FB\u3057\
    \u305F\u5148\n    \"\"\"\n    assert all(0 <= v < len(nxt) for v in nxt)\n   \
    \ dp = [array('I', nxt)]\n    for _ in range(1, max_steps.bit_length()):\n   \
    \     prev = dp[-1]\n        cur = array('I', [0]) * len(prev)\n        for v\
    \ in range(len(prev)): cur[v] = prev[prev[v]]\n        dp.append(cur)\n    return\
    \ dp\n\n\ndef query(dp, j, k):\n    \"\"\"\n    j \u304B\u3089\u59CB\u3081\u3066\
    \ k \u56DE\u79FB\u52D5\u3059\u308B\n    \"\"\"\n    tmp = j\n    while k:\n  \
    \      i = k.bit_length() - 1\n        tmp = dp[i][tmp]\n        k ^= 1 << i\n\
    \    return tmp\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/python/techniques/Doubling.py
  requiredBy: []
  timestamp: '2026-11-10 18:33:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/python/techniques/Doubling.py
layout: document
redirect_from:
- /library/algorithm_library/python/techniques/Doubling.py
- /library/algorithm_library/python/techniques/Doubling.py.html
title: algorithm_library/python/techniques/Doubling.py
---
