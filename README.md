[![Actions Status](https://github.com/yu-0811/competitive-programming-library/workflows/verify/badge.svg)](https://github.com/yu-0811/competitive-programming-library/actions) 。  

[![GitHub Pages](https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github)](https://yu-0811.github.io/competitive-programming-library/)

## PythonライブラリのPDF生成

`algorithm_library/python` 以下の `.py` ファイル（`template.py` を除く）を、カテゴリ別目次・行番号付きのA4・2段組PDFにまとめます。`ICPCtemplate.py` は収録し、カテゴリは Templates、gen、残りのカテゴリの名前順で並べます。日本語コメントと長い行の折り返しに対応しています。

コードはカラーのシンタックスハイライト付きです。必要環境は Python 3、Pygments、LuaLaTeX、LuaTeX-ja、fvextra、IPAexフォントです。Ubuntu / Debianでは次のようにインストールできます。

```sh
sudo apt install python3-pygments texlive-luatex texlive-lang-japanese texlive-latex-extra fonts-ipaexfont
python3 tools/build_notebook.py
```

出力先は `algorithm_library/python/notebook.pdf` で、PDFもGit管理対象です。ローカルでPDFを更新する場合も上記のコマンドで再生成できます。別の場所に保存する場合は `--output /tmp/notebook.pdf` を指定してください。実行時の作業ディレクトリによらず、このリポジトリのコードを収録します。中間ファイルは一時ディレクトリに作成し、終了時に削除します。

`pre-commit install` でフックを有効にすると、Pythonコードまたは生成スクリプトの変更をコミットする際に、ローカルでPDFを自動再生成します。PDFが更新されてコミットが停止したら、`git add algorithm_library/python/notebook.pdf` して再度コミットしてください。生成日時を固定し、一時ディレクトリ名などで変動するPDFメタデータを抑制して、同じ環境・同じコードからの再生成で差分が出ないようにしています。
