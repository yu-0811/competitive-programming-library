# problem: https://judge.yosupo.jp/problem/predecessor_problem
# include: algorithm_library/python/data_structure/Segtree.py


def is_zero(x):
    return x == 0


def main():
    N, Q = map(int, readline().split())
    tree = segtree([c - 48 for c in readline().strip()], lambda a, b: a + b, 0)
    ans = []
    for _ in range(Q):
        t, k = map(int, readline().split())
        if t < 2:
            tree.set(k, 1 - t)
        elif t == 2:
            ans.append(str(tree.get(k)))
        elif t == 3:
            x = tree.max_right(k, is_zero)
            ans.append(str(x if x < N else -1))
        else:
            ans.append(str(tree.min_left(k + 1, is_zero) - 1))
    sys.stdout.write("\n".join(ans) + ("\n" if ans else ""))


if __name__ == "__main__":
    main()
