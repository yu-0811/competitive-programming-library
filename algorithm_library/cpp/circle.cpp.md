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
  bundledCode: "#line 1 \"algorithm_library/cpp/circle.cpp\"\n// Speed Star \u30E9\
    \u30A4\u30D6\u30E9\u30EA\u304B\u3089\u7A83\u76D7\uFF1Ahttps://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry\n\
    \n#include <bits/stdc++.h>\nusing namespace std;\n\nconst double eps = 1e-10;\n\
    const double INF = 1e18;\n\n// \u88DC\u52A9\u95A2\u6570\n// \u8AA4\u5DEE\u4ED8\
    \u304D\u3067\u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63: 1, \u8CA0: -1, \u307B\u307C\
    \ 0: 0\nint sgn(double x) {\n   if(x > eps) return 1;\n   if(x < -eps) return\
    \ -1;\n   return 0;\n}\n\n// 2\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\
    \u3002\u52A0\u6E1B\u7B97\u3084\u30B9\u30AB\u30E9\u30FC\u500D\u3092\u30D9\u30AF\
    \u30C8\u30EB\u3068\u3057\u3066\u6271\u3048\u308B\nstruct point {\n   double x,\
    \ y;\n\n   point() : x(0), y(0) {}\n   point(double x, double y) : x(x), y(y)\
    \ {}\n\n   point operator+() const { return *this; }\n   point operator-() const\
    \ { return point(-x, -y); }\n   point operator+(const point &p) const { return\
    \ point(x + p.x, y + p.y); }\n   point operator-(const point &p) const { return\
    \ point(x - p.x, y - p.y); }\n   point operator*(double k) const { return point(x\
    \ * k, y * k); }\n   point operator/(double k) const { return point(x / k, y /\
    \ k); }\n   point &operator+=(const point &p) {\n      x += p.x;\n      y += p.y;\n\
    \      return *this;\n   }\n   point &operator-=(const point &p) {\n      x -=\
    \ p.x;\n      y -= p.y;\n      return *this;\n   }\n   point &operator*=(double\
    \ k) {\n      x *= k;\n      y *= k;\n      return *this;\n   }\n   point &operator/=(double\
    \ k) {\n      x /= k;\n      y /= k;\n      return *this;\n   }\n   bool operator==(const\
    \ point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }\n   bool\
    \ operator!=(const point &p) const { return !(*this == p); }\n   bool operator<(const\
    \ point &p) const {\n      if(abs(x - p.x) >= eps) return x < p.x;\n      return\
    \ y < p.y - eps;\n   }\n};\n\npoint operator*(double k, const point &p) { return\
    \ p * k; }\n\nistream &operator>>(istream &is, point &p) { return is >> p.x >>\
    \ p.y; }\nostream &operator<<(ostream &os, const point &p) { return os << p.x\
    \ << ' ' << p.y; }\n\n// 2\u70B9 A, B \u3092\u901A\u308B\u76F4\u7DDA\u3002\u7DDA\
    \u5206\u3068\u3057\u3066\u4F7F\u3046\u95A2\u6570\u3067\u306F\u7AEF\u70B9 A, B\
    \ \u3092\u7AEF\u3068\u307F\u306A\u3059\nstruct line {\n   point A, B;\n\n   line()\
    \ = default;\n   line(point A, point B) : A(A), B(B) {}\n};\n\n// \u76F4\u7DDA\
    \u30FB\u7DDA\u5206 L \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB B - A\npoint vec(line\
    \ L) { return L.B - L.A; }\n// \u5185\u7A4D\ndouble dot(point P, point Q) { return\
    \ P.x * Q.x + P.y * Q.y; }\n// \u5916\u7A4D\ndouble cross(point P, point Q) {\
    \ return P.x * Q.y - P.y * Q.x; }\n// \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\
    \u306E 2 \u4E57\ndouble norm(point P) { return dot(P, P); }\n// \u30D9\u30AF\u30C8\
    \u30EB\u306E\u9577\u3055\ndouble abs(point P) { return sqrt(norm(P)); }\n// 2\u70B9\
    \u9593\u8DDD\u96E2\ndouble dist(point P, point Q) { return abs(P - Q); }\n// \u53CD\
    \u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\u56DE\u8EE2\npoint rotate90(point P)\
    \ { return point(-P.y, P.x); }\n// \u53CD\u6642\u8A08\u56DE\u308A\u306B theta\
    \ \u30E9\u30B8\u30A2\u30F3\u56DE\u8EE2\npoint rotate(point P, double theta) {\n\
    \   double c = cos(theta), s = sin(theta);\n   return point(c * P.x - s * P.y,\
    \ s * P.x + c * P.y);\n}\n\n// \u70B9 C \u304C\u6709\u5411\u7DDA\u5206 AB \u306B\
    \u5BFE\u3057\u3066\u3069\u306E\u4F4D\u7F6E\u306B\u3042\u308B\u304B\n// 1: \u53CD\
    \u6642\u8A08\u56DE\u308A, -1: \u6642\u8A08\u56DE\u308A, 2: A-B-C, -2: C-A-B, 0:\
    \ A-C-B\nint ccw(point A, point B, point C) {\n   point AB = B - A, AC = C - A;\n\
    \   if(cross(AB, AC) > eps) return 1;\n   if(cross(AB, AC) < -eps) return -1;\n\
    \   if(dot(AB, AC) < -eps) return 2;\n   if(norm(AB) < norm(AC) - eps) return\
    \ -2;\n   return 0;\n}\n/////////////////////////////////////////////////////////////\n\
    \n// \u70B9 P \u304C\u76F4\u7DDA L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_line(point\
    \ P, line L) { return abs(cross(P - L.A, vec(L))) < eps; }\n\n// \u70B9 P \u304C\
    \u7DDA\u5206 L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_segment(point P,\
    \ line L) {\n   return point_on_line(P, L) && dot(P - L.A, P - L.B) < eps;\n}\n\
    \n// \u70B9 P \u304B\u3089\u76F4\u7DDA L \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\
    \u306E\u8DB3\npoint projection(point P, line L) { return L.A + vec(L) * dot(P\
    \ - L.A, vec(L)) / norm(vec(L)); }\n\n// \u70B9 P \u3092\u76F4\u7DDA L \u306B\u95A2\
    \u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\npoint reflection(point\
    \ P, line L) { return projection(P, L) * 2 - P; }\n\n// \u70B9 P \u3068\u76F4\u7DDA\
    \ L \u306E\u8DDD\u96E2\ndouble point_line_distance(point P, line L) { return abs(cross(P\
    \ - L.A, vec(L))) / abs(vec(L)); }\n\n// \u70B9 P \u3068\u7DDA\u5206 L \u306E\u8DDD\
    \u96E2\ndouble point_segment_distance(point P, line L) {\n   if(dot(P - L.A, vec(L))\
    \ < 0) {\n      return dist(P, L.A);\n   } else if(dot(P - L.B, vec(L)) > 0) {\n\
    \      return dist(P, L.B);\n   } else {\n      return point_line_distance(P,\
    \ L);\n   }\n}\n\n// 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\nbool is_parallel(line\
    \ L1, line L2) { return abs(cross(vec(L1), vec(L2))) < eps; }\n\n// 2\u76F4\u7DDA\
    \u304C\u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line L1, line L2) { return\
    \ abs(dot(vec(L1), vec(L2))) < eps; }\n\n// 2\u76F4\u7DDA\u306E\u4EA4\u70B9\u3002\
    \u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npoint line_intersection(line\
    \ L1, line L2) {\n   assert(!is_parallel(L1, L2));\n   return L1.A + vec(L1) *\
    \ cross(L2.A - L1.A, vec(L2)) / cross(vec(L1), vec(L2));\n}\n\n// 2\u7DDA\u5206\
    \u304C\u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\
    \u5834\u5408\u3082 true\nbool segment_intersect(line L1, line L2) {\n   return\
    \ ccw(L1.A, L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0\n          && ccw(L2.A, L2.B,\
    \ L1.A) * ccw(L2.A, L2.B, L1.B) <= 0;\n}\n\n// 2\u7DDA\u5206\u9593\u306E\u8DDD\
    \u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble segment_distance(line\
    \ L1, line L2) {\n   if(segment_intersect(L1, L2)) {\n      return 0;\n   } else\
    \ {\n      double ans = INF;\n      ans = min(ans, point_segment_distance(L1.A,\
    \ L2));\n      ans = min(ans, point_segment_distance(L1.B, L2));\n      ans =\
    \ min(ans, point_segment_distance(L2.A, L1));\n      ans = min(ans, point_segment_distance(L2.B,\
    \ L1));\n      return ans;\n   }\n}\n\n/////////////////////////////////////////////\n\
    \nstruct circle {\n   point C; // \u4E2D\u5FC3\n   double r; // \u534A\u5F84\n\
    \n   circle() {}\n   circle(point C, double r) : C(C), r(r) {}\n};\n\n// \u76F4\
    \u7DDA L \u3068\u5186 C \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\
    \u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npair<point, point> line_circle_intersection(line\
    \ L, circle C) {\n   point P = projection(C.C, L);\n   double d = point_line_distance(C.C,\
    \ L);\n   assert(d <= C.r + eps);\n   double h = sqrt(max(0.0, C.r * C.r - d *\
    \ d));\n   point A = P + vec(L) / abs(vec(L)) * h;\n   point B = P - vec(L) /\
    \ abs(vec(L)) * h;\n   return make_pair(A, B);\n}\n\n// 2\u5186 C1, C2 \u306E\u4EA4\
    \u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\u5834\u5408\u3084\u540C\u5FC3\u5186\
    \u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npair<point, point> circle_intersection(circle\
    \ C1, circle C2) {\n   double d = dist(C1.C, C2.C);\n   assert(d > eps);\n   assert(abs(C1.r\
    \ - C2.r) <= d + eps && d <= C1.r + C2.r + eps);\n   double m = (C1.r * C1.r -\
    \ C2.r * C2.r + d * d) / (d * 2);\n   point M = C1.C + (C2.C - C1.C) / d * m;\n\
    \   double h = sqrt(max(0.0, C1.r * C1.r - m * m));\n   point H = rotate90(C2.C\
    \ - C1.C) / d * h;\n   return make_pair(M - H, M + H);\n}\n\n// \u70B9 P \u304B\
    \u3089\u5186 C \u3078\u5F15\u3044\u305F 2 \u672C\u306E\u63A5\u7DDA\u306E\u63A5\
    \u70B9\u3002P \u304C\u5186\u306E\u5185\u5074\u306B\u3042\u308B\u5834\u5408\u306F\
    \ assert \u3067\u843D\u3068\u3059\npair<point, point> circle_tangent(point P,\
    \ circle C) {\n   double d = dist(P, C.C);\n   assert(C.r <= d + eps);\n   double\
    \ r = sqrt(max(0.0, d * d - C.r * C.r));\n   return circle_intersection(C, circle(P,\
    \ r));\n}\n\n// 2\u5186 C1, C2 \u306E\u5171\u901A\u63A5\u7DDA\nvector<line> common_tangent(circle\
    \ C1, circle C2) {\n   if(C1.r < C2.r) { swap(C1, C2); }\n   double d = dist(C1.C,\
    \ C2.C);\n   vector<line> L;\n   if(C1.r - C2.r <= d + eps) {\n      if(C1.r -\
    \ C2.r <= eps) {\n         assert(d > eps);\n         point D = rotate90(C2.C\
    \ - C1.C) / d * C1.r;\n         L.push_back(line(C1.C + D, C2.C + D));\n     \
    \    L.push_back(line(C1.C - D, C2.C - D));\n      } else {\n         double m\
    \ = (C1.r - C2.r) * (C1.r - C2.r) / d;\n         point M = C1.C + (C2.C - C1.C)\
    \ / d * m;\n         double h = sqrt((C1.r - C2.r) * (C1.r - C2.r) - m * m);\n\
    \         point H1 = M + rotate90(C2.C - C1.C) / d * h;\n         point D1 = (H1\
    \ - C1.C) / dist(H1, C1.C) * C2.r;\n         L.push_back(line(H1 + D1, C2.C +\
    \ D1));\n         point H2 = M - rotate90(C2.C - C1.C) / d * h;\n         point\
    \ D2 = (H2 - C1.C) / dist(H2, C1.C) * C2.r;\n         L.push_back(line(H2 + D2,\
    \ C2.C + D2));\n      }\n   }\n   if(C1.r + C2.r <= d + eps) {\n      assert(d\
    \ > eps);\n      double m = (C1.r + C2.r) * (C1.r + C2.r) / d;\n      point M\
    \ = C1.C + (C2.C - C1.C) / d * m;\n      double h = sqrt((C1.r + C2.r) * (C1.r\
    \ + C2.r) - m * m);\n      point H1 = M + rotate90(C2.C - C1.C) / d * h;\n   \
    \   point D1 = (H1 - C1.C) / dist(H1, C1.C) * C2.r;\n      L.push_back(line(H1\
    \ - D1, C2.C - D1));\n      point H2 = M - rotate90(C2.C - C1.C) / d * h;\n  \
    \    point D2 = (H2 - C1.C) / dist(H2, C1.C) * C2.r;\n      L.push_back(line(H2\
    \ - D2, C2.C - D2));\n   }\n   return L;\n}\n"
  code: "// Speed Star \u30E9\u30A4\u30D6\u30E9\u30EA\u304B\u3089\u7A83\u76D7\uFF1A\
    https://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry\n\n#include\
    \ <bits/stdc++.h>\nusing namespace std;\n\nconst double eps = 1e-10;\nconst double\
    \ INF = 1e18;\n\n// \u88DC\u52A9\u95A2\u6570\n// \u8AA4\u5DEE\u4ED8\u304D\u3067\
    \u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63: 1, \u8CA0: -1, \u307B\u307C 0: 0\n\
    int sgn(double x) {\n   if(x > eps) return 1;\n   if(x < -eps) return -1;\n  \
    \ return 0;\n}\n\n// 2\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\u3002\u52A0\
    \u6E1B\u7B97\u3084\u30B9\u30AB\u30E9\u30FC\u500D\u3092\u30D9\u30AF\u30C8\u30EB\
    \u3068\u3057\u3066\u6271\u3048\u308B\nstruct point {\n   double x, y;\n\n   point()\
    \ : x(0), y(0) {}\n   point(double x, double y) : x(x), y(y) {}\n\n   point operator+()\
    \ const { return *this; }\n   point operator-() const { return point(-x, -y);\
    \ }\n   point operator+(const point &p) const { return point(x + p.x, y + p.y);\
    \ }\n   point operator-(const point &p) const { return point(x - p.x, y - p.y);\
    \ }\n   point operator*(double k) const { return point(x * k, y * k); }\n   point\
    \ operator/(double k) const { return point(x / k, y / k); }\n   point &operator+=(const\
    \ point &p) {\n      x += p.x;\n      y += p.y;\n      return *this;\n   }\n \
    \  point &operator-=(const point &p) {\n      x -= p.x;\n      y -= p.y;\n   \
    \   return *this;\n   }\n   point &operator*=(double k) {\n      x *= k;\n   \
    \   y *= k;\n      return *this;\n   }\n   point &operator/=(double k) {\n   \
    \   x /= k;\n      y /= k;\n      return *this;\n   }\n   bool operator==(const\
    \ point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }\n   bool\
    \ operator!=(const point &p) const { return !(*this == p); }\n   bool operator<(const\
    \ point &p) const {\n      if(abs(x - p.x) >= eps) return x < p.x;\n      return\
    \ y < p.y - eps;\n   }\n};\n\npoint operator*(double k, const point &p) { return\
    \ p * k; }\n\nistream &operator>>(istream &is, point &p) { return is >> p.x >>\
    \ p.y; }\nostream &operator<<(ostream &os, const point &p) { return os << p.x\
    \ << ' ' << p.y; }\n\n// 2\u70B9 A, B \u3092\u901A\u308B\u76F4\u7DDA\u3002\u7DDA\
    \u5206\u3068\u3057\u3066\u4F7F\u3046\u95A2\u6570\u3067\u306F\u7AEF\u70B9 A, B\
    \ \u3092\u7AEF\u3068\u307F\u306A\u3059\nstruct line {\n   point A, B;\n\n   line()\
    \ = default;\n   line(point A, point B) : A(A), B(B) {}\n};\n\n// \u76F4\u7DDA\
    \u30FB\u7DDA\u5206 L \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB B - A\npoint vec(line\
    \ L) { return L.B - L.A; }\n// \u5185\u7A4D\ndouble dot(point P, point Q) { return\
    \ P.x * Q.x + P.y * Q.y; }\n// \u5916\u7A4D\ndouble cross(point P, point Q) {\
    \ return P.x * Q.y - P.y * Q.x; }\n// \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\
    \u306E 2 \u4E57\ndouble norm(point P) { return dot(P, P); }\n// \u30D9\u30AF\u30C8\
    \u30EB\u306E\u9577\u3055\ndouble abs(point P) { return sqrt(norm(P)); }\n// 2\u70B9\
    \u9593\u8DDD\u96E2\ndouble dist(point P, point Q) { return abs(P - Q); }\n// \u53CD\
    \u6642\u8A08\u56DE\u308A\u306B 90 \u5EA6\u56DE\u8EE2\npoint rotate90(point P)\
    \ { return point(-P.y, P.x); }\n// \u53CD\u6642\u8A08\u56DE\u308A\u306B theta\
    \ \u30E9\u30B8\u30A2\u30F3\u56DE\u8EE2\npoint rotate(point P, double theta) {\n\
    \   double c = cos(theta), s = sin(theta);\n   return point(c * P.x - s * P.y,\
    \ s * P.x + c * P.y);\n}\n\n// \u70B9 C \u304C\u6709\u5411\u7DDA\u5206 AB \u306B\
    \u5BFE\u3057\u3066\u3069\u306E\u4F4D\u7F6E\u306B\u3042\u308B\u304B\n// 1: \u53CD\
    \u6642\u8A08\u56DE\u308A, -1: \u6642\u8A08\u56DE\u308A, 2: A-B-C, -2: C-A-B, 0:\
    \ A-C-B\nint ccw(point A, point B, point C) {\n   point AB = B - A, AC = C - A;\n\
    \   if(cross(AB, AC) > eps) return 1;\n   if(cross(AB, AC) < -eps) return -1;\n\
    \   if(dot(AB, AC) < -eps) return 2;\n   if(norm(AB) < norm(AC) - eps) return\
    \ -2;\n   return 0;\n}\n/////////////////////////////////////////////////////////////\n\
    \n// \u70B9 P \u304C\u76F4\u7DDA L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_line(point\
    \ P, line L) { return abs(cross(P - L.A, vec(L))) < eps; }\n\n// \u70B9 P \u304C\
    \u7DDA\u5206 L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_segment(point P,\
    \ line L) {\n   return point_on_line(P, L) && dot(P - L.A, P - L.B) < eps;\n}\n\
    \n// \u70B9 P \u304B\u3089\u76F4\u7DDA L \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\
    \u306E\u8DB3\npoint projection(point P, line L) { return L.A + vec(L) * dot(P\
    \ - L.A, vec(L)) / norm(vec(L)); }\n\n// \u70B9 P \u3092\u76F4\u7DDA L \u306B\u95A2\
    \u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\npoint reflection(point\
    \ P, line L) { return projection(P, L) * 2 - P; }\n\n// \u70B9 P \u3068\u76F4\u7DDA\
    \ L \u306E\u8DDD\u96E2\ndouble point_line_distance(point P, line L) { return abs(cross(P\
    \ - L.A, vec(L))) / abs(vec(L)); }\n\n// \u70B9 P \u3068\u7DDA\u5206 L \u306E\u8DDD\
    \u96E2\ndouble point_segment_distance(point P, line L) {\n   if(dot(P - L.A, vec(L))\
    \ < 0) {\n      return dist(P, L.A);\n   } else if(dot(P - L.B, vec(L)) > 0) {\n\
    \      return dist(P, L.B);\n   } else {\n      return point_line_distance(P,\
    \ L);\n   }\n}\n\n// 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\nbool is_parallel(line\
    \ L1, line L2) { return abs(cross(vec(L1), vec(L2))) < eps; }\n\n// 2\u76F4\u7DDA\
    \u304C\u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line L1, line L2) { return\
    \ abs(dot(vec(L1), vec(L2))) < eps; }\n\n// 2\u76F4\u7DDA\u306E\u4EA4\u70B9\u3002\
    \u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npoint line_intersection(line\
    \ L1, line L2) {\n   assert(!is_parallel(L1, L2));\n   return L1.A + vec(L1) *\
    \ cross(L2.A - L1.A, vec(L2)) / cross(vec(L1), vec(L2));\n}\n\n// 2\u7DDA\u5206\
    \u304C\u4EA4\u5DEE\u3059\u308B\u304B\u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\
    \u5834\u5408\u3082 true\nbool segment_intersect(line L1, line L2) {\n   return\
    \ ccw(L1.A, L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0\n          && ccw(L2.A, L2.B,\
    \ L1.A) * ccw(L2.A, L2.B, L1.B) <= 0;\n}\n\n// 2\u7DDA\u5206\u9593\u306E\u8DDD\
    \u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble segment_distance(line\
    \ L1, line L2) {\n   if(segment_intersect(L1, L2)) {\n      return 0;\n   } else\
    \ {\n      double ans = INF;\n      ans = min(ans, point_segment_distance(L1.A,\
    \ L2));\n      ans = min(ans, point_segment_distance(L1.B, L2));\n      ans =\
    \ min(ans, point_segment_distance(L2.A, L1));\n      ans = min(ans, point_segment_distance(L2.B,\
    \ L1));\n      return ans;\n   }\n}\n\n/////////////////////////////////////////////\n\
    \nstruct circle {\n   point C; // \u4E2D\u5FC3\n   double r; // \u534A\u5F84\n\
    \n   circle() {}\n   circle(point C, double r) : C(C), r(r) {}\n};\n\n// \u76F4\
    \u7DDA L \u3068\u5186 C \u306E\u4EA4\u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\
    \u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npair<point, point> line_circle_intersection(line\
    \ L, circle C) {\n   point P = projection(C.C, L);\n   double d = point_line_distance(C.C,\
    \ L);\n   assert(d <= C.r + eps);\n   double h = sqrt(max(0.0, C.r * C.r - d *\
    \ d));\n   point A = P + vec(L) / abs(vec(L)) * h;\n   point B = P - vec(L) /\
    \ abs(vec(L)) * h;\n   return make_pair(A, B);\n}\n\n// 2\u5186 C1, C2 \u306E\u4EA4\
    \u70B9\u3002\u4EA4\u70B9\u304C\u306A\u3044\u5834\u5408\u3084\u540C\u5FC3\u5186\
    \u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npair<point, point> circle_intersection(circle\
    \ C1, circle C2) {\n   double d = dist(C1.C, C2.C);\n   assert(d > eps);\n   assert(abs(C1.r\
    \ - C2.r) <= d + eps && d <= C1.r + C2.r + eps);\n   double m = (C1.r * C1.r -\
    \ C2.r * C2.r + d * d) / (d * 2);\n   point M = C1.C + (C2.C - C1.C) / d * m;\n\
    \   double h = sqrt(max(0.0, C1.r * C1.r - m * m));\n   point H = rotate90(C2.C\
    \ - C1.C) / d * h;\n   return make_pair(M - H, M + H);\n}\n\n// \u70B9 P \u304B\
    \u3089\u5186 C \u3078\u5F15\u3044\u305F 2 \u672C\u306E\u63A5\u7DDA\u306E\u63A5\
    \u70B9\u3002P \u304C\u5186\u306E\u5185\u5074\u306B\u3042\u308B\u5834\u5408\u306F\
    \ assert \u3067\u843D\u3068\u3059\npair<point, point> circle_tangent(point P,\
    \ circle C) {\n   double d = dist(P, C.C);\n   assert(C.r <= d + eps);\n   double\
    \ r = sqrt(max(0.0, d * d - C.r * C.r));\n   return circle_intersection(C, circle(P,\
    \ r));\n}\n\n// 2\u5186 C1, C2 \u306E\u5171\u901A\u63A5\u7DDA\nvector<line> common_tangent(circle\
    \ C1, circle C2) {\n   if(C1.r < C2.r) { swap(C1, C2); }\n   double d = dist(C1.C,\
    \ C2.C);\n   vector<line> L;\n   if(C1.r - C2.r <= d + eps) {\n      if(C1.r -\
    \ C2.r <= eps) {\n         assert(d > eps);\n         point D = rotate90(C2.C\
    \ - C1.C) / d * C1.r;\n         L.push_back(line(C1.C + D, C2.C + D));\n     \
    \    L.push_back(line(C1.C - D, C2.C - D));\n      } else {\n         double m\
    \ = (C1.r - C2.r) * (C1.r - C2.r) / d;\n         point M = C1.C + (C2.C - C1.C)\
    \ / d * m;\n         double h = sqrt((C1.r - C2.r) * (C1.r - C2.r) - m * m);\n\
    \         point H1 = M + rotate90(C2.C - C1.C) / d * h;\n         point D1 = (H1\
    \ - C1.C) / dist(H1, C1.C) * C2.r;\n         L.push_back(line(H1 + D1, C2.C +\
    \ D1));\n         point H2 = M - rotate90(C2.C - C1.C) / d * h;\n         point\
    \ D2 = (H2 - C1.C) / dist(H2, C1.C) * C2.r;\n         L.push_back(line(H2 + D2,\
    \ C2.C + D2));\n      }\n   }\n   if(C1.r + C2.r <= d + eps) {\n      assert(d\
    \ > eps);\n      double m = (C1.r + C2.r) * (C1.r + C2.r) / d;\n      point M\
    \ = C1.C + (C2.C - C1.C) / d * m;\n      double h = sqrt((C1.r + C2.r) * (C1.r\
    \ + C2.r) - m * m);\n      point H1 = M + rotate90(C2.C - C1.C) / d * h;\n   \
    \   point D1 = (H1 - C1.C) / dist(H1, C1.C) * C2.r;\n      L.push_back(line(H1\
    \ - D1, C2.C - D1));\n      point H2 = M - rotate90(C2.C - C1.C) / d * h;\n  \
    \    point D2 = (H2 - C1.C) / dist(H2, C1.C) * C2.r;\n      L.push_back(line(H2\
    \ - D2, C2.C - D2));\n   }\n   return L;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/circle.cpp
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/circle.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/circle.cpp
- /library/algorithm_library/cpp/circle.cpp.html
title: algorithm_library/cpp/circle.cpp
---
