## math
### 幾何系
- AngularSort.py
    - 2点 p1, p2 が原点から見て同じ偏角（同じ方向）にあるか判定する

- geometry.py
    - (x1,y1) - (x2,y2) の正規化ベクトルを返す
    - (x0,y0) - (x1,y1) を通る直線の上に (px,py) があるか判定
    - 2点 (x0, y0), (x1, y1) を通る直線 ax + by + c = 0 の (a, b, c) を返す
    - 始点(sx, sy) → 終点(gx, gy) を速さ v で動くとき、t 秒後の位置を返す

- Truangle.py
    - 3点を頂点とする三角形の面積を求める

### 整数系
- extGCD.py
    - ax + by = gcd(a,b) を満たす (x,y) を求める
    - ax ≡ 1 (mod m) を満たす x (a の逆元) を求める
    - ax ≡ b (mod m) を満たす x を求める
    - x ≡ B[i] (mod M[i]) を満たす x ≡ r (mod lcm(M)) を求める

- modDiv.py
    - P/Q mod m
    - R 以下で r ≡ x (mod m) を満たす最大の整数 x を求める
    - L 以上で r ≡ x (mod m) を満たす最小の整数 x を求める

- modComb.py
    - 前計算 O(n)、クエリ O(1) で nCk, nHk を求める
    - 前計算 O(k)、クエリ O(k) で nCk を求める
    - 任意 mod (素数でなくていい) で mod 上の nCk を O(N^2) で求める (パスカルの三角形)

- factorization.py
    - 素因数分解をしたい最大の数を N として前処理 O(N)、素因数分解をクエリ毎 O(log N) でおこなう
    - エラトステネスの篩 O(N log log N)
    - M 以下の素数を O(M log log M) で列挙

- PIE.py
    - クエリの引数を N として前処理 O(N log log N)で素因数分解クエリを O(log n)、約数列挙クエリを O(n^(1/3))

- mobius.py
    - 高速メビウス変換

- FFT.py

- MatrixPower.py
    - 行列 A,B の積を返す
    - 行列 A の累乗 A^K