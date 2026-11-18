# 先頭 k 成分だけを比較するタプル最小ヒープ

`algorithm_library/python/data_structure/TupleHeap.py` の `TupleHeap(k=1, values=())`
は、タプルの先頭 k 成分だけを辞書順で比較する。
残りの成分はデータとして保持し、同じキーの要素同士でも比較しない。

```python
h = TupleHeap(1, [(0, start)])  # (距離, 頂点) を距離だけで比較
h.push((10, 3))
d, v = h.pop()
best = h.top()                 # 最小要素の参照
size = len(h)
while h:
    d, v = h.pop()

# 先頭2成分を比較し、その後ろには比較できないデータも載せられる
h = TupleHeap(2)
h.push((3, 1, {"vertex": 7}))
h.push((3, 1, {"vertex": 2}))
h.push((2, 5, {"vertex": 9}))
# 最初に (2, 5, {"vertex": 9}) が返る。同じキー (3, 1) の順序は不定。
```

タプルの長さは固定しなくてよい。全成分を比較する場合は、
そのタプルの長さを k に指定する。
`values` にはリストやイテレータを渡せる。元のリストは変更しない。
空の `pop()`・`top()` は `IndexError`。同じキーの取り出し順は保証しない。

## 実装と入力条件

タプル本体と比較キーを別々のリストに保存した二分ヒープ。
`k=1` は `x[0]` を直接比較し、1要素タプルの生成・比較を省く。
`k>1` は初期化・追加時に `x[:k]` を一度だけ作り、比較のたびには作らない。
要素の移動ではタプル全体への参照を移し、後続成分の数だけコピーすることはない。
`pop()`・`top()` は保存したタプルをそのまま返す。

写経用なので入力条件の検証は呼出側で行う。
`k >= 1`、各入力タプルの長さが k 以上であること。
キーの各成分には一貫した全順序が必要で、NaN は使わない。
負数・多倍長整数・浮動小数点数・文字列などを使えるが、
同じ位置のキー同士は比較できる型に揃える。
初期化後に `k` や内部リストを変更しないこと。
タプルの後続成分にある辞書などは変更できる。

成分の比較を O(1) とすると、初期化 O(nk)、push/pop は最悪 O(k log n)、
top・len は O(1)、比較キーの追加領域は O(nk)。
`k=1` なら初期化 O(n)、push/pop は O(log n)、追加領域 O(n)。

通常のタプル比較も、先頭成分で大小が決まればそこで終了する。
そのため、頂点番号の比較を省くだけで常に高速化するとは限らない。
この実装はキーの直接比較と、同値キー時に後続成分を比較しないことを目的とする。
速度はタプルの長さ、同値キーの多さ、ヒープのサイズ、PyPy の JIT に依存する。

## Library Checker での確認

提出用と検証用には、次の生成済みファイルを兼用する。

- [Shortest Path](../../../library-checker-submitcode/graph/shortest_path_tuple_heap.test.py):
  `(距離, 頂点)` を `k=1` で比較するダイクストラ。
- [Double-Ended Priority Queue](../../../library-checker-submitcode/data_structure/double_ended_priority_queue_tuple_heap.test.py):
  最小側は `k=1`、最大側は `divmod(-値, 2**16)` をキーとする `k=2`。
  辞書を末尾に載せ、同じキーでも辞書を比較せずに処理する。
  初期化、空からの追加、top、pop も使う。

リポジトリ直下で生成物を更新・確認し、Library Checker の公式ケースだけで検証する。
実行環境は PyPy を使う。

```bash
python3 library-checker-submitcode/generate.py
python3 library-checker-submitcode/generate.py --check
oj-verify run library-checker-submitcode/graph/shortest_path_tuple_heap.test.py
oj-verify run library-checker-submitcode/data_structure/double_ended_priority_queue_tuple_heap.test.py
```

## 整数タプルの全成分を比較する場合

既存の `PackedTupleHeap.py` は、整数タプルの全成分を1整数に符号化して
`heapq` で比較する。先頭 k 成分だけの比較には `TupleHeap` を使う。

```python
h = PackedTupleHeap(3, bits=(8, 12), values=[(-5, 255, 4095)])
h.push((0, 10, 20))
x = h.pop()
```

引数は `PackedTupleHeap(arity=2, bits=20, values=None)`。
先頭成分は負数も使え、後続成分 xi は `0 <= xi < 2**bi` が必要。
`bits` が整数なら後続の全成分に同じ幅を使い、列なら長さは arity−1 とする。
符号化・復元には各 O(arity) が必要で、整数のビット長にも演算コストが依存する。
