// Speed Star ライブラリから窃盗：https://github.com/KentaroMatsushita/icpc_library/tree/main/src/geometry

#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-10;

// contains の返り値
// _OUT: 外部, _ON: 辺上, _IN: 内部
const int _OUT = 0;
const int _ON = 1;
const int _IN = 2;

// 2次元点・ベクトル
struct Point {
   double x, y;

   Point() : x(0), y(0) {}
   Point(double x, double y) : x(x), y(y) {}

   Point operator+() const { return *this; }
   Point operator-() const { return Point(-x, -y); }
   Point operator+(const Point &p) const { return Point(x + p.x, y + p.y); }
   Point operator-(const Point &p) const { return Point(x - p.x, y - p.y); }
   Point operator*(double k) const { return Point(x * k, y * k); }
   Point operator/(double k) const { return Point(x / k, y / k); }
   Point &operator+=(const Point &p) {
      x += p.x;
      y += p.y;
      return *this;
   }
   Point &operator-=(const Point &p) {
      x -= p.x;
      y -= p.y;
      return *this;
   }
   Point &operator*=(double k) {
      x *= k;
      y *= k;
      return *this;
   }
   Point &operator/=(double k) {
      x /= k;
      y /= k;
      return *this;
   }
   bool operator==(const Point &p) const { return abs(x - p.x) < eps && abs(y - p.y) < eps; }
   bool operator!=(const Point &p) const { return !(*this == p); }
   bool operator<(const Point &p) const {
      if(abs(x - p.x) >= eps) return x < p.x;
      return y < p.y - eps;
   }
};

Point operator*(double k, const Point &p) { return p * k; }

istream &operator>>(istream &is, Point &p) { return is >> p.x >> p.y; }
ostream &operator<<(ostream &os, const Point &p) { return os << p.x << ' ' << p.y; }

using Polygon = vector<Point>;

double dot(Point P, Point Q) { return P.x * Q.x + P.y * Q.y; }

double cross(Point P, Point Q) { return P.x * Q.y - P.y * Q.x; }

///////////////////////////////////////////

// 多角形 Q に対して点 p の内外判定
int contains(const Polygon& Q, const Point& p) {
   bool in = false;
   for(size_t i = 0; i < Q.size(); i++) {
      Point a = Q[i] - p, b = Q[(i + 1) % Q.size()] - p;
      if(a.y > b.y) swap(a, b);
      if(a.y <= eps && eps < b.y && cross(a, b) < -eps) in = !in;
      if(abs(cross(a, b)) < eps && dot(a, b) <= eps) return _ON;
   }
   return in ? _IN : _OUT;
}
