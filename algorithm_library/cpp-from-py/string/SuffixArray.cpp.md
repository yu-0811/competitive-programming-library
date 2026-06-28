---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/string/SuffixArray.cpp\"\n\
    #include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> sa_is(const vector<int>&\
    \ s, int upper) {\n    int n = (int)s.size();\n    if (n == 0) return {};\n  \
    \  if (n == 1) return {0};\n    if (n == 2) return s[0] < s[1] ? vector<int>{0,\
    \ 1} : vector<int>{1, 0};\n    vector<int> sa(n), ls(n);\n    for (int i = n -\
    \ 2; i >= 0; i--) ls[i] = (s[i] == s[i + 1]) ? ls[i + 1] : (s[i] < s[i + 1]);\n\
    \    vector<int> sum_l(upper + 1), sum_s(upper + 1);\n    for (int i = 0; i <\
    \ n; i++) {\n        if (!ls[i]) sum_s[s[i]]++;\n        else sum_l[s[i] + 1]++;\n\
    \    }\n    for (int i = 0; i <= upper; i++) {\n        sum_s[i] += sum_l[i];\n\
    \        if (i < upper) sum_l[i + 1] += sum_s[i];\n    }\n    auto induce = [&](const\
    \ vector<int>& lms) {\n        fill(sa.begin(), sa.end(), -1);\n        vector<int>\
    \ buf = sum_s;\n        for (int d : lms) {\n            if (d == n) continue;\n\
    \            sa[buf[s[d]]++] = d;\n        }\n        buf = sum_l;\n        sa[buf[s[n\
    \ - 1]]++] = n - 1;\n        for (int i = 0; i < n; i++) {\n            int v\
    \ = sa[i];\n            if (v >= 1 && !ls[v - 1]) sa[buf[s[v - 1]]++] = v - 1;\n\
    \        }\n        buf = sum_l;\n        for (int i = n - 1; i >= 0; i--) {\n\
    \            int v = sa[i];\n            if (v >= 1 && ls[v - 1]) sa[--buf[s[v\
    \ - 1] + 1]] = v - 1;\n        }\n    };\n    vector<int> lms_map(n + 1, -1);\n\
    \    int m = 0;\n    for (int i = 1; i < n; i++) if (!ls[i - 1] && ls[i]) lms_map[i]\
    \ = m++;\n    vector<int> lms;\n    for (int i = 1; i < n; i++) if (!ls[i - 1]\
    \ && ls[i]) lms.push_back(i);\n    induce(lms);\n    if (m) {\n        vector<int>\
    \ sorted_lms;\n        for (int v : sa) if (v >= 0 && lms_map[v] != -1) sorted_lms.push_back(v);\n\
    \        vector<int> rec_s(m);\n        int rec_upper = 0;\n        rec_s[lms_map[sorted_lms[0]]]\
    \ = 0;\n        for (int i = 1; i < m; i++) {\n            int l = sorted_lms[i\
    \ - 1], r = sorted_lms[i];\n            int end_l = (lms_map[l] + 1 < m) ? lms[lms_map[l]\
    \ + 1] : n;\n            int end_r = (lms_map[r] + 1 < m) ? lms[lms_map[r] + 1]\
    \ : n;\n            bool same = true;\n            if (end_l - l != end_r - r)\
    \ same = false;\n            else {\n                while (l < end_l) {\n   \
    \                 if (s[l] != s[r]) break;\n                    l++;\n       \
    \             r++;\n                }\n                if (l == n || s[l] != s[r])\
    \ same = false;\n            }\n            if (!same) rec_upper++;\n        \
    \    rec_s[lms_map[sorted_lms[i]]] = rec_upper;\n        }\n        vector<int>\
    \ rec_sa = sa_is(rec_s, rec_upper);\n        for (int i = 0; i < m; i++) sorted_lms[i]\
    \ = lms[rec_sa[i]];\n        induce(sorted_lms);\n    }\n    return sa;\n}\n\n\
    vector<int> suffix_array_upper(const vector<int>& s, int upper) {\n    assert(0\
    \ <= upper);\n    for (int d : s) assert(0 <= d && d <= upper);\n    return sa_is(s,\
    \ upper);\n}\n\nvector<int> suffix_array(const string& s) {\n    vector<int> s2(s.size());\n\
    \    for (int i = 0; i < (int)s.size(); i++) s2[i] = (unsigned char)s[i];\n  \
    \  return sa_is(s2, 255);\n}\n\ntemplate <class T>\nvector<int> suffix_array(const\
    \ vector<T>& s) {\n    int n = (int)s.size();\n    vector<int> idx(n);\n    iota(idx.begin(),\
    \ idx.end(), 0);\n    sort(idx.begin(), idx.end(), [&](int i, int j) { return\
    \ s[i] < s[j]; });\n    vector<int> s2(n);\n    int now = 0;\n    for (int i =\
    \ 0; i < n; i++) {\n        if (i && s[idx[i - 1]] != s[idx[i]]) now++;\n    \
    \    s2[idx[i]] = now;\n    }\n    return sa_is(s2, now);\n}\n\nvector<int> lcp_array(const\
    \ string& s, const vector<int>& sa) {\n    int n = (int)s.size();\n    assert(n\
    \ >= 1);\n    vector<int> rnk(n), lcp(n - 1);\n    for (int i = 0; i < n; i++)\
    \ rnk[sa[i]] = i;\n    int h = 0;\n    for (int i = 0; i < n; i++) {\n       \
    \ if (h > 0) h--;\n        if (rnk[i] == 0) continue;\n        int j = sa[rnk[i]\
    \ - 1];\n        while (j + h < n && i + h < n && s[j + h] == s[i + h]) h++;\n\
    \        lcp[rnk[i] - 1] = h;\n    }\n    return lcp;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nvector<int> sa_is(const\
    \ vector<int>& s, int upper) {\n    int n = (int)s.size();\n    if (n == 0) return\
    \ {};\n    if (n == 1) return {0};\n    if (n == 2) return s[0] < s[1] ? vector<int>{0,\
    \ 1} : vector<int>{1, 0};\n    vector<int> sa(n), ls(n);\n    for (int i = n -\
    \ 2; i >= 0; i--) ls[i] = (s[i] == s[i + 1]) ? ls[i + 1] : (s[i] < s[i + 1]);\n\
    \    vector<int> sum_l(upper + 1), sum_s(upper + 1);\n    for (int i = 0; i <\
    \ n; i++) {\n        if (!ls[i]) sum_s[s[i]]++;\n        else sum_l[s[i] + 1]++;\n\
    \    }\n    for (int i = 0; i <= upper; i++) {\n        sum_s[i] += sum_l[i];\n\
    \        if (i < upper) sum_l[i + 1] += sum_s[i];\n    }\n    auto induce = [&](const\
    \ vector<int>& lms) {\n        fill(sa.begin(), sa.end(), -1);\n        vector<int>\
    \ buf = sum_s;\n        for (int d : lms) {\n            if (d == n) continue;\n\
    \            sa[buf[s[d]]++] = d;\n        }\n        buf = sum_l;\n        sa[buf[s[n\
    \ - 1]]++] = n - 1;\n        for (int i = 0; i < n; i++) {\n            int v\
    \ = sa[i];\n            if (v >= 1 && !ls[v - 1]) sa[buf[s[v - 1]]++] = v - 1;\n\
    \        }\n        buf = sum_l;\n        for (int i = n - 1; i >= 0; i--) {\n\
    \            int v = sa[i];\n            if (v >= 1 && ls[v - 1]) sa[--buf[s[v\
    \ - 1] + 1]] = v - 1;\n        }\n    };\n    vector<int> lms_map(n + 1, -1);\n\
    \    int m = 0;\n    for (int i = 1; i < n; i++) if (!ls[i - 1] && ls[i]) lms_map[i]\
    \ = m++;\n    vector<int> lms;\n    for (int i = 1; i < n; i++) if (!ls[i - 1]\
    \ && ls[i]) lms.push_back(i);\n    induce(lms);\n    if (m) {\n        vector<int>\
    \ sorted_lms;\n        for (int v : sa) if (v >= 0 && lms_map[v] != -1) sorted_lms.push_back(v);\n\
    \        vector<int> rec_s(m);\n        int rec_upper = 0;\n        rec_s[lms_map[sorted_lms[0]]]\
    \ = 0;\n        for (int i = 1; i < m; i++) {\n            int l = sorted_lms[i\
    \ - 1], r = sorted_lms[i];\n            int end_l = (lms_map[l] + 1 < m) ? lms[lms_map[l]\
    \ + 1] : n;\n            int end_r = (lms_map[r] + 1 < m) ? lms[lms_map[r] + 1]\
    \ : n;\n            bool same = true;\n            if (end_l - l != end_r - r)\
    \ same = false;\n            else {\n                while (l < end_l) {\n   \
    \                 if (s[l] != s[r]) break;\n                    l++;\n       \
    \             r++;\n                }\n                if (l == n || s[l] != s[r])\
    \ same = false;\n            }\n            if (!same) rec_upper++;\n        \
    \    rec_s[lms_map[sorted_lms[i]]] = rec_upper;\n        }\n        vector<int>\
    \ rec_sa = sa_is(rec_s, rec_upper);\n        for (int i = 0; i < m; i++) sorted_lms[i]\
    \ = lms[rec_sa[i]];\n        induce(sorted_lms);\n    }\n    return sa;\n}\n\n\
    vector<int> suffix_array_upper(const vector<int>& s, int upper) {\n    assert(0\
    \ <= upper);\n    for (int d : s) assert(0 <= d && d <= upper);\n    return sa_is(s,\
    \ upper);\n}\n\nvector<int> suffix_array(const string& s) {\n    vector<int> s2(s.size());\n\
    \    for (int i = 0; i < (int)s.size(); i++) s2[i] = (unsigned char)s[i];\n  \
    \  return sa_is(s2, 255);\n}\n\ntemplate <class T>\nvector<int> suffix_array(const\
    \ vector<T>& s) {\n    int n = (int)s.size();\n    vector<int> idx(n);\n    iota(idx.begin(),\
    \ idx.end(), 0);\n    sort(idx.begin(), idx.end(), [&](int i, int j) { return\
    \ s[i] < s[j]; });\n    vector<int> s2(n);\n    int now = 0;\n    for (int i =\
    \ 0; i < n; i++) {\n        if (i && s[idx[i - 1]] != s[idx[i]]) now++;\n    \
    \    s2[idx[i]] = now;\n    }\n    return sa_is(s2, now);\n}\n\nvector<int> lcp_array(const\
    \ string& s, const vector<int>& sa) {\n    int n = (int)s.size();\n    assert(n\
    \ >= 1);\n    vector<int> rnk(n), lcp(n - 1);\n    for (int i = 0; i < n; i++)\
    \ rnk[sa[i]] = i;\n    int h = 0;\n    for (int i = 0; i < n; i++) {\n       \
    \ if (h > 0) h--;\n        if (rnk[i] == 0) continue;\n        int j = sa[rnk[i]\
    \ - 1];\n        while (j + h < n && i + h < n && s[j + h] == s[i + h]) h++;\n\
    \        lcp[rnk[i] - 1] = h;\n    }\n    return lcp;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/string/SuffixArray.cpp
  requiredBy: []
  timestamp: '2026-06-28 23:41:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/string/SuffixArray.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/string/SuffixArray.cpp
- /library/algorithm_library/cpp-from-py/string/SuffixArray.cpp.html
title: algorithm_library/cpp-from-py/string/SuffixArray.cpp
---
