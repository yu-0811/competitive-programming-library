# 2 要素タプル向け最小ヒープ

`algorithm_library/python/data-structure/TupleHeap.py` に 2 方式を実装した。
両方とも `(x, y)` を辞書順で比較し、最小値をタプルで返す。
第 1 成分が等しいときは第 2 成分も比較する。

| 実装 | 保存方法 | 入力の条件 |
| --- | --- | --- |
| `TupleHeap` | 第 1・第 2 成分を別々のリストに保存する自作二分ヒープ | 成分の型ごとに一貫した全順序が必要。負数・多倍長整数・浮動小数点数・文字列を利用可能 |
| `PackedTupleHeap` | `(x << bits) \| y` に符号化して `heapq` に保存 | 整数 2 個。`0 <= y < 2**bits`。`x` は負数も利用可能 |

今回の実装は **2 要素専用**。3 要素以上のタプルには対応しない。
`TupleHeap` に NaN や比較できない型の混在を渡さない。
安定性や入力タプルのオブジェクト同一性は保証しない。

## 使い方

ライブラリのクラスを読み込むか、競技用コードに貼り付けて利用する。

```python
h = TupleHeap([(3, 9), (1, 8), (1, 2)])
h.push((2, 5))
assert h.peek() == (1, 2)
assert h.pop() == (1, 2)
assert h.replace((4, 0)) == (1, 8)  # 最小値を取り出して挿入
assert h.pushpop((0, 7)) == (0, 7)  # 挿入して最小値を取り出す
assert len(h) == 3
while h:
    priority, vertex = h.pop()

# 例えば頂点番号 0 <= v < n を第 2 成分に持つ場合
n = 100000
h = PackedTupleHeap(bits=(n - 1).bit_length())
h.push((-5, n - 1))
assert h.pop() == (-5, n - 1)
```

