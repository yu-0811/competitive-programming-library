---
title: Simulated Annealing (焼きなまし法)
documentation_of: //heu_library/SA.cpp
---


高速化 tips
- sqrt をとらない
- pow は遅いからできれば前計算する
- 評価関数を工夫するといいときもある (ex. 誤差 -> 誤差^2)