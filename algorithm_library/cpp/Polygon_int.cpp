#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

// contains の返り値
// _OUT: 外部, _ON: 辺上, _IN: 内部
const int _OUT = 0;
const int _ON = 1;
const int _IN = 2;

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

using Polygon = vector<point>;

i128 dot(point P, point Q) { return (i128)P.x * Q.x + (i128)P.y * Q.y; }

i128 cross(point P, point Q) { return (i128)P.x * Q.y - (i128)P.y * Q.x; }

int contains(const Polygon &Q, const point &p) {
   bool in = false;
   for(size_t i = 0; i < Q.size(); i++) {
      point a = Q[i] - p, b = Q[(i + 1) % Q.size()] - p;
      if(a.y > b.y) swap(a, b);
      if(a.y <= 0 && 0 < b.y && cross(a, b) < 0) in = !in;
      if(cross(a, b) == 0 && dot(a, b) <= 0) return _ON;
   }
   return in ? _IN : _OUT;
}
