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
