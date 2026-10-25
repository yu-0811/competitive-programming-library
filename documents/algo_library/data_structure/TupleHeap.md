# 写経用のタプル最小ヒープ

必要な方のクラスだけをコピーして使う。要素数 k は 1 以上の任意の整数。
どちらも全成分を辞書順で比較する。

| ファイル | 本体の長さ（冒頭の使い方コメントを除く） | 方式 |
| --- | ---: | --- |
| `algorithm_library/python/data-structure/TupleHeap.py` | 54 行・1,229 字 | 成分を別々のリストに保存する自作二分ヒープ |
| `algorithm_library/python/data-structure/PackedTupleHeap.py` | 39 行・916 字 | 整数タプルを 1 整数に符号化して `heapq` を使う |

## 使い方

```python
h = TupleHeap(3)
h.push((1, 8, 4))
h.push((1, 8, 2))
assert h.top() == (1, 8, 2)
assert h.pop() == (1, 8, 2)
assert len(h) == 1
while h:
    x = h.pop()

# 初期値がある場合
h = TupleHeap(3, [(2, 5, 9), (1, 8, 4)])

# 整数符号化版も同じ基本操作
h = PackedTupleHeap(3, bits=20)
h.push((-5, 10, 20))
assert h.pop() == (-5, 10, 20)

# 第 2 成分が 8 bit、第 3 成分が 12 bit の場合
h = PackedTupleHeap(3, bits=(8, 12), values=[(-5, 255, 4095)])
assert h.pop() == (-5, 255, 4095)
```

API は初期化・`push`・`pop`・`top`・`len`。空の `pop`・`top` は `IndexError`。
引数は `TupleHeap(arity=2, values=())`、
`PackedTupleHeap(arity=2, bits=20, values=None)` の順。
初期値にはリストやイテレータを渡せる。入力リストは変更しない。

## 入力条件と計算量

写経用なので入力条件の検証は呼出側で行う。
`arity >= 1`、すべての入力タプルの長さが `arity` であること。

`TupleHeap` は各成分に一貫した全順序があれば使える。
負数・多倍長整数・浮動小数点数・文字列などを扱える。NaN は使わない。
`_lt` で先頭から順に成分を比較し、`_swap` で全成分を交換する。
成分の比較を O(1) とすると、初期化 O(kn)、push/pop は最悪 O(k log n)、
top は O(k)、len は O(1)、使用領域は O(kn)。

`PackedTupleHeap` は整数専用。先頭は負数も利用可能。
後続成分 xi は `0 <= xi < 2**bi` を満たす必要がある。
`bits` が整数なら後続の全成分に同じ幅を使い、列なら長さは k−1 とする。
幅 0 の成分には 0 だけを渡す。
先頭から `v = (v << bi) | xi` で符号化し、末尾からマスクと右シフトで復元する。
符号化・復元に各 O(k) が必要で、その上で通常の `heapq` の操作を行う。
多倍長整数の比較・演算コストは整数のビット長にも依存する。

## 短い版の測定

- 測定日: 2026-10-25。AMD Ryzen AI 7 350、Linux / WSL2 x86_64。
- PyPy 7.3.20 / Python 3.11.13、および CPython 3.14.4。
- CPU を `taskset -c 2` で固定。方式ごとに別プロセスを使用。
- ランダムな 100,000 タプルをすべて push してからすべて pop。
  先頭は `[0, 10**9)`、後続成分は各 `[0, 100000)`、seed は 20261025。
- 2 回ウォームアップ後に 5 回測った中央値。整数符号化は `bits=20`。
- 入力生成・読込・プロセス起動・明示的な GC・結果検証は計測外。
  ヒープ操作・符号化・復元・取り出した全成分の和の計算・自動 GC は含む。
- 全 pop の値と順序を `heapq` と照合。
- 倍率は `heapq の時間 / 各方式の時間`。1 未満は遅くなったことを示す。
  負荷や JIT の状態によって結果は変動する。

| 環境 / 要素数 | heapq (ms) | 成分分離 (ms・倍率) | 整数符号化 (ms・倍率) |
| --- | ---: | ---: | ---: |
| PyPy / 3 | 319.837 | 176.785 (1.81 倍) | 151.068 (2.12 倍) |
| PyPy / 8 | 320.696 | 230.558 (1.39 倍) | 202.701 (1.58 倍) |
| CPython / 3 | 236.899 | 793.433 (0.30 倍) | 179.529 (1.32 倍) |

今回の PyPy の測定では両方式で改善した。CPython では成分分離型が遅くなった。
入力条件に合うなら、整数符号化版は写経量が少なく、今回の 3 条件では最も速かった。

現在の測定値は [TupleHeap.variable-arity.benchmark.json](TupleHeap.variable-arity.benchmark.json)。
以前の 2 要素専用版の記録は [TupleHeap.benchmark.json](TupleHeap.benchmark.json) に残している。
実装とチェックサム処理が異なるため、以前の数値と直接比較しないこと。

## 再現と検証

標準ライブラリ以外の依存は不要。リポジトリ直下で実行する。

```bash
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --arity 3 --workloads batch --cases random
taskset -c 2 pypy3 -B tests/data_structure/benchmark_tuple_heap.py --arity 8 --workloads batch --cases random
taskset -c 2 python3 -B tests/data_structure/benchmark_tuple_heap.py --arity 3 --workloads batch --cases random

python3 -B -m unittest discover -s tests/data_structure -p 'test_tuple_heap.py' -v
pypy3 -B -m unittest discover -s tests/data_structure -p 'test_tuple_heap.py' -v
```

`--arity`、`--sizes`、`--cases`、`--workloads`、`--bits`、`--repeat`、
`--warmup`、`--fresh-process`、`--output` で条件を変更できる。
`dijkstra` は `(距離, 頂点番号)` を使うため 2 要素専用。
それ以外の要素数では、既定の workload は `batch` と `mixed`。

テストでは 1〜19・32・1000 要素、長い共通接頭辞、ランダムな push/pop、
初期化・空・1 要素・木の境界、浮動小数点数・文字列・巨大な正負の整数、
成分ごとに異なるビット幅、入力リストの独立性を確認する。
