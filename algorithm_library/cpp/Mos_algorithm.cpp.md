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
  bundledCode: "#line 1 \"algorithm_library/cpp/Mos_algorithm.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nstruct Mo {\n  // \u521D\u671F\u5316 : Mo \u5909\u6570\
    \u540D(\u6570\u5217\u306E\u9577\u3055)\n  // \u30AF\u30A8\u30EA\u8FFD\u52A0 :\
    \ \u5909\u6570\u540D.add(\u30AF\u30A8\u30EA\u306E\u5DE6\u7AEF, \u30AF\u30A8\u30EA\
    \u306E\u53F3\u7AEF) <- \u534A\u958B\u533A\u9593\n  // \u30AF\u30A8\u30EA\u51E6\
    \u7406 : Mo\u5909\u6570\u540D.build(\u8FFD\u52A0\u51E6\u7406, \u524A\u9664\u51E6\
    \u7406, \u30AF\u30A8\u30EA\u51E6\u7406)\n  // \u30E9\u30E0\u30C0\u5F0F\u3067 add,\
    \ erase, out \u3092\u5B9A\u7FA9\u3057\u3066 build \u306B\u6E21\u3059\n  // add(int\
    \ i) : i \u756A\u76EE\u306E\u8981\u7D20\u3092\u8FFD\u52A0\u3059\u308B\u51E6\u7406\
    \n  // erase(int i) : i \u756A\u76EE\u306E\u8981\u7D20\u3092\u524A\u9664\u3059\
    \u308B\u51E6\u7406\n  // out(int q) : q \u756A\u76EE\u306E\u30AF\u30A8\u30EA\u306E\
    \u51E6\u7406\n  // add, erase, out \u304B\u3089\u306F main \u95A2\u6570\u5185\u306E\
    \u5909\u6570\u306B\u5F15\u6570\u306B\u4F55\u3082\u6E21\u3055\u305A\u306B\u30A2\
    \u30AF\u30BB\u30B9\u3067\u304D\u308B\n  // auto add = [&](int i) { ... };\n  //\
    \ auto erase = [&](int i) { ... };\n  // auto out = [&](int q) { ... };\n\n  int\
    \ n; vector<pair<int, int>> lr;\n  \n  explicit Mo(int n) : n(n) {}\n\n  void\
    \ add(int l, int r) { /* [l, r) */\n    lr.emplace_back(l, r);\n  }\n\n  // \u53F3\
    \u62E1\u5F35\u3068\u5DE6\u62E1\u5F35\u3067\u5225\u306E\u95A2\u6570\u3092\u4F7F\
    \u3046\u5834\u5408\u306F\u3053\u3063\u3061\u304C\u76F4\u63A5\u547C\u3073\u51FA\
    \u3055\u308C\u308B\n  template< typename AL, typename AR, typename EL, typename\
    \ ER, typename O >\n  void build(const AL &add_left, const AR &add_right, const\
    \ EL &erase_left, const ER &erase_right, const O &out) {\n    int q = (int) lr.size();\n\
    \    int bs = n / min< int >(n, sqrt(q));\n    vector< int > ord(q);\n    iota(begin(ord),\
    \ end(ord), 0);\n    sort(begin(ord), end(ord), [&](int a, int b) {\n      int\
    \ ablock = lr[a].first / bs, bblock = lr[b].first / bs;\n      if(ablock != bblock)\
    \ return ablock < bblock;\n      return (ablock & 1) ? lr[a].second > lr[b].second\
    \ : lr[a].second < lr[b].second;\n    });\n    int l = 0, r = 0;\n    for(auto\
    \ idx : ord) {\n      while(l > lr[idx].first) add_left(--l);\n      while(r <\
    \ lr[idx].second) add_right(r++);\n      while(l < lr[idx].first) erase_left(l++);\n\
    \      while(r > lr[idx].second) erase_right(--r);\n      out(idx);\n    }\n \
    \ }\n\n  // add : \u62E1\u5F35\u51E6\u7406\n  // erase : \u7E2E\u5C0F\u51E6\u7406\
    \n  // out : \u30AF\u30A8\u30EA\u89E3\u7B54\u51E6\u7406\n  template< typename\
    \ A, typename E, typename O >\n  void build(const A &add, const E &erase, const\
    \ O &out) {\n    build(add, add, erase, erase, out);\n  }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct Mo {\n  // \u521D\
    \u671F\u5316 : Mo \u5909\u6570\u540D(\u6570\u5217\u306E\u9577\u3055)\n  // \u30AF\
    \u30A8\u30EA\u8FFD\u52A0 : \u5909\u6570\u540D.add(\u30AF\u30A8\u30EA\u306E\u5DE6\
    \u7AEF, \u30AF\u30A8\u30EA\u306E\u53F3\u7AEF) <- \u534A\u958B\u533A\u9593\n  //\
    \ \u30AF\u30A8\u30EA\u51E6\u7406 : Mo\u5909\u6570\u540D.build(\u8FFD\u52A0\u51E6\
    \u7406, \u524A\u9664\u51E6\u7406, \u30AF\u30A8\u30EA\u51E6\u7406)\n  // \u30E9\
    \u30E0\u30C0\u5F0F\u3067 add, erase, out \u3092\u5B9A\u7FA9\u3057\u3066 build\
    \ \u306B\u6E21\u3059\n  // add(int i) : i \u756A\u76EE\u306E\u8981\u7D20\u3092\
    \u8FFD\u52A0\u3059\u308B\u51E6\u7406\n  // erase(int i) : i \u756A\u76EE\u306E\
    \u8981\u7D20\u3092\u524A\u9664\u3059\u308B\u51E6\u7406\n  // out(int q) : q \u756A\
    \u76EE\u306E\u30AF\u30A8\u30EA\u306E\u51E6\u7406\n  // add, erase, out \u304B\u3089\
    \u306F main \u95A2\u6570\u5185\u306E\u5909\u6570\u306B\u5F15\u6570\u306B\u4F55\
    \u3082\u6E21\u3055\u305A\u306B\u30A2\u30AF\u30BB\u30B9\u3067\u304D\u308B\n  //\
    \ auto add = [&](int i) { ... };\n  // auto erase = [&](int i) { ... };\n  //\
    \ auto out = [&](int q) { ... };\n\n  int n; vector<pair<int, int>> lr;\n  \n\
    \  explicit Mo(int n) : n(n) {}\n\n  void add(int l, int r) { /* [l, r) */\n \
    \   lr.emplace_back(l, r);\n  }\n\n  // \u53F3\u62E1\u5F35\u3068\u5DE6\u62E1\u5F35\
    \u3067\u5225\u306E\u95A2\u6570\u3092\u4F7F\u3046\u5834\u5408\u306F\u3053\u3063\
    \u3061\u304C\u76F4\u63A5\u547C\u3073\u51FA\u3055\u308C\u308B\n  template< typename\
    \ AL, typename AR, typename EL, typename ER, typename O >\n  void build(const\
    \ AL &add_left, const AR &add_right, const EL &erase_left, const ER &erase_right,\
    \ const O &out) {\n    int q = (int) lr.size();\n    int bs = n / min< int >(n,\
    \ sqrt(q));\n    vector< int > ord(q);\n    iota(begin(ord), end(ord), 0);\n \
    \   sort(begin(ord), end(ord), [&](int a, int b) {\n      int ablock = lr[a].first\
    \ / bs, bblock = lr[b].first / bs;\n      if(ablock != bblock) return ablock <\
    \ bblock;\n      return (ablock & 1) ? lr[a].second > lr[b].second : lr[a].second\
    \ < lr[b].second;\n    });\n    int l = 0, r = 0;\n    for(auto idx : ord) {\n\
    \      while(l > lr[idx].first) add_left(--l);\n      while(r < lr[idx].second)\
    \ add_right(r++);\n      while(l < lr[idx].first) erase_left(l++);\n      while(r\
    \ > lr[idx].second) erase_right(--r);\n      out(idx);\n    }\n  }\n\n  // add\
    \ : \u62E1\u5F35\u51E6\u7406\n  // erase : \u7E2E\u5C0F\u51E6\u7406\n  // out\
    \ : \u30AF\u30A8\u30EA\u89E3\u7B54\u51E6\u7406\n  template< typename A, typename\
    \ E, typename O >\n  void build(const A &add, const E &erase, const O &out) {\n\
    \    build(add, add, erase, erase, out);\n  }\n};"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/Mos_algorithm.cpp
  requiredBy: []
  timestamp: '2025-11-30 11:50:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/Mos_algorithm.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/Mos_algorithm.cpp
- /library/algorithm_library/cpp/Mos_algorithm.cpp.html
title: algorithm_library/cpp/Mos_algorithm.cpp
---
