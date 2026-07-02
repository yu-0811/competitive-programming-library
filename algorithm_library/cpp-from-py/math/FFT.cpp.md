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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/math/FFT.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nstruct FFT {\n    int mod, g;\n\n    FFT(int MOD) : mod(MOD),\
    \ g(primitive_root_constexpr(MOD)) {}\n\n    long long modpow(long long a, long\
    \ long e) const {\n        long long r = 1;\n        while (e) {\n           \
    \ if (e & 1) r = r * a % mod;\n            a = a * a % mod;\n            e >>=\
    \ 1;\n        }\n        return r;\n    }\n\n    static int primitive_root_constexpr(int\
    \ m) {\n        if (m == 2) return 1;\n        if (m == 167772161) return 3;\n\
    \        if (m == 469762049) return 3;\n        if (m == 754974721) return 11;\n\
    \        if (m == 998244353) return 3;\n        vector<int> divs;\n        int\
    \ x = (m - 1) / 2;\n        divs.push_back(2);\n        while (x % 2 == 0) x /=\
    \ 2;\n        for (long long i = 3; i * i <= x; i += 2) {\n            if (x %\
    \ i == 0) {\n                divs.push_back((int)i);\n                while (x\
    \ % i == 0) x /= i;\n            }\n        }\n        if (x > 1) divs.push_back(x);\n\
    \        for (int g = 2;; g++) {\n            bool ok = true;\n            for\
    \ (int d : divs) {\n                long long r = 1, a = g, e = (m - 1) / d;\n\
    \                while (e) {\n                    if (e & 1) r = r * a % m;\n\
    \                    a = a * a % m;\n                    e >>= 1;\n          \
    \      }\n                if (r == 1) {\n                    ok = false;\n   \
    \                 break;\n                }\n            }\n            if (ok)\
    \ return g;\n        }\n    }\n\n    void ntt(vector<long long>& a, bool inverse)\
    \ const {\n        int n = (int)a.size();\n        for (int i = 1, j = 0; i <\
    \ n; i++) {\n            int bit = n >> 1;\n            for (; j & bit; bit >>=\
    \ 1) j ^= bit;\n            j ^= bit;\n            if (i < j) swap(a[i], a[j]);\n\
    \        }\n        for (int len = 2; len <= n; len <<= 1) {\n            long\
    \ long wlen = modpow(g, (mod - 1) / len);\n            if (inverse) wlen = modpow(wlen,\
    \ mod - 2);\n            for (int i = 0; i < n; i += len) {\n                long\
    \ long w = 1;\n                for (int j = 0; j < len / 2; j++) {\n         \
    \           long long u = a[i + j];\n                    long long v = a[i + j\
    \ + len / 2] * w % mod;\n                    a[i + j] = (u + v) % mod;\n     \
    \               a[i + j + len / 2] = (u - v + mod) % mod;\n                  \
    \  w = w * wlen % mod;\n                }\n            }\n        }\n        if\
    \ (inverse) {\n            long long inv_n = modpow(n, mod - 2);\n           \
    \ for (auto& x : a) x = x * inv_n % mod;\n        }\n    }\n\n    vector<long\
    \ long> convolution(vector<long long> a, vector<long long> b) const {\n      \
    \  int n = (int)a.size(), m = (int)b.size();\n        if (n == 0 || m == 0) return\
    \ {};\n        if (min(n, m) <= 40) {\n            vector<long long> res(n + m\
    \ - 1);\n            for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) res[i\
    \ + j] = (res[i + j] + a[i] * b[j]) % mod;\n            return res;\n        }\n\
    \        int z = 1;\n        while (z < n + m - 1) z <<= 1;\n        a.resize(z);\n\
    \        b.resize(z);\n        ntt(a, false);\n        ntt(b, false);\n      \
    \  for (int i = 0; i < z; i++) a[i] = a[i] * b[i] % mod;\n        ntt(a, true);\n\
    \        a.resize(n + m - 1);\n        return a;\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct FFT {\n    int mod,\
    \ g;\n\n    FFT(int MOD) : mod(MOD), g(primitive_root_constexpr(MOD)) {}\n\n \
    \   long long modpow(long long a, long long e) const {\n        long long r =\
    \ 1;\n        while (e) {\n            if (e & 1) r = r * a % mod;\n         \
    \   a = a * a % mod;\n            e >>= 1;\n        }\n        return r;\n   \
    \ }\n\n    static int primitive_root_constexpr(int m) {\n        if (m == 2) return\
    \ 1;\n        if (m == 167772161) return 3;\n        if (m == 469762049) return\
    \ 3;\n        if (m == 754974721) return 11;\n        if (m == 998244353) return\
    \ 3;\n        vector<int> divs;\n        int x = (m - 1) / 2;\n        divs.push_back(2);\n\
    \        while (x % 2 == 0) x /= 2;\n        for (long long i = 3; i * i <= x;\
    \ i += 2) {\n            if (x % i == 0) {\n                divs.push_back((int)i);\n\
    \                while (x % i == 0) x /= i;\n            }\n        }\n      \
    \  if (x > 1) divs.push_back(x);\n        for (int g = 2;; g++) {\n          \
    \  bool ok = true;\n            for (int d : divs) {\n                long long\
    \ r = 1, a = g, e = (m - 1) / d;\n                while (e) {\n              \
    \      if (e & 1) r = r * a % m;\n                    a = a * a % m;\n       \
    \             e >>= 1;\n                }\n                if (r == 1) {\n   \
    \                 ok = false;\n                    break;\n                }\n\
    \            }\n            if (ok) return g;\n        }\n    }\n\n    void ntt(vector<long\
    \ long>& a, bool inverse) const {\n        int n = (int)a.size();\n        for\
    \ (int i = 1, j = 0; i < n; i++) {\n            int bit = n >> 1;\n          \
    \  for (; j & bit; bit >>= 1) j ^= bit;\n            j ^= bit;\n            if\
    \ (i < j) swap(a[i], a[j]);\n        }\n        for (int len = 2; len <= n; len\
    \ <<= 1) {\n            long long wlen = modpow(g, (mod - 1) / len);\n       \
    \     if (inverse) wlen = modpow(wlen, mod - 2);\n            for (int i = 0;\
    \ i < n; i += len) {\n                long long w = 1;\n                for (int\
    \ j = 0; j < len / 2; j++) {\n                    long long u = a[i + j];\n  \
    \                  long long v = a[i + j + len / 2] * w % mod;\n             \
    \       a[i + j] = (u + v) % mod;\n                    a[i + j + len / 2] = (u\
    \ - v + mod) % mod;\n                    w = w * wlen % mod;\n               \
    \ }\n            }\n        }\n        if (inverse) {\n            long long inv_n\
    \ = modpow(n, mod - 2);\n            for (auto& x : a) x = x * inv_n % mod;\n\
    \        }\n    }\n\n    vector<long long> convolution(vector<long long> a, vector<long\
    \ long> b) const {\n        int n = (int)a.size(), m = (int)b.size();\n      \
    \  if (n == 0 || m == 0) return {};\n        if (min(n, m) <= 40) {\n        \
    \    vector<long long> res(n + m - 1);\n            for (int i = 0; i < n; i++)\
    \ for (int j = 0; j < m; j++) res[i + j] = (res[i + j] + a[i] * b[j]) % mod;\n\
    \            return res;\n        }\n        int z = 1;\n        while (z < n\
    \ + m - 1) z <<= 1;\n        a.resize(z);\n        b.resize(z);\n        ntt(a,\
    \ false);\n        ntt(b, false);\n        for (int i = 0; i < z; i++) a[i] =\
    \ a[i] * b[i] % mod;\n        ntt(a, true);\n        a.resize(n + m - 1);\n  \
    \      return a;\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/math/FFT.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/math/FFT.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/math/FFT.cpp
- /library/algorithm_library/cpp-from-py/math/FFT.cpp.html
title: algorithm_library/cpp-from-py/math/FFT.cpp
---
