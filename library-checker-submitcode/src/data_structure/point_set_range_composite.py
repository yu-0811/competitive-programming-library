# problem: https://judge.yosupo.jp/problem/point_set_range_composite
# include: algorithm_library/python/data-structure/Segtree.py


def compose(left, right):
    a, b = left
    c, d = right
    return a * c % mod, (b * c + d) % mod


def main():
    N, Q = map(int, readline().split())
    functions = [tuple(map(int, readline().split())) for _ in range(N)]
    tree = segtree(functions, compose, (1, 0))
    ans = []
    for _ in range(Q):
        t, *values = map(int, readline().split())
        if t == 0:
            p, a, b = values
            tree.set(p, (a, b))
        else:
            l, r, x = values
            a, b = tree.prod(l, r) if l < r else (1, 0)
            ans.append(str((a * x + b) % mod))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
