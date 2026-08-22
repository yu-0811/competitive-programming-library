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
  bundledCode: "#line 1 \"algorithm_library/cpp/line_int.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nusing ll = long long;\nusing i128 = __int128_t;\n\n//\
    \ \u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63: 1, \u8CA0: -1, 0: 0\nint sgn(i128\
    \ x) {\n   if(x > 0) return 1;\n   if(x < 0) return -1;\n   return 0;\n}\n\n//\
    \ \u6574\u6570\u5EA7\u6A19\u306E2\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\
    \u3002\u5EA7\u6A19\u306F long long \u3067\u6301\u3064\nstruct point {\n   ll x,\
    \ y;\n\n   point() : x(0), y(0) {}\n   point(ll x, ll y) : x(x), y(y) {}\n\n \
    \  point operator+() const { return *this; }\n   point operator-() const { return\
    \ point(-x, -y); }\n   point operator+(const point &p) const { return point(x\
    \ + p.x, y + p.y); }\n   point operator-(const point &p) const { return point(x\
    \ - p.x, y - p.y); }\n   point operator*(ll k) const { return point(x * k, y *\
    \ k); }\n   point &operator+=(const point &p) {\n      x += p.x;\n      y += p.y;\n\
    \      return *this;\n   }\n   point &operator-=(const point &p) {\n      x -=\
    \ p.x;\n      y -= p.y;\n      return *this;\n   }\n   point &operator*=(ll k)\
    \ {\n      x *= k;\n      y *= k;\n      return *this;\n   }\n   bool operator==(const\
    \ point &p) const { return x == p.x && y == p.y; }\n   bool operator!=(const point\
    \ &p) const { return !(*this == p); }\n   bool operator<(const point &p) const\
    \ {\n      if(x != p.x) return x < p.x;\n      return y < p.y;\n   }\n};\n\npoint\
    \ operator*(ll k, const point &p) { return p * k; }\n\nistream &operator>>(istream\
    \ &is, point &p) { return is >> p.x >> p.y; }\nostream &operator<<(ostream &os,\
    \ const point &p) { return os << p.x << ' ' << p.y; }\n\n// 2\u70B9 A, B \u3092\
    \u901A\u308B\u76F4\u7DDA\u3002\u7DDA\u5206\u3068\u3057\u3066\u4F7F\u3046\u95A2\
    \u6570\u3067\u306F\u7AEF\u70B9 A, B \u3092\u7AEF\u3068\u307F\u306A\u3059\nstruct\
    \ line {\n   point A, B;\n\n   line() = default;\n   line(point A, point B) :\
    \ A(A), B(B) {}\n};\n\n// \u76F4\u7DDA\u30FB\u7DDA\u5206 L \u306E\u65B9\u5411\u30D9\
    \u30AF\u30C8\u30EB B - A\npoint vec(line L) { return L.B - L.A; }\n\n// \u5185\
    \u7A4D\ni128 dot(point P, point Q) { return (i128)P.x * Q.x + (i128)P.y * Q.y;\
    \ }\n\n// \u5916\u7A4D\ni128 cross(point P, point Q) { return (i128)P.x * Q.y\
    \ - (i128)P.y * Q.x; }\n\n// \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\u306E\
    \ 2 \u4E57\ni128 norm(point P) { return dot(P, P); }\n\n// 2\u70B9\u9593\u8DDD\
    \u96E2\u306E 2 \u4E57\ni128 dist2(point P, point Q) { return norm(P - Q); }\n\n\
    // \u53CD\u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\u56DE\u8EE2\npoint rotate90(point\
    \ P) { return point(-P.y, P.x); }\n\n// \u70B9 C \u304C\u6709\u5411\u7DDA\u5206\
    \ AB \u306B\u5BFE\u3057\u3066\u3069\u306E\u4F4D\u7F6E\u306B\u3042\u308B\u304B\n\
    // 1: \u53CD\u6642\u8A08\u56DE\u308A, -1: \u6642\u8A08\u56DE\u308A, 2: A-B-C,\
    \ -2: C-A-B, 0: A-C-B\nint ccw(point A, point B, point C) {\n   point AB = B -\
    \ A, AC = C - A;\n   i128 cr = cross(AB, AC);\n   if(cr > 0) return 1;\n   if(cr\
    \ < 0) return -1;\n   if(dot(AB, AC) < 0) return 2;\n   if(norm(AB) < norm(AC))\
    \ return -2;\n   return 0;\n}\n\n// \u70B9 P \u304C\u76F4\u7DDA L \u4E0A\u306B\
    \u3042\u308B\u304B\nbool point_on_line(point P, line L) { return cross(P - L.A,\
    \ vec(L)) == 0; }\n\n// \u70B9 P \u304C\u7DDA\u5206 L \u4E0A\u306B\u3042\u308B\
    \u304B\nbool point_on_segment(point P, line L) {\n   return point_on_line(P, L)\
    \ && dot(P - L.A, P - L.B) <= 0;\n}\n\n// 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\
    \nbool is_parallel(line L1, line L2) { return cross(vec(L1), vec(L2)) == 0; }\n\
    \n// 2\u76F4\u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line\
    \ L1, line L2) { return dot(vec(L1), vec(L2)) == 0; }\n\n// 2\u7DDA\u5206\u304C\
    \u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\u5834\
    \u5408\u3082 true\nbool segment_intersect(line L1, line L2) {\n   return ccw(L1.A,\
    \ L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0\n          && ccw(L2.A, L2.B, L1.A)\
    \ * ccw(L2.A, L2.B, L1.B) <= 0;\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nusing ll = long long;\n\
    using i128 = __int128_t;\n\n// \u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63: 1,\
    \ \u8CA0: -1, 0: 0\nint sgn(i128 x) {\n   if(x > 0) return 1;\n   if(x < 0) return\
    \ -1;\n   return 0;\n}\n\n// \u6574\u6570\u5EA7\u6A19\u306E2\u6B21\u5143\u70B9\
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
    \ << ' ' << p.y; }\n\n// 2\u70B9 A, B \u3092\u901A\u308B\u76F4\u7DDA\u3002\u7DDA\
    \u5206\u3068\u3057\u3066\u4F7F\u3046\u95A2\u6570\u3067\u306F\u7AEF\u70B9 A, B\
    \ \u3092\u7AEF\u3068\u307F\u306A\u3059\nstruct line {\n   point A, B;\n\n   line()\
    \ = default;\n   line(point A, point B) : A(A), B(B) {}\n};\n\n// \u76F4\u7DDA\
    \u30FB\u7DDA\u5206 L \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB B - A\npoint vec(line\
    \ L) { return L.B - L.A; }\n\n// \u5185\u7A4D\ni128 dot(point P, point Q) { return\
    \ (i128)P.x * Q.x + (i128)P.y * Q.y; }\n\n// \u5916\u7A4D\ni128 cross(point P,\
    \ point Q) { return (i128)P.x * Q.y - (i128)P.y * Q.x; }\n\n// \u30D9\u30AF\u30C8\
    \u30EB\u306E\u9577\u3055\u306E 2 \u4E57\ni128 norm(point P) { return dot(P, P);\
    \ }\n\n// 2\u70B9\u9593\u8DDD\u96E2\u306E 2 \u4E57\ni128 dist2(point P, point\
    \ Q) { return norm(P - Q); }\n\n// \u53CD\u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\
    \u56DE\u8EE2\npoint rotate90(point P) { return point(-P.y, P.x); }\n\n// \u70B9\
    \ C \u304C\u6709\u5411\u7DDA\u5206 AB \u306B\u5BFE\u3057\u3066\u3069\u306E\u4F4D\
    \u7F6E\u306B\u3042\u308B\u304B\n// 1: \u53CD\u6642\u8A08\u56DE\u308A, -1: \u6642\
    \u8A08\u56DE\u308A, 2: A-B-C, -2: C-A-B, 0: A-C-B\nint ccw(point A, point B, point\
    \ C) {\n   point AB = B - A, AC = C - A;\n   i128 cr = cross(AB, AC);\n   if(cr\
    \ > 0) return 1;\n   if(cr < 0) return -1;\n   if(dot(AB, AC) < 0) return 2;\n\
    \   if(norm(AB) < norm(AC)) return -2;\n   return 0;\n}\n\n// \u70B9 P \u304C\u76F4\
    \u7DDA L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_line(point P, line L) {\
    \ return cross(P - L.A, vec(L)) == 0; }\n\n// \u70B9 P \u304C\u7DDA\u5206 L \u4E0A\
    \u306B\u3042\u308B\u304B\nbool point_on_segment(point P, line L) {\n   return\
    \ point_on_line(P, L) && dot(P - L.A, P - L.B) <= 0;\n}\n\n// 2\u76F4\u7DDA\u304C\
    \u5E73\u884C\u304B\nbool is_parallel(line L1, line L2) { return cross(vec(L1),\
    \ vec(L2)) == 0; }\n\n// 2\u76F4\u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\nbool\
    \ is_orthogonal(line L1, line L2) { return dot(vec(L1), vec(L2)) == 0; }\n\n//\
    \ 2\u7DDA\u5206\u304C\u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\
    \u3059\u308B\u5834\u5408\u3082 true\nbool segment_intersect(line L1, line L2)\
    \ {\n   return ccw(L1.A, L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0\n          &&\
    \ ccw(L2.A, L2.B, L1.A) * ccw(L2.A, L2.B, L1.B) <= 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/line_int.cpp
  requiredBy: []
  timestamp: '2026-08-23 01:04:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/line_int.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/line_int.cpp
- /library/algorithm_library/cpp/line_int.cpp.html
title: algorithm_library/cpp/line_int.cpp
---
