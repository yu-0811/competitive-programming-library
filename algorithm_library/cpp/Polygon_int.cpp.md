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
  bundledCode: "#line 1 \"algorithm_library/cpp/Polygon_int.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nusing ll = long long;\nusing i128 = __int128_t;\n\n//\
    \ contains \u306E\u8FD4\u308A\u5024\n// _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A\
    , _IN: \u5185\u90E8\nconst int _OUT = 0;\nconst int _ON = 1;\nconst int _IN =\
    \ 2;\n\n// \u6574\u6570\u5EA7\u6A19\u306E2\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\
    \u30C8\u30EB\u3002\u5EA7\u6A19\u306F long long \u3067\u6301\u3064\nstruct point\
    \ {\n   ll x, y;\n\n   point() : x(0), y(0) {}\n   point(ll x, ll y) : x(x), y(y)\
    \ {}\n\n   point operator+() const { return *this; }\n   point operator-() const\
    \ { return point(-x, -y); }\n   point operator+(const point &p) const { return\
    \ point(x + p.x, y + p.y); }\n   point operator-(const point &p) const { return\
    \ point(x - p.x, y - p.y); }\n   point operator*(ll k) const { return point(x\
    \ * k, y * k); }\n   point &operator+=(const point &p) {\n      x += p.x;\n  \
    \    y += p.y;\n      return *this;\n   }\n   point &operator-=(const point &p)\
    \ {\n      x -= p.x;\n      y -= p.y;\n      return *this;\n   }\n   point &operator*=(ll\
    \ k) {\n      x *= k;\n      y *= k;\n      return *this;\n   }\n   bool operator==(const\
    \ point &p) const { return x == p.x && y == p.y; }\n   bool operator!=(const point\
    \ &p) const { return !(*this == p); }\n   bool operator<(const point &p) const\
    \ {\n      if(x != p.x) return x < p.x;\n      return y < p.y;\n   }\n};\n\npoint\
    \ operator*(ll k, const point &p) { return p * k; }\n\nistream &operator>>(istream\
    \ &is, point &p) { return is >> p.x >> p.y; }\nostream &operator<<(ostream &os,\
    \ const point &p) { return os << p.x << ' ' << p.y; }\n\nusing Polygon = vector<point>;\n\
    \ni128 dot(point P, point Q) { return (i128)P.x * Q.x + (i128)P.y * Q.y; }\n\n\
    i128 cross(point P, point Q) { return (i128)P.x * Q.y - (i128)P.y * Q.x; }\n\n\
    int contains(const Polygon &Q, const point &p) {\n   bool in = false;\n   for(size_t\
    \ i = 0; i < Q.size(); i++) {\n      point a = Q[i] - p, b = Q[(i + 1) % Q.size()]\
    \ - p;\n      if(a.y > b.y) swap(a, b);\n      if(a.y <= 0 && 0 < b.y && cross(a,\
    \ b) < 0) in = !in;\n      if(cross(a, b) == 0 && dot(a, b) <= 0) return _ON;\n\
    \   }\n   return in ? _IN : _OUT;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nusing ll = long long;\n\
    using i128 = __int128_t;\n\n// contains \u306E\u8FD4\u308A\u5024\n// _OUT: \u5916\
    \u90E8, _ON: \u8FBA\u4E0A, _IN: \u5185\u90E8\nconst int _OUT = 0;\nconst int _ON\
    \ = 1;\nconst int _IN = 2;\n\n// \u6574\u6570\u5EA7\u6A19\u306E2\u6B21\u5143\u70B9\
    \u30FB\u30D9\u30AF\u30C8\u30EB\u3002\u5EA7\u6A19\u306F long long \u3067\u6301\u3064\
    \nstruct point {\n   ll x, y;\n\n   point() : x(0), y(0) {}\n   point(ll x, ll\
    \ y) : x(x), y(y) {}\n\n   point operator+() const { return *this; }\n   point\
    \ operator-() const { return point(-x, -y); }\n   point operator+(const point\
    \ &p) const { return point(x + p.x, y + p.y); }\n   point operator-(const point\
    \ &p) const { return point(x - p.x, y - p.y); }\n   point operator*(ll k) const\
    \ { return point(x * k, y * k); }\n   point &operator+=(const point &p) {\n  \
    \    x += p.x;\n      y += p.y;\n      return *this;\n   }\n   point &operator-=(const\
    \ point &p) {\n      x -= p.x;\n      y -= p.y;\n      return *this;\n   }\n \
    \  point &operator*=(ll k) {\n      x *= k;\n      y *= k;\n      return *this;\n\
    \   }\n   bool operator==(const point &p) const { return x == p.x && y == p.y;\
    \ }\n   bool operator!=(const point &p) const { return !(*this == p); }\n   bool\
    \ operator<(const point &p) const {\n      if(x != p.x) return x < p.x;\n    \
    \  return y < p.y;\n   }\n};\n\npoint operator*(ll k, const point &p) { return\
    \ p * k; }\n\nistream &operator>>(istream &is, point &p) { return is >> p.x >>\
    \ p.y; }\nostream &operator<<(ostream &os, const point &p) { return os << p.x\
    \ << ' ' << p.y; }\n\nusing Polygon = vector<point>;\n\ni128 dot(point P, point\
    \ Q) { return (i128)P.x * Q.x + (i128)P.y * Q.y; }\n\ni128 cross(point P, point\
    \ Q) { return (i128)P.x * Q.y - (i128)P.y * Q.x; }\n\nint contains(const Polygon\
    \ &Q, const point &p) {\n   bool in = false;\n   for(size_t i = 0; i < Q.size();\
    \ i++) {\n      point a = Q[i] - p, b = Q[(i + 1) % Q.size()] - p;\n      if(a.y\
    \ > b.y) swap(a, b);\n      if(a.y <= 0 && 0 < b.y && cross(a, b) < 0) in = !in;\n\
    \      if(cross(a, b) == 0 && dot(a, b) <= 0) return _ON;\n   }\n   return in\
    \ ? _IN : _OUT;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/Polygon_int.cpp
  requiredBy: []
  timestamp: '2026-08-28 16:05:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/Polygon_int.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/Polygon_int.cpp
- /library/algorithm_library/cpp/Polygon_int.cpp.html
title: algorithm_library/cpp/Polygon_int.cpp
---
