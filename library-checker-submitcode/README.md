# Library Checker 提出コード

`src/` の問題ごとのコードに、`template.py` と `# include:` で指定した
ライブラリの最新の内容を埋め込み、単独で提出できる Python ファイルを生成します。

```bash
python3 library-checker-submitcode/generate.py
```

たとえば `src/graph/unionfind.py` から `graph/unionfind.py` と
`../tests/library_checker/official/graph/unionfind.test.py` を生成します。
検証用ファイルは提出コードの先頭に `verification-helper: PROBLEM` を付けたものです。
生成されたファイルを Library Checker に提出してください。
提出コードを直す場合は `src/`、ライブラリを直す場合は
`algorithm_library/python/` を編集します。

## 自動更新

リポジトリの pre-commit フックで、コミット前に自動生成します。
ライブラリやテンプレートの変更も反映されます。生成ファイルが変更された場合は
コミットが一度止まるので、そのファイルも `git add` して再度コミットしてください。

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
指定したファイルをそのまま埋め込むので、その中のローカルライブラリへの
import は自動展開されません。必要なファイルはそれぞれ明示してください。

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

22 個のライブラリを、21 問・25 本の提出コードで確認できます。
同じ問題に複数の実装を用意しているものもあります。

| ライブラリ | 提出コード | Library Checker 問題 |
| --- | --- | --- |
| `graph/UnionFind.py` | [graph/unionfind.py](graph/unionfind.py) | [Unionfind](https://judge.yosupo.jp/problem/unionfind) |
| `graph/PotentialUnionFind.py` | [graph/unionfind_with_potential.py](graph/unionfind_with_potential.py) | [Unionfind with Potential](https://judge.yosupo.jp/problem/unionfind_with_potential) |
| `graph/SCC.py` | [graph/scc.py](graph/scc.py) | [Strongly Connected Components](https://judge.yosupo.jp/problem/scc) |
| `graph/LCA.py` | [graph/lca.py](graph/lca.py) | [Lowest Common Ancestor](https://judge.yosupo.jp/problem/lca) |
| `graph/EulerTour.py` | [graph/lca_euler_tour.py](graph/lca_euler_tour.py) | [Lowest Common Ancestor](https://judge.yosupo.jp/problem/lca) |
| `graph/LCA.py` + `techniques/Doubling.py` | [graph/jump_on_tree.py](graph/jump_on_tree.py) | [Jump on Tree](https://judge.yosupo.jp/problem/jump_on_tree) |
| `graph/maxflow.py` | [graph/bipartitematching.py](graph/bipartitematching.py) | [Bipartite Matching](https://judge.yosupo.jp/problem/bipartitematching) |
| `data-structure/BIT.py` | [data_structure/point_add_range_sum_bit.py](data_structure/point_add_range_sum_bit.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) |
| `data-structure/Segtree.py` | [data_structure/point_add_range_sum_segtree.py](data_structure/point_add_range_sum_segtree.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) |
| `data-structure/Segtree.py` | [data_structure/point_set_range_composite.py](data_structure/point_set_range_composite.py) | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) |
| `data-structure/TupleSegtree.py` | [data_structure/point_set_range_composite_tuple.py](data_structure/point_set_range_composite_tuple.py) | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) |
| `data-structure/SparseTable.py` | [data_structure/staticrmq.py](data_structure/staticrmq.py) | [Static RMQ](https://judge.yosupo.jp/problem/staticrmq) |
| `data-structure/DisjointSparseTable.py` | [data_structure/static_range_sum.py](data_structure/static_range_sum.py) | [Static Range Sum](https://judge.yosupo.jp/problem/static_range_sum) |
| `data-structure/MargeSortTree.py` | [data_structure/static_range_frequency.py](data_structure/static_range_frequency.py) | [Static Range Frequency](https://judge.yosupo.jp/problem/static_range_frequency) |
| `data-structure/CartesianTree.py` | [data_structure/cartesian_tree.py](data_structure/cartesian_tree.py) | [Cartesian Tree](https://judge.yosupo.jp/problem/cartesian_tree) |
| `data-structure/LazySegtree.py` | [data_structure/range_affine_range_sum.py](data_structure/range_affine_range_sum.py) | [Range Affine Range Sum](https://judge.yosupo.jp/problem/range_affine_range_sum) |
| `data-structure/TupleLazySegtree.py` | [data_structure/range_affine_range_sum_tuple.py](data_structure/range_affine_range_sum_tuple.py) | [Range Affine Range Sum](https://judge.yosupo.jp/problem/range_affine_range_sum) |
| `string/SuffixArray.py` | [string/suffixarray.py](string/suffixarray.py) | [Suffix Array](https://judge.yosupo.jp/problem/suffixarray) |
| `string/SuffixArray.py` | [string/number_of_substrings.py](string/number_of_substrings.py) | [Number of Substrings](https://judge.yosupo.jp/problem/number_of_substrings) |
| `string/SuffixArray.py` | [string/longest_common_substring.py](string/longest_common_substring.py) | [Longest Common Substring](https://judge.yosupo.jp/problem/longest_common_substring) |
| `string/Z-algo.py` | [string/zalgorithm.py](string/zalgorithm.py) | [Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm) |
| `math/FFT.py` | [math/convolution_mod.py](math/convolution_mod.py) | [Convolution](https://judge.yosupo.jp/problem/convolution_mod) |
| `math/MatrixPower.py` | [math/matrix_product.py](math/matrix_product.py) | [Matrix Product](https://judge.yosupo.jp/problem/matrix_product) |
| `math/MatrixPower.py` | [math/pow_of_matrix.py](math/pow_of_matrix.py) | [Power of Matrix](https://judge.yosupo.jp/problem/pow_of_matrix) |
| `math/AngularSort.py` + `techniques/CmpSort.py` | [math/sort_points_by_argument.py](math/sort_points_by_argument.py) | [Sort Points by Argument](https://judge.yosupo.jp/problem/sort_points_by_argument) |

## ローカルでの確認

Python 3.11 と C++ コンパイラ、Git を用意し、リポジトリ直下で実行します。
`oj-verify` が Library Checker の公式ケースを生成して検証します。
答えが一意でない問題も、公式 checker で判定します。
依存パッケージは、Python の依存解析の修正を含む公式リポジトリの版を
コミット単位で固定しています。

```bash
python3 -m pip install -r library-checker-submitcode/requirements-verify.txt
python3 library-checker-submitcode/generate.py
oj-verify run tests/library_checker/official/graph/unionfind.test.py
```

全件を検証する場合は `oj-verify run` を実行します。検証済みのコードは、
変更がなければスキップされます。再実行したい場合はローカルの
`.verify-helper/timestamps.local.json` を削除してください。

CI も PR または main の対象コードを検証し、公式ケースと生成ツールをキャッシュします。
初回はケースの生成と全件の検証に時間がかかります。
ケースごとの制限時間は `oj-verify` の既定値の60秒です。
Library Checker 上への提出や AC の記録は行わず、公式サイトと同じ時間・メモリ制限での
通過を保証するものではありません。
