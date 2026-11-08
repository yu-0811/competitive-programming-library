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
    - https://judge.yosupo.jp/problem/longest_common_substring
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/longest_common_substring\n# include:\
    \ algorithm_library/python/string/RollingHash.py\n\n\ndef main():\n    S = readline().decode().strip()\n\
    \    T = readline().decode().strip()\n    left, right = RollingHash(S), RollingHash(T)\n\
    \    n, m = len(S), len(T)\n\n    def find(length):\n        positions = {left.get_hash(i,\
    \ i + length): i for i in range(n - length + 1)}\n        for j in range(m - length\
    \ + 1):\n            key = right.get_hash(j, j + length)\n            if key in\
    \ positions:\n                return positions[key], j\n        return None\n\n\
    \    lo, hi = 0, min(n, m) + 1\n    a = b = 0\n    while hi - lo > 1:\n      \
    \  length = (lo + hi) // 2\n        match = find(length)\n        if match is\
    \ None:\n            hi = length\n        else:\n            lo = length\n   \
    \         a, b = match\n    print(a, a + lo, b, b + lo)\n\n\nif __name__ == \"\
    __main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/string/longest_common_substring_rollinghash.py
  requiredBy: []
  timestamp: '2026-11-08 19:01:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/string/longest_common_substring_rollinghash.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/string/longest_common_substring_rollinghash.py
- /library/library-checker-submitcode/src/string/longest_common_substring_rollinghash.py.html
title: library-checker-submitcode/src/string/longest_common_substring_rollinghash.py
---
