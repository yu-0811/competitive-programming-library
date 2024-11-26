[![Actions Status](https://github.com/yu-0811/competitive-programming-library/workflows/verify/badge.svg)](https://github.com/yu-0811/competitive-programming-library/actions) 

競技プログラミングのライブラリです。   
詳しくは以下のページを見てください。  

[![GitHub Pages](https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github)](https://yu-0811.github.io/competitive-programming-library/) 

利用範囲に制限はありませんが、なにか不利益を被っても責任は負いません。  
もし、バグっているなど問題点があれば issue を立てていただけると助かります。

実行環境は、AtCoder や codeforces での pypy を想定しています。  

### コードの書き方のポイント
実行速度やタイプ数削減を最優先しているため、可読性が低い場合があります。

* リスト内包表記や for 文の内包表記を使った高速化
* max(), min() を使わず if 文を使った高速化
* pypy の再帰は遅いので非再帰で書いて高速化
* タプルや多次元配列をできるだけ避けて高速化
