import sys;
def input():return sys.stdin.readline().rstrip()

# 入力など
def ii(): return int(input())
def ms(): return map(int, input().split())
def li(): return list(map(int,input().split()))
inf = pow(10,18)
mod = 998244353

# ライブラリ系
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**9)
from collections import defaultdict,deque
from itertools import combinations,permutations,accumulate,product
from bisect import bisect_left,bisect_right
from heapq import heappop,heappush,heapify
