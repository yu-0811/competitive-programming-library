# 単純連結無向グラフの生成（1-indexed）
from random import randint, shuffle

N = randint(3, 10)
V = list(range(1, N + 1))
shuffle(V)
M = []
for i in range(1, N):
    p = randint(0, i - 1)  # 前の頂点から必ず1つつなぐ
    for j in range(i):
        if j == p or randint(0, 1):
            M.append((V[j], V[i]))

print(N, len(M))
for e in M:
    print(*e)
