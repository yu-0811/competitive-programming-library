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
  bundledCode: "#line 1 \"heu_library/SA.cpp\"\n#include <bits/stdc++.h>\n#line 3\
    \ \"heu_library/SA.cpp\"\nusing namespace std;\n#define rep(i, n) for (int i =\
    \ 0; i < (int)(n); i++)\n#define ll long long\n\n// \u6642\u9593\u8A08\u6E2C\n\
    class Timer {\n    chrono::time_point<chrono::steady_clock> start;\npublic:\n\
    \    Timer() : start(chrono::steady_clock::now()) {}\n    long long get_ms() {\
    \ // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto now_time = chrono::steady_clock::now();\n\
    \        return chrono::duration_cast<chrono::milliseconds>(now_time - start).count();\n\
    \    }\n};\n\n// \u6E29\u5EA6\u95A2\u6570////////////////////////////////\n//\
    \ \u958B\u59CB\u6E29\u5EA6\nconstexpr double tempInit = 500;\n// \u7D42\u4E86\u6E29\
    \u5EA6\nconstexpr double tempFinish = 10;\ndouble temp = tempInit;\nconstexpr\
    \ int timeLimit = 4950;\n\n// \u7DDA\u5F62\u306E\u6E29\u5EA6\u95A2\u6570\n// (\u713C\
    \u304D\u306A\u307E\u3057\u958B\u59CB\u6642\u9593,\u73FE\u5728\u6642\u9593)\ndouble\
    \ linearTemp(double &startTime, double &nowTime){\n  return tempInit - (tempInit\
    \ - tempFinish) * (nowTime - startTime) / timeLimit ;\n}\n\n// \u9077\u79FB\u78BA\
    \u7387\u95A2\u6570 /////////////////////////////\n// (\u65B0\u30B9\u30B3\u30A2\
    ,\u65E7\u30B9\u30B3\u30A2,\u6E29\u5EA6)\n\n// \u30B9\u30B3\u30A2\u306E\u6700\u5927\
    \u5316\u554F\u984C\u306E\u3068\u304D\n// newScore>=prevScore \u306E\u3068\u304D\
    \u78BA\u7387\u306F 1 \u4EE5\u4E0A\ndouble calcProbability_Maximum(ll &newScore,\
    \ ll &prevScore, double &temp){\n  return exp((newScore - prevScore)/temp);\n\
    }\n\n// \u30B9\u30B3\u30A2\u306E\u6700\u5C0F\u5316\u554F\u984C\u306E\u554F\u984C\
    \ndouble calcProbability_Minimum(ll &newScore, ll &prevScore, double &temp){\n\
    \  return exp((prevScore - newScore)/temp);\n}\n\n\n// \u4F7F\u7528\u4F8B/////////////////////////////\n\
    class Random {\n    static uint32_t xorshift() {\n        static uint32_t x =\
    \ 123456789, y = 362436039, z = 521288629, w = 88675123; \n        uint32_t t\
    \ = x ^ (x << 11);\n        x = y; y = z; z = w;\n        return w = (w ^ (w >>\
    \ 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    // [0, x)\n    inline static uint32_t\
    \ randrange(unsigned x) { return xorshift() % x; }\n    // [x, y)\n    inline\
    \ static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x)\
    \ + x; }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n\n};\n\n// \u72B6\u614B\u9077\u79FB\nvoid transitionState(vector<int>\
    \ &state){\n  \n  ll nex_score;\n  if (calcProbability_Maximum(SCORE,nex_score,temp)\
    \ > Random::random()){\n    SCORE = nex_score;\n    // \u9077\u79FB\u3059\u308B\
    \n  }\n  else{\n    // \u72B6\u614B\u3092\u623B\u3059\n  }\n}\n\nTimer timer;\n\
    double NOW_TIME = 0.0;\nll SCORE = 0;\nvector<int> state; // \u72B6\u614B\n\n\
    int main(){\n  ios::sync_with_stdio(false); cin.tie(0);\n  timer = Timer(); //\
    \ \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\n  \n  int ITER_CNT = 0; // \u713C\
    \u304D\u306A\u307E\u3057\u5B9F\u884C\u56DE\u6570\n  double SA_START_TIME = timer.get_ms();\n\
    \  // \u713C\u304D\u306A\u307E\u3057\u958B\u59CB\n  while (true){\n    if (ITER_CNT%1000==0){//\
    \ \u9AD8\u901F\u5316\u306E\u305F\u3081\u306B 1000 \u56DE\u306B 1 \u56DE\u3060\u3051\
    \u6642\u9593\u8A08\u6E2C\u3059\u308B\n      NOW_TIME = timer.get_ms();\n     \
    \ if (NOW_TIME>timeLimit) break; \n      temp = linearTemp(SA_START_TIME, NOW_TIME);\
    \ // \u6E29\u5EA6\u3082\u3064\u3044\u3067\u306B\n    }\n\n    transitionState(state);\n\
    \  }\n}\n"
  code: "#include <bits/stdc++.h>\n#include <chrono>\nusing namespace std;\n#define\
    \ rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\n\n// \u6642\
    \u9593\u8A08\u6E2C\nclass Timer {\n    chrono::time_point<chrono::steady_clock>\
    \ start;\npublic:\n    Timer() : start(chrono::steady_clock::now()) {}\n    long\
    \ long get_ms() { // \u7D4C\u904E\u6642\u9593\u3092\u8FD4\u3059\n        auto\
    \ now_time = chrono::steady_clock::now();\n        return chrono::duration_cast<chrono::milliseconds>(now_time\
    \ - start).count();\n    }\n};\n\n// \u6E29\u5EA6\u95A2\u6570////////////////////////////////\n\
    // \u958B\u59CB\u6E29\u5EA6\nconstexpr double tempInit = 500;\n// \u7D42\u4E86\
    \u6E29\u5EA6\nconstexpr double tempFinish = 10;\ndouble temp = tempInit;\nconstexpr\
    \ int timeLimit = 4950;\n\n// \u7DDA\u5F62\u306E\u6E29\u5EA6\u95A2\u6570\n// (\u713C\
    \u304D\u306A\u307E\u3057\u958B\u59CB\u6642\u9593,\u73FE\u5728\u6642\u9593)\ndouble\
    \ linearTemp(double &startTime, double &nowTime){\n  return tempInit - (tempInit\
    \ - tempFinish) * (nowTime - startTime) / timeLimit ;\n}\n\n// \u9077\u79FB\u78BA\
    \u7387\u95A2\u6570 /////////////////////////////\n// (\u65B0\u30B9\u30B3\u30A2\
    ,\u65E7\u30B9\u30B3\u30A2,\u6E29\u5EA6)\n\n// \u30B9\u30B3\u30A2\u306E\u6700\u5927\
    \u5316\u554F\u984C\u306E\u3068\u304D\n// newScore>=prevScore \u306E\u3068\u304D\
    \u78BA\u7387\u306F 1 \u4EE5\u4E0A\ndouble calcProbability_Maximum(ll &newScore,\
    \ ll &prevScore, double &temp){\n  return exp((newScore - prevScore)/temp);\n\
    }\n\n// \u30B9\u30B3\u30A2\u306E\u6700\u5C0F\u5316\u554F\u984C\u306E\u554F\u984C\
    \ndouble calcProbability_Minimum(ll &newScore, ll &prevScore, double &temp){\n\
    \  return exp((prevScore - newScore)/temp);\n}\n\n\n// \u4F7F\u7528\u4F8B/////////////////////////////\n\
    class Random {\n    static uint32_t xorshift() {\n        static uint32_t x =\
    \ 123456789, y = 362436039, z = 521288629, w = 88675123; \n        uint32_t t\
    \ = x ^ (x << 11);\n        x = y; y = z; z = w;\n        return w = (w ^ (w >>\
    \ 19)) ^ (t ^ (t >> 8));\n    }\npublic:\n    // [0, x)\n    inline static uint32_t\
    \ randrange(unsigned x) { return xorshift() % x; }\n    // [x, y)\n    inline\
    \ static uint32_t randrange(unsigned x, unsigned y) { return randrange(y - x)\
    \ + x; }\n    // [0.0, 1.0)\n    inline static double random() { return (xorshift()\
    \ + 0.5) * (1.0 / UINT_MAX); }\n\n};\n\n// \u72B6\u614B\u9077\u79FB\nvoid transitionState(vector<int>\
    \ &state){\n  \n  ll nex_score;\n  if (calcProbability_Maximum(SCORE,nex_score,temp)\
    \ > Random::random()){\n    SCORE = nex_score;\n    // \u9077\u79FB\u3059\u308B\
    \n  }\n  else{\n    // \u72B6\u614B\u3092\u623B\u3059\n  }\n}\n\nTimer timer;\n\
    double NOW_TIME = 0.0;\nll SCORE = 0;\nvector<int> state; // \u72B6\u614B\n\n\
    int main(){\n  ios::sync_with_stdio(false); cin.tie(0);\n  timer = Timer(); //\
    \ \u30BF\u30A4\u30DE\u30FC\u521D\u671F\u5316\n  \n  int ITER_CNT = 0; // \u713C\
    \u304D\u306A\u307E\u3057\u5B9F\u884C\u56DE\u6570\n  double SA_START_TIME = timer.get_ms();\n\
    \  // \u713C\u304D\u306A\u307E\u3057\u958B\u59CB\n  while (true){\n    if (ITER_CNT%1000==0){//\
    \ \u9AD8\u901F\u5316\u306E\u305F\u3081\u306B 1000 \u56DE\u306B 1 \u56DE\u3060\u3051\
    \u6642\u9593\u8A08\u6E2C\u3059\u308B\n      NOW_TIME = timer.get_ms();\n     \
    \ if (NOW_TIME>timeLimit) break; \n      temp = linearTemp(SA_START_TIME, NOW_TIME);\
    \ // \u6E29\u5EA6\u3082\u3064\u3044\u3067\u306B\n    }\n\n    transitionState(state);\n\
    \  }\n}"
  dependsOn: []
  isVerificationFile: false
  path: heu_library/SA.cpp
  requiredBy: []
  timestamp: '2024-09-24 23:58:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heu_library/SA.cpp
layout: document
title: "Simulated Annealing (\u713C\u304D\u306A\u307E\u3057\u6CD5)"
---

後で書く