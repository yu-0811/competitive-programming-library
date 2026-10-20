# problem: https://judge.yosupo.jp/problem/range_affine_range_sum
# include: algorithm_library/python/data-structure/LazySegtree.py


def combine(left, right):
    return (left[0] + right[0]) % mod, left[1] + right[1]


def mapping(f, value):
    a, b = f
    total, length = value
    return (a * total + b * length) % mod, length


def composition(f, g):
    a, b = f
    c, d = g
    return a * c % mod, (a * d + b) % mod


def main():
    N, Q = map(int, readline().split())
    values = [(a, 1) for a in map(int, readline().split())]
    tree = lazy_segtree(values, combine, (0, 0), mapping, composition, (1, 0))
    ans = []
    for _ in range(Q):
        t, l, r, *rest = map(int, readline().split())
        if t == 0:
            tree.apply(l, r, tuple(rest))
        else:
            ans.append(str(tree.prod(l, r)[0]))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
