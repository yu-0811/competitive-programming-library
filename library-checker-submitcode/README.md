# Library Checker 提出コード

`src/` の問題ごとのコードに、`template.py` と `# include:` で指定した
ライブラリの最新の内容を埋め込み、単独で提出できる Python ファイルを生成します。

```bash
python3 library-checker-submitcode/generate.py
```

たとえば `src/graph/unionfind.py` から `graph/unionfind.test.py` を生成します。
生成コードの先頭に `verification-helper: PROBLEM` を付け、提出用と検証用で兼用します。
生成されたファイルを Library Checker に提出してください。
提出コードを直す場合は `src/`、ライブラリを直す場合は
`algorithm_library/python/` を編集します。

## 自動更新

リポジトリの pre-commit フックで、コミット前に自動生成します。
ライブラリやテンプレートの変更も反映されます。更新した生成ファイルは
フック内で自動的にステージし、同じコミットに含めます。

新しい作業環境では、最初にフックを有効にします。

```bash
pre-commit install
```

CI でも以下を実行し、更新漏れがあれば失敗します。

```bash
python3 library-checker-submitcode/generate.py --check
```

## 問題の追加

`src/graph/xxx.py` などを作り、問題 URL と必要なライブラリを指定してから、
問題ごとの入出力コードを書きます。`# include:` のパスはリポジトリ直下からの
相対パスです。複数のライブラリが必要なら、必要な順序で複数行指定できます。
指定したファイル内の `from algorithm_library.python... import ...` も再帰的に
展開します。同じライブラリは一度だけ埋め込まれます。
内部ライブラリの import には絶対パスを使い、別名や `*` は使いません。

```python
# problem: https://judge.yosupo.jp/problem/unionfind
# include: algorithm_library/python/graph/UnionFind.py


def main():
    # template.py の readline なども利用可能
    ...


if __name__ == "__main__":
    main()
```

## 追加済みの提出コード

34 個のライブラリを、33 問・42 本の提出コードで確認できます。
同じ問題に複数の実装を用意しているものもあります。

