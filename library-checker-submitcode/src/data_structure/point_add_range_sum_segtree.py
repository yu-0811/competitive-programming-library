# problem: https://judge.yosupo.jp/problem/point_add_range_sum
# include: algorithm_library/python/data-structure/Segtree.py


def main():
    N, Q = map(int, readline().split())
    tree = segtree(list(map(int, readline().split())), lambda a, b: a + b, 0)
    ans = []
    for _ in range(Q):
        t, x, y = map(int, readline().split())
        if t == 0:
            tree.add(x, y)
        else:
            ans.append(str(tree.prod(x, y) if x < y else 0))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
