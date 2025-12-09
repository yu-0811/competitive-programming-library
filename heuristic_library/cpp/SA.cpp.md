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
  bundledCode: "#line 1 \"heuristic_library/cpp/SA.cpp\"\n#include <iostream>\n#include\
    \ <vector>\n#include <algorithm>\n#include <unordered_set>\n#include <utility>\n\
    #include <climits>\n#include <deque>\n#include <bitset>\n#include <cmath>\n#include\
    \ <string>\n#include <cstdlib>\n#include <cassert>\n#include <chrono>\n#include\
    \ <cstring>\nusing namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n);\
    \ i++)\n#define ll long long\n\nclass Random {\n    static uint32_t xorshift()\
    \ {\n        static uint32_t x = 123456789, y = 362436039, z = 521288629, w =\
    \ 88675123; \n        uint32_t t = x ^ (x << 11); x = y; y = z; z = w;\n     \
    \   return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    inline static\
    \ uint32_t randrange(unsigned x) { return xorshift() % x; } // [0, x)\n    inline\
    \ static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x)\
    \ + x; } // [x, y)\n    inline static float random() { return (xorshift() + 0.5)\
    \ * (1.0 / UINT_MAX); } // [0.0, 1.0)\n};\n\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    unsigned\
    \ short get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\nTimer timer;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF\
    \ ///////////////////////////////////\n#ifndef ONLINE_JUDGE\n    constexpr int\
    \ time_limit = 1990 + 1000;\n#else\n    constexpr int time_limit = 1987; // \u30B8\
    \u30E3\u30C3\u30B8\u3067\u306F 1990 ms\n#endif\n// \u63D0\u51FA\u7528\nconstexpr\
    \ float start_temp = 500;\nconstexpr float end_temp = 1;\n\n// optuna \u7528\n\
    // constexpr float default_start_temp = 200;\n// constexpr float default_end_temp\
    \ = 1;\n// float start_temp = default_start_temp;\n// float end_temp = default_end_temp;\n\
    void get_param() {\n    const char* p;\n    // p = std::getenv(\"start_temp\"\
    ); assert(p); start_temp = std::stof(p);\n    // p = std::getenv(\"end_temp\"\
    ); assert(p); end_temp = std::stof(p);\n}\n////////////////////////////////////////////////\n\
    // \u713C\u304D\u306A\u307E\u3057\u306B\u95A2\u3059\u308B\u95A2\u6570 /////////////////////////\n\
    // \u7DDA\u5F62\u6E29\u5EA6\u7BA1\u7406\nfloat linear_temp(unsigned short &SA_start_time,\
    \ unsigned short &now_time) {\n    return start_temp - (start_temp - end_temp)\
    \ * (now_time - SA_start_time) / time_limit;\n}\n\n// \u6307\u6570\u6E29\u5EA6\
    \u7BA1\u7406\nfloat expo_temp(unsigned short &SA_start_time, unsigned short &now_time)\
    \ {\n    float p = (float)(now_time - SA_start_time) / time_limit;\n    return\
    \ start_temp * pow(end_temp / start_temp, p);\n}\n\n// \u9077\u79FB\u78BA\u7387\
    \u95A2\u6570\n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\nfloat\
    \ calc_prob_maximize(auto &now_score, auto &next_score, float &temp) {\n    if\
    \ (next_score > now_score) return 1.0;\n    return exp((next_score - now_score)\
    \ / temp);\n}\n\n// \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\nfloat\
    \ calc_prob_minimize(auto &now_score, auto &next_score, float &temp) {\n    if\
    \ (next_score < now_score) return 1.0;\n    return exp((now_score - next_score)\
    \ / temp);\n}\n///////////////////////////////////////////////////////\n\n// \u3053\
    \u3053\u304B\u3089\u4E0B\u306B\u89E3\u6CD5\u3092\u66F8\u304F\n\n// \u713C\u304D\
    \u306A\u307E\u3057\u3067\u4F7F\u3046\u69CB\u9020\u4F53\nstruct WorkSpace {\n\n\
    };\n// \u89E3\u3092\u69CB\u7BC9\u3059\u308B\u305F\u3081\u306B\u5FC5\u8981\u306A\
    \u69CB\u9020\u4F53\n// \u713C\u304D\u306A\u307E\u3057\u3067\u4F7F\u3046\u3051\u3069\
    \u89E3\u306E\u69CB\u7BC9\u306B\u306F\u3044\u3089\u306A\u3044 (ex. \u30B9\u30B3\
    \u30A2\u306E\u5DEE\u5206\u66F4\u65B0\u306B\u4F7F\u3046\u914D\u5217\u306A\u3069\
    ) \u304C\u3042\u308B\u306E\u3067\u3053\u306E\u69CB\u6210\u306B\u3057\u3066\u3044\
    \u308B\n// WorkSpace \u304C Answer \u3092\u5305\u542B\u3059\u308B\u30A4\u30E1\u30FC\
    \u30B8\nstruct Answer {\n\n    // \u300CAnswer = WorkSpace\u300D\u3068\u3044\u3046\
    \u4EE3\u5165\u3092\u53EF\u80FD\u306B\u3059\u308B (\u6F14\u7B97\u5B50\u30AA\u30FC\
    \u30D0\u30FC\u30ED\u30FC\u30C9)\n    Answer& operator=(const WorkSpace& sol) {\n\
    \        return *this;\n    }\n};\n\n// \u5165\u529B\n\n// \u521D\u671F\u89E3\u751F\
    \u6210\nWorkSpace make_initial_solution(){\n    WorkSpace res;\n\n    return res;\n\
    }\n\nauto initialize_score(WorkSpace &sol) {\n    double score = 0.0;\n\n    return\
    \ score;\n}\n\nauto calc_score(WorkSpace &sol) {\n    double score = 0.0;\n\n\
    \    return score;\n}\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\u30B3\u30A2\u8A08\
    \u7B97 + \u53D7\u5BB9\u5224\u5B9A -> \u65B0\u3057\u3044\u30B9\u30B3\u30A2\u3092\
    \u8FD4\u3059 /////////////////\nauto generate_neighborhood(auto &now_score, auto\
    \ &temp, WorkSpace &sol) {\n    // \u8FD1\u508D\u751F\u6210 //////////////////////////////////////\n\
    \n    //////////////////////////////////////////////////\n    // \u30B9\u30B3\u30A2\
    \u8A08\u7B97 ////////////////////////////////////\n\n    //////////////////////////////////////////////////\n\
    \    if (calc_prob_minimize(now_score, next_score, temp) > Random::random()) {\
    \ // TODO: \u6700\u5C0F\u5316 or \u6700\u5927\u5316\n        // \u72B6\u614B\u3092\
    \u66F4\u65B0\n\n        return next_score;\n    }\n    else {\n        // \u72B6\
    \u614B\u3092\u3082\u3068\u306B\u623B\u3059\n\n        return now_score;\n    }\n\
    }\n\nAnswer SA() {\n    unsigned int counter = 0; unsigned int iter = 0;\n   \
    \ auto SA_start_time = timer.get_ms();\n    float temp = start_temp;\n\n    WorkSpace\
    \ current_solution = make_initial_solution();\n    auto now_score = initialize_score(current_solution);\n\
    \n    auto best_score = now_score;\n    Answer best_answer;\n    best_answer =\
    \ current_solution;\n    cerr << \"start score: \" << now_score << \"\\n\";\n\
    \    auto now_time = timer.get_ms();\n\n    while (true) {\n        if (counter\
    \ == 30) {\n            now_time = timer.get_ms();\n            if (now_time >\
    \ time_limit) break;\n            temp = linear_temp(SA_start_time, now_time);\n\
    \            counter = 0;\n        }\n        now_score = generate_neighborhood(now_score,\
    \ temp, current_solution);\n        if (now_score < best_score) { // TODO: \u6700\
    \u5C0F\u5316 or \u6700\u5927\u5316\n            best_score = now_score;\n    \
    \        best_answer = current_solution;\n        }\n        iter++; counter++;\n\
    \    }\n    cerr << \"best score: \" << best_score << \"\\n\";\n    cerr << \"\
    iter: \" << iter << \"\\n\";\n    return best_answer;\n}\n\nint main(){\n    ios::sync_with_stdio(false);\
    \ cin.tie(0);\n    timer = Timer(); // \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\
    \n    // get_param(); // optuna \u3092\u4F7F\u3046\u3068\u304D\u306F\u30B3\u30E1\
    \u30F3\u30C8\u30A2\u30A6\u30C8\u3092\u5916\u3059\n\n    // \u5165\u529B //////////////////////////////////////////\n\
    \    \n    //////////////////////////////////////////////////\n\n    Answer best_answer\
    \ = SA();\n\n    // \u51FA\u529B //////////////////////////////////////////\n\n\
    \    //////////////////////////////////////////////////\n}\n"
  code: "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <unordered_set>\n\
    #include <utility>\n#include <climits>\n#include <deque>\n#include <bitset>\n\
    #include <cmath>\n#include <string>\n#include <cstdlib>\n#include <cassert>\n\
    #include <chrono>\n#include <cstring>\nusing namespace std;\n#define rep(i, n)\
    \ for (int i = 0; i < (int)(n); i++)\n#define ll long long\n\nclass Random {\n\
    \    static uint32_t xorshift() {\n        static uint32_t x = 123456789, y =\
    \ 362436039, z = 521288629, w = 88675123; \n        uint32_t t = x ^ (x << 11);\
    \ x = y; y = z; z = w;\n        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));\n\
    \    }\npublic:\n    inline static uint32_t randrange(unsigned x) { return xorshift()\
    \ % x; } // [0, x)\n    inline static uint32_t randrange(unsigned x, unsigned\
    \ y) { return randrange(y - x) + x; } // [x, y)\n    inline static float random()\
    \ { return (xorshift() + 0.5) * (1.0 / UINT_MAX); } // [0.0, 1.0)\n};\n\nclass\
    \ Timer {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n    Timer()\
    \ : start(chrono::steady_clock::now()) {}\n    unsigned short get_ms() { // \u7D4C\
    \u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\nTimer timer;\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ///////////////////////////////////\n\
    #ifndef ONLINE_JUDGE\n    constexpr int time_limit = 1990 + 1000;\n#else\n   \
    \ constexpr int time_limit = 1987; // \u30B8\u30E3\u30C3\u30B8\u3067\u306F 1990\
    \ ms\n#endif\n// \u63D0\u51FA\u7528\nconstexpr float start_temp = 500;\nconstexpr\
    \ float end_temp = 1;\n\n// optuna \u7528\n// constexpr float default_start_temp\
    \ = 200;\n// constexpr float default_end_temp = 1;\n// float start_temp = default_start_temp;\n\
    // float end_temp = default_end_temp;\nvoid get_param() {\n    const char* p;\n\
    \    // p = std::getenv(\"start_temp\"); assert(p); start_temp = std::stof(p);\n\
    \    // p = std::getenv(\"end_temp\"); assert(p); end_temp = std::stof(p);\n}\n\
    ////////////////////////////////////////////////\n// \u713C\u304D\u306A\u307E\u3057\
    \u306B\u95A2\u3059\u308B\u95A2\u6570 /////////////////////////\n// \u7DDA\u5F62\
    \u6E29\u5EA6\u7BA1\u7406\nfloat linear_temp(unsigned short &SA_start_time, unsigned\
    \ short &now_time) {\n    return start_temp - (start_temp - end_temp) * (now_time\
    \ - SA_start_time) / time_limit;\n}\n\n// \u6307\u6570\u6E29\u5EA6\u7BA1\u7406\
    \nfloat expo_temp(unsigned short &SA_start_time, unsigned short &now_time) {\n\
    \    float p = (float)(now_time - SA_start_time) / time_limit;\n    return start_temp\
    \ * pow(end_temp / start_temp, p);\n}\n\n// \u9077\u79FB\u78BA\u7387\u95A2\u6570\
    \n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\u304D\nfloat calc_prob_maximize(auto\
    \ &now_score, auto &next_score, float &temp) {\n    if (next_score > now_score)\
    \ return 1.0;\n    return exp((next_score - now_score) / temp);\n}\n\n// \u30B9\
    \u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\u304D\nfloat calc_prob_minimize(auto\
    \ &now_score, auto &next_score, float &temp) {\n    if (next_score < now_score)\
    \ return 1.0;\n    return exp((now_score - next_score) / temp);\n}\n///////////////////////////////////////////////////////\n\
    \n// \u3053\u3053\u304B\u3089\u4E0B\u306B\u89E3\u6CD5\u3092\u66F8\u304F\n\n//\
    \ \u713C\u304D\u306A\u307E\u3057\u3067\u4F7F\u3046\u69CB\u9020\u4F53\nstruct WorkSpace\
    \ {\n\n};\n// \u89E3\u3092\u69CB\u7BC9\u3059\u308B\u305F\u3081\u306B\u5FC5\u8981\
    \u306A\u69CB\u9020\u4F53\n// \u713C\u304D\u306A\u307E\u3057\u3067\u4F7F\u3046\u3051\
    \u3069\u89E3\u306E\u69CB\u7BC9\u306B\u306F\u3044\u3089\u306A\u3044 (ex. \u30B9\
    \u30B3\u30A2\u306E\u5DEE\u5206\u66F4\u65B0\u306B\u4F7F\u3046\u914D\u5217\u306A\
    \u3069) \u304C\u3042\u308B\u306E\u3067\u3053\u306E\u69CB\u6210\u306B\u3057\u3066\
    \u3044\u308B\n// WorkSpace \u304C Answer \u3092\u5305\u542B\u3059\u308B\u30A4\u30E1\
    \u30FC\u30B8\nstruct Answer {\n\n    // \u300CAnswer = WorkSpace\u300D\u3068\u3044\
    \u3046\u4EE3\u5165\u3092\u53EF\u80FD\u306B\u3059\u308B (\u6F14\u7B97\u5B50\u30AA\
    \u30FC\u30D0\u30FC\u30ED\u30FC\u30C9)\n    Answer& operator=(const WorkSpace&\
    \ sol) {\n        return *this;\n    }\n};\n\n// \u5165\u529B\n\n// \u521D\u671F\
    \u89E3\u751F\u6210\nWorkSpace make_initial_solution(){\n    WorkSpace res;\n\n\
    \    return res;\n}\n\nauto initialize_score(WorkSpace &sol) {\n    double score\
    \ = 0.0;\n\n    return score;\n}\n\nauto calc_score(WorkSpace &sol) {\n    double\
    \ score = 0.0;\n\n    return score;\n}\n\n// \u8FD1\u508D\u751F\u6210 + \u30B9\
    \u30B3\u30A2\u8A08\u7B97 + \u53D7\u5BB9\u5224\u5B9A -> \u65B0\u3057\u3044\u30B9\
    \u30B3\u30A2\u3092\u8FD4\u3059 /////////////////\nauto generate_neighborhood(auto\
    \ &now_score, auto &temp, WorkSpace &sol) {\n    // \u8FD1\u508D\u751F\u6210 //////////////////////////////////////\n\
    \n    //////////////////////////////////////////////////\n    // \u30B9\u30B3\u30A2\
    \u8A08\u7B97 ////////////////////////////////////\n\n    //////////////////////////////////////////////////\n\
    \    if (calc_prob_minimize(now_score, next_score, temp) > Random::random()) {\
    \ // TODO: \u6700\u5C0F\u5316 or \u6700\u5927\u5316\n        // \u72B6\u614B\u3092\
    \u66F4\u65B0\n\n        return next_score;\n    }\n    else {\n        // \u72B6\
    \u614B\u3092\u3082\u3068\u306B\u623B\u3059\n\n        return now_score;\n    }\n\
    }\n\nAnswer SA() {\n    unsigned int counter = 0; unsigned int iter = 0;\n   \
    \ auto SA_start_time = timer.get_ms();\n    float temp = start_temp;\n\n    WorkSpace\
    \ current_solution = make_initial_solution();\n    auto now_score = initialize_score(current_solution);\n\
    \n    auto best_score = now_score;\n    Answer best_answer;\n    best_answer =\
    \ current_solution;\n    cerr << \"start score: \" << now_score << \"\\n\";\n\
    \    auto now_time = timer.get_ms();\n\n    while (true) {\n        if (counter\
    \ == 30) {\n            now_time = timer.get_ms();\n            if (now_time >\
    \ time_limit) break;\n            temp = linear_temp(SA_start_time, now_time);\n\
    \            counter = 0;\n        }\n        now_score = generate_neighborhood(now_score,\
    \ temp, current_solution);\n        if (now_score < best_score) { // TODO: \u6700\
    \u5C0F\u5316 or \u6700\u5927\u5316\n            best_score = now_score;\n    \
    \        best_answer = current_solution;\n        }\n        iter++; counter++;\n\
    \    }\n    cerr << \"best score: \" << best_score << \"\\n\";\n    cerr << \"\
    iter: \" << iter << \"\\n\";\n    return best_answer;\n}\n\nint main(){\n    ios::sync_with_stdio(false);\
    \ cin.tie(0);\n    timer = Timer(); // \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\
    \n    // get_param(); // optuna \u3092\u4F7F\u3046\u3068\u304D\u306F\u30B3\u30E1\
    \u30F3\u30C8\u30A2\u30A6\u30C8\u3092\u5916\u3059\n\n    // \u5165\u529B //////////////////////////////////////////\n\
    \    \n    //////////////////////////////////////////////////\n\n    Answer best_answer\
    \ = SA();\n\n    // \u51FA\u529B //////////////////////////////////////////\n\n\
    \    //////////////////////////////////////////////////\n}"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/SA.cpp
  requiredBy: []
  timestamp: '2025-12-09 12:08:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/SA.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/SA.cpp
- /library/heuristic_library/cpp/SA.cpp.html
title: heuristic_library/cpp/SA.cpp
---
