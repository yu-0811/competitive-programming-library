#include <bits/stdc++.h>
using namespace std;

struct Mo {
  // 初期化 : Mo 変数名(数列の長さ)
  // クエリ追加 : 変数名.add(クエリの左端, クエリの右端) <- 半開区間
  // クエリ処理 : Mo変数名.build(追加処理, 削除処理, クエリ処理)
  // ラムダ式で add, erase, out を定義して build に渡す
  // add(int i) : i 番目の要素を追加する処理
  // erase(int i) : i 番目の要素を削除する処理
  // out(int q) : q 番目のクエリの処理
  // add, erase, out からは main 関数内の変数に引数に何も渡さずにアクセスできる
  // auto add = [&](int i) { ... };
  // auto erase = [&](int i) { ... };
  // auto out = [&](int q) { ... };

  int n; vector<pair<int, int>> lr;
  
  explicit Mo(int n) : n(n) {}

  void add(int l, int r) { /* [l, r) */
    lr.emplace_back(l, r);
  }

  // 右拡張と左拡張で別の関数を使う場合はこっちが直接呼び出される
  template< typename AL, typename AR, typename EL, typename ER, typename O >
  void build(const AL &add_left, const AR &add_right, const EL &erase_left, const ER &erase_right, const O &out) {
    int q = (int) lr.size();
    int bs = n / min< int >(n, sqrt(q));
    vector< int > ord(q);
    iota(begin(ord), end(ord), 0);
    sort(begin(ord), end(ord), [&](int a, int b) {
      int ablock = lr[a].first / bs, bblock = lr[b].first / bs;
      if(ablock != bblock) return ablock < bblock;
      return (ablock & 1) ? lr[a].second > lr[b].second : lr[a].second < lr[b].second;
    });
    int l = 0, r = 0;
    for(auto idx : ord) {
      while(l > lr[idx].first) add_left(--l);
      while(r < lr[idx].second) add_right(r++);
      while(l < lr[idx].first) erase_left(l++);
      while(r > lr[idx].second) erase_right(--r);
      out(idx);
    }
  }

  // add : 拡張処理
  // erase : 縮小処理
  // out : クエリ解答処理
  template< typename A, typename E, typename O >
  void build(const A &add, const E &erase, const O &out) {
    build(add, add, erase, erase, out);
  }
};