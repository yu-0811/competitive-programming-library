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
  bundledCode: "#line 1 \"heuristic_library/cpp/beam_search_no_hash.cpp\"\n#include\
    \ <bits/stdc++.h>\n#line 3 \"heuristic_library/cpp/beam_search_no_hash.cpp\"\n\
    using namespace std;\n#define rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define\
    \ ll long long\nusing u64 = unsigned long long;\n#pragma GCC target(\"avx2\")\n\
    #pragma GCC optimize(\"O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nconstexpr\
    \ int T = 100;\nshort P[T], Q[T], R[T];\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ########################################\n\
    const int beam_width = 60000;\nconst int MAX_TURN = 100;\n//#####################################################\n\
    \n// \u72B6\u614B #############################################\nstruct Operation\
    \ {\n  char dx;\n};\n\nusing EvalType = int; // TODO\n\nstruct State {\n  EvalType\
    \ eval;\n  int zero_count;\n  short X[100];\n  Operation history[MAX_TURN];\n\n\
    \  State(int eval, int zero_count) : eval(eval), zero_count(zero_count) {}\n};\n\
    \nstruct Evaluator {\n  EvalType eval;\n  int zero_count;\n  unsigned short parent_state_index;\n\
    \  unsigned char operation_index;\n\n  Evaluator() = default; \n\n  Evaluator(EvalType\
    \ eval, int zero_count, unsigned short parent_state_index, unsigned char operation_index)\
    \ :\n    eval(eval), zero_count(zero_count), parent_state_index(parent_state_index),\
    \ operation_index(operation_index) {}\n};\n\n// \u30BD\u30FC\u30C8\u95A2\u6570\
    ########################################\n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\
    \u306E\u3068\u304D\nbool comp_max(const Evaluator &a1, const Evaluator &a2){\n\
    \    return a1.eval > a2.eval;\n}\n// \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\
    \u3068\u304D\nbool comp_min(const Evaluator &a1, const Evaluator &a2){\n    return\
    \ a1.eval < a2.eval;\n}\n//#####################################################\n\
    \n// \u8A55\u4FA1\u95A2\u6570########################################\nEvaluator\
    \ calc_new_eval(const State &s, const size_t state_idx, Operation &op, const size_t\
    \ op_idx,  const int& turn){\n  EvalType new_zero_count = s.zero_count;\n  if\
    \ (s.X[P[turn]] + op.dx == 0) new_zero_count++;\n  else if (s.X[P[turn]] == 0)\
    \ new_zero_count--;\n  if (s.X[Q[turn]] + op.dx == 0) new_zero_count++;\n  else\
    \ if (s.X[Q[turn]] == 0) new_zero_count--;\n  if (s.X[R[turn]] + op.dx == 0) new_zero_count++;\n\
    \  else if (s.X[R[turn]] == 0) new_zero_count--;\n  EvalType new_score = s.eval\
    \ + new_zero_count;\n  Evaluator new_evaluator(new_score, new_zero_count, state_idx,\
    \ op_idx);\n  return new_evaluator;\n}\n//#####################################################\n\
    \n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State operate(const State& s, const Evaluator& e, const Operation& op, int turn){\n\
    \  State new_s = s;\n  new_s.zero_count = e.zero_count;\n  new_s.eval = e.eval;\n\
    \  new_s.X[P[turn]] += op.dx;\n  new_s.X[Q[turn]] += op.dx;\n  new_s.X[R[turn]]\
    \ += op.dx;\n  new_s.history[turn] = op;\n  return new_s;\n}\n//#####################################################\n\
    \nauto beam_search(State &init_state){\n    vector<State> now;\n    now.emplace_back(init_state);\n\
    \    vector<State> next;\n    vector<Evaluator> cand;\n    now.reserve(beam_width);\n\
    \    next.reserve(beam_width);\n    cand.reserve(2*beam_width);\n\n    // \u9077\
    \u79FB\u5019\u88DC \n    vector<Operation> possible_op = {\n      {1},\n     \
    \ {-1}\n    };\n\n\n    for (int turn = 0; turn < MAX_TURN; turn++){\n       \
    \ bool sorted = false;\n        for (int i = 0; i < now.size(); i++){\n      \
    \      const State& s = now[i];\n            // \u5019\u88DC\u3092\u751F\u6210\
    \n            for (int j = 0; j < possible_op.size(); j++){\n                //\
    \ \u72B6\u614B\u3092\u5909\u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\
    \u5024\u3092\u8A08\n                auto new_evaluator = calc_new_eval(s, i, possible_op[j],\
    \ j, turn);\n\n                // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\
    \u304D, \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\u306E\u8A55\
    \u4FA1\u5024\u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\u307F\u8FFD\
    \u52A0\n                if (sorted && new_evaluator.eval <= cand[beam_width-1].eval)\
    \ continue;\n                // \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\
    \u304D, \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5927\u306E\u8A55\
    \u4FA1\u5024\u3088\u308A\u3082\u5C0F\u3055\u3044\u5834\u5408\u306E\u307F\u8FFD\
    \u52A0\n                // if (sorted && new_evaluator.eval >= cand[beam_width-1].eval)\
    \ continue;\n\n                cand.emplace_back(new_evaluator);\n\n         \
    \       // \u30BD\u30FC\u30C8\n                if (cand.size() >= 2*beam_width){\n\
    \                    sort(cand.begin(), cand.end(), comp_max);\n             \
    \       cand.resize(beam_width);\n                    sorted = true;\n       \
    \         }\n            }\n        }\n        if (cand.empty()) break;\n    \
    \    sort(cand.begin(), cand.end(), comp_max);\n        if (cand.size() > beam_width)\
    \ cand.resize(beam_width);\n        // \u9077\u79FB\u3092\u5B9F\u884C\n      \
    \  for (auto &e: cand){\n            State new_s = operate(now[e.parent_state_index],\
    \ e, possible_op[e.operation_index], turn);\n            next.emplace_back(new_s);\n\
    \        }\n\n        swap(now, next);\n        if (turn != MAX_TURN-1) {\n  \
    \        cand.clear();\n          next.clear();\n        }\n    }\n  return now[0];\n\
    }\n\nint main() {\n  ios::sync_with_stdio(false); cin.tie(0);\n  int _T; cin >>\
    \ _T;\n  for (int i=0; i<T; i++){\n    cin >> P[i] >> Q[i] >> R[i];\n    P[i]--;\
    \ Q[i]--; R[i]--;\n  }\n\n  State init_state(0, 100);\n  fill(init_state.X, init_state.X+100,\
    \ 0);\n\n  auto best_state = beam_search(init_state);\n  cerr << \"best eval:\
    \ \" << best_state.eval << \"\\n\";\n  for (auto op: best_state.history){\n  \
    \  if (op.dx == 1) cout << 'A' << \"\\n\";\n    else cout << 'B' << \"\\n\";\n\
    \  }\n}\n"
  code: "#include <bits/stdc++.h>\n#include <cassert>\nusing namespace std;\n#define\
    \ rep(i, n) for (int i = 0; i < (int)(n); i++)\n#define ll long long\nusing u64\
    \ = unsigned long long;\n#pragma GCC target(\"avx2\")\n#pragma GCC optimize(\"\
    O3\")\n#pragma GCC optimize(\"unroll-loops\")\n\nconstexpr int T = 100;\nshort\
    \ P[T], Q[T], R[T];\n\n// \u30D1\u30E9\u30E1\u30FC\u30BF ########################################\n\
    const int beam_width = 60000;\nconst int MAX_TURN = 100;\n//#####################################################\n\
    \n// \u72B6\u614B #############################################\nstruct Operation\
    \ {\n  char dx;\n};\n\nusing EvalType = int; // TODO\n\nstruct State {\n  EvalType\
    \ eval;\n  int zero_count;\n  short X[100];\n  Operation history[MAX_TURN];\n\n\
    \  State(int eval, int zero_count) : eval(eval), zero_count(zero_count) {}\n};\n\
    \nstruct Evaluator {\n  EvalType eval;\n  int zero_count;\n  unsigned short parent_state_index;\n\
    \  unsigned char operation_index;\n\n  Evaluator() = default; \n\n  Evaluator(EvalType\
    \ eval, int zero_count, unsigned short parent_state_index, unsigned char operation_index)\
    \ :\n    eval(eval), zero_count(zero_count), parent_state_index(parent_state_index),\
    \ operation_index(operation_index) {}\n};\n\n// \u30BD\u30FC\u30C8\u95A2\u6570\
    ########################################\n// \u30B9\u30B3\u30A2\u6700\u5927\u5316\
    \u306E\u3068\u304D\nbool comp_max(const Evaluator &a1, const Evaluator &a2){\n\
    \    return a1.eval > a2.eval;\n}\n// \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\
    \u3068\u304D\nbool comp_min(const Evaluator &a1, const Evaluator &a2){\n    return\
    \ a1.eval < a2.eval;\n}\n//#####################################################\n\
    \n// \u8A55\u4FA1\u95A2\u6570########################################\nEvaluator\
    \ calc_new_eval(const State &s, const size_t state_idx, Operation &op, const size_t\
    \ op_idx,  const int& turn){\n  EvalType new_zero_count = s.zero_count;\n  if\
    \ (s.X[P[turn]] + op.dx == 0) new_zero_count++;\n  else if (s.X[P[turn]] == 0)\
    \ new_zero_count--;\n  if (s.X[Q[turn]] + op.dx == 0) new_zero_count++;\n  else\
    \ if (s.X[Q[turn]] == 0) new_zero_count--;\n  if (s.X[R[turn]] + op.dx == 0) new_zero_count++;\n\
    \  else if (s.X[R[turn]] == 0) new_zero_count--;\n  EvalType new_score = s.eval\
    \ + new_zero_count;\n  Evaluator new_evaluator(new_score, new_zero_count, state_idx,\
    \ op_idx);\n  return new_evaluator;\n}\n//#####################################################\n\
    \n// \u72B6\u614B\u9077\u79FB\u95A2\u6570########################################\n\
    State operate(const State& s, const Evaluator& e, const Operation& op, int turn){\n\
    \  State new_s = s;\n  new_s.zero_count = e.zero_count;\n  new_s.eval = e.eval;\n\
    \  new_s.X[P[turn]] += op.dx;\n  new_s.X[Q[turn]] += op.dx;\n  new_s.X[R[turn]]\
    \ += op.dx;\n  new_s.history[turn] = op;\n  return new_s;\n}\n//#####################################################\n\
    \nauto beam_search(State &init_state){\n    vector<State> now;\n    now.emplace_back(init_state);\n\
    \    vector<State> next;\n    vector<Evaluator> cand;\n    now.reserve(beam_width);\n\
    \    next.reserve(beam_width);\n    cand.reserve(2*beam_width);\n\n    // \u9077\
    \u79FB\u5019\u88DC \n    vector<Operation> possible_op = {\n      {1},\n     \
    \ {-1}\n    };\n\n\n    for (int turn = 0; turn < MAX_TURN; turn++){\n       \
    \ bool sorted = false;\n        for (int i = 0; i < now.size(); i++){\n      \
    \      const State& s = now[i];\n            // \u5019\u88DC\u3092\u751F\u6210\
    \n            for (int j = 0; j < possible_op.size(); j++){\n                //\
    \ \u72B6\u614B\u3092\u5909\u5316\u3055\u305B\u305F\u3068\u304D\u306E\u8A55\u4FA1\
    \u5024\u3092\u8A08\n                auto new_evaluator = calc_new_eval(s, i, possible_op[j],\
    \ j, turn);\n\n                // \u30B9\u30B3\u30A2\u6700\u5927\u5316\u306E\u3068\
    \u304D, \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5C0F\u306E\u8A55\
    \u4FA1\u5024\u3088\u308A\u3082\u5927\u304D\u3044\u5834\u5408\u306E\u307F\u8FFD\
    \u52A0\n                if (sorted && new_evaluator.eval <= cand[beam_width-1].eval)\
    \ continue;\n                // \u30B9\u30B3\u30A2\u6700\u5C0F\u5316\u306E\u3068\
    \u304D, \u30BD\u30FC\u30C8\u6E08\u307F\u306E\u4E2D\u3067\u6700\u5927\u306E\u8A55\
    \u4FA1\u5024\u3088\u308A\u3082\u5C0F\u3055\u3044\u5834\u5408\u306E\u307F\u8FFD\
    \u52A0\n                // if (sorted && new_evaluator.eval >= cand[beam_width-1].eval)\
    \ continue;\n\n                cand.emplace_back(new_evaluator);\n\n         \
    \       // \u30BD\u30FC\u30C8\n                if (cand.size() >= 2*beam_width){\n\
    \                    sort(cand.begin(), cand.end(), comp_max);\n             \
    \       cand.resize(beam_width);\n                    sorted = true;\n       \
    \         }\n            }\n        }\n        if (cand.empty()) break;\n    \
    \    sort(cand.begin(), cand.end(), comp_max);\n        if (cand.size() > beam_width)\
    \ cand.resize(beam_width);\n        // \u9077\u79FB\u3092\u5B9F\u884C\n      \
    \  for (auto &e: cand){\n            State new_s = operate(now[e.parent_state_index],\
    \ e, possible_op[e.operation_index], turn);\n            next.emplace_back(new_s);\n\
    \        }\n\n        swap(now, next);\n        if (turn != MAX_TURN-1) {\n  \
    \        cand.clear();\n          next.clear();\n        }\n    }\n  return now[0];\n\
    }\n\nint main() {\n  ios::sync_with_stdio(false); cin.tie(0);\n  int _T; cin >>\
    \ _T;\n  for (int i=0; i<T; i++){\n    cin >> P[i] >> Q[i] >> R[i];\n    P[i]--;\
    \ Q[i]--; R[i]--;\n  }\n\n  State init_state(0, 100);\n  fill(init_state.X, init_state.X+100,\
    \ 0);\n\n  auto best_state = beam_search(init_state);\n  cerr << \"best eval:\
    \ \" << best_state.eval << \"\\n\";\n  for (auto op: best_state.history){\n  \
    \  if (op.dx == 1) cout << 'A' << \"\\n\";\n    else cout << 'B' << \"\\n\";\n\
    \  }\n}"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/cpp/beam_search_no_hash.cpp
  requiredBy: []
  timestamp: '2025-12-08 11:04:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/cpp/beam_search_no_hash.cpp
layout: document
redirect_from:
- /library/heuristic_library/cpp/beam_search_no_hash.cpp
- /library/heuristic_library/cpp/beam_search_no_hash.cpp.html
title: heuristic_library/cpp/beam_search_no_hash.cpp
---
