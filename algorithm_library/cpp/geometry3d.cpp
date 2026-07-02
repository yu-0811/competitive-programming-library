#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-10;
const double INF = 1e18;

// 誤差付きで符号を返す。正: 1, 負: -1, ほぼ 0: 0
int sgn(double x) {
   if(x > eps) return 1;
   if(x < -eps) return -1;
   return 0;
}

// [0, 1] に丸める
double clamp01(double x) { return max(0.0, min(1.0, x)); }
// acos などに渡す値を [-1, 1] に丸める
double clamp_unit(double x) { return max(-1.0, min(1.0, x)); }

// 3次元点・ベクトル。加減算やスカラー倍をベクトルとして扱える
struct point3d {
   double x, y, z;

   point3d() : x(0), y(0), z(0) {}
   point3d(double x, double y, double z) : x(x), y(y), z(z) {}

   point3d operator+() const { return *this; }
   point3d operator-() const { return point3d(-x, -y, -z); }
   point3d operator+(const point3d &p) const { return point3d(x + p.x, y + p.y, z + p.z); }
   point3d operator-(const point3d &p) const { return point3d(x - p.x, y - p.y, z - p.z); }
   point3d operator*(double k) const { return point3d(x * k, y * k, z * k); }
   point3d operator/(double k) const { return point3d(x / k, y / k, z / k); }
   point3d &operator+=(const point3d &p) {
      x += p.x;
      y += p.y;
      z += p.z;
      return *this;
   }
   point3d &operator-=(const point3d &p) {
      x -= p.x;
      y -= p.y;
      z -= p.z;
      return *this;
   }
   point3d &operator*=(double k) {
      x *= k;
      y *= k;
      z *= k;
      return *this;
   }
   point3d &operator/=(double k) {
      x /= k;
      y /= k;
      z /= k;
      return *this;
   }
   bool operator==(const point3d &p) const {
      return abs(x - p.x) < eps && abs(y - p.y) < eps && abs(z - p.z) < eps;
   }
   bool operator!=(const point3d &p) const { return !(*this == p); }
   bool operator<(const point3d &p) const {
      if(abs(x - p.x) >= eps) return x < p.x;
      if(abs(y - p.y) >= eps) return y < p.y;
      return z < p.z - eps;
   }
};

point3d operator*(double k, const point3d &p) { return p * k; }

istream &operator>>(istream &is, point3d &p) { return is >> p.x >> p.y >> p.z; }
ostream &operator<<(ostream &os, const point3d &p) { return os << p.x << ' ' << p.y << ' ' << p.z; }

using vec3d = point3d;

// 2点 A, B を通る直線。線分として使う関数では端点 A, B を端とみなす
struct line3d {
   point3d A, B;

   line3d() = default;
   line3d(point3d A, point3d B) : A(A), B(B) {}
};

// 点 P を通り、法線ベクトル N を持つ平面
struct plane3d {
   point3d P, N;

   plane3d() = default;
   plane3d(point3d P, point3d N) : P(P), N(N) {}
   // 3点 A, B, C を通る平面。3点が一直線上の場合は法線がゼロになる
   plane3d(point3d A, point3d B, point3d C) : P(A), N((B - A).y * (C - A).z - (B - A).z * (C - A).y,
                                                   (B - A).z * (C - A).x - (B - A).x * (C - A).z,
                                                   (B - A).x * (C - A).y - (B - A).y * (C - A).x) {}
};

// 中心 C、半径 r の球
struct sphere3d {
   point3d C;
   double r;

   sphere3d() : C(), r(0) {}
   sphere3d(point3d C, double r) : C(C), r(r) {}
};

// 3次元空間上の円。中心 C、円を含む平面の法線 N、半径 r
struct circle3d {
   point3d C, N;
   double r;

   circle3d() : C(), N(), r(0) {}
   circle3d(point3d C, point3d N, double r) : C(C), N(N), r(r) {}
};

// 直線・線分 L の方向ベクトル B - A
point3d vec(line3d L) { return L.B - L.A; }

// 内積
double dot(point3d P, point3d Q) { return P.x * Q.x + P.y * Q.y + P.z * Q.z; }

// 外積
point3d cross(point3d P, point3d Q) {
   return point3d(P.y * Q.z - P.z * Q.y,
                  P.z * Q.x - P.x * Q.z,
                  P.x * Q.y - P.y * Q.x);
}

