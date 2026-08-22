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
  bundledCode: "#line 1 \"algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp\"\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nstruct SumSegtree {\n    int\
    \ n, size, log;\n    unsigned long long mod;\n    vector<unsigned long long> data;\n\
    \n    SumSegtree() {}\n    SumSegtree(const vector<unsigned long long>& V, unsigned\
    \ long long mod_) : n(V.size()), mod(mod_) {\n        log = 0;\n        size =\
    \ 1;\n        while (size < n) size <<= 1, log++;\n        data.assign(2 * size,\
    \ 0);\n        for (int i = 0; i < n; i++) data[size + i] = V[i] % mod;\n    \
    \    for (int i = size - 1; i > 0; i--) update(i);\n    }\n\n    void update(int\
    \ k) { data[k] = (data[2 * k] + data[2 * k + 1]) % mod; }\n    void set_val(int\
    \ p, unsigned long long x) {\n        assert(0 <= p && p < n);\n        p += size;\n\
    \        data[p] = x % mod;\n        for (int i = 1; i <= log; i++) update(p >>\
    \ i);\n    }\n    unsigned long long prod(int l, int r) const {\n        assert(0\
    \ <= l && l <= r && r <= n);\n        unsigned long long sml = 0, smr = 0;\n \
    \       for (l += size, r += size; l < r; l >>= 1, r >>= 1) {\n            if\
    \ (l & 1) sml = (sml + data[l++]) % mod;\n            if (r & 1) smr = (data[--r]\
    \ + smr) % mod;\n        }\n        return (sml + smr) % mod;\n    }\n};\n\nstruct\
    \ changeable_RollingHash {\n    int N;\n    int ord_base = 'a';\n    unsigned\
    \ long long base, mod, inv;\n    vector<unsigned long long> base_pow, base_inv;\n\
    \    SumSegtree seg;\n\n    changeable_RollingHash(const string& S, unsigned long\
    \ long base_ = 1237, unsigned long long mod_ = (1ULL << 61) - 1)\n        : N(S.size()),\
    \ base(base_), mod(mod_) {\n        inv = mod_pow(base, mod - 2);\n        base_pow.assign(N\
    \ + 1, 1);\n        base_inv.assign(N + 1, 1);\n        for (int i = 0; i < N;\
    \ i++) {\n            base_pow[i + 1] = mul(base_pow[i], base);\n            base_inv[i\
    \ + 1] = mul(base_inv[i], inv);\n        }\n        vector<unsigned long long>\
    \ h(N);\n        for (int idx = 0; idx < N; idx++) h[idx] = mul(S[idx] - ord_base\
    \ + 1, base_pow[N - idx - 1]);\n        seg = SumSegtree(h, mod);\n    }\n\n \
    \   unsigned long long mul(unsigned long long a, unsigned long long b) const {\n\
    \        return (__uint128_t)a * b % mod;\n    }\n\n    unsigned long long mod_pow(unsigned\
    \ long long a, unsigned long long e) const {\n        unsigned long long r = 1;\n\
    \        while (e) {\n            if (e & 1) r = (__uint128_t)r * a % mod;\n \
    \           a = (__uint128_t)a * a % mod;\n            e >>= 1;\n        }\n \
    \       return r;\n    }\n\n    void change(int x, char c) {\n        seg.set_val(x,\
    \ mul(c - ord_base + 1, base_pow[N - x - 1]));\n    }\n\n    unsigned long long\
    \ get_hash(int l, int r) const {\n        return mul(seg.prod(l, r), base_inv[N\
    \ - r]);\n    }\n};\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nstruct SumSegtree {\n \
    \   int n, size, log;\n    unsigned long long mod;\n    vector<unsigned long long>\
    \ data;\n\n    SumSegtree() {}\n    SumSegtree(const vector<unsigned long long>&\
    \ V, unsigned long long mod_) : n(V.size()), mod(mod_) {\n        log = 0;\n \
    \       size = 1;\n        while (size < n) size <<= 1, log++;\n        data.assign(2\
    \ * size, 0);\n        for (int i = 0; i < n; i++) data[size + i] = V[i] % mod;\n\
    \        for (int i = size - 1; i > 0; i--) update(i);\n    }\n\n    void update(int\
    \ k) { data[k] = (data[2 * k] + data[2 * k + 1]) % mod; }\n    void set_val(int\
    \ p, unsigned long long x) {\n        assert(0 <= p && p < n);\n        p += size;\n\
    \        data[p] = x % mod;\n        for (int i = 1; i <= log; i++) update(p >>\
    \ i);\n    }\n    unsigned long long prod(int l, int r) const {\n        assert(0\
    \ <= l && l <= r && r <= n);\n        unsigned long long sml = 0, smr = 0;\n \
    \       for (l += size, r += size; l < r; l >>= 1, r >>= 1) {\n            if\
    \ (l & 1) sml = (sml + data[l++]) % mod;\n            if (r & 1) smr = (data[--r]\
    \ + smr) % mod;\n        }\n        return (sml + smr) % mod;\n    }\n};\n\nstruct\
    \ changeable_RollingHash {\n    int N;\n    int ord_base = 'a';\n    unsigned\
    \ long long base, mod, inv;\n    vector<unsigned long long> base_pow, base_inv;\n\
    \    SumSegtree seg;\n\n    changeable_RollingHash(const string& S, unsigned long\
    \ long base_ = 1237, unsigned long long mod_ = (1ULL << 61) - 1)\n        : N(S.size()),\
    \ base(base_), mod(mod_) {\n        inv = mod_pow(base, mod - 2);\n        base_pow.assign(N\
    \ + 1, 1);\n        base_inv.assign(N + 1, 1);\n        for (int i = 0; i < N;\
    \ i++) {\n            base_pow[i + 1] = mul(base_pow[i], base);\n            base_inv[i\
    \ + 1] = mul(base_inv[i], inv);\n        }\n        vector<unsigned long long>\
    \ h(N);\n        for (int idx = 0; idx < N; idx++) h[idx] = mul(S[idx] - ord_base\
    \ + 1, base_pow[N - idx - 1]);\n        seg = SumSegtree(h, mod);\n    }\n\n \
    \   unsigned long long mul(unsigned long long a, unsigned long long b) const {\n\
    \        return (__uint128_t)a * b % mod;\n    }\n\n    unsigned long long mod_pow(unsigned\
    \ long long a, unsigned long long e) const {\n        unsigned long long r = 1;\n\
    \        while (e) {\n            if (e & 1) r = (__uint128_t)r * a % mod;\n \
    \           a = (__uint128_t)a * a % mod;\n            e >>= 1;\n        }\n \
    \       return r;\n    }\n\n    void change(int x, char c) {\n        seg.set_val(x,\
    \ mul(c - ord_base + 1, base_pow[N - x - 1]));\n    }\n\n    unsigned long long\
    \ get_hash(int l, int r) const {\n        return mul(seg.prod(l, r), base_inv[N\
    \ - r]);\n    }\n};\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp
- /library/algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp.html
title: algorithm_library/cpp-from-py/string/changeable_RollingHash.cpp
---
