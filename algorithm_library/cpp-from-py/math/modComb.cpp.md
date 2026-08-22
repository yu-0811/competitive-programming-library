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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/modComb.cpp\"\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nstruct Comb {\n    int k;\n    long\
    \ long mod;\n    vector<long long> fact_inv, inv;\n\n    Comb(int k_, long long\
    \ mod_) : k(k_), mod(mod_), fact_inv(k + 1, 0), inv(k + 1, 0) {\n        fact_inv[0]\
    \ = 1;\n        if (k >= 1) fact_inv[1] = 1, inv[1] = 1;\n        for (int i =\
    \ 2; i <= k; i++) {\n            inv[i] = mod - inv[mod % i] * (mod / i) % mod;\n\
    \            fact_inv[i] = fact_inv[i - 1] * inv[i] % mod;\n        }\n    }\n\
    \n    long long nCk(long long n, int kk) const {\n        if (kk < 0 || kk > n)\
    \ return 0;\n        if (kk > k) throw invalid_argument(\"precomputed k is too\
    \ small\");\n        long long ans = 1;\n        for (int i = 0; i < kk; i++)\
    \ ans = ans * ((n - i) % mod) % mod;\n        return ans * fact_inv[kk] % mod;\n\
    \    }\n};\n\nstruct CombAll {\n    int n;\n    long long mod;\n    vector<long\
    \ long> fact, factinv, inv;\n\n    CombAll(int n_, long long mod_) : n(n_), mod(mod_),\
    \ fact{1, 1}, factinv{1, 1}, inv{0, 1} {\n        for (int i = 2; i <= n; i++)\
    \ {\n            fact.push_back(fact[i - 1] * i % mod);\n            inv.push_back((mod\
    \ - inv[mod % i] * (mod / i) % mod) % mod);\n            factinv.push_back(factinv[i\
    \ - 1] * inv[i] % mod);\n        }\n    }\n\n    long long C(int nn, int kk) const\
    \ {\n        assert(nn <= n);\n        if (kk < 0 || nn < 0 || nn < kk) return\
    \ 0;\n        if (kk == 1) return nn;\n        kk = min(kk, nn - kk);\n      \
    \  return fact[nn] * factinv[kk] % mod * factinv[nn - kk] % mod;\n    }\n\n  \
    \  long long H(int nn, int r) const {\n        return C(nn + r - 1, r);\n    }\n\
    };\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct Comb {\n    int\
    \ k;\n    long long mod;\n    vector<long long> fact_inv, inv;\n\n    Comb(int\
    \ k_, long long mod_) : k(k_), mod(mod_), fact_inv(k + 1, 0), inv(k + 1, 0) {\n\
    \        fact_inv[0] = 1;\n        if (k >= 1) fact_inv[1] = 1, inv[1] = 1;\n\
    \        for (int i = 2; i <= k; i++) {\n            inv[i] = mod - inv[mod %\
    \ i] * (mod / i) % mod;\n            fact_inv[i] = fact_inv[i - 1] * inv[i] %\
    \ mod;\n        }\n    }\n\n    long long nCk(long long n, int kk) const {\n \
    \       if (kk < 0 || kk > n) return 0;\n        if (kk > k) throw invalid_argument(\"\
    precomputed k is too small\");\n        long long ans = 1;\n        for (int i\
    \ = 0; i < kk; i++) ans = ans * ((n - i) % mod) % mod;\n        return ans * fact_inv[kk]\
    \ % mod;\n    }\n};\n\nstruct CombAll {\n    int n;\n    long long mod;\n    vector<long\
    \ long> fact, factinv, inv;\n\n    CombAll(int n_, long long mod_) : n(n_), mod(mod_),\
    \ fact{1, 1}, factinv{1, 1}, inv{0, 1} {\n        for (int i = 2; i <= n; i++)\
    \ {\n            fact.push_back(fact[i - 1] * i % mod);\n            inv.push_back((mod\
    \ - inv[mod % i] * (mod / i) % mod) % mod);\n            factinv.push_back(factinv[i\
    \ - 1] * inv[i] % mod);\n        }\n    }\n\n    long long C(int nn, int kk) const\
    \ {\n        assert(nn <= n);\n        if (kk < 0 || nn < 0 || nn < kk) return\
    \ 0;\n        if (kk == 1) return nn;\n        kk = min(kk, nn - kk);\n      \
    \  return fact[nn] * factinv[kk] % mod * factinv[nn - kk] % mod;\n    }\n\n  \
    \  long long H(int nn, int r) const {\n        return C(nn + r - 1, r);\n    }\n\
    };\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/modComb.cpp
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/modComb.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/modComb.cpp
- /library/algorithm_library/cpp-from-py/math/modComb.cpp.html
title: algorithm_library/cpp-from-py/math/modComb.cpp
---
