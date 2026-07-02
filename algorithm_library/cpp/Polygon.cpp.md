---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry
  bundledCode: "#line 1 \"algorithm_library/cpp/Polygon.cpp\"\n// Speed Star \u30E9\
    \u30A4\u30D6\u30E9\u30EA\u304B\u3089\u7A83\u76D7\uFF1Ahttps://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry\n\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nconst double eps = 1e-10;\n\
    \n// contains \u306E\u8FD4\u308A\u5024\n// _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A\
    , _IN: \u5185\u90E8\nconst int _OUT = 0;\nconst int _ON = 1;\nconst int _IN =\
    \ 2;\n\n// 2\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\nstruct Point {\n\
    \   double x, y;\n\n   Point() : x(0), y(0) {}\n   Point(double x, double y) :\
    \ x(x), y(y) {}\n\n   Point operator+() const { return *this; }\n   Point operator-()\
    \ const { return Point(-x, -y); }\n   Point operator+(const Point &p) const {\
    \ return Point(x + p.x, y + p.y); }\n   Point operator-(const Point &p) const\
    \ { return Point(x - p.x, y - p.y); }\n   Point operator*(double k) const { return\
    \ Point(x * k, y * k); }\n   Point operator/(double k) const { return Point(x\
    \ / k, y / k); }\n   Point &operator+=(const Point &p) {\n      x += p.x;\n  \
    \    y += p.y;\n      return *this;\n   }\n   Point &operator-=(const Point &p)\
    \ {\n      x -= p.x;\n      y -= p.y;\n      return *this;\n   }\n   Point &operator*=(double\
    \ k) {\n      x *= k;\n      y *= k;\n      return *this;\n   }\n   Point &operator/=(double\
    \ k) {\n      x /= k;\n      y /= k;\n      return *this;\n   }\n   bool operator==(const\
    \ Point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }\n   bool\
    \ operator!=(const Point &p) const { return !(*this == p); }\n   bool operator<(const\
    \ Point &p) const {\n      if(abs(x - p.x) >= eps) return x < p.x;\n      return\
    \ y < p.y - eps;\n   }\n};\n\nPoint operator*(double k, const Point &p) { return\
    \ p * k; }\n\nistream &operator>>(istream &is, Point &p) { return is >> p.x >>\
    \ p.y; }\nostream &operator<<(ostream &os, const Point &p) { return os << p.x\
    \ << ' ' << p.y; }\n\nusing Polygon = vector<Point>;\n\ndouble dot(Point P, Point\
    \ Q) { return P.x * Q.x + P.y * Q.y; }\n\ndouble cross(Point P, Point Q) { return\
    \ P.x * Q.y - P.y * Q.x; }\n\n///////////////////////////////////////////\n\n\
    // \u591A\u89D2\u5F62 Q \u306B\u5BFE\u3057\u3066\u70B9 p \u306E\u5185\u5916\u5224\
    \u5B9A\nint contains(const Polygon& Q, const Point& p) {\n   bool in = false;\n\
    \   for(size_t i = 0; i < Q.size(); i++) {\n      Point a = Q[i] - p, b = Q[(i\
    \ + 1) % Q.size()] - p;\n      if(a.y > b.y) swap(a, b);\n      if(a.y <= eps\
    \ && eps < b.y && cross(a, b) < -eps) in = !in;\n      if(abs(cross(a, b)) < eps\
    \ && dot(a, b) <= eps) return _ON;\n   }\n   return in ? _IN : _OUT;\n}\n"
  code: "// Speed Star \u30E9\u30A4\u30D6\u30E9\u30EA\u304B\u3089\u7A83\u76D7\uFF1A\
    https://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry\n\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nconst double eps = 1e-10;\n\n// contains\
    \ \u306E\u8FD4\u308A\u5024\n// _OUT: \u5916\u90E8, _ON: \u8FBA\u4E0A, _IN: \u5185\
    \u90E8\nconst int _OUT = 0;\nconst int _ON = 1;\nconst int _IN = 2;\n\n// 2\u6B21\
    \u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\nstruct Point {\n   double x, y;\n\n\
    \   Point() : x(0), y(0) {}\n   Point(double x, double y) : x(x), y(y) {}\n\n\
    \   Point operator+() const { return *this; }\n   Point operator-() const { return\
    \ Point(-x, -y); }\n   Point operator+(const Point &p) const { return Point(x\
    \ + p.x, y + p.y); }\n   Point operator-(const Point &p) const { return Point(x\
    \ - p.x, y - p.y); }\n   Point operator*(double k) const { return Point(x * k,\
    \ y * k); }\n   Point operator/(double k) const { return Point(x / k, y / k);\
    \ }\n   Point &operator+=(const Point &p) {\n      x += p.x;\n      y += p.y;\n\
    \      return *this;\n   }\n   Point &operator-=(const Point &p) {\n      x -=\
    \ p.x;\n      y -= p.y;\n      return *this;\n   }\n   Point &operator*=(double\
    \ k) {\n      x *= k;\n      y *= k;\n      return *this;\n   }\n   Point &operator/=(double\
    \ k) {\n      x /= k;\n      y /= k;\n      return *this;\n   }\n   bool operator==(const\
    \ Point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }\n   bool\
    \ operator!=(const Point &p) const { return !(*this == p); }\n   bool operator<(const\
    \ Point &p) const {\n      if(abs(x - p.x) >= eps) return x < p.x;\n      return\
    \ y < p.y - eps;\n   }\n};\n\nPoint operator*(double k, const Point &p) { return\
    \ p * k; }\n\nistream &operator>>(istream &is, Point &p) { return is >> p.x >>\
    \ p.y; }\nostream &operator<<(ostream &os, const Point &p) { return os << p.x\
    \ << ' ' << p.y; }\n\nusing Polygon = vector<Point>;\n\ndouble dot(Point P, Point\
    \ Q) { return P.x * Q.x + P.y * Q.y; }\n\ndouble cross(Point P, Point Q) { return\
    \ P.x * Q.y - P.y * Q.x; }\n\n///////////////////////////////////////////\n\n\
    // \u591A\u89D2\u5F62 Q \u306B\u5BFE\u3057\u3066\u70B9 p \u306E\u5185\u5916\u5224\
    \u5B9A\nint contains(const Polygon& Q, const Point& p) {\n   bool in = false;\n\
    \   for(size_t i = 0; i < Q.size(); i++) {\n      Point a = Q[i] - p, b = Q[(i\
    \ + 1) % Q.size()] - p;\n      if(a.y > b.y) swap(a, b);\n      if(a.y <= eps\
    \ && eps < b.y && cross(a, b) < -eps) in = !in;\n      if(abs(cross(a, b)) < eps\
    \ && dot(a, b) <= eps) return _ON;\n   }\n   return in ? _IN : _OUT;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/Polygon.cpp
  requiredBy: []
  timestamp: '2026-07-02 14:44:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/Polygon.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/Polygon.cpp
- /library/algorithm_library/cpp/Polygon.cpp.html
title: algorithm_library/cpp/Polygon.cpp
---