// スカラー三重積。符号付き平行六面体体積
double triple(point3d A, point3d B, point3d C) { return dot(A, cross(B, C)); }

// ベクトルの長さの 2 乗
double norm(point3d P) { return dot(P, P); }

// ベクトルの長さ
double abs(point3d P) { return sqrt(norm(P)); }

// 2点間距離
double dist(point3d P, point3d Q) { return abs(P - Q); }

// 単位ベクトル。ゼロベクトルの場合は assert で落とす
point3d unit(point3d P) {
   double len = abs(P);
   assert(len > eps);
   return P / len;
}

// 2ベクトルのなす角 [0, pi]
double angle(point3d P, point3d Q) {
   assert(abs(P) > eps && abs(Q) > eps);
   return acos(clamp_unit(dot(P, Q) / abs(P) / abs(Q)));
}

// 原点を通る axis を軸として P を theta ラジアン回転
point3d rotate_around_axis(point3d P, point3d axis, double theta) {
   point3d U = unit(axis);
   double c = cos(theta), s = sin(theta);
   return P * c + cross(U, P) * s + U * dot(U, P) * (1 - c);
}

// 直線 axis を軸として P を theta ラジアン回転
point3d rotate(point3d P, line3d axis, double theta) {
   return axis.A + rotate_around_axis(P - axis.A, vec(axis), theta);
}

// 3点 A, B, C を頂点とする三角形の面積
double triangle_area(point3d A, point3d B, point3d C) { return abs(cross(B - A, C - A)) / 2; }

// 4点 A, B, C, D を頂点とする四面体の体積
double tetrahedron_volume(point3d A, point3d B, point3d C, point3d D) {
   return abs(triple(B - A, C - A, D - A)) / 6;
}

// 点 P が直線 L 上にあるか
bool point_on_line(point3d P, line3d L) {
   assert(abs(vec(L)) > eps);
   return abs(cross(P - L.A, vec(L))) <= eps * abs(vec(L));
}

// 点 P が線分 S 上にあるか
bool point_on_segment(point3d P, line3d S) {
   return point_on_line(P, S) && dot(P - S.A, P - S.B) <= eps;
}

// 点 P から直線 L へ下ろした垂線の足
point3d projection(point3d P, line3d L) {
   point3d V = vec(L);
   assert(abs(V) > eps);
   return L.A + V * dot(P - L.A, V) / norm(V);
}

// 点 P を直線 L に関して対称移動した点
point3d reflection(point3d P, line3d L) { return projection(P, L) * 2 - P; }

// 線分 S 上で点 P に最も近い点
point3d closest_point_on_segment(point3d P, line3d S) {
   point3d V = vec(S);
   if(norm(V) < eps) return S.A;
   double t = clamp01(dot(P - S.A, V) / norm(V));
   return S.A + V * t;
}

// 点 P と直線 L の距離
double point_line_distance(point3d P, line3d L) {
   assert(abs(vec(L)) > eps);
   return abs(cross(P - L.A, vec(L))) / abs(vec(L));
}

// 点 P と線分 S の距離
double point_segment_distance(point3d P, line3d S) { return dist(P, closest_point_on_segment(P, S)); }

// 2直線が平行か
bool is_parallel(line3d L1, line3d L2) {
   assert(abs(vec(L1)) > eps && abs(vec(L2)) > eps);
   return abs(cross(vec(L1), vec(L2))) < eps;
}

// 2直線が直交するか
bool is_orthogonal(line3d L1, line3d L2) {
   assert(abs(vec(L1)) > eps && abs(vec(L2)) > eps);
   return abs(dot(vec(L1), vec(L2))) < eps;
}

// 2直線が同一直線か
bool same_line(line3d L1, line3d L2) { return is_parallel(L1, L2) && point_on_line(L2.A, L1); }

// 2直線間の距離。ねじれの位置にも対応
double line_line_distance(line3d L1, line3d L2) {
   point3d U = vec(L1), V = vec(L2);
   assert(abs(U) > eps && abs(V) > eps);
   point3d W = cross(U, V);
   if(abs(W) < eps) return point_line_distance(L2.A, L1);
   return abs(triple(L2.A - L1.A, U, V)) / abs(W);
}

