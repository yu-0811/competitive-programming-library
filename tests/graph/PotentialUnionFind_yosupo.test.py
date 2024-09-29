# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential

from algo_library.python.graph.PotentialUnionFind import PotentialUnionFind

import sys
def input():return sys.stdin.readline().rstrip()
mod = 998244353

N,Q = map(int,input().split())
uf = PotentialUnionFind(N)
for _ in range(Q):
  t,*P = map(int,input().split())
  if t==0:
    u,v,x = P
    res = uf.dist(v,u)
    if res!=uf.inf and res%mod!=x:
      print(0)
    else:
      print(1)
      uf.union(v,u,x)
  else:
    u,v = P
    res = uf.dist(v,u)
    if res!=uf.inf: print(res%mod)
    else: print(-1)