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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/PIE.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nstruct eratosthenes {\n    int MAX;\n    vector<bool>\
    \ isprime;\n    vector<int> mebius, min_factor;\n\n    eratosthenes(int MAX_)\
    \ : MAX(MAX_), isprime(MAX + 1, true), mebius(MAX + 1, 1), min_factor(MAX + 1,\
    \ -1) {\n        if (MAX >= 0) isprime[0] = false, min_factor[0] = 0;\n      \
    \  if (MAX >= 1) isprime[1] = false, min_factor[1] = 1;\n        for (int i =\
    \ 2; i <= MAX; i++) {\n            if (!isprime[i]) continue;\n            mebius[i]\
    \ = -1;\n            min_factor[i] = i;\n            for (long long j = 2LL *\
    \ i; j <= MAX; j += i) {\n                isprime[j] = false;\n              \
    \  if ((j / i) % i == 0) mebius[j] = 0;\n                else mebius[j] *= -1;\n\
    \                if (min_factor[j] == -1) min_factor[j] = i;\n            }\n\
    \        }\n    }\n\n    vector<pair<int, int>> prime_factors(int n) const {\n\
    \        vector<pair<int, int>> res;\n        while (n != 1) {\n            int\
    \ prime = min_factor[n], exp = 0;\n            while (n != 1 && min_factor[n]\
    \ == prime) {\n                exp++;\n                n /= prime;\n         \
    \   }\n            res.emplace_back(prime, exp);\n        }\n        return res;\n\
    \    }\n\n    vector<int> divisors(int n) const {\n        vector<int> res{1};\n\
    \        for (auto [prime, exp] : prime_factors(n)) {\n            int current_size\
    \ = (int)res.size();\n            for (int i = 0; i < current_size; i++) {\n \
    \               int value = 1;\n                for (int j = 0; j < exp; j++)\
    \ {\n                    value *= prime;\n                    res.push_back(res[i]\
    \ * value);\n                }\n            }\n        }\n        return res;\n\
    \    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct eratosthenes {\n\
    \    int MAX;\n    vector<bool> isprime;\n    vector<int> mebius, min_factor;\n\
    \n    eratosthenes(int MAX_) : MAX(MAX_), isprime(MAX + 1, true), mebius(MAX +\
    \ 1, 1), min_factor(MAX + 1, -1) {\n        if (MAX >= 0) isprime[0] = false,\
    \ min_factor[0] = 0;\n        if (MAX >= 1) isprime[1] = false, min_factor[1]\
    \ = 1;\n        for (int i = 2; i <= MAX; i++) {\n            if (!isprime[i])\
    \ continue;\n            mebius[i] = -1;\n            min_factor[i] = i;\n   \
    \         for (long long j = 2LL * i; j <= MAX; j += i) {\n                isprime[j]\
    \ = false;\n                if ((j / i) % i == 0) mebius[j] = 0;\n           \
    \     else mebius[j] *= -1;\n                if (min_factor[j] == -1) min_factor[j]\
    \ = i;\n            }\n        }\n    }\n\n    vector<pair<int, int>> prime_factors(int\
    \ n) const {\n        vector<pair<int, int>> res;\n        while (n != 1) {\n\
    \            int prime = min_factor[n], exp = 0;\n            while (n != 1 &&\
    \ min_factor[n] == prime) {\n                exp++;\n                n /= prime;\n\
    \            }\n            res.emplace_back(prime, exp);\n        }\n       \
    \ return res;\n    }\n\n    vector<int> divisors(int n) const {\n        vector<int>\
    \ res{1};\n        for (auto [prime, exp] : prime_factors(n)) {\n            int\
    \ current_size = (int)res.size();\n            for (int i = 0; i < current_size;\
    \ i++) {\n                int value = 1;\n                for (int j = 0; j <\
    \ exp; j++) {\n                    value *= prime;\n                    res.push_back(res[i]\
    \ * value);\n                }\n            }\n        }\n        return res;\n\
    \    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/PIE.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/PIE.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/PIE.cpp
- /library/algorithm_library/cpp-from-py/math/PIE.cpp.html
title: algorithm_library/cpp-from-py/math/PIE.cpp
---
