from collections import defaultdict
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, math.isqrt(n) + 1))

"""
高速素因数分解 https://atcoder.jp/contests/abc177/editorial/82
素因数分解をしたい最大の数を N として
構築 O(N log log N)
素因数分解 O(log N)
init_factorization の引数に最大の数 N を入れて初期化
"""


def init_factorization(N: int) -> list[int]:
    # N 以下の整数に対して最小の素因数を求める
    # D[i] = i の最小の素因数
    D = list(range(N + 1))
    for i in range(2, isqrt(N) + 1):
        if D[i] == i:
            for j in range(i * i, N + 1, i):
                if D[j] == j:
                    D[j] = i
    return D


D = []  # 使用前に D = init_factorization(N) で初期化する


# 素因数分解
def factorization(x: int) -> dict[int, int]:
    res = defaultdict(int)
    while x != 1:
        res[D[x]] += 1
        x //= D[x]
    return res


# エラトステネスの篩
# O (N log log N)
def eratosthenes(N: int):
    # 素数
    isprime = bytearray(b"\1") * (N + 1)  # isprime[i]==True なら i は素数
    isprime[:2] = bytes(min(2, N + 1))
    for p in range(2, isqrt(N) + 1):
        if isprime[p]:
            isprime[p * p::p] = bytes((N - p * p) // p + 1)
    return [p for p in range(2, N + 1) if isprime[p]], [bool(x) for x in isprime]


# M 以下の素数リストを返す
# O(M log log M)
def res_primeList(M):
    if M < 2:
        return []
    s = bytearray(b"\1") * ((M + 1) // 2)  # s[k] は奇数 2*k+1 のフラグ
    for i in range(3, isqrt(M) + 1, 2):
        if s[i // 2]:
            j = i * i // 2
            s[j::i] = bytes((len(s) - 1 - j) // i + 1)
    res = [i for i in range(1, M + 1, 2) if s[i // 2]]
    res[0] = 2
    return res
