# Library Checker 提出コード

`src/` の問題ごとのコードに、`template.py` と `# include:` で指定した
ライブラリの最新の内容を埋め込み、単独で提出できる Python ファイルを生成します。

```bash
python3 library-checker-submitcode/generate.py
```

たとえば `src/graph/unionfind.py` から `graph/unionfind.py` を生成します。
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
