# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
def input():return sys.stdin.readline().rstrip()
def ii(): return int(input())
def ms(): return map(int, input().split())
def li(): return list(map(int,input().split()))
#/////////////////////////////////

from algo_library.python.graph.scc import SCC

N,M = ms()
scc = SCC(N)
for _ in range(M):
  a,b = ms()
  scc.addEdge(a,b)

groups = scc.doSCC()
print(len(groups))
for ans in groups:
  print(len(ans),*ans)