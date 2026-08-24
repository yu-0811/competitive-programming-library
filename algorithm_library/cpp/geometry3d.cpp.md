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
  bundledCode: "#line 1 \"algorithm_library/cpp/geometry3d.cpp\"\n#include <bits/stdc++.h>\n\
    using namespace std;\n\nconst double eps = 1e-10;\nconst double INF = 1e18;\n\n\
    // \u8AA4\u5DEE\u4ED8\u304D\u3067\u7B26\u53F7\u3092\u8FD4\u3059\u3002\u6B63: 1,\
    \ \u8CA0: -1, \u307B\u307C 0: 0\nint sgn(double x) {\n   if(x > eps) return 1;\n\
    \   if(x < -eps) return -1;\n   return 0;\n}\n\n// [0, 1] \u306B\u4E38\u3081\u308B\
    \ndouble clamp01(double x) { return max(0.0, min(1.0, x)); }\n// acos \u306A\u3069\
    \u306B\u6E21\u3059\u5024\u3092 [-1, 1] \u306B\u4E38\u3081\u308B\ndouble clamp_unit(double\
    \ x) { return max(-1.0, min(1.0, x)); }\n\n// 3\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\
    \u30C8\u30EB\u3002\u52A0\u6E1B\u7B97\u3084\u30B9\u30AB\u30E9\u30FC\u500D\u3092\
    \u30D9\u30AF\u30C8\u30EB\u3068\u3057\u3066\u6271\u3048\u308B\nstruct point3d {\n\
    \   double x, y, z;\n\n   point3d() : x(0), y(0), z(0) {}\n   point3d(double x,\
    \ double y, double z) : x(x), y(y), z(z) {}\n\n   point3d operator+() const {\
    \ return *this; }\n   point3d operator-() const { return point3d(-x, -y, -z);\
    \ }\n   point3d operator+(const point3d &p) const { return point3d(x + p.x, y\
    \ + p.y, z + p.z); }\n   point3d operator-(const point3d &p) const { return point3d(x\
    \ - p.x, y - p.y, z - p.z); }\n   point3d operator*(double k) const { return point3d(x\
    \ * k, y * k, z * k); }\n   point3d operator/(double k) const { return point3d(x\
    \ / k, y / k, z / k); }\n   point3d &operator+=(const point3d &p) {\n      x +=\
    \ p.x;\n      y += p.y;\n      z += p.z;\n      return *this;\n   }\n   point3d\
    \ &operator-=(const point3d &p) {\n      x -= p.x;\n      y -= p.y;\n      z -=\
    \ p.z;\n      return *this;\n   }\n   point3d &operator*=(double k) {\n      x\
    \ *= k;\n      y *= k;\n      z *= k;\n      return *this;\n   }\n   point3d &operator/=(double\
    \ k) {\n      x /= k;\n      y /= k;\n      z /= k;\n      return *this;\n   }\n\
    \   bool operator==(const point3d &p) const {\n      return abs(x - p.x) < eps\
    \ && abs(y - p.y) < eps && abs(z - p.z) < eps;\n   }\n   bool operator!=(const\
    \ point3d &p) const { return !(*this == p); }\n   bool operator<(const point3d\
    \ &p) const {\n      if(abs(x - p.x) >= eps) return x < p.x;\n      if(abs(y -\
    \ p.y) >= eps) return y < p.y;\n      return z < p.z - eps;\n   }\n};\n\npoint3d\
    \ operator*(double k, const point3d &p) { return p * k; }\n\nistream &operator>>(istream\
    \ &is, point3d &p) { return is >> p.x >> p.y >> p.z; }\nostream &operator<<(ostream\
    \ &os, const point3d &p) { return os << p.x << ' ' << p.y << ' ' << p.z; }\n\n\
    using vec3d = point3d;\n\n// 2\u70B9 A, B \u3092\u901A\u308B\u76F4\u7DDA\u3002\
    \u7DDA\u5206\u3068\u3057\u3066\u4F7F\u3046\u95A2\u6570\u3067\u306F\u7AEF\u70B9\
    \ A, B \u3092\u7AEF\u3068\u307F\u306A\u3059\nstruct line3d {\n   point3d A, B;\n\
    \n   line3d() = default;\n   line3d(point3d A, point3d B) : A(A), B(B) {}\n};\n\
    \n// \u70B9 P \u3092\u901A\u308A\u3001\u6CD5\u7DDA\u30D9\u30AF\u30C8\u30EB N \u3092\
    \u6301\u3064\u5E73\u9762\nstruct plane3d {\n   point3d P, N;\n\n   plane3d() =\
    \ default;\n   plane3d(point3d P, point3d N) : P(P), N(N) {}\n   // 3\u70B9 A,\
    \ B, C \u3092\u901A\u308B\u5E73\u9762\u30023\u70B9\u304C\u4E00\u76F4\u7DDA\u4E0A\
    \u306E\u5834\u5408\u306F\u6CD5\u7DDA\u304C\u30BC\u30ED\u306B\u306A\u308B\n   plane3d(point3d\
    \ A, point3d B, point3d C) : P(A), N((B - A).y * (C - A).z - (B - A).z * (C -\
    \ A).y,\n                                                   (B - A).z * (C - A).x\
    \ - (B - A).x * (C - A).z,\n                                                 \
    \  (B - A).x * (C - A).y - (B - A).y * (C - A).x) {}\n};\n\n// \u4E2D\u5FC3 C\u3001\
    \u534A\u5F84 r \u306E\u7403\nstruct sphere3d {\n   point3d C;\n   double r;\n\n\
    \   sphere3d() : C(), r(0) {}\n   sphere3d(point3d C, double r) : C(C), r(r) {}\n\
    };\n\n// 3\u6B21\u5143\u7A7A\u9593\u4E0A\u306E\u5186\u3002\u4E2D\u5FC3 C\u3001\
    \u5186\u3092\u542B\u3080\u5E73\u9762\u306E\u6CD5\u7DDA N\u3001\u534A\u5F84 r\n\
    struct circle3d {\n   point3d C, N;\n   double r;\n\n   circle3d() : C(), N(),\
    \ r(0) {}\n   circle3d(point3d C, point3d N, double r) : C(C), N(N), r(r) {}\n\
    };\n\n// \u76F4\u7DDA\u30FB\u7DDA\u5206 L \u306E\u65B9\u5411\u30D9\u30AF\u30C8\
    \u30EB B - A\npoint3d vec(line3d L) { return L.B - L.A; }\n\n// \u5185\u7A4D\n\
    double dot(point3d P, point3d Q) { return P.x * Q.x + P.y * Q.y + P.z * Q.z; }\n\
    \n// \u5916\u7A4D\npoint3d cross(point3d P, point3d Q) {\n   return point3d(P.y\
    \ * Q.z - P.z * Q.y,\n                  P.z * Q.x - P.x * Q.z,\n             \
    \     P.x * Q.y - P.y * Q.x);\n}\n\n// \u30B9\u30AB\u30E9\u30FC\u4E09\u91CD\u7A4D\
    \u3002\u7B26\u53F7\u4ED8\u304D\u5E73\u884C\u516D\u9762\u4F53\u4F53\u7A4D\ndouble\
    \ triple(point3d A, point3d B, point3d C) { return dot(A, cross(B, C)); }\n\n\
    // \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\u306E 2 \u4E57\ndouble norm(point3d\
    \ P) { return dot(P, P); }\n\n// \u30D9\u30AF\u30C8\u30EB\u306E\u9577\u3055\n\
    double abs(point3d P) { return sqrt(norm(P)); }\n\n// 2\u70B9\u9593\u8DDD\u96E2\
    \ndouble dist(point3d P, point3d Q) { return abs(P - Q); }\n\n// \u5358\u4F4D\u30D9\
    \u30AF\u30C8\u30EB\u3002\u30BC\u30ED\u30D9\u30AF\u30C8\u30EB\u306E\u5834\u5408\
    \u306F assert \u3067\u843D\u3068\u3059\npoint3d unit(point3d P) {\n   double len\
    \ = abs(P);\n   assert(len > eps);\n   return P / len;\n}\n\n// 2\u30D9\u30AF\u30C8\
    \u30EB\u306E\u306A\u3059\u89D2 [0, pi]\ndouble angle(point3d P, point3d Q) {\n\
    \   assert(abs(P) > eps && abs(Q) > eps);\n   return acos(clamp_unit(dot(P, Q)\
    \ / abs(P) / abs(Q)));\n}\n\n// \u539F\u70B9\u3092\u901A\u308B axis \u3092\u8EF8\
    \u3068\u3057\u3066 P \u3092 theta \u30E9\u30B8\u30A2\u30F3\u56DE\u8EE2\npoint3d\
    \ rotate_around_axis(point3d P, point3d axis, double theta) {\n   point3d U =\
    \ unit(axis);\n   double c = cos(theta), s = sin(theta);\n   return P * c + cross(U,\
    \ P) * s + U * dot(U, P) * (1 - c);\n}\n\n// \u76F4\u7DDA axis \u3092\u8EF8\u3068\
    \u3057\u3066 P \u3092 theta \u30E9\u30B8\u30A2\u30F3\u56DE\u8EE2\npoint3d rotate(point3d\
    \ P, line3d axis, double theta) {\n   return axis.A + rotate_around_axis(P - axis.A,\
    \ vec(axis), theta);\n}\n\n// 3\u70B9 A, B, C \u3092\u9802\u70B9\u3068\u3059\u308B\
    \u4E09\u89D2\u5F62\u306E\u9762\u7A4D\ndouble triangle_area(point3d A, point3d\
    \ B, point3d C) { return abs(cross(B - A, C - A)) / 2; }\n\n// 4\u70B9 A, B, C,\
    \ D \u3092\u9802\u70B9\u3068\u3059\u308B\u56DB\u9762\u4F53\u306E\u4F53\u7A4D\n\
    double tetrahedron_volume(point3d A, point3d B, point3d C, point3d D) {\n   return\
    \ abs(triple(B - A, C - A, D - A)) / 6;\n}\n\n// \u70B9 P \u304C\u76F4\u7DDA L\
    \ \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_line(point3d P, line3d L) {\n\
    \   assert(abs(vec(L)) > eps);\n   return abs(cross(P - L.A, vec(L))) <= eps *\
    \ abs(vec(L));\n}\n\n// \u70B9 P \u304C\u7DDA\u5206 S \u4E0A\u306B\u3042\u308B\
    \u304B\nbool point_on_segment(point3d P, line3d S) {\n   return point_on_line(P,\
    \ S) && dot(P - S.A, P - S.B) <= eps;\n}\n\n// \u70B9 P \u304B\u3089\u76F4\u7DDA\
    \ L \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\u306E\u8DB3\npoint3d projection(point3d\
    \ P, line3d L) {\n   point3d V = vec(L);\n   assert(abs(V) > eps);\n   return\
    \ L.A + V * dot(P - L.A, V) / norm(V);\n}\n\n// \u70B9 P \u3092\u76F4\u7DDA L\
    \ \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\npoint3d\
    \ reflection(point3d P, line3d L) { return projection(P, L) * 2 - P; }\n\n// \u7DDA\
    \u5206 S \u4E0A\u3067\u70B9 P \u306B\u6700\u3082\u8FD1\u3044\u70B9\npoint3d closest_point_on_segment(point3d\
    \ P, line3d S) {\n   point3d V = vec(S);\n   if(norm(V) < eps) return S.A;\n \
    \  double t = clamp01(dot(P - S.A, V) / norm(V));\n   return S.A + V * t;\n}\n\
    \n// \u70B9 P \u3068\u76F4\u7DDA L \u306E\u8DDD\u96E2\ndouble point_line_distance(point3d\
    \ P, line3d L) {\n   assert(abs(vec(L)) > eps);\n   return abs(cross(P - L.A,\
    \ vec(L))) / abs(vec(L));\n}\n\n// \u70B9 P \u3068\u7DDA\u5206 S \u306E\u8DDD\u96E2\
    \ndouble point_segment_distance(point3d P, line3d S) { return dist(P, closest_point_on_segment(P,\
    \ S)); }\n\n// 2\u76F4\u7DDA\u304C\u5E73\u884C\u304B\nbool is_parallel(line3d\
    \ L1, line3d L2) {\n   assert(abs(vec(L1)) > eps && abs(vec(L2)) > eps);\n   return\
    \ abs(cross(vec(L1), vec(L2))) < eps;\n}\n\n// 2\u76F4\u7DDA\u304C\u76F4\u4EA4\
    \u3059\u308B\u304B\nbool is_orthogonal(line3d L1, line3d L2) {\n   assert(abs(vec(L1))\
    \ > eps && abs(vec(L2)) > eps);\n   return abs(dot(vec(L1), vec(L2))) < eps;\n\
    }\n\n// 2\u76F4\u7DDA\u304C\u540C\u4E00\u76F4\u7DDA\u304B\nbool same_line(line3d\
    \ L1, line3d L2) { return is_parallel(L1, L2) && point_on_line(L2.A, L1); }\n\n\
    // 2\u76F4\u7DDA\u9593\u306E\u8DDD\u96E2\u3002\u306D\u3058\u308C\u306E\u4F4D\u7F6E\
    \u306B\u3082\u5BFE\u5FDC\ndouble line_line_distance(line3d L1, line3d L2) {\n\
    \   point3d U = vec(L1), V = vec(L2);\n   assert(abs(U) > eps && abs(V) > eps);\n\
    \   point3d W = cross(U, V);\n   if(abs(W) < eps) return point_line_distance(L2.A,\
    \ L1);\n   return abs(triple(L2.A - L1.A, U, V)) / abs(W);\n}\n\n// 2\u76F4\u7DDA\
    \u4E0A\u306E\u6700\u8FD1\u70B9\u306E\u7D44\u3002\u5E73\u884C\u306A\u5834\u5408\
    \u306F assert \u3067\u843D\u3068\u3059\npair<point3d, point3d> closest_points_between_lines(line3d\
    \ L1, line3d L2) {\n   point3d U = vec(L1), V = vec(L2), W = L1.A - L2.A;\n  \
    \ double a = dot(U, U), b = dot(U, V), c = dot(V, V);\n   double d = dot(U, W),\
    \ e = dot(V, W);\n   double den = a * c - b * b;\n   assert(abs(U) > eps && abs(V)\
    \ > eps && abs(den) > eps);\n   double s = (b * e - c * d) / den;\n   double t\
    \ = (a * e - b * d) / den;\n   return {L1.A + U * s, L2.A + V * t};\n}\n\n// 2\u76F4\
    \u7DDA\u304C\u4EA4\u5DEE\u3059\u308B\u304B\nbool line_intersect(line3d L1, line3d\
    \ L2) { return line_line_distance(L1, L2) <= eps; }\n\n// 2\u76F4\u7DDA\u306E\u4EA4\
    \u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u3084\u306D\u3058\u308C\u306E\u4F4D\
    \u7F6E\u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npoint3d line_intersection(line3d\
    \ L1, line3d L2) {\n   assert(line_intersect(L1, L2) && !is_parallel(L1, L2));\n\
    \   auto [P, Q] = closest_points_between_lines(L1, L2);\n   return (P + Q) / 2;\n\
    }\n\n// 2\u7DDA\u5206\u4E0A\u306E\u6700\u8FD1\u70B9\u306E\u7D44\u3002\u7DDA\u5206\
    \u304C\u9000\u5316\u3057\u3066\u70B9\u306B\u306A\u3063\u3066\u3044\u308B\u5834\
    \u5408\u306B\u3082\u5BFE\u5FDC\npair<point3d, point3d> closest_points_between_segments(line3d\
    \ S1, line3d S2) {\n   point3d U = vec(S1), V = vec(S2), W = S1.A - S2.A;\n  \
    \ double a = dot(U, U), b = dot(U, V), c = dot(V, V);\n   double d = dot(U, W),\
    \ e = dot(V, W), D = a * c - b * b;\n\n   if(a < eps && c < eps) return {S1.A,\
    \ S2.A};\n   if(a < eps) return {S1.A, closest_point_on_segment(S1.A, S2)};\n\
    \   if(c < eps) return {closest_point_on_segment(S2.A, S1), S2.A};\n\n   double\
    \ sN, sD = D, tN, tD = D;\n   if(D < eps) {\n      sN = 0.0;\n      sD = 1.0;\n\
    \      tN = e;\n      tD = c;\n   } else {\n      sN = b * e - c * d;\n      tN\
    \ = a * e - b * d;\n      if(sN < 0.0) {\n         sN = 0.0;\n         tN = e;\n\
    \         tD = c;\n      } else if(sN > sD) {\n         sN = sD;\n         tN\
    \ = e + b;\n         tD = c;\n      }\n   }\n\n   if(tN < 0.0) {\n      tN = 0.0;\n\
    \      if(-d < 0.0) {\n         sN = 0.0;\n      } else if(-d > a) {\n       \
    \  sN = sD;\n      } else {\n         sN = -d;\n         sD = a;\n      }\n  \
    \ } else if(tN > tD) {\n      tN = tD;\n      if(-d + b < 0.0) {\n         sN\
    \ = 0.0;\n      } else if(-d + b > a) {\n         sN = sD;\n      } else {\n \
    \        sN = -d + b;\n         sD = a;\n      }\n   }\n\n   double s = abs(sN)\
    \ < eps ? 0.0 : sN / sD;\n   double t = abs(tN) < eps ? 0.0 : tN / tD;\n   return\
    \ {S1.A + U * s, S2.A + V * t};\n}\n\n// 2\u7DDA\u5206\u9593\u306E\u8DDD\u96E2\
    \u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble segment_distance(line3d\
    \ S1, line3d S2) {\n   auto [P, Q] = closest_points_between_segments(S1, S2);\n\
    \   return dist(P, Q);\n}\n\n// 2\u7DDA\u5206\u304C\u4EA4\u5DEE\u3059\u308B\u304B\
    \u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\u5834\u5408\u3082 true\nbool segment_intersect(line3d\
    \ S1, line3d S2) { return segment_distance(S1, S2) <= eps; }\n\n// \u70B9 P \u304C\
    \u5E73\u9762 H \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_plane(point3d P,\
    \ plane3d H) {\n   assert(abs(H.N) > eps);\n   return abs(dot(P - H.P, H.N)) <=\
    \ eps * abs(H.N);\n}\n\n// \u70B9 P \u304B\u3089\u5E73\u9762 H \u3078\u4E0B\u308D\
    \u3057\u305F\u5782\u7DDA\u306E\u8DB3\npoint3d projection(point3d P, plane3d H)\
    \ {\n   assert(abs(H.N) > eps);\n   return P - H.N * dot(P - H.P, H.N) / norm(H.N);\n\
    }\n\n// \u70B9 P \u3092\u5E73\u9762 H \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\
    \u52D5\u3057\u305F\u70B9\npoint3d reflection(point3d P, plane3d H) { return projection(P,\
    \ H) * 2 - P; }\n\n// \u70B9 P \u3068\u5E73\u9762 H \u306E\u7B26\u53F7\u4ED8\u304D\
    \u8DDD\u96E2\u3002\u6CD5\u7DDA\u65B9\u5411\u304C\u6B63\ndouble signed_point_plane_distance(point3d\
    \ P, plane3d H) {\n   assert(abs(H.N) > eps);\n   return dot(P - H.P, H.N) / abs(H.N);\n\
    }\n\n// \u70B9 P \u3068\u5E73\u9762 H \u306E\u8DDD\u96E2\ndouble point_plane_distance(point3d\
    \ P, plane3d H) { return abs(signed_point_plane_distance(P, H)); }\n\n// \u76F4\
    \u7DDA L \u3068\u5E73\u9762 H \u304C\u5E73\u884C\u304B\nbool is_parallel(line3d\
    \ L, plane3d H) {\n   assert(abs(vec(L)) > eps && abs(H.N) > eps);\n   return\
    \ abs(dot(vec(L), H.N)) < eps;\n}\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u304C\
    \u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line3d L, plane3d H) {\n  \
    \ assert(abs(vec(L)) > eps && abs(H.N) > eps);\n   return abs(cross(vec(L), H.N))\
    \ < eps;\n}\n\n// \u76F4\u7DDA L \u304C\u5E73\u9762 H \u4E0A\u306B\u3042\u308B\
    \u304B\nbool line_on_plane(line3d L, plane3d H) { return point_on_plane(L.A, H)\
    \ && point_on_plane(L.B, H); }\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u306E\
    \u4EA4\u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\u843D\u3068\
    \u3059\npoint3d line_plane_intersection(line3d L, plane3d H) {\n   assert(!is_parallel(L,\
    \ H));\n   point3d V = vec(L);\n   double t = dot(H.P - L.A, H.N) / dot(V, H.N);\n\
    \   return L.A + V * t;\n}\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u306E\u8DDD\
    \u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble line_plane_distance(line3d\
    \ L, plane3d H) {\n   if(!is_parallel(L, H)) return 0;\n   return point_plane_distance(L.A,\
    \ H);\n}\n\n// 2\u5E73\u9762\u304C\u5E73\u884C\u304B\nbool is_parallel(plane3d\
    \ H1, plane3d H2) {\n   assert(abs(H1.N) > eps && abs(H2.N) > eps);\n   return\
    \ abs(cross(H1.N, H2.N)) < eps;\n}\n\n// 2\u5E73\u9762\u304C\u76F4\u4EA4\u3059\
    \u308B\u304B\nbool is_orthogonal(plane3d H1, plane3d H2) {\n   assert(abs(H1.N)\
    \ > eps && abs(H2.N) > eps);\n   return abs(dot(H1.N, H2.N)) < eps;\n}\n\n// 2\u5E73\
    \u9762\u304C\u540C\u4E00\u5E73\u9762\u304B\nbool same_plane(plane3d H1, plane3d\
    \ H2) { return is_parallel(H1, H2) && point_on_plane(H2.P, H1); }\n\n// 2\u5E73\
    \u9762\u306E\u4EA4\u7DDA\u3002\u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\
    \u843D\u3068\u3059\nline3d plane_intersection(plane3d H1, plane3d H2) {\n   assert(!is_parallel(H1,\
    \ H2));\n   point3d D = cross(H1.N, H2.N);\n   double d1 = dot(H1.N, H1.P);\n\
    \   double d2 = dot(H2.N, H2.P);\n   point3d P = cross(H2.N * d1 - H1.N * d2,\
    \ D) / norm(D);\n   return line3d(P, P + D);\n}\n\n// 2\u5E73\u9762\u9593\u306E\
    \u8DDD\u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble plane_plane_distance(plane3d\
    \ H1, plane3d H2) {\n   if(!is_parallel(H1, H2)) return 0;\n   return point_plane_distance(H2.P,\
    \ H1);\n}\n\n// \u70B9 P \u304C\u7403 S \u306E\u5185\u90E8\u307E\u305F\u306F\u8868\
    \u9762\u306B\u3042\u308B\u304B\nbool point_in_sphere(point3d P, sphere3d S) {\
    \ return dist(P, S.C) <= S.r + eps; }\n\n// \u70B9 P \u304C\u7403 S \u306E\u8868\
    \u9762\u306B\u3042\u308B\u304B\nbool point_on_sphere(point3d P, sphere3d S) {\
    \ return abs(dist(P, S.C) - S.r) <= eps; }\n\n// \u76F4\u7DDA L \u3068\u7403 S\
    \ \u306E\u4EA4\u70B9\u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\
    \u3001\u901A\u5E38\u306F2\u500B\u8FD4\u3059\nvector<point3d> line_sphere_intersection(line3d\
    \ L, sphere3d S) {\n   point3d P = projection(S.C, L);\n   double d = point_line_distance(S.C,\
    \ L);\n   if(d > S.r + eps) return {};\n   point3d U = unit(vec(L));\n   double\
    \ h = sqrt(max(0.0, S.r * S.r - d * d));\n   if(h < eps) return {P};\n   return\
    \ {P - U * h, P + U * h};\n}\n\n// \u7DDA\u5206 Seg \u3068\u7403 S \u306E\u4EA4\
    \u70B9\u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\u3001\u901A\
    \u5E38\u306F2\u500B\u8FD4\u3059\nvector<point3d> segment_sphere_intersection(line3d\
    \ Seg, sphere3d S) {\n   vector<point3d> res;\n   for(point3d P : line_sphere_intersection(Seg,\
    \ S)) {\n      if(point_on_segment(P, Seg)) res.push_back(P);\n   }\n   return\
    \ res;\n}\n\n// \u5E73\u9762 H \u3068\u7403 S \u306E\u4EA4\u5186\u3002\u4EA4\u308F\
    \u3089\u306A\u3044\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ncircle3d\
    \ plane_sphere_intersection(plane3d H, sphere3d S) {\n   point3d C = projection(S.C,\
    \ H);\n   double d = point_plane_distance(S.C, H);\n   assert(d <= S.r + eps);\n\
    \   double r = sqrt(max(0.0, S.r * S.r - d * d));\n   return circle3d(C, H.N,\
    \ r);\n}\n\n// 2\u7403 S1, S2 \u306E\u4EA4\u5186\u3002\u4EA4\u308F\u3089\u306A\
    \u3044\u5834\u5408\u3084\u540C\u5FC3\u7403\u306E\u5834\u5408\u306F assert \u3067\
    \u843D\u3068\u3059\ncircle3d sphere_sphere_intersection(sphere3d S1, sphere3d\
    \ S2) {\n   double d = dist(S1.C, S2.C);\n   assert(d > eps);\n   assert(abs(S1.r\
    \ - S2.r) <= d + eps && d <= S1.r + S2.r + eps);\n   point3d U = (S2.C - S1.C)\
    \ / d;\n   double x = (S1.r * S1.r - S2.r * S2.r + d * d) / (2 * d);\n   point3d\
    \ C = S1.C + U * x;\n   double r = sqrt(max(0.0, S1.r * S1.r - x * x));\n   return\
    \ circle3d(C, U, r);\n}\n"
  code: "#include <bits/stdc++.h>\nusing namespace std;\n\nconst double eps = 1e-10;\n\
    const double INF = 1e18;\n\n// \u8AA4\u5DEE\u4ED8\u304D\u3067\u7B26\u53F7\u3092\
    \u8FD4\u3059\u3002\u6B63: 1, \u8CA0: -1, \u307B\u307C 0: 0\nint sgn(double x)\
    \ {\n   if(x > eps) return 1;\n   if(x < -eps) return -1;\n   return 0;\n}\n\n\
    // [0, 1] \u306B\u4E38\u3081\u308B\ndouble clamp01(double x) { return max(0.0,\
    \ min(1.0, x)); }\n// acos \u306A\u3069\u306B\u6E21\u3059\u5024\u3092 [-1, 1]\
    \ \u306B\u4E38\u3081\u308B\ndouble clamp_unit(double x) { return max(-1.0, min(1.0,\
    \ x)); }\n\n// 3\u6B21\u5143\u70B9\u30FB\u30D9\u30AF\u30C8\u30EB\u3002\u52A0\u6E1B\
    \u7B97\u3084\u30B9\u30AB\u30E9\u30FC\u500D\u3092\u30D9\u30AF\u30C8\u30EB\u3068\
    \u3057\u3066\u6271\u3048\u308B\nstruct point3d {\n   double x, y, z;\n\n   point3d()\
    \ : x(0), y(0), z(0) {}\n   point3d(double x, double y, double z) : x(x), y(y),\
    \ z(z) {}\n\n   point3d operator+() const { return *this; }\n   point3d operator-()\
    \ const { return point3d(-x, -y, -z); }\n   point3d operator+(const point3d &p)\
    \ const { return point3d(x + p.x, y + p.y, z + p.z); }\n   point3d operator-(const\
    \ point3d &p) const { return point3d(x - p.x, y - p.y, z - p.z); }\n   point3d\
    \ operator*(double k) const { return point3d(x * k, y * k, z * k); }\n   point3d\
    \ operator/(double k) const { return point3d(x / k, y / k, z / k); }\n   point3d\
    \ &operator+=(const point3d &p) {\n      x += p.x;\n      y += p.y;\n      z +=\
    \ p.z;\n      return *this;\n   }\n   point3d &operator-=(const point3d &p) {\n\
    \      x -= p.x;\n      y -= p.y;\n      z -= p.z;\n      return *this;\n   }\n\
    \   point3d &operator*=(double k) {\n      x *= k;\n      y *= k;\n      z *=\
    \ k;\n      return *this;\n   }\n   point3d &operator/=(double k) {\n      x /=\
    \ k;\n      y /= k;\n      z /= k;\n      return *this;\n   }\n   bool operator==(const\
    \ point3d &p) const {\n      return abs(x - p.x) < eps && abs(y - p.y) < eps &&\
    \ abs(z - p.z) < eps;\n   }\n   bool operator!=(const point3d &p) const { return\
    \ !(*this == p); }\n   bool operator<(const point3d &p) const {\n      if(abs(x\
    \ - p.x) >= eps) return x < p.x;\n      if(abs(y - p.y) >= eps) return y < p.y;\n\
    \      return z < p.z - eps;\n   }\n};\n\npoint3d operator*(double k, const point3d\
    \ &p) { return p * k; }\n\nistream &operator>>(istream &is, point3d &p) { return\
    \ is >> p.x >> p.y >> p.z; }\nostream &operator<<(ostream &os, const point3d &p)\
    \ { return os << p.x << ' ' << p.y << ' ' << p.z; }\n\nusing vec3d = point3d;\n\
    \n// 2\u70B9 A, B \u3092\u901A\u308B\u76F4\u7DDA\u3002\u7DDA\u5206\u3068\u3057\
    \u3066\u4F7F\u3046\u95A2\u6570\u3067\u306F\u7AEF\u70B9 A, B \u3092\u7AEF\u3068\
    \u307F\u306A\u3059\nstruct line3d {\n   point3d A, B;\n\n   line3d() = default;\n\
    \   line3d(point3d A, point3d B) : A(A), B(B) {}\n};\n\n// \u70B9 P \u3092\u901A\
    \u308A\u3001\u6CD5\u7DDA\u30D9\u30AF\u30C8\u30EB N \u3092\u6301\u3064\u5E73\u9762\
    \nstruct plane3d {\n   point3d P, N;\n\n   plane3d() = default;\n   plane3d(point3d\
    \ P, point3d N) : P(P), N(N) {}\n   // 3\u70B9 A, B, C \u3092\u901A\u308B\u5E73\
    \u9762\u30023\u70B9\u304C\u4E00\u76F4\u7DDA\u4E0A\u306E\u5834\u5408\u306F\u6CD5\
    \u7DDA\u304C\u30BC\u30ED\u306B\u306A\u308B\n   plane3d(point3d A, point3d B, point3d\
    \ C) : P(A), N((B - A).y * (C - A).z - (B - A).z * (C - A).y,\n              \
    \                                     (B - A).z * (C - A).x - (B - A).x * (C -\
    \ A).z,\n                                                   (B - A).x * (C - A).y\
    \ - (B - A).y * (C - A).x) {}\n};\n\n// \u4E2D\u5FC3 C\u3001\u534A\u5F84 r \u306E\
    \u7403\nstruct sphere3d {\n   point3d C;\n   double r;\n\n   sphere3d() : C(),\
    \ r(0) {}\n   sphere3d(point3d C, double r) : C(C), r(r) {}\n};\n\n// 3\u6B21\u5143\
    \u7A7A\u9593\u4E0A\u306E\u5186\u3002\u4E2D\u5FC3 C\u3001\u5186\u3092\u542B\u3080\
    \u5E73\u9762\u306E\u6CD5\u7DDA N\u3001\u534A\u5F84 r\nstruct circle3d {\n   point3d\
    \ C, N;\n   double r;\n\n   circle3d() : C(), N(), r(0) {}\n   circle3d(point3d\
    \ C, point3d N, double r) : C(C), N(N), r(r) {}\n};\n\n// \u76F4\u7DDA\u30FB\u7DDA\
    \u5206 L \u306E\u65B9\u5411\u30D9\u30AF\u30C8\u30EB B - A\npoint3d vec(line3d\
    \ L) { return L.B - L.A; }\n\n// \u5185\u7A4D\ndouble dot(point3d P, point3d Q)\
    \ { return P.x * Q.x + P.y * Q.y + P.z * Q.z; }\n\n// \u5916\u7A4D\npoint3d cross(point3d\
    \ P, point3d Q) {\n   return point3d(P.y * Q.z - P.z * Q.y,\n                \
    \  P.z * Q.x - P.x * Q.z,\n                  P.x * Q.y - P.y * Q.x);\n}\n\n//\
    \ \u30B9\u30AB\u30E9\u30FC\u4E09\u91CD\u7A4D\u3002\u7B26\u53F7\u4ED8\u304D\u5E73\
    \u884C\u516D\u9762\u4F53\u4F53\u7A4D\ndouble triple(point3d A, point3d B, point3d\
    \ C) { return dot(A, cross(B, C)); }\n\n// \u30D9\u30AF\u30C8\u30EB\u306E\u9577\
    \u3055\u306E 2 \u4E57\ndouble norm(point3d P) { return dot(P, P); }\n\n// \u30D9\
    \u30AF\u30C8\u30EB\u306E\u9577\u3055\ndouble abs(point3d P) { return sqrt(norm(P));\
    \ }\n\n// 2\u70B9\u9593\u8DDD\u96E2\ndouble dist(point3d P, point3d Q) { return\
    \ abs(P - Q); }\n\n// \u5358\u4F4D\u30D9\u30AF\u30C8\u30EB\u3002\u30BC\u30ED\u30D9\
    \u30AF\u30C8\u30EB\u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npoint3d\
    \ unit(point3d P) {\n   double len = abs(P);\n   assert(len > eps);\n   return\
    \ P / len;\n}\n\n// 2\u30D9\u30AF\u30C8\u30EB\u306E\u306A\u3059\u89D2 [0, pi]\n\
    double angle(point3d P, point3d Q) {\n   assert(abs(P) > eps && abs(Q) > eps);\n\
    \   return acos(clamp_unit(dot(P, Q) / abs(P) / abs(Q)));\n}\n\n// \u539F\u70B9\
    \u3092\u901A\u308B axis \u3092\u8EF8\u3068\u3057\u3066 P \u3092 theta \u30E9\u30B8\
    \u30A2\u30F3\u56DE\u8EE2\npoint3d rotate_around_axis(point3d P, point3d axis,\
    \ double theta) {\n   point3d U = unit(axis);\n   double c = cos(theta), s = sin(theta);\n\
    \   return P * c + cross(U, P) * s + U * dot(U, P) * (1 - c);\n}\n\n// \u76F4\u7DDA\
    \ axis \u3092\u8EF8\u3068\u3057\u3066 P \u3092 theta \u30E9\u30B8\u30A2\u30F3\u56DE\
    \u8EE2\npoint3d rotate(point3d P, line3d axis, double theta) {\n   return axis.A\
    \ + rotate_around_axis(P - axis.A, vec(axis), theta);\n}\n\n// 3\u70B9 A, B, C\
    \ \u3092\u9802\u70B9\u3068\u3059\u308B\u4E09\u89D2\u5F62\u306E\u9762\u7A4D\ndouble\
    \ triangle_area(point3d A, point3d B, point3d C) { return abs(cross(B - A, C -\
    \ A)) / 2; }\n\n// 4\u70B9 A, B, C, D \u3092\u9802\u70B9\u3068\u3059\u308B\u56DB\
    \u9762\u4F53\u306E\u4F53\u7A4D\ndouble tetrahedron_volume(point3d A, point3d B,\
    \ point3d C, point3d D) {\n   return abs(triple(B - A, C - A, D - A)) / 6;\n}\n\
    \n// \u70B9 P \u304C\u76F4\u7DDA L \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_line(point3d\
    \ P, line3d L) {\n   assert(abs(vec(L)) > eps);\n   return abs(cross(P - L.A,\
    \ vec(L))) <= eps * abs(vec(L));\n}\n\n// \u70B9 P \u304C\u7DDA\u5206 S \u4E0A\
    \u306B\u3042\u308B\u304B\nbool point_on_segment(point3d P, line3d S) {\n   return\
    \ point_on_line(P, S) && dot(P - S.A, P - S.B) <= eps;\n}\n\n// \u70B9 P \u304B\
    \u3089\u76F4\u7DDA L \u3078\u4E0B\u308D\u3057\u305F\u5782\u7DDA\u306E\u8DB3\n\
    point3d projection(point3d P, line3d L) {\n   point3d V = vec(L);\n   assert(abs(V)\
    \ > eps);\n   return L.A + V * dot(P - L.A, V) / norm(V);\n}\n\n// \u70B9 P \u3092\
    \u76F4\u7DDA L \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\u52D5\u3057\u305F\u70B9\
    \npoint3d reflection(point3d P, line3d L) { return projection(P, L) * 2 - P; }\n\
    \n// \u7DDA\u5206 S \u4E0A\u3067\u70B9 P \u306B\u6700\u3082\u8FD1\u3044\u70B9\n\
    point3d closest_point_on_segment(point3d P, line3d S) {\n   point3d V = vec(S);\n\
    \   if(norm(V) < eps) return S.A;\n   double t = clamp01(dot(P - S.A, V) / norm(V));\n\
    \   return S.A + V * t;\n}\n\n// \u70B9 P \u3068\u76F4\u7DDA L \u306E\u8DDD\u96E2\
    \ndouble point_line_distance(point3d P, line3d L) {\n   assert(abs(vec(L)) > eps);\n\
    \   return abs(cross(P - L.A, vec(L))) / abs(vec(L));\n}\n\n// \u70B9 P \u3068\
    \u7DDA\u5206 S \u306E\u8DDD\u96E2\ndouble point_segment_distance(point3d P, line3d\
    \ S) { return dist(P, closest_point_on_segment(P, S)); }\n\n// 2\u76F4\u7DDA\u304C\
    \u5E73\u884C\u304B\nbool is_parallel(line3d L1, line3d L2) {\n   assert(abs(vec(L1))\
    \ > eps && abs(vec(L2)) > eps);\n   return abs(cross(vec(L1), vec(L2))) < eps;\n\
    }\n\n// 2\u76F4\u7DDA\u304C\u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line3d\
    \ L1, line3d L2) {\n   assert(abs(vec(L1)) > eps && abs(vec(L2)) > eps);\n   return\
    \ abs(dot(vec(L1), vec(L2))) < eps;\n}\n\n// 2\u76F4\u7DDA\u304C\u540C\u4E00\u76F4\
    \u7DDA\u304B\nbool same_line(line3d L1, line3d L2) { return is_parallel(L1, L2)\
    \ && point_on_line(L2.A, L1); }\n\n// 2\u76F4\u7DDA\u9593\u306E\u8DDD\u96E2\u3002\
    \u306D\u3058\u308C\u306E\u4F4D\u7F6E\u306B\u3082\u5BFE\u5FDC\ndouble line_line_distance(line3d\
    \ L1, line3d L2) {\n   point3d U = vec(L1), V = vec(L2);\n   assert(abs(U) > eps\
    \ && abs(V) > eps);\n   point3d W = cross(U, V);\n   if(abs(W) < eps) return point_line_distance(L2.A,\
    \ L1);\n   return abs(triple(L2.A - L1.A, U, V)) / abs(W);\n}\n\n// 2\u76F4\u7DDA\
    \u4E0A\u306E\u6700\u8FD1\u70B9\u306E\u7D44\u3002\u5E73\u884C\u306A\u5834\u5408\
    \u306F assert \u3067\u843D\u3068\u3059\npair<point3d, point3d> closest_points_between_lines(line3d\
    \ L1, line3d L2) {\n   point3d U = vec(L1), V = vec(L2), W = L1.A - L2.A;\n  \
    \ double a = dot(U, U), b = dot(U, V), c = dot(V, V);\n   double d = dot(U, W),\
    \ e = dot(V, W);\n   double den = a * c - b * b;\n   assert(abs(U) > eps && abs(V)\
    \ > eps && abs(den) > eps);\n   double s = (b * e - c * d) / den;\n   double t\
    \ = (a * e - b * d) / den;\n   return {L1.A + U * s, L2.A + V * t};\n}\n\n// 2\u76F4\
    \u7DDA\u304C\u4EA4\u5DEE\u3059\u308B\u304B\nbool line_intersect(line3d L1, line3d\
    \ L2) { return line_line_distance(L1, L2) <= eps; }\n\n// 2\u76F4\u7DDA\u306E\u4EA4\
    \u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u3084\u306D\u3058\u308C\u306E\u4F4D\
    \u7F6E\u306E\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\npoint3d line_intersection(line3d\
    \ L1, line3d L2) {\n   assert(line_intersect(L1, L2) && !is_parallel(L1, L2));\n\
    \   auto [P, Q] = closest_points_between_lines(L1, L2);\n   return (P + Q) / 2;\n\
    }\n\n// 2\u7DDA\u5206\u4E0A\u306E\u6700\u8FD1\u70B9\u306E\u7D44\u3002\u7DDA\u5206\
    \u304C\u9000\u5316\u3057\u3066\u70B9\u306B\u306A\u3063\u3066\u3044\u308B\u5834\
    \u5408\u306B\u3082\u5BFE\u5FDC\npair<point3d, point3d> closest_points_between_segments(line3d\
    \ S1, line3d S2) {\n   point3d U = vec(S1), V = vec(S2), W = S1.A - S2.A;\n  \
    \ double a = dot(U, U), b = dot(U, V), c = dot(V, V);\n   double d = dot(U, W),\
    \ e = dot(V, W), D = a * c - b * b;\n\n   if(a < eps && c < eps) return {S1.A,\
    \ S2.A};\n   if(a < eps) return {S1.A, closest_point_on_segment(S1.A, S2)};\n\
    \   if(c < eps) return {closest_point_on_segment(S2.A, S1), S2.A};\n\n   double\
    \ sN, sD = D, tN, tD = D;\n   if(D < eps) {\n      sN = 0.0;\n      sD = 1.0;\n\
    \      tN = e;\n      tD = c;\n   } else {\n      sN = b * e - c * d;\n      tN\
    \ = a * e - b * d;\n      if(sN < 0.0) {\n         sN = 0.0;\n         tN = e;\n\
    \         tD = c;\n      } else if(sN > sD) {\n         sN = sD;\n         tN\
    \ = e + b;\n         tD = c;\n      }\n   }\n\n   if(tN < 0.0) {\n      tN = 0.0;\n\
    \      if(-d < 0.0) {\n         sN = 0.0;\n      } else if(-d > a) {\n       \
    \  sN = sD;\n      } else {\n         sN = -d;\n         sD = a;\n      }\n  \
    \ } else if(tN > tD) {\n      tN = tD;\n      if(-d + b < 0.0) {\n         sN\
    \ = 0.0;\n      } else if(-d + b > a) {\n         sN = sD;\n      } else {\n \
    \        sN = -d + b;\n         sD = a;\n      }\n   }\n\n   double s = abs(sN)\
    \ < eps ? 0.0 : sN / sD;\n   double t = abs(tN) < eps ? 0.0 : tN / tD;\n   return\
    \ {S1.A + U * s, S2.A + V * t};\n}\n\n// 2\u7DDA\u5206\u9593\u306E\u8DDD\u96E2\
    \u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble segment_distance(line3d\
    \ S1, line3d S2) {\n   auto [P, Q] = closest_points_between_segments(S1, S2);\n\
    \   return dist(P, Q);\n}\n\n// 2\u7DDA\u5206\u304C\u4EA4\u5DEE\u3059\u308B\u304B\
    \u3002\u7AEF\u70B9\u3067\u63A5\u3059\u308B\u5834\u5408\u3082 true\nbool segment_intersect(line3d\
    \ S1, line3d S2) { return segment_distance(S1, S2) <= eps; }\n\n// \u70B9 P \u304C\
    \u5E73\u9762 H \u4E0A\u306B\u3042\u308B\u304B\nbool point_on_plane(point3d P,\
    \ plane3d H) {\n   assert(abs(H.N) > eps);\n   return abs(dot(P - H.P, H.N)) <=\
    \ eps * abs(H.N);\n}\n\n// \u70B9 P \u304B\u3089\u5E73\u9762 H \u3078\u4E0B\u308D\
    \u3057\u305F\u5782\u7DDA\u306E\u8DB3\npoint3d projection(point3d P, plane3d H)\
    \ {\n   assert(abs(H.N) > eps);\n   return P - H.N * dot(P - H.P, H.N) / norm(H.N);\n\
    }\n\n// \u70B9 P \u3092\u5E73\u9762 H \u306B\u95A2\u3057\u3066\u5BFE\u79F0\u79FB\
    \u52D5\u3057\u305F\u70B9\npoint3d reflection(point3d P, plane3d H) { return projection(P,\
    \ H) * 2 - P; }\n\n// \u70B9 P \u3068\u5E73\u9762 H \u306E\u7B26\u53F7\u4ED8\u304D\
    \u8DDD\u96E2\u3002\u6CD5\u7DDA\u65B9\u5411\u304C\u6B63\ndouble signed_point_plane_distance(point3d\
    \ P, plane3d H) {\n   assert(abs(H.N) > eps);\n   return dot(P - H.P, H.N) / abs(H.N);\n\
    }\n\n// \u70B9 P \u3068\u5E73\u9762 H \u306E\u8DDD\u96E2\ndouble point_plane_distance(point3d\
    \ P, plane3d H) { return abs(signed_point_plane_distance(P, H)); }\n\n// \u76F4\
    \u7DDA L \u3068\u5E73\u9762 H \u304C\u5E73\u884C\u304B\nbool is_parallel(line3d\
    \ L, plane3d H) {\n   assert(abs(vec(L)) > eps && abs(H.N) > eps);\n   return\
    \ abs(dot(vec(L), H.N)) < eps;\n}\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u304C\
    \u76F4\u4EA4\u3059\u308B\u304B\nbool is_orthogonal(line3d L, plane3d H) {\n  \
    \ assert(abs(vec(L)) > eps && abs(H.N) > eps);\n   return abs(cross(vec(L), H.N))\
    \ < eps;\n}\n\n// \u76F4\u7DDA L \u304C\u5E73\u9762 H \u4E0A\u306B\u3042\u308B\
    \u304B\nbool line_on_plane(line3d L, plane3d H) { return point_on_plane(L.A, H)\
    \ && point_on_plane(L.B, H); }\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u306E\
    \u4EA4\u70B9\u3002\u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\u843D\u3068\
    \u3059\npoint3d line_plane_intersection(line3d L, plane3d H) {\n   assert(!is_parallel(L,\
    \ H));\n   point3d V = vec(L);\n   double t = dot(H.P - L.A, H.N) / dot(V, H.N);\n\
    \   return L.A + V * t;\n}\n\n// \u76F4\u7DDA L \u3068\u5E73\u9762 H \u306E\u8DDD\
    \u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble line_plane_distance(line3d\
    \ L, plane3d H) {\n   if(!is_parallel(L, H)) return 0;\n   return point_plane_distance(L.A,\
    \ H);\n}\n\n// 2\u5E73\u9762\u304C\u5E73\u884C\u304B\nbool is_parallel(plane3d\
    \ H1, plane3d H2) {\n   assert(abs(H1.N) > eps && abs(H2.N) > eps);\n   return\
    \ abs(cross(H1.N, H2.N)) < eps;\n}\n\n// 2\u5E73\u9762\u304C\u76F4\u4EA4\u3059\
    \u308B\u304B\nbool is_orthogonal(plane3d H1, plane3d H2) {\n   assert(abs(H1.N)\
    \ > eps && abs(H2.N) > eps);\n   return abs(dot(H1.N, H2.N)) < eps;\n}\n\n// 2\u5E73\
    \u9762\u304C\u540C\u4E00\u5E73\u9762\u304B\nbool same_plane(plane3d H1, plane3d\
    \ H2) { return is_parallel(H1, H2) && point_on_plane(H2.P, H1); }\n\n// 2\u5E73\
    \u9762\u306E\u4EA4\u7DDA\u3002\u5E73\u884C\u306A\u5834\u5408\u306F assert \u3067\
    \u843D\u3068\u3059\nline3d plane_intersection(plane3d H1, plane3d H2) {\n   assert(!is_parallel(H1,\
    \ H2));\n   point3d D = cross(H1.N, H2.N);\n   double d1 = dot(H1.N, H1.P);\n\
    \   double d2 = dot(H2.N, H2.P);\n   point3d P = cross(H2.N * d1 - H1.N * d2,\
    \ D) / norm(D);\n   return line3d(P, P + D);\n}\n\n// 2\u5E73\u9762\u9593\u306E\
    \u8DDD\u96E2\u3002\u4EA4\u5DEE\u3059\u308B\u5834\u5408\u306F 0\ndouble plane_plane_distance(plane3d\
    \ H1, plane3d H2) {\n   if(!is_parallel(H1, H2)) return 0;\n   return point_plane_distance(H2.P,\
    \ H1);\n}\n\n// \u70B9 P \u304C\u7403 S \u306E\u5185\u90E8\u307E\u305F\u306F\u8868\
    \u9762\u306B\u3042\u308B\u304B\nbool point_in_sphere(point3d P, sphere3d S) {\
    \ return dist(P, S.C) <= S.r + eps; }\n\n// \u70B9 P \u304C\u7403 S \u306E\u8868\
    \u9762\u306B\u3042\u308B\u304B\nbool point_on_sphere(point3d P, sphere3d S) {\
    \ return abs(dist(P, S.C) - S.r) <= eps; }\n\n// \u76F4\u7DDA L \u3068\u7403 S\
    \ \u306E\u4EA4\u70B9\u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\
    \u3001\u901A\u5E38\u306F2\u500B\u8FD4\u3059\nvector<point3d> line_sphere_intersection(line3d\
    \ L, sphere3d S) {\n   point3d P = projection(S.C, L);\n   double d = point_line_distance(S.C,\
    \ L);\n   if(d > S.r + eps) return {};\n   point3d U = unit(vec(L));\n   double\
    \ h = sqrt(max(0.0, S.r * S.r - d * d));\n   if(h < eps) return {P};\n   return\
    \ {P - U * h, P + U * h};\n}\n\n// \u7DDA\u5206 Seg \u3068\u7403 S \u306E\u4EA4\
    \u70B9\u30020\u500B\u3001\u63A5\u3059\u308B\u5834\u5408\u306F1\u500B\u3001\u901A\
    \u5E38\u306F2\u500B\u8FD4\u3059\nvector<point3d> segment_sphere_intersection(line3d\
    \ Seg, sphere3d S) {\n   vector<point3d> res;\n   for(point3d P : line_sphere_intersection(Seg,\
    \ S)) {\n      if(point_on_segment(P, Seg)) res.push_back(P);\n   }\n   return\
    \ res;\n}\n\n// \u5E73\u9762 H \u3068\u7403 S \u306E\u4EA4\u5186\u3002\u4EA4\u308F\
    \u3089\u306A\u3044\u5834\u5408\u306F assert \u3067\u843D\u3068\u3059\ncircle3d\
    \ plane_sphere_intersection(plane3d H, sphere3d S) {\n   point3d C = projection(S.C,\
    \ H);\n   double d = point_plane_distance(S.C, H);\n   assert(d <= S.r + eps);\n\
    \   double r = sqrt(max(0.0, S.r * S.r - d * d));\n   return circle3d(C, H.N,\
    \ r);\n}\n\n// 2\u7403 S1, S2 \u306E\u4EA4\u5186\u3002\u4EA4\u308F\u3089\u306A\
    \u3044\u5834\u5408\u3084\u540C\u5FC3\u7403\u306E\u5834\u5408\u306F assert \u3067\
    \u843D\u3068\u3059\ncircle3d sphere_sphere_intersection(sphere3d S1, sphere3d\
    \ S2) {\n   double d = dist(S1.C, S2.C);\n   assert(d > eps);\n   assert(abs(S1.r\
    \ - S2.r) <= d + eps && d <= S1.r + S2.r + eps);\n   point3d U = (S2.C - S1.C)\
    \ / d;\n   double x = (S1.r * S1.r - S2.r * S2.r + d * d) / (2 * d);\n   point3d\
    \ C = S1.C + U * x;\n   double r = sqrt(max(0.0, S1.r * S1.r - x * x));\n   return\
    \ circle3d(C, U, r);\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: algorithm_library/cpp/geometry3d.cpp
  requiredBy: []
  timestamp: '2026-08-24 15:06:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: algorithm_library/cpp/geometry3d.cpp
layout: document
redirect_from:
- /library/algorithm_library/cpp/geometry3d.cpp
- /library/algorithm_library/cpp/geometry3d.cpp.html
title: algorithm_library/cpp/geometry3d.cpp
---
