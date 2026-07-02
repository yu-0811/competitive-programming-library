// Speed Star ライブラリから窃盗：https://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry

#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-10;
const double INF = 1e18;

// 補助関数
// 誤差付きで符号を返す。正: 1, 負: -1, ほぼ 0: 0
int sgn(double x) {
   if(x > eps) return 1;
   if(x < -eps) return -1;
   return 0;
}

// 2次元点・ベクトル。加減算やスカラー倍をベクトルとして扱える
struct point {
   double x, y;

   point() : x(0), y(0) {}
   point(double x, double y) : x(x), y(y) {}

   point operator+() const { return *this; }
   point operator-() const { return point(-x, -y); }
   point operator+(const point &p) const { return point(x + p.x, y + p.y); }
   point operator-(const point &p) const { return point(x - p.x, y - p.y); }
   point operator*(double k) const { return point(x * k, y * k); }
   point operator/(double k) const { return point(x / k, y / k); }
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
   point &operator*=(double k) {
      x *= k;
      y *= k;
      return *this;
   }
   point &operator/=(double k) {
      x /= k;
      y /= k;
      return *this;
   }
   bool operator==(const point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }
   bool operator!=(const point &p) const { return !(*this == p); }
   bool operator<(const point &p) const {
      if(abs(x - p.x) >= eps) return x < p.x;
      return y < p.y - eps;
   }
};

point operator*(double k, const point &p) { return p * k; }

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
double dot(point P, point Q) { return P.x * Q.x + P.y * Q.y; }
// 外積
double cross(point P, point Q) { return P.x * Q.y - P.y * Q.x; }
// ベクトルの長さの 2 乗
double norm(point P) { return dot(P, P); }
// ベクトルの長さ
double abs(point P) { return sqrt(norm(P)); }
// 2点間距離
double dist(point P, point Q) { return abs(P - Q); }
// 反時計回りに 90 度回転
point rotate90(point P) { return point(-P.y, P.x); }
// 反時計回りに theta ラジアン回転
point rotate(point P, double theta) {
   double c = cos(theta), s = sin(theta);
   return point(c * P.x - s * P.y, s * P.x + c * P.y);
}

// 点 C が有向線分 AB に対してどの位置にあるか
// 1: 反時計回り, -1: 時計回り, 2: A-B-C, -2: C-A-B, 0: A-C-B
int ccw(point A, point B, point C) {
   point AB = B - A, AC = C - A;
   if(cross(AB, AC) > eps) return 1;
   if(cross(AB, AC) < -eps) return -1;
   if(dot(AB, AC) < -eps) return 2;
   if(norm(AB) < norm(AC) - eps) return -2;
   return 0;
}
/////////////////////////////////////////////////////////////

// 点 P が直線 L 上にあるか
bool point_on_line(point P, line L) { return abs(cross(P - L.A, vec(L))) < eps; }

// 点 P が線分 L 上にあるか
bool point_on_segment(point P, line L) {
   return point_on_line(P, L) && dot(P - L.A, P - L.B) < eps;
}

// 点 P から直線 L へ下ろした垂線の足
point projection(point P, line L) { return L.A + vec(L) * dot(P - L.A, vec(L)) / norm(vec(L)); }

// 点 P を直線 L に関して対称移動した点
point reflection(point P, line L) { return projection(P, L) * 2 - P; }

// 点 P と直線 L の距離
double point_line_distance(point P, line L) { return abs(cross(P - L.A, vec(L))) / abs(vec(L)); }

// 点 P と線分 L の距離
double point_segment_distance(point P, line L) {
   if(dot(P - L.A, vec(L)) < 0) {
      return dist(P, L.A);
   } else if(dot(P - L.B, vec(L)) > 0) {
      return dist(P, L.B);
   } else {
      return point_line_distance(P, L);
   }
}

// 2直線が平行か
bool is_parallel(line L1, line L2) { return abs(cross(vec(L1), vec(L2))) < eps; }

// 2直線が直交するか
bool is_orthogonal(line L1, line L2) { return abs(dot(vec(L1), vec(L2))) < eps; }

// 2直線の交点。平行な場合は assert で落とす
point line_intersection(line L1, line L2) {
   assert(!is_parallel(L1, L2));
   return L1.A + vec(L1) * cross(L2.A - L1.A, vec(L2)) / cross(vec(L1), vec(L2));
}

// 2線分が交差するか。端点で接する場合も true
bool segment_intersect(line L1, line L2) {
   return ccw(L1.A, L1.B, L2.A) * ccw(L1.A, L1.B, L2.B) <= 0
          && ccw(L2.A, L2.B, L1.A) * ccw(L2.A, L2.B, L1.B) <= 0;
}

// 2線分間の距離。交差する場合は 0
double segment_distance(line L1, line L2) {
   if(segment_intersect(L1, L2)) {
      return 0;
   } else {
      double ans = INF;
      ans = min(ans, point_segment_distance(L1.A, L2));
      ans = min(ans, point_segment_distance(L1.B, L2));
      ans = min(ans, point_segment_distance(L2.A, L1));
      ans = min(ans, point_segment_distance(L2.B, L1));
      return ans;
   }
}
