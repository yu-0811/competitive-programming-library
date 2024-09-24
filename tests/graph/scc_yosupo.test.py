# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
input = sys.stdin.buffer.readline

from algo_library.python.graph.scc import SCC

N,M = map(int,input().split())
scc = SCC(N)
for _ in range(M):
  a,b = map(int,input().split())
  scc.addEdge(a,b)

groups = scc.doSCC()
print(len(groups))
for ans in groups:
  print(len(ans),*ans)