どちらも初期化は O(n)、`push`・`pop`・`replace` は O(log n)、
`pushpop` は最悪 O(log n)、`peek`・`len` は O(1)、使用領域は O(n)。
成分の比較・整数演算を O(1) と見た場合の計算量である。
空のヒープに対する `pop`・`peek`・`replace` は `IndexError`。
空のヒープへの `pushpop` は入力の値を返し、ヒープは空のまま。
これらの意味は標準の [`heapq`](https://docs.python.org/3.14/library/heapq.html) に合わせている。

## 方式の意図と制約

`TupleHeap` はタプル自体を内部に保存せず、比較を
`x < u or (x == u and y < v)` と展開する。
取り出すときは小さい方の子を葉まで引き上げ、末尾の値を適切な位置まで戻す。
成分を分ける理由は、PyPy に整数だけ・浮動小数点数だけのリストを
効率よく保存する仕組みがあるため。
この仕組みは [PyPy の公式解説](https://pypy.org/posts/2011/10/more-compact-lists-with-list-strategies-8229304944653956829.html)
に記載されている。実際にどれだけ速くなるかは以下の実測で判断する。

`PackedTupleHeap` はヒープ操作そのものには標準の `heapq` を使い、
タプルの比較を整数 1 個の比較に置き換える。
符号化した値は `x * 2**bits + y` なので、条件を満たせば負の `x` でも辞書順を保つ。
復元は `value >> bits, value & ((1 << bits) - 1)`。
範囲外の第 2 成分は `ValueError` とし、黙って誤った順序で処理しない。
`bits` の既定値は 20。第 2 成分が負の場合は利用側で既知の下限を引くなどの変換が必要。

PyPy では符号化した整数が機械語の整数に収まるかも影響する。
64 bit 環境で `bits <= 63`、非負の `x` なら、
`x < 2**(63 - bits)` が符号付き 64 bit に収まる目安。
多倍長整数に拡張されても正しく動くが、速さは別途確認する。

## 測定方法

- 測定日: 2026-10-25
- CPU: AMD Ryzen AI 7 350、Linux / WSL2 x86_64。`taskset -c 2` で CPU を固定。
- PyPy 7.3.20 / Python 3.11.13、および CPython 3.14.4。
- 比較対象はラッパークラスを挟まない `heapq.heappush(heap, pair)` / `heappop(heap)`。
- `packed` は範囲検証・符号化・復元も測定に含む。`bits=20`。
- 入力生成・ファイル読込・明示的な GC・結果検証・プロセス起動を除き、
  ヒープの生成、操作、実行中のメモリ確保、自動 GC、JIT コンパイルを含める。
- `batch`: n 個すべてを push してから n 回 pop。入力の生成は含めない。
- `mixed`: n/4 個で初期化し、残りの入力ごとに pop → push。最後にすべて pop。
  初期化・最後の取り出しも含み、合計 n 回取り出す。
- `dijkstra`: n 頂点・8n 辺の有向グラフ。重みは正整数。
  サイクルを含むため全頂点に到達可能。古い候補を pop 時に捨てる通常の実装。
  `(距離, 頂点番号)` の生成、距離更新、辺の走査を含むアルゴリズム全体を測る。
- `random`: batch/mixed の第 1 成分は `[0, 10**9)`、第 2 成分は `[0, n)`。
  Dijkstra の重みは `[1, 1000]`。
- `ties`: batch/mixed の第 1 成分は `[0, 8)`。Dijkstra の重みは `[1, 3]`。
- `wide`: batch/mixed の第 1 成分は `[0, 2**90)`。
  Dijkstra の重みは `[1, 2**80]`。符号化すると多倍長整数になるケース。
- `ascending` / `descending`: random のタプルを辞書順に昇順 / 降順に並べた入力。
- 反復実行は、方式・入力条件ごとに別プロセスで 2 回ウォームアップ後、5 回の中央値。
- 初回実行は、計測するたびに新しいプロセスを起動し、最初の 1 回を測った 3 回の中央値。
- 各計測の結果を `heapq` と照合する。さらに計測後の別実行で、
  **すべての pop の値と順序**を照合する。Dijkstra は距離配列全体も照合する。
- 倍率は `heapq の時間 / 各方式の時間`。1 未満は遅くなったことを示す。
  同じ環境でも負荷や JIT の状態で変動する。

## PyPy の反復実行: n = 100,000

| 処理 / 入力 | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: |
| batch / random | 54.394 | 41.012 (1.33 倍) | 33.371 (1.63 倍) |
| batch / ties | 65.105 | 47.610 (1.37 倍) | 31.130 (2.09 倍) |
| batch / wide | 247.952 | 201.708 (1.23 倍) | 154.174 (1.61 倍) |
| mixed / random | 35.173 | 32.338 (1.09 倍) | 24.481 (1.44 倍) |
| mixed / ties | 46.990 | 42.219 (1.11 倍) | 23.264 (2.02 倍) |
| mixed / wide | 114.195 | 97.259 (1.17 倍) | 92.212 (1.24 倍) |
| dijkstra / random | 357.177 | 294.157 (1.21 倍) | 254.448 (1.40 倍) |
| dijkstra / ties | 217.232 | 204.291 (1.06 倍) | 173.054 (1.26 倍) |
| dijkstra / wide | 701.028 | 621.302 (1.13 倍) | 657.718 (1.07 倍) |

通常の整数を使う random / ties の 6 条件では、成分分離は 1.06〜1.37 倍、
整数符号化は 1.26〜2.09 倍だった。Dijkstra 全体でも改善したが、
ヒープ以外の処理も含まれるため、ヒープ操作だけの倍率とは異なる。

## PyPy の初回実行: n = 100,000

| 処理 / 入力 | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: |
| batch / random | 50.129 | 46.155 (1.09 倍) | 39.031 (1.28 倍) |
| batch / ties | 68.164 | 53.570 (1.27 倍) | 36.047 (1.89 倍) |
| batch / wide | 137.114 | 126.900 (1.08 倍) | 101.994 (1.34 倍) |
| mixed / random | 57.687 | 53.053 (1.09 倍) | 51.221 (1.13 倍) |
| mixed / ties | 176.629 | 140.236 (1.26 倍) | 80.549 (2.19 倍) |
| mixed / wide | 176.123 | 164.666 (1.07 倍) | 191.071 (0.92 倍) |
| dijkstra / random | 527.917 | 453.845 (1.16 倍) | 453.959 (1.16 倍) |
| dijkstra / ties | 398.703 | 346.023 (1.15 倍) | 248.790 (1.60 倍) |
| dijkstra / wide | 1392.745 | 1041.428 (1.34 倍) | 1212.953 (1.15 倍) |

反復実行だけを見て提出コードの速度を予測しないこと。
例えば wide の mixed では整数符号化が遅くなる結果も得られた。
多倍長整数の処理と JIT の負担を含め、用途ごとに確認する必要がある。

## 小さい入力: PyPy の batch / random

| 実行 | n | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: | ---: |
| 初回 | 1,000 | 5.835 | 6.252 (0.93 倍) | 6.386 (0.91 倍) |
| 初回 | 10,000 | 17.128 | 18.282 (0.94 倍) | 18.163 (0.94 倍) |
| 反復 | 1,000 | 0.264 | 0.404 (0.65 倍) | 0.295 (0.89 倍) |
| 反復 | 10,000 | 1.984 | 2.855 (0.70 倍) | 1.806 (1.10 倍) |

## 整列済み入力: PyPy の反復実行、n = 100,000

| 処理 / 入力 | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: |
| batch / ascending | 18.117 | 16.853 (1.07 倍) | 11.718 (1.55 倍) |
| batch / descending | 19.875 | 18.620 (1.07 倍) | 14.685 (1.35 倍) |
| mixed / ascending | 15.171 | 14.432 (1.05 倍) | 11.333 (1.34 倍) |
| mixed / descending | 14.368 | 15.584 (0.92 倍) | 11.226 (1.28 倍) |

## CPython の反復実行: n = 100,000、random

| 処理 / 入力 | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: |
| batch / random | 103.207 | 181.773 (0.57 倍) | 57.893 (1.78 倍) |
| mixed / random | 49.501 | 166.178 (0.30 倍) | 46.118 (1.07 倍) |
| dijkstra / random | 530.255 | 695.466 (0.76 倍) | 412.827 (1.28 倍) |

この環境の CPython では成分分離型の自作ヒープは全 3 条件で遅くなった。
整数符号化は 1.07〜1.78 倍で、batch と Dijkstra では改善が見られた。

## 選び方

- 整数 2 個で第 2 成分の範囲が決まっているなら、今回の結果では `PackedTupleHeap` が第一候補。
  例えば `(距離, 頂点番号)` に適用できる。`bits` は必要な幅を指定する。
- PyPy で負の第 2 成分や浮動小数点数もそのまま扱いたいなら `TupleHeap` を候補にする。
  速度改善の実測は主に整数入力に対するもので、他の型の改善は保証しない。
- 少量の入力や CPython の自作ループでは、普通の `heapq` が速い場合がある。
  初回実行も比較して選ぶ。

全測定値は [TupleHeap.benchmark.json](TupleHeap.benchmark.json) に保存した。
表は条件ごとに 5 回（初回は 3 回）測った中央値。

## 再現と検証

標準ライブラリ以外の依存は不要。リポジトリ直下で実行する。

```bash
# PyPy の反復実行、10 万要素 / 10 万頂点
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --output /tmp/tuple-heap-pypy-warm.json

# PyPy の初回実行
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --fresh-process --repeat 3 --output /tmp/tuple-heap-pypy-fresh.json

# 小さい入力・整列済み入力・CPython も同じスクリプトで測定可能
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --sizes 1000 10000 --cases random --workloads batch
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --cases ascending descending --workloads batch mixed
taskset -c 2 python3 -B tests/data_structure/benchmark_tuple_heap.py --cases random

python3 -B -m unittest discover -s tests/data_structure -p 'test_tuple_heap.py' -v
pypy3 -B -m unittest discover -s tests/data_structure -p 'test_tuple_heap.py' -v
python3 -B library-checker-submitcode/generate.py --check
```

テストでは短い列の全列挙、ランダム操作列、同順位での第 2 成分の比較、
初期化・空・1 要素・二分木の境界、巨大な正負の整数、浮動小数点数、文字列、
`replace` / `pushpop`、符号化のビット境界、入力検証と入力リストの独立性を確認する。