// 2直線上の最近点の組。平行な場合は assert で落とす
pair<point3d, point3d> closest_points_between_lines(line3d L1, line3d L2) {
   point3d U = vec(L1), V = vec(L2), W = L1.A - L2.A;
   double a = dot(U, U), b = dot(U, V), c = dot(V, V);
   double d = dot(U, W), e = dot(V, W);
   double den = a * c - b * b;
   assert(abs(U) > eps && abs(V) > eps && abs(den) > eps);
   double s = (b * e - c * d) / den;
   double t = (a * e - b * d) / den;
   return {L1.A + U * s, L2.A + V * t};
}

// 2直線が交差するか
bool line_intersect(line3d L1, line3d L2) { return line_line_distance(L1, L2) <= eps; }

// 2直線の交点。平行な場合やねじれの位置の場合は assert で落とす
point3d line_intersection(line3d L1, line3d L2) {
   assert(line_intersect(L1, L2) && !is_parallel(L1, L2));
   auto [P, Q] = closest_points_between_lines(L1, L2);
   return (P + Q) / 2;
}

// 2線分上の最近点の組。線分が退化して点になっている場合にも対応
pair<point3d, point3d> closest_points_between_segments(line3d S1, line3d S2) {
   point3d U = vec(S1), V = vec(S2), W = S1.A - S2.A;
   double a = dot(U, U), b = dot(U, V), c = dot(V, V);
   double d = dot(U, W), e = dot(V, W), D = a * c - b * b;

   if(a < eps && c < eps) return {S1.A, S2.A};
   if(a < eps) return {S1.A, closest_point_on_segment(S1.A, S2)};
   if(c < eps) return {closest_point_on_segment(S2.A, S1), S2.A};

   double sN, sD = D, tN, tD = D;
   if(D < eps) {
      sN = 0.0;
      sD = 1.0;
      tN = e;
      tD = c;
   } else {
      sN = b * e - c * d;
      tN = a * e - b * d;
      if(sN < 0.0) {
         sN = 0.0;
         tN = e;
         tD = c;
      } else if(sN > sD) {
         sN = sD;
         tN = e + b;
         tD = c;
      }
   }

   if(tN < 0.0) {
      tN = 0.0;
      if(-d < 0.0) {
         sN = 0.0;
      } else if(-d > a) {
         sN = sD;
      } else {
         sN = -d;
         sD = a;
      }
   } else if(tN > tD) {
      tN = tD;
      if(-d + b < 0.0) {
         sN = 0.0;
      } else if(-d + b > a) {
         sN = sD;
      } else {
         sN = -d + b;
         sD = a;
      }
   }

   double s = abs(sN) < eps ? 0.0 : sN / sD;
   double t = abs(tN) < eps ? 0.0 : tN / tD;
   return {S1.A + U * s, S2.A + V * t};
}

// 2線分間の距離。交差する場合は 0
double segment_distance(line3d S1, line3d S2) {
   auto [P, Q] = closest_points_between_segments(S1, S2);
   return dist(P, Q);
}

// 2線分が交差するか。端点で接する場合も true
bool segment_intersect(line3d S1, line3d S2) { return segment_distance(S1, S2) <= eps; }

// 点 P が平面 H 上にあるか
bool point_on_plane(point3d P, plane3d H) {
   assert(abs(H.N) > eps);
   return abs(dot(P - H.P, H.N)) <= eps * abs(H.N);
}

// 点 P から平面 H へ下ろした垂線の足
point3d projection(point3d P, plane3d H) {
   assert(abs(H.N) > eps);
   return P - H.N * dot(P - H.P, H.N) / norm(H.N);
}

// 点 P を平面 H に関して対称移動した点
point3d reflection(point3d P, plane3d H) { return projection(P, H) * 2 - P; }

// 点 P と平面 H の符号付き距離。法線方向が正
double signed_point_plane_distance(point3d P, plane3d H) {
   assert(abs(H.N) > eps);
   return dot(P - H.P, H.N) / abs(H.N);
}

// 点 P と平面 H の距離
double point_plane_distance(point3d P, plane3d H) { return abs(signed_point_plane_distance(P, H)); }

// 直線 L と平面 H が平行か
bool is_parallel(line3d L, plane3d H) {
   assert(abs(vec(L)) > eps && abs(H.N) > eps);
   return abs(dot(vec(L), H.N)) < eps;
}

