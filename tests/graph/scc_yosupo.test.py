# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
input = sys.stdin.buffer.readline

from algorithm_library.python.graph.SCC import SCC

N,M = map(int,input().split())
scc = SCC(N)
for _ in range(M):
  a,b = map(int,input().split())
  scc.addEdge(a,b)

groups = scc.build_scc()
print(len(groups))
for ans in groups:
  print(len(ans),*ans)