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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# problem: https://judge.yosupo.jp/problem/longest_common_substring\n# include:\
    \ algorithm_library/python/string/SuffixArray.py\n\n\ndef main():\n    S = readline().decode().strip()\n\
    \    T = readline().decode().strip()\n    split = len(S)\n    text = S + \"$\"\
    \ + T\n    sa = suffix_array(text)\n    lcp = lcp_array(text, sa)\n    best =\
    \ a = c = 0\n    for i, length in enumerate(lcp):\n        u, v = sa[i], sa[i\
    \ + 1]\n        if u > v:\n            u, v = v, u\n        if u < split < v and\
    \ length > best:\n            best, a, c = length, u, v - split - 1\n    print(a,\
    \ a + best, c, c + best)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: library-checker-submitcode/src/string/longest_common_substring.py
  requiredBy: []
  timestamp: '2026-10-20 13:27:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library-checker-submitcode/src/string/longest_common_substring.py
layout: document
redirect_from:
- /library/library-checker-submitcode/src/string/longest_common_substring.py
- /library/library-checker-submitcode/src/string/longest_common_substring.py.html
title: library-checker-submitcode/src/string/longest_common_substring.py
---
