#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

// 符号を返す。正: 1, 負: -1, 0: 0
int sgn(i128 x) {
   if(x > 0) return 1;
   if(x < 0) return -1;
   return 0;
}

// 整数座標の2次元点・ベクトル。座標は long long で持つ
struct point {
   ll x, y;

   point() : x(0), y(0) {}
   point(ll x, ll y) : x(x), y(y) {}

   point operator+() const { return *this; }
   point operator-() const { return point(-x, -y); }
   point operator+(const point &p) const { return point(x + p.x, y + p.y); }
   point operator-(const point &p) const { return point(x - p.x, y - p.y); }
   point operator*(ll k) const { return point(x * k, y * k); }
   point &operator+=(const point &p) {
      x += p.x;
      y += p.y;
      return *this;
   }
   point &operator-=(const point &p) {
      x -= p.x;
      y -= p.y;
      return *this;
   }
   point &operator*=(ll k) {
      x *= k;
      y *= k;
      return *this;
   }
   bool operator==(const point &p) const { return x == p.x && y == p.y; }
   bool operator!=(const point &p) const { return !(*this == p); }
   bool operator<(const point &p) const {
      if(x != p.x) return x < p.x;
      return y < p.y;
   }
};

point operator*(ll k, const point &p) { return p * k; }

istream &operator>>(istream &is, point &p) { return is >> p.x >> p.y; }
ostream &operator<<(ostream &os, const point &p) { return os << p.x << ' ' << p.y; }

// 2点 A, B を通る直線。線分として使う関数では端点 A, B を端とみなす
struct line {
   point A, B;

   line() = default;
   line(point A, point B) : A(A), B(B) {}
};

// 直線・線分 L の方向ベクトル B - A
point vec(line L) { return L.B - L.A; }

// 内積
i128 dot(point P, point Q) { return (i128)P.x * Q.x + (i128)P.y * Q.y; }

// 外積
i128 cross(point P, point Q) { return (i128)P.x * Q.y - (i128)P.y * Q.x; }

// ベクトルの長さの 2 乗
i128 norm(point P) { return dot(P, P); }

// 2点間距離の 2 乗
i128 dist2(point P, point Q) { return norm(P - Q); }

// 反時計回りに 90 度回転
point rotate90(point P) { return point(-P.y, P.x); }

// 点 C が有向線分 AB に対してどの位置にあるか
// 1: 反時計回り, -1: 時計回り, 2: A-B-C, -2: C-A-B, 0: A-C-B
int ccw(point A, point B, point C) {
   point AB = B - A, AC = C - A;
   i128 cr = cross(AB, AC);
   if(cr > 0) return 1;
   if(cr < 0) return -1;
   if(dot(AB, AC) < 0) return 2;
   if(norm(AB) < norm(AC)) return -2;
   return 0;
}

// 点 P が直線 L 上にあるか
bool point_on_line(point P, line L) { return cross(P - L.A, vec(L)) == 0; }

// 点 P が線分 L 上にあるか
bool point_on_segment(point P, line L) {
   return point_on_line(P, L) && dot(P - L.A, P - L.B) <= 0;
}

// 2直線が平行か
bool is_parallel(line L1, line L2) { return cross(vec(L1), vec(L2)) == 0; }

// 2直線が直交するか
bool is_orthogonal(line L1, line L2) { return dot(vec(L1), vec(L2)) == 0; }

// 2線分が交差するか。端点で接する場合も true
bool segment_intersect(line L1, line L2) {
   return ccw(L1.A, L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0
          && ccw(L2.A, L2.B, L1.A) * ccw(L2.A, L2.B, L1.B) <= 0;
}

// 中心 C、半径 r の円。半径は整数で持つ
struct circle {
   point C;
   ll r;

   circle() {}
   circle(point C, ll r) : C(C), r(r) { assert(r >= 0); }
};

i128 radius2(circle C) {
   assert(C.r >= 0);
   return (i128)C.r * C.r;
}

// 点 P と円 C の位置関係。-1: 内部, 0: 円周上, 1: 外部
int point_circle_relation(point P, circle C) { return sgn(dist2(P, C.C) - radius2(C)); }

// 点 P が円 C の円周上にあるか
bool point_on_circle(point P, circle C) { return point_circle_relation(P, C) == 0; }

// 点 P が円 C の内部または円周上にあるか
bool point_in_circle(point P, circle C) { return point_circle_relation(P, C) <= 0; }

// 直線 L と円 C の交点数。ゼロ長直線の場合は assert で落とす
int line_circle_intersection_count(line L, circle C) {
   i128 v2 = norm(vec(L));
   assert(v2 > 0);
   i128 cr = cross(C.C - L.A, vec(L));
   i128 x = cr * cr - radius2(C) * v2;
   if(x > 0) return 0;
   return x == 0 ? 1 : 2;
}

// 直線 L と円 C が交わるか。接する場合も true
bool line_circle_intersect(line L, circle C) { return line_circle_intersection_count(L, C) > 0; }

// 線分 L と円 C の円周が交わるか。端点で接する場合も true
bool segment_circle_intersect(line L, circle C) {
   i128 r2 = radius2(C);
   i128 dA = dist2(L.A, C.C);
   i128 dB = dist2(L.B, C.C);
   if(L.A == L.B) return dA == r2;
   if(dA == r2 || dB == r2) return true;
   if(dA < r2 && dB < r2) return false;
   if((dA < r2) != (dB < r2)) return true;

   point v = vec(L);
   i128 v2 = norm(v);
   assert(v2 > 0);
   if(dot(C.C - L.A, v) < 0 || dot(C.C - L.B, -v) < 0) return false;
   i128 cr = cross(C.C - L.A, v);
   return cr * cr <= r2 * v2;
}

// 2円 C1, C2 の交点数。完全に一致する場合は -1 を返す
int circle_intersection_count(circle C1, circle C2) {
   assert(C1.r >= 0 && C2.r >= 0);
   i128 d2 = dist2(C1.C, C2.C);
   if(d2 == 0) return C1.r == C2.r ? -1 : 0;

   i128 rd = C1.r > C2.r ? (i128)C1.r - C2.r : (i128)C2.r - C1.r;
   i128 rs = (i128)C1.r + C2.r;
   i128 diff2 = rd * rd;
   i128 sum2 = rs * rs;
   if(d2 < diff2 || sum2 < d2) return 0;
   if(d2 == diff2 || d2 == sum2) return 1;
   return 2;
}

// 2円 C1, C2 の円周が交わるか。完全に一致する場合も true
bool circle_intersect(circle C1, circle C2) { return circle_intersection_count(C1, C2) != 0; }

// 2円 C1, C2 の共通接線の本数。完全に一致する場合は -1 を返す
int common_tangent_count(circle C1, circle C2) {
   assert(C1.r >= 0 && C2.r >= 0);
   i128 d2 = dist2(C1.C, C2.C);
   if(d2 == 0 && C1.r == C2.r) return -1;

   i128 rd = C1.r > C2.r ? (i128)C1.r - C2.r : (i128)C2.r - C1.r;
   i128 rs = (i128)C1.r + C2.r;
   i128 diff2 = rd * rd;
   i128 sum2 = rs * rs;
   if(d2 < diff2) return 0;
   if(d2 == diff2) return 1;
   if(d2 < sum2) return 2;
   if(d2 == sum2) return 3;
   return 4;
}