// 直線 L と平面 H が直交するか
bool is_orthogonal(line3d L, plane3d H) {
   assert(abs(vec(L)) > eps && abs(H.N) > eps);
   return abs(cross(vec(L), H.N)) < eps;
}

// 直線 L が平面 H 上にあるか
bool line_on_plane(line3d L, plane3d H) { return point_on_plane(L.A, H) && point_on_plane(L.B, H); }

// 直線 L と平面 H の交点。平行な場合は assert で落とす
point3d line_plane_intersection(line3d L, plane3d H) {
   assert(!is_parallel(L, H));
   point3d V = vec(L);
   double t = dot(H.P - L.A, H.N) / dot(V, H.N);
   return L.A + V * t;
}

// 直線 L と平面 H の距離。交差する場合は 0
double line_plane_distance(line3d L, plane3d H) {
   if(!is_parallel(L, H)) return 0;
   return point_plane_distance(L.A, H);
}

// 2平面が平行か
bool is_parallel(plane3d H1, plane3d H2) {
   assert(abs(H1.N) > eps && abs(H2.N) > eps);
   return abs(cross(H1.N, H2.N)) < eps;
}

// 2平面が直交するか
bool is_orthogonal(plane3d H1, plane3d H2) {
   assert(abs(H1.N) > eps && abs(H2.N) > eps);
   return abs(dot(H1.N, H2.N)) < eps;
}

// 2平面が同一平面か
bool same_plane(plane3d H1, plane3d H2) { return is_parallel(H1, H2) && point_on_plane(H2.P, H1); }

// 2平面の交線。平行な場合は assert で落とす
line3d plane_intersection(plane3d H1, plane3d H2) {
   assert(!is_parallel(H1, H2));
   point3d D = cross(H1.N, H2.N);
   double d1 = dot(H1.N, H1.P);
   double d2 = dot(H2.N, H2.P);
   point3d P = cross(H2.N * d1 - H1.N * d2, D) / norm(D);
   return line3d(P, P + D);
}

// 2平面間の距離。交差する場合は 0
double plane_plane_distance(plane3d H1, plane3d H2) {
   if(!is_parallel(H1, H2)) return 0;
   return point_plane_distance(H2.P, H1);
}

// 点 P が球 S の内部または表面にあるか
bool point_in_sphere(point3d P, sphere3d S) { return dist(P, S.C) <= S.r + eps; }

// 点 P が球 S の表面にあるか
bool point_on_sphere(point3d P, sphere3d S) { return abs(dist(P, S.C) - S.r) <= eps; }

// 直線 L と球 S の交点。0個、接する場合は1個、通常は2個返す
vector<point3d> line_sphere_intersection(line3d L, sphere3d S) {
   point3d P = projection(S.C, L);
   double d = point_line_distance(S.C, L);
   if(d > S.r + eps) return {};
   point3d U = unit(vec(L));
   double h = sqrt(max(0.0, S.r * S.r - d * d));
   if(h < eps) return {P};
   return {P - U * h, P + U * h};
}

// 線分 Seg と球 S の交点。0個、接する場合は1個、通常は2個返す
vector<point3d> segment_sphere_intersection(line3d Seg, sphere3d S) {
   vector<point3d> res;
   for(point3d P : line_sphere_intersection(Seg, S)) {
      if(point_on_segment(P, Seg)) res.push_back(P);
   }
   return res;
}

// 平面 H と球 S の交円。交わらない場合は assert で落とす
circle3d plane_sphere_intersection(plane3d H, sphere3d S) {
   point3d C = projection(S.C, H);
   double d = point_plane_distance(S.C, H);
   assert(d <= S.r + eps);
   double r = sqrt(max(0.0, S.r * S.r - d * d));
   return circle3d(C, H.N, r);
}

// 2球 S1, S2 の交円。交わらない場合や同心球の場合は assert で落とす
circle3d sphere_sphere_intersection(sphere3d S1, sphere3d S2) {
   double d = dist(S1.C, S2.C);
   assert(d > eps);
   assert(abs(S1.r - S2.r) <= d + eps && d <= S1.r + S2.r + eps);
   point3d U = (S2.C - S1.C) / d;
   double x = (S1.r * S1.r - S2.r * S2.r + d * d) / (2 * d);
   point3d C = S1.C + U * x;
   double r = sqrt(max(0.0, S1.r * S1.r - x * x));
   return circle3d(C, U, r);
}
