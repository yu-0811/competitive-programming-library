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
  bundledCode: "#line 1 \"heuristic_library/beam_search.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define\
    \ ll long long\n\nconst int beam_width = 70000;\n\nstruct State {\n    int score;\n\
    \    bitset<100> move_history;\n    \n    State() : score(0), move_history(0)\
    \ {}\n};\n\n// \u8A55\u4FA1\u95A2\u6570########################################\n\
    // a1 > a2 \u306E\u3068\u304D true \u3092\u8FD4\u3059\u3088\u3046\u306B\u3059\u308B\
    \n// a1 \u3088\u308A a2 \u306E\u65B9\u3092\u8A55\u4FA1\u3057\u305F\u3044\u3068\
    \u304D\uFF08\u9078\u3073\u305F\u3044\u3068\u304D\uFF09true \u3092\u8FD4\u3059\uFF08\
    a1 \u306E\u65B9\u304C\u524D\u306B\u6765\u308B\uFF09\nbool comp(const State &a1,\
    \ const State &a2){\n    return a1.score > a2.score;\n}\n//#####################################################\n\
    \n\n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State operate(State s, int op, int &i){\n\n}\n//#####################################################\n\
    \nauto beam_search(State &init_state, int beam_width, int depth){\n    vector<State>\
    \ now;\n    now.emplace_back(init_state);\n    vector<State> next;\n\n    for\
    \ (int i=0; i<depth; i++){\n        bool sorted = false;\n        for (auto &s\
    \ : now){\n            // \u72B6\u614B\u3092\u9077\u79FB\u3055\u305B\u308B\n \
    \           for (auto op: {-1,1}){\n                // \u72B6\u614B\u3092\u5909\
    \u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\u5024\u3092\u8A08\u7B97\
    ###############\n                int nex_score;\n                //#################################################\n\
    \n                // \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\
    \u306E\u8A55\u4FA1\u5024\u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\
    \u307F\u9077\u79FB\n                if (sorted && nex_score <= next[beam_width-1].score)\
    \ continue;\n                auto nex = operate(s, op, i);\n                next.emplace_back(nex);\n\
    \n                if (next.size() >= 2*beam_width){\n                    sort(next.begin(),\
    \ next.end(), comp);\n                    next.resize(beam_width);\n         \
    \           sorted = true;\n                }\n            }\n        }\n    \
    \    sort(next.begin(), next.end(), comp);\n        swap(now, next);\n       \
    \ next.clear();\n    }\n\n    return now[0].move_history;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n#define rep(i, n) for (int\
    \ i = 0; i < (int)(n); i++)\n#define ll long long\n\nconst int beam_width = 70000;\n\
    \nstruct State {\n    int score;\n    bitset<100> move_history;\n    \n    State()\
    \ : score(0), move_history(0) {}\n};\n\n// \u8A55\u4FA1\u95A2\u6570########################################\n\
    // a1 > a2 \u306E\u3068\u304D true \u3092\u8FD4\u3059\u3088\u3046\u306B\u3059\u308B\
    \n// a1 \u3088\u308A a2 \u306E\u65B9\u3092\u8A55\u4FA1\u3057\u305F\u3044\u3068\
    \u304D\uFF08\u9078\u3073\u305F\u3044\u3068\u304D\uFF09true \u3092\u8FD4\u3059\uFF08\
    a1 \u306E\u65B9\u304C\u524D\u306B\u6765\u308B\uFF09\nbool comp(const State &a1,\
    \ const State &a2){\n    return a1.score > a2.score;\n}\n//#####################################################\n\
    \n\n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State operate(State s, int op, int &i){\n\n}\n//#####################################################\n\
    \nauto beam_search(State &init_state, int beam_width, int depth){\n    vector<State>\
    \ now;\n    now.emplace_back(init_state);\n    vector<State> next;\n\n    for\
    \ (int i=0; i<depth; i++){\n        bool sorted = false;\n        for (auto &s\
    \ : now){\n            // \u72B6\u614B\u3092\u9077\u79FB\u3055\u305B\u308B\n \
    \           for (auto op: {-1,1}){\n                // \u72B6\u614B\u3092\u5909\
    \u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\u5024\u3092\u8A08\u7B97\
    ###############\n                int nex_score;\n                //#################################################\n\
    \n                // \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\
    \u306E\u8A55\u4FA1\u5024\u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\
    \u307F\u9077\u79FB\n                if (sorted && nex_score <= next[beam_width-1].score)\
    \ continue;\n                auto nex = operate(s, op, i);\n                next.emplace_back(nex);\n\
    \n                if (next.size() >= 2*beam_width){\n                    sort(next.begin(),\
    \ next.end(), comp);\n                    next.resize(beam_width);\n         \
    \           sorted = true;\n                }\n            }\n        }\n    \
    \    sort(next.begin(), next.end(), comp);\n        swap(now, next);\n       \
    \ next.clear();\n    }\n\n    return now[0].move_history;\n}"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/beam_search.cpp
  requiredBy: []
  timestamp: '2024-12-08 13:07:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/beam_search.cpp
layout: document
redirect_from:
- /library/heuristic_library/beam_search.cpp
- /library/heuristic_library/beam_search.cpp.html
title: heuristic_library/beam_search.cpp
---
