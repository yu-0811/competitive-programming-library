# 検証方針

- ライブラリの動作確認は、`library-checker-submitcode` の提出コードを使い、Library Checker の公式ケースだけで行う。
- `library-checker-submitcode/generate.py` が生成する `library-checker-submitcode/**/*.test.py` を提出用と検証用で兼用する。`tests` ディレクトリや重複する検証コードは作らない。
- 独自の単体テスト、乱数テスト、回帰テストなどの補助テストは不要。リポジトリに追加・保存しない。
- 実行時間の比較コード、ベンチマーク、一時的な調査用スクリプトやその出力は、`/tmp` などリポジトリ外の一時ディレクトリに置く。このリポジトリ内には残さない。
- ライブラリや提出コードを変更したら `python3 library-checker-submitcode/generate.py` で生成物を更新し、`python3 library-checker-submitcode/generate.py --check` で整合性を確認する。
