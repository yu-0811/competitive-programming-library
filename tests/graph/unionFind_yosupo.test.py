# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
import sys
input = sys.stdin.buffer.readline

from algorithm_library.python.graph.UnionFind import UnionFind

def main() -> None:
    N, Q = map(int, input().split())
    uft = UnionFind(N + 1)
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t == 0:
            uft.union(u, v)
        else:
            print(int(uft.isSame(u, v)))


if __name__ == "__main__":
    main()