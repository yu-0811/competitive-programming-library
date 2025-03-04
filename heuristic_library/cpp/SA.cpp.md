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
  bundledCode: "#line 1 \"heuristic_library/cpp/SA.cpp\"\n#include <bits/stdc++.h>\n\
    #line 3 \"heuristic_library/cpp/SA.cpp\"\nusing namespace std;\n#define rep(i,\
    \ n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\n#pragma GCC target(\"\
    avx2\")\n#pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\
    \nclass Random {\n    static uint32_t xorshift() {\n        static uint32_t x\
    \ = 123456789, y = 362436039, z = 521288629, w = 88675123; \n        uint32_t\
    \ t = x ^ (x << 11);\n        x = y; y = z; z = w;\n        return w = (w ^ (w\
    \ >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    // [0, x)\n    inline static\
    \ uint32_t randrange(unsigned x) { return xorshift() % x; }\n    // [x, y)\n \
    \   inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y\
    \ - x) + x; }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n\n};\n\n// \u6642\u9593\u8A08\u6E2C\nclass Timer\
    \ {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n    Timer()\
    \ : start(chrono::steady_clock::now()) {}\n    long long get_ms() { // \u7D4C\u904E\
    \u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\nTimer timer;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ///////////////////////////////////\n\
    constexpr double start_temp = 500;\nconstexpr double end_temp = 10;\nconstexpr\
    \ int time_limit = 4950; // \u5358\u4F4D ms\n////////////////////////////////////////////////\n\
    \n// \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\ndouble linear_temp(double &SA_start_time,\
    \ double &now_time) {\n    return start_temp - (start_temp - end_temp) * (now_time\
    \ - SA_start_time) / time_limit;\n}\n\n// \u9077\u79FB\u78BA\u7387\u95A2\u6570\
    \n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\ndouble calc_prob_maximize(auto\
    \ &now_score, auto &next_score, double &temp) {\n    if (next_score > now_score)\
    \ return 1.0;\n    return exp((next_score - now_score) / temp);\n}\n\n// \u30B9\
    \u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\ndouble calc_prob_minimize(auto\
    \ &now_score, auto &next_score, double &temp) {\n    if (next_score < now_score)\
    \ return 1.0;\n    return exp((now_score - next_score) / temp);\n}\n\n// \u30B0\
    \u30ED\u30FC\u30D0\u30EB\u5909\u6570 ///////////////////////////////////\n\n////////////////////////////////////////////////////\n\
    \ndouble calc_score(int &idx){\n  return;\n}\n\nauto initialize_score(){\n  return;\n\
    }\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\u7B97 + \u53D7\u5BB9\
    \u5224\u5B9A -> \u65B0\u3057\u3044\u30B9\u30B3\u30A2\u3092\u8FD4\u3059 /////////////////\n\
    auto generate_neighborhood(auto &now_score, auto &temp){\n  // \u8FD1\u508D\u751F\
    \u6210 //////////////////////////////////////\n\n  //////////////////////////////////////////////////\n\
    \  // \u30B9\u30B3\u30A2\u8A08\u7B97 ////////////////////////////////////\n  auto\
    \ next_score\n  if (calc_prob_maximize(now_score, next_score, temp) > Random::random())\
    \ {\n    // \u5FC5\u8981\u3067\u3042\u308C\u3070\u72B6\u614B\u3092\u66F4\u65B0\
    \ ////////////////////\n\n    //////////////////////////////////////////////\n\
    \    return next_score;\n  }\n  else {\n    // \u72B6\u614B\u3092\u3082\u3068\u306B\
    \u623B\u3059 //////////////////////////\n\n    //////////////////////////////////////////////\n\
    \    return now_score;\n  }\n}\n\nvoid SA() {\n  double SA_start_time = timer.get_ms();\n\
    \  int iter = 1;\n  double temp = start_temp;\n  double now_score = initialize_score();\n\
    \  while (true) {\n    if (iter % 1000 == 0) {\n      double now_time = timer.get_ms();\n\
    \      if (now_time > time_limit) break;\n      temp = linear_temp(SA_start_time,\
    \ now_time);\n    }\n    now_score = generate_neighborhood(now_score, temp);\n\
    \    iter++;\n  }\n  cerr << \"iter: \" << iter << endl;\n}\n\nint main(){\n \
    \ ios::sync_with_stdio(false); cin.tie(0);\n  timer = Timer(); // \u30BF\u30A4\
    \u30DE\u30FC\u521D\u671F\u5316\n\n  // \u5165\u529B //////////////////////////////////////////\n\
    \n  //////////////////////////////////////////////////\n\n  SA();\n\n  // \u51FA\
    \u529B //////////////////////////////////////////\n\n  //////////////////////////////////////////////////\n\
    }\n"
  code: "#include <bits/stdc++.h>\n#include <chrono>\nusing namespace std;\n#define\
    \ rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\n#pragma\
    \ GCC target(\"avx2\")\n#pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"\
    unroll-loops\")\n\nclass Random {\n    static uint32_t xorshift() {\n        static\
    \ uint32_t x = 123456789, y = 362436039, z = 521288629, w = 88675123; \n     \
    \   uint32_t t = x ^ (x << 11);\n        x = y; y = z; z = w;\n        return\
    \ w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    // [0, x)\n    inline\
    \ static uint32_t randrange(unsigned x) { return xorshift() % x; }\n    // [x,\
    \ y)\n    inline static uint32_t randrange(unsigned x, unsigned y) { return randrange(y\
    \ - x) + x; }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n\n};\n\n// \u6642\u9593\u8A08\u6E2C\nclass Timer\
    \ {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n    Timer()\
    \ : start(chrono::steady_clock::now()) {}\n    long long get_ms() { // \u7D4C\u904E\
    \u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\nTimer timer;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ///////////////////////////////////\n\
    constexpr double start_temp = 500;\nconstexpr double end_temp = 10;\nconstexpr\
    \ int time_limit = 4950; // \u5358\u4F4D ms\n////////////////////////////////////////////////\n\
    \n// \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\ndouble linear_temp(double &SA_start_time,\
    \ double &now_time) {\n    return start_temp - (start_temp - end_temp) * (now_time\
    \ - SA_start_time) / time_limit;\n}\n\n// \u9077\u79FB\u78BA\u7387\u95A2\u6570\
    \n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\ndouble calc_prob_maximize(auto\
    \ &now_score, auto &next_score, double &temp) {\n    if (next_score > now_score)\
    \ return 1.0;\n    return exp((next_score - now_score) / temp);\n}\n\n// \u30B9\
    \u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\ndouble calc_prob_minimize(auto\
    \ &now_score, auto &next_score, double &temp) {\n    if (next_score < now_score)\
    \ return 1.0;\n    return exp((now_score - next_score) / temp);\n}\n\n// \u30B0\
    \u30ED\u30FC\u30D0\u30EB\u5909\u6570 ///////////////////////////////////\n\n////////////////////////////////////////////////////\n\
    \ndouble calc_score(int &idx){\n  return;\n}\n\nauto initialize_score(){\n  return;\n\
    }\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\u7B97 + \u53D7\u5BB9\
    \u5224\u5B9A -> \u65B0\u3057\u3044\u30B9\u30B3\u30A2\u3092\u8FD4\u3059 /////////////////\n\
    auto generate_neighborhood(auto &now_score, auto &temp){\n  // \u8FD1\u508D\u751F\
    \u6210 //////////////////////////////////////\n\n  //////////////////////////////////////////////////\n\
    \  // \u30B9\u30B3\u30A2\u8A08\u7B97 ////////////////////////////////////\n  auto\
    \ next_score\n  if (calc_prob_maximize(now_score, next_score, temp) > Random::random())\
    \ {\n    // \u5FC5\u8981\u3067\u3042\u308C\u3070\u72B6\u614B\u3092\u66F4\u65B0\
    \ ////////////////////\n\n    //////////////////////////////////////////////\n\
    \    return next_score;\n  }\n  else {\n    // \u72B6\u614B\u3092\u3082\u3068\u306B\
    \u623B\u3059 //////////////////////////\n\n    //////////////////////////////////////////////\n\
    \    return now_score;\n  }\n}\n\nvoid SA() {\n  double SA_start_time = timer.get_ms();\n\
    \  int iter = 1;\n  double temp = start_temp;\n  double now_score = initialize_score();\n\
    \  while (true) {\n    if (iter % 1000 == 0) {\n      double now_time = timer.get_ms();\n\
    \      if (now_time > time_limit) break;\n      temp = linear_temp(SA_start_time,\
    \ now_time);\n    }\n    now_score = generate_neighborhood(now_score, temp);\n\
    \    iter++;\n  }\n  cerr << \"iter: \" << iter << endl;\n}\n\nint main(){\n \
    \ ios::sync_with_stdio(false); cin.tie(0);\n  timer = Timer(); // \u30BF\u30A4\
    \u30DE\u30FC\u521D\u671F\u5316\n\n  // \u5165\u529B //////////////////////////////////////////\n\
    \n  //////////////////////////////////////////////////\n\n  SA();\n\n  // \u51FA\
    \u529B //////////////////////////////////////////\n\n  //////////////////////////////////////////////////\n\
    }"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/SA.cpp
  requiredBy: []
  timestamp: '2025-03-04 22:47:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/SA.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/SA.cpp
- /library/heuristic_library/cpp/SA.cpp.html
title: heuristic_library/cpp/SA.cpp
---
