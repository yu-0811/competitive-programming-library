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
  bundledCode: "#line 1 \"algorithm_library/cpp/RangeFactorize.cpp\"\n#include <iostream>\n\
    #include <vector>\n#include <cmath>\n#include <numeric>\nusing namespace std;\n\
    \n// \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\n// N\u4EE5\u4E0B\u306E\
    \u7D20\u6570\u3092\u5217\u6319\u3059\u308B\nvector<int> eratosthenes(int N) {\n\
    \    vector<bool> is_prime(N + 1, true);\n    is_prime[0] = is_prime[1] = false;\n\
    \    for (int p = 2; p * p <= N; ++p) {\n        if (is_prime[p]) {\n        \
    \    for (int q = p * p; q <= N; q += p) {\n                is_prime[q] = false;\n\
    \            }\n        }\n    }\n    vector<int> prime_numbers;\n    for (int\
    \ p = 2; p <= N; ++p) {\n        if (is_prime[p]) {\n            prime_numbers.push_back(p);\n\
    \        }\n    }\n    return prime_numbers;\n}\n\n// \u533A\u9593\u30A8\u30E9\
    \u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\uFF08\u7D20\u56E0\u6570\u5206\u89E3\
    \u7248\uFF09\n// [L, R]\u306E\u5404\u6570\u3092\u7D20\u56E0\u6570\u5206\u89E3\u3059\
    \u308B\nvector<vector<long long>> range_factorize(long long L, long long R) {\n\
    \    if (L > R) return {};\n    int sqrtR = sqrt(R);\n    vector<int> primes =\
    \ eratosthenes(sqrtR);\n    \n    long long range_size = R - L + 1;\n    vector<vector<long\
    \ long>> divisors(range_size);\n    vector<long long> num(range_size);\n    iota(num.begin(),\
    \ num.end(), L); // num\u3092 L, L+1, ..., R \u3067\u521D\u671F\u5316\n\n    for\
    \ (int p : primes) {\n        long long start = (L + p - 1) / p * p; // L\u4EE5\
    \u4E0A\u306E\u6700\u5C0F\u306Ep\u306E\u500D\u6570\n        for (long long q =\
    \ start; q <= R; q += p) {\n            long long idx = q - L;\n            while\
    \ (num[idx] % p == 0) {\n                divisors[idx].push_back(p);\n       \
    \         num[idx] /= p;\n            }\n        }\n    }\n\n    // sqrt(R)\u3088\
    \u308A\u5927\u304D\u3044\u7D20\u56E0\u6570\u3092\u51E6\u7406\n    for (long long\
    \ i = 0; i < range_size; ++i) {\n        if (num[i] > 1) {\n            divisors[i].push_back(num[i]);\n\
    \        }\n    }\n    \n    return divisors;\n}\n\n"
  code: "#include <iostream>\n#include <vector>\n#include <cmath>\n#include <numeric>\n\
    using namespace std;\n\n// \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\
    \n// N\u4EE5\u4E0B\u306E\u7D20\u6570\u3092\u5217\u6319\u3059\u308B\nvector<int>\
    \ eratosthenes(int N) {\n    vector<bool> is_prime(N + 1, true);\n    is_prime[0]\
    \ = is_prime[1] = false;\n    for (int p = 2; p * p <= N; ++p) {\n        if (is_prime[p])\
    \ {\n            for (int q = p * p; q <= N; q += p) {\n                is_prime[q]\
    \ = false;\n            }\n        }\n    }\n    vector<int> prime_numbers;\n\
    \    for (int p = 2; p <= N; ++p) {\n        if (is_prime[p]) {\n            prime_numbers.push_back(p);\n\
    \        }\n    }\n    return prime_numbers;\n}\n\n// \u533A\u9593\u30A8\u30E9\
    \u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\uFF08\u7D20\u56E0\u6570\u5206\u89E3\
    \u7248\uFF09\n// [L, R]\u306E\u5404\u6570\u3092\u7D20\u56E0\u6570\u5206\u89E3\u3059\
    \u308B\nvector<vector<long long>> range_factorize(long long L, long long R) {\n\
    \    if (L > R) return {};\n    int sqrtR = sqrt(R);\n    vector<int> primes =\
    \ eratosthenes(sqrtR);\n    \n    long long range_size = R - L + 1;\n    vector<vector<long\
    \ long>> divisors(range_size);\n    vector<long long> num(range_size);\n    iota(num.begin(),\
    \ num.end(), L); // num\u3092 L, L+1, ..., R \u3067\u521D\u671F\u5316\n\n    for\
    \ (int p : primes) {\n        long long start = (L + p - 1) / p * p; // L\u4EE5\
    \u4E0A\u306E\u6700\u5C0F\u306Ep\u306E\u500D\u6570\n        for (long long q =\
    \ start; q <= R; q += p) {\n            long long idx = q - L;\n            while\
    \ (num[idx] % p == 0) {\n                divisors[idx].push_back(p);\n       \
    \         num[idx] /= p;\n            }\n        }\n    }\n\n    // sqrt(R)\u3088\
    \u308A\u5927\u304D\u3044\u7D20\u56E0\u6570\u3092\u51E6\u7406\n    for (long long\
    \ i = 0; i < range_size; ++i) {\n        if (num[i] > 1) {\n            divisors[i].push_back(num[i]);\n\
    \        }\n    }\n    \n    return divisors;\n}\n\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/RangeFactorize.cpp
  requiredBy: []
  timestamp: '2025-07-29 17:33:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/RangeFactorize.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/RangeFactorize.cpp
- /library/algorithm_library/cpp/RangeFactorize.cpp.html
title: algorithm_library/cpp/RangeFactorize.cpp
---
