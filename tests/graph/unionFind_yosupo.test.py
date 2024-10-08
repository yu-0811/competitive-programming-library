# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
import sys
input = sys.stdin.buffer.readline

from algo_library.python.graph.unionFind import UnionFind


def main() -> None:
    N, Q = map(int, input().split())
    uft = UnionFind(N)
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t == 0:
            uft.union(u, v)
        else:
            print(int(uft.isSame(u, v)))


if __name__ == "__main__":
    main()