| ライブラリ | 提出コード | Library Checker 問題 |
| --- | --- | --- |
| `graph/UnionFind.py` | [graph/unionfind.test.py](graph/unionfind.test.py) | [Unionfind](https://judge.yosupo.jp/problem/unionfind) |
| `graph/PotentialUnionFind.py` | [graph/unionfind_with_potential.test.py](graph/unionfind_with_potential.test.py) | [Unionfind with Potential](https://judge.yosupo.jp/problem/unionfind_with_potential) |
| `graph/SCC.py` | [graph/scc.test.py](graph/scc.test.py) | [Strongly Connected Components](https://judge.yosupo.jp/problem/scc) |
| `graph/LCA.py` | [graph/lca.test.py](graph/lca.test.py) | [Lowest Common Ancestor](https://judge.yosupo.jp/problem/lca) |
| `graph/EulerTour.py` | [graph/lca_euler_tour.test.py](graph/lca_euler_tour.test.py) | [Lowest Common Ancestor](https://judge.yosupo.jp/problem/lca) |
| `graph/EulerTour.py` | [graph/vertex_add_path_sum_euler_tour.test.py](graph/vertex_add_path_sum_euler_tour.test.py) | [Vertex Add Path Sum](https://judge.yosupo.jp/problem/vertex_add_path_sum) |
| `graph/LCA.py` + `techniques/Doubling.py` | [graph/jump_on_tree.test.py](graph/jump_on_tree.test.py) | [Jump on Tree](https://judge.yosupo.jp/problem/jump_on_tree) |
| `graph/VertexAddSubtreeSum.py` | [graph/vertex_add_subtree_sum.test.py](graph/vertex_add_subtree_sum.test.py) | [Vertex Add Subtree Sum](https://judge.yosupo.jp/problem/vertex_add_subtree_sum) |
| `graph/EulerTourOrder.py` + `data_structure/BIT.py` | [graph/vertex_add_subtree_sum_euler_tour.test.py](graph/vertex_add_subtree_sum_euler_tour.test.py) | [Vertex Add Subtree Sum](https://judge.yosupo.jp/problem/vertex_add_subtree_sum) |
| `graph/Rerooting.py` | [graph/tree_path_composite_sum.test.py](graph/tree_path_composite_sum.test.py) | [Tree Path Composite Sum](https://judge.yosupo.jp/problem/tree_path_composite_sum) |
| `graph/cycle_detect.py` | [graph/cycle_detection_undirected.test.py](graph/cycle_detection_undirected.test.py) | [Cycle Detection (Undirected)](https://judge.yosupo.jp/problem/cycle_detection_undirected) |
| `graph/maxflow.py` | [graph/bipartitematching.test.py](graph/bipartitematching.test.py) | [Bipartite Matching](https://judge.yosupo.jp/problem/bipartitematching) |
| `data_structure/BIT.py` | [data_structure/point_add_range_sum_bit.test.py](data_structure/point_add_range_sum_bit.test.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) |
| `data_structure/BIT.py` | [data_structure/predecessor_problem_bit.test.py](data_structure/predecessor_problem_bit.test.py) | [Predecessor Problem](https://judge.yosupo.jp/problem/predecessor_problem) |
| `data_structure/BucketList.py` | [data_structure/deque_bucket_list.test.py](data_structure/deque_bucket_list.test.py) | [Deque](https://judge.yosupo.jp/problem/deque) |
| `data_structure/SortedSet.py` | [data_structure/ordered_set.test.py](data_structure/ordered_set.test.py) | [Ordered Set](https://judge.yosupo.jp/problem/ordered_set) |
| `data_structure/SortedMultiset.py` | [data_structure/ordered_set_multiset.test.py](data_structure/ordered_set_multiset.test.py) | [Ordered Set](https://judge.yosupo.jp/problem/ordered_set) |
| `data_structure/SortedMultiset.py` | [data_structure/double_ended_priority_queue_multiset.test.py](data_structure/double_ended_priority_queue_multiset.test.py) | [Double-Ended Priority Queue](https://judge.yosupo.jp/problem/double_ended_priority_queue) |
| `data_structure/Segtree.py` | [data_structure/point_add_range_sum_segtree.test.py](data_structure/point_add_range_sum_segtree.test.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) |
| `data_structure/Segtree.py` | [data_structure/point_set_range_composite.test.py](data_structure/point_set_range_composite.test.py) | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) |
| `data_structure/Segtree.py`（左右の境界探索） | [data_structure/predecessor_problem_segtree.test.py](data_structure/predecessor_problem_segtree.test.py) | [Predecessor Problem](https://judge.yosupo.jp/problem/predecessor_problem) |
| `data_structure/TupleSegtree.py` | [data_structure/point_set_range_composite_tuple.test.py](data_structure/point_set_range_composite_tuple.test.py) | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) |
| `data_structure/SparseTable.py` | [data_structure/staticrmq.test.py](data_structure/staticrmq.test.py) | [Static RMQ](https://judge.yosupo.jp/problem/staticrmq) |
| `data_structure/DisjointSparseTable.py` | [data_structure/static_range_sum.test.py](data_structure/static_range_sum.test.py) | [Static Range Sum](https://judge.yosupo.jp/problem/static_range_sum) |
| `data_structure/MargeSortTree.py` | [data_structure/static_range_frequency.test.py](data_structure/static_range_frequency.test.py) | [Static Range Frequency](https://judge.yosupo.jp/problem/static_range_frequency) |
| `data_structure/CartesianTree.py` | [data_structure/cartesian_tree.test.py](data_structure/cartesian_tree.test.py) | [Cartesian Tree](https://judge.yosupo.jp/problem/cartesian_tree) |
| `data_structure/LazySegtree.py` | [data_structure/range_affine_range_sum.test.py](data_structure/range_affine_range_sum.test.py) | [Range Affine Range Sum](https://judge.yosupo.jp/problem/range_affine_range_sum) |
| `data_structure/TupleLazySegtree.py` | [data_structure/range_affine_range_sum_tuple.test.py](data_structure/range_affine_range_sum_tuple.test.py) | [Range Affine Range Sum](https://judge.yosupo.jp/problem/range_affine_range_sum) |
| `string/SuffixArray.py` | [string/suffixarray.test.py](string/suffixarray.test.py) | [Suffix Array](https://judge.yosupo.jp/problem/suffixarray) |
| `string/SuffixArray.py` | [string/number_of_substrings.test.py](string/number_of_substrings.test.py) | [Number of Substrings](https://judge.yosupo.jp/problem/number_of_substrings) |
| `string/SuffixArray.py` | [string/longest_common_substring.test.py](string/longest_common_substring.test.py) | [Longest Common Substring](https://judge.yosupo.jp/problem/longest_common_substring) |
| `string/RollingHash.py`（クラス版） | [string/longest_common_substring_rollinghash.test.py](string/longest_common_substring_rollinghash.test.py) | [Longest Common Substring](https://judge.yosupo.jp/problem/longest_common_substring) |
| `string/Z_algo.py` | [string/zalgorithm.test.py](string/zalgorithm.test.py) | [Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm) |
| `math/FFT.py` | [math/convolution_mod.test.py](math/convolution_mod.test.py) | [Convolution](https://judge.yosupo.jp/problem/convolution_mod) |
| `math/MatrixPower.py` | [math/matrix_product.test.py](math/matrix_product.test.py) | [Matrix Product](https://judge.yosupo.jp/problem/matrix_product) |
| `math/MatrixPower.py` | [math/pow_of_matrix.test.py](math/pow_of_matrix.test.py) | [Power of Matrix](https://judge.yosupo.jp/problem/pow_of_matrix) |
| `math/MatrixPower.py`（`vec_mul`） | [math/pow_of_matrix_vec.test.py](math/pow_of_matrix_vec.test.py) | [Power of Matrix](https://judge.yosupo.jp/problem/pow_of_matrix) |
| `math/mobius.py` | [math/bitwise_and_convolution.test.py](math/bitwise_and_convolution.test.py) | [Bitwise And Convolution](https://judge.yosupo.jp/problem/bitwise_and_convolution) |
| `math/factorization.py`（素数列挙） | [math/enumerate_primes.test.py](math/enumerate_primes.test.py) | [Enumerate Primes](https://judge.yosupo.jp/problem/enumerate_primes) |
| `math/AngularSort.py` + `techniques/CmpSort.py` | [math/sort_points_by_argument.test.py](math/sort_points_by_argument.test.py) | [Sort Points by Argument](https://judge.yosupo.jp/problem/sort_points_by_argument) |
| `techniques/2-SAT.py` | [techniques/two_sat.test.py](techniques/two_sat.test.py) | [2 Sat](https://judge.yosupo.jp/problem/two_sat) |
| `techniques/Compression.py` + `data_structure/BIT.py`（Mo テンプレートの具体化） | [techniques/static_range_inversions_query.test.py](techniques/static_range_inversions_query.test.py) | [Static Range Inversions Query](https://judge.yosupo.jp/problem/static_range_inversions_query) |

## ローカルでの確認

Python 3.11 と C++ コンパイラ、Git を用意し、リポジトリ直下で実行します。
`oj-verify` が Library Checker の公式ケースを生成して検証します。
答えが一意でない問題も、公式 checker で判定します。
依存パッケージは、Python の依存解析の修正を含む公式リポジトリの版を
コミット単位で固定しています。

```bash
python3 -m pip install -r library-checker-submitcode/requirements-verify.txt
python3 library-checker-submitcode/generate.py
oj-verify run library-checker-submitcode/graph/unionfind.test.py
```

全件を検証する場合は `oj-verify run` を実行します。検証済みのコードは、
変更がなければスキップされます。再実行したい場合はローカルの
`.verify-helper/timestamps.local.json` を削除してください。

CI も PR または main の対象コードを検証し、公式ケースと生成ツールをキャッシュします。
初回はケースの生成と全件の検証に時間がかかります。
ケースごとの制限時間は `oj-verify` の既定値の60秒です。
Library Checker 上への提出や AC の記録は行わず、公式サイトと同じ時間・メモリ制限での
通過を保証するものではありません。
