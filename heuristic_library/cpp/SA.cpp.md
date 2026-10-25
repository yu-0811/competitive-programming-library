---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: heuristic_library/cpp/template.cpp
    title: heuristic_library/cpp/template.cpp
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#line 1 \"heuristic_library/cpp/template.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\nusing\
    \ ll = long long;\nusing u64 = unsigned long long;\n#pragma GCC target(\"avx2\"\
    )\n#pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nclass\
    \ Random {\n    static uint32_t xorshift32() {\n        static uint32_t x = 123456789,\
    \ y = 362436039, z = 521288629, w = 88675123; \n        uint32_t t = x ^ (x <<\
    \ 11);\n        x = y; y = z; z = w;\n        return w = (w ^ (w >> 19)) ^ (t\
    \ ^ (t >> 8));\n    }\npublic:\n    inline static u64 xorshift64() {\n       \
    \ static u64 state = 88172645463325252ULL;\n        u64 x = state;\n        x\
    \ ^= x << 7;\n        x ^= x >> 9;\n        return state = x;\n    }\n    // [0,\
    \ x)\n    inline static uint32_t randrange(unsigned x) { return xorshift32() %\
    \ x; }\n    // [x, y)\n    inline static uint32_t randrange(unsigned x, unsigned\
    \ y) { \n        assert(x < y);\n        return randrange(y - x) + x;\n    }\n\
    \    // [0.0, 1.0)\n    inline static double random() { return (xorshift32() +\
    \ 0.5) * (1.0 / UINT_MAX); }\n};\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\ninline Timer timer;\n\n#ifndef ONLINE_JUDGE\n\
    \    constexpr int time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit\
    \ = 1987;\n#endif\n#line 2 \"heuristic_library/cpp/SA.cpp\"\n\n// \u30D1\u30E9\
    \u30E1\u30FC\u30BF ///////////////////////////////////\n// \u63D0\u51FA\u7528\n\
    constexpr float start_temp = 500;\nconstexpr float end_temp = 1;\n\n// optuna\
    \ \u7528\n// constexpr float default_start_temp = 200;\n// constexpr float default_end_temp\
    \ = 1;\n// float start_temp = default_start_temp;\n// float end_temp = default_end_temp;\n\
    void get_param() {\n    const char* p;\n    // p = std::getenv(\"start_temp\"\
    ); assert(p); start_temp = std::stof(p);\n    // p = std::getenv(\"end_temp\"\
    ); assert(p); end_temp = std::stof(p);\n}\n////////////////////////////////////////////////\n\
    \n// \u713C\u304D\u306A\u307E\u3057\u306B\u95A2\u3059\u308B\u95A2\u6570 /////////////////////////\n\
    // \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\nfloat linear_temp(unsigned short &SA_start_time,\
    \ unsigned short &now_time) {\n    return start_temp - (start_temp - end_temp)\
    \ * (now_time - SA_start_time) / time_limit;\n}\n\n// \u6307\u6570\u6E29\u5EA6\
    \u7BA1\u7406\nfloat expo_temp(unsigned short &SA_start_time, unsigned short &now_time)\
    \ {\n    float p = (float)(now_time - SA_start_time) / time_limit;\n    return\
    \ start_temp * pow(end_temp / start_temp, p);\n}\n\n// \u9077\u79FB\u78BA\u7387\
    \u95A2\u6570\nconstexpr bool maximize = false; // false: \u6700\u5C0F\u5316, true:\
    \ \u6700\u5927\u5316\n\ntemplate<class Score>\nbool is_better(const Score& a,\
    \ const Score& b) {\n    if constexpr (maximize) return a > b;\n    else return\
    \ a < b;\n}\n\ntemplate<class Score>\ndouble calc_prob(const Score& now_score,\
    \ const Score& next_score, double temp) {\n    if (is_better(next_score, now_score))\
    \ return 1.0;\n    if constexpr (maximize) {\n        return exp((next_score -\
    \ now_score) / temp);\n    } else {\n        return exp((now_score - next_score)\
    \ / temp);\n    }\n}\n\n// \u30B9\u30B3\u30A2\u306E\u578B\nusing Score = int;\n\
    ///////////////////////////////////////////////////////\n\n// \u3053\u3053\u304B\
    \u3089\u4E0B\u306B\u89E3\u6CD5\u3092\u66F8\u304F\n\n// \u713C\u304D\u306A\u307E\
    \u3057\u3067\u4F7F\u3046\u69CB\u9020\u4F53\n// \u30B9\u30B3\u30A2\u306E\u5DEE\u5206\
    \u66F4\u65B0\u306B\u4F7F\u3046\u914D\u5217\u306A\u3069\u3092\u6301\u3064\nstruct\
    \ WorkSpace {\n    Score score;\n};\n\n// \u6700\u826F\u89E3\u3092\u4FDD\u6301\
    \u3059\u308B\u305F\u3081\u306E\u69CB\u9020\u4F53\n// WorkSpace \u306E\u3046\u3061\
    \u3001\u30B9\u30B3\u30A2\u3068\u89E3\u306E\u51FA\u529B\u306B\u5FC5\u8981\u306A\
    \u60C5\u5831\u3060\u3051\u3092\u6301\u3064\nstruct Answer {\n    Score score;\n\
    \    // \u300CAnswer = WorkSpace\u300D\u3068\u3044\u3046\u4EE3\u5165\u3092\u53EF\
    \u80FD\u306B\u3059\u308B (\u6F14\u7B97\u5B50\u30AA\u30FC\u30D0\u30FC\u30ED\u30FC\
    \u30C9)\n    Answer& operator=(const WorkSpace& sol) {\n        score = sol.score;\n\
    \        return *this;\n    }\n};\n\n// \u5165\u529B\n\n// \u521D\u671F\u89E3\u751F\
    \u6210\nWorkSpace make_initial_solution(){\n    WorkSpace res{};\n\n    return\
    \ res;\n}\n\nScore initialize_score(WorkSpace &sol) {\n    Score score = 0;\n\n\
    \    return score;\n}\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\
    \u7B97 + \u53D7\u5BB9\u5224\u5B9A + \u72B6\u614B\u66F4\u65B0 -> \u8FD1\u508D\u751F\
    \u6210\u304C\u6210\u529F\u3057\u305F\u304B\u3069\u3046\u304B \u3092\u8FD4\u3059\
    \n// \u72B6\u614B\u306F sol \u3092\u76F4\u63A5\u66F8\u304D\u63DB\u3048\u308B\n\
    bool generate_neighborhood(auto &temp, WorkSpace &sol) {\n    // \u8FD1\u508D\u751F\
    \u6210\n\n\n    // \u30B9\u30B3\u30A2\u8A08\u7B97 \n\n\n    if (calc_prob(now_score,\
    \ next_score, temp) > Random::random()) {\n\n        return true;\n    }\n   \
    \ else {\n        // \u72B6\u614B\u3092\u3082\u3068\u306B\u623B\u3059\n\n    \
    \    return true;\n    }\n}\n\nAnswer SA() {\n    unsigned int counter = 0; unsigned\
    \ int iter = 0; unsigned int failed_neighborhood = 0;\n    auto SA_start_time\
    \ = timer.get_ms();\n    float temp = start_temp;\n\n    WorkSpace current_solution\
    \ = make_initial_solution();\n    auto best_score = current_solution.score;\n\
    \    Answer best_ans;\n    best_ans = current_solution;\n    cerr << \"start score:\
    \ \" << current_solution.score << \"\\n\";\n    auto now_time = timer.get_ms();\n\
    \n    while (true) {\n        if (counter == 30) {\n            now_time = timer.get_ms();\n\
    \            if (now_time > time_limit) break;\n            temp = linear_temp(SA_start_time,\
    \ now_time);\n            counter = 0;\n        }\n        if (!generate_neighborhood(temp,\
    \ current_solution)) {\n            failed_neighborhood++;\n        }\n      \
    \  if (is_better(current_solution.score, best_score)) {\n            best_score\
    \ = current_solution.score;\n            best_ans = current_solution;\n      \
    \  }\n        iter++; counter++;\n    }\n    cerr << \"best score: \" << best_score\
    \ << \"\\n\";\n    cerr << \"iter: \" << iter << \"\\n\";\n    cerr << \"successful\
    \ neighborhood: \" << iter - failed_neighborhood << \"\\n\";\n    return best_ans;\n\
    }\n\nint main(){\n    ios::sync_with_stdio(false); cin.tie(0);\n    timer = Timer();\n\
    \    // get_param(); // optuna \u3092\u4F7F\u3046\u3068\u304D\u306F\u30B3\u30E1\
    \u30F3\u30C8\u30A2\u30A6\u30C8\u3092\u5916\u3059\n\n    // \u5165\u529B //////////////////////////////////////////\n\
    \    \n    //////////////////////////////////////////////////\n\n    Answer best_ans\
    \ = SA();\n\n    // \u51FA\u529B //////////////////////////////////////////\n\n\
    \    //////////////////////////////////////////////////\n}\n"
  code: "#include \"template.cpp\"\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ///////////////////////////////////\n\
    // \u63D0\u51FA\u7528\nconstexpr float start_temp = 500;\nconstexpr float end_temp\
    \ = 1;\n\n// optuna \u7528\n// constexpr float default_start_temp = 200;\n// constexpr\
    \ float default_end_temp = 1;\n// float start_temp = default_start_temp;\n// float\
    \ end_temp = default_end_temp;\nvoid get_param() {\n    const char* p;\n    //\
    \ p = std::getenv(\"start_temp\"); assert(p); start_temp = std::stof(p);\n   \
    \ // p = std::getenv(\"end_temp\"); assert(p); end_temp = std::stof(p);\n}\n////////////////////////////////////////////////\n\
    \n// \u713C\u304D\u306A\u307E\u3057\u306B\u95A2\u3059\u308B\u95A2\u6570 /////////////////////////\n\
    // \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\nfloat linear_temp(unsigned short &SA_start_time,\
    \ unsigned short &now_time) {\n    return start_temp - (start_temp - end_temp)\
    \ * (now_time - SA_start_time) / time_limit;\n}\n\n// \u6307\u6570\u6E29\u5EA6\
    \u7BA1\u7406\nfloat expo_temp(unsigned short &SA_start_time, unsigned short &now_time)\
    \ {\n    float p = (float)(now_time - SA_start_time) / time_limit;\n    return\
    \ start_temp * pow(end_temp / start_temp, p);\n}\n\n// \u9077\u79FB\u78BA\u7387\
    \u95A2\u6570\nconstexpr bool maximize = false; // false: \u6700\u5C0F\u5316, true:\
    \ \u6700\u5927\u5316\n\ntemplate<class Score>\nbool is_better(const Score& a,\
    \ const Score& b) {\n    if constexpr (maximize) return a > b;\n    else return\
    \ a < b;\n}\n\ntemplate<class Score>\ndouble calc_prob(const Score& now_score,\
    \ const Score& next_score, double temp) {\n    if (is_better(next_score, now_score))\
    \ return 1.0;\n    if constexpr (maximize) {\n        return exp((next_score -\
    \ now_score) / temp);\n    } else {\n        return exp((now_score - next_score)\
    \ / temp);\n    }\n}\n\n// \u30B9\u30B3\u30A2\u306E\u578B\nusing Score = int;\n\
    ///////////////////////////////////////////////////////\n\n// \u3053\u3053\u304B\
    \u3089\u4E0B\u306B\u89E3\u6CD5\u3092\u66F8\u304F\n\n// \u713C\u304D\u306A\u307E\
    \u3057\u3067\u4F7F\u3046\u69CB\u9020\u4F53\n// \u30B9\u30B3\u30A2\u306E\u5DEE\u5206\
    \u66F4\u65B0\u306B\u4F7F\u3046\u914D\u5217\u306A\u3069\u3092\u6301\u3064\nstruct\
    \ WorkSpace {\n    Score score;\n};\n\n// \u6700\u826F\u89E3\u3092\u4FDD\u6301\
    \u3059\u308B\u305F\u3081\u306E\u69CB\u9020\u4F53\n// WorkSpace \u306E\u3046\u3061\
    \u3001\u30B9\u30B3\u30A2\u3068\u89E3\u306E\u51FA\u529B\u306B\u5FC5\u8981\u306A\
    \u60C5\u5831\u3060\u3051\u3092\u6301\u3064\nstruct Answer {\n    Score score;\n\
    \    // \u300CAnswer = WorkSpace\u300D\u3068\u3044\u3046\u4EE3\u5165\u3092\u53EF\
    \u80FD\u306B\u3059\u308B (\u6F14\u7B97\u5B50\u30AA\u30FC\u30D0\u30FC\u30ED\u30FC\
    \u30C9)\n    Answer& operator=(const WorkSpace& sol) {\n        score = sol.score;\n\
    \        return *this;\n    }\n};\n\n// \u5165\u529B\n\n// \u521D\u671F\u89E3\u751F\
    \u6210\nWorkSpace make_initial_solution(){\n    WorkSpace res{};\n\n    return\
    \ res;\n}\n\nScore initialize_score(WorkSpace &sol) {\n    Score score = 0;\n\n\
    \    return score;\n}\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\
    \u7B97 + \u53D7\u5BB9\u5224\u5B9A + \u72B6\u614B\u66F4\u65B0 -> \u8FD1\u508D\u751F\
    \u6210\u304C\u6210\u529F\u3057\u305F\u304B\u3069\u3046\u304B \u3092\u8FD4\u3059\
    \n// \u72B6\u614B\u306F sol \u3092\u76F4\u63A5\u66F8\u304D\u63DB\u3048\u308B\n\
    bool generate_neighborhood(auto &temp, WorkSpace &sol) {\n    // \u8FD1\u508D\u751F\
    \u6210\n\n\n    // \u30B9\u30B3\u30A2\u8A08\u7B97 \n\n\n    if (calc_prob(now_score,\
    \ next_score, temp) > Random::random()) {\n\n        return true;\n    }\n   \
    \ else {\n        // \u72B6\u614B\u3092\u3082\u3068\u306B\u623B\u3059\n\n    \
    \    return true;\n    }\n}\n\nAnswer SA() {\n    unsigned int counter = 0; unsigned\
    \ int iter = 0; unsigned int failed_neighborhood = 0;\n    auto SA_start_time\
    \ = timer.get_ms();\n    float temp = start_temp;\n\n    WorkSpace current_solution\
    \ = make_initial_solution();\n    auto best_score = current_solution.score;\n\
    \    Answer best_ans;\n    best_ans = current_solution;\n    cerr << \"start score:\
    \ \" << current_solution.score << \"\\n\";\n    auto now_time = timer.get_ms();\n\
    \n    while (true) {\n        if (counter == 30) {\n            now_time = timer.get_ms();\n\
    \            if (now_time > time_limit) break;\n            temp = linear_temp(SA_start_time,\
    \ now_time);\n            counter = 0;\n        }\n        if (!generate_neighborhood(temp,\
    \ current_solution)) {\n            failed_neighborhood++;\n        }\n      \
    \  if (is_better(current_solution.score, best_score)) {\n            best_score\
    \ = current_solution.score;\n            best_ans = current_solution;\n      \
    \  }\n        iter++; counter++;\n    }\n    cerr << \"best score: \" << best_score\
    \ << \"\\n\";\n    cerr << \"iter: \" << iter << \"\\n\";\n    cerr << \"successful\
    \ neighborhood: \" << iter - failed_neighborhood << \"\\n\";\n    return best_ans;\n\
    }\n\nint main(){\n    ios::sync_with_stdio(false); cin.tie(0);\n    timer = Timer();\n\
    \    // get_param(); // optuna \u3092\u4F7F\u3046\u3068\u304D\u306F\u30B3\u30E1\
    \u30F3\u30C8\u30A2\u30A6\u30C8\u3092\u5916\u3059\n\n    // \u5165\u529B //////////////////////////////////////////\n\
    \    \n    //////////////////////////////////////////////////\n\n    Answer best_ans\
    \ = SA();\n\n    // \u51FA\u529B //////////////////////////////////////////\n\n\
    \    //////////////////////////////////////////////////\n}\n"
  dependsOn:
  - heuristic_library/cpp/template.cpp
  isVerificationFile: false
  path: heuristic_library/cpp/SA.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/SA.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/SA.cpp
- /library/heuristic_library/cpp/SA.cpp.html
title: heuristic_library/cpp/SA.cpp
---
