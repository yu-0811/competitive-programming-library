import random
import runpy
import unittest
from pathlib import Path


LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/data-structure"
)
TupleLazySegtree = runpy.run_path(str(LIBRARY / "TupleLazySegtree.py"))[
    "TupleLazySegtree"
]


def affine_tree(values, mod=None):
    def normalize(x):
        return x if mod is None else x % mod

    def op(x, y):
        return normalize(x[0] + y[0]), x[1] + y[1]

    def mp(f, x):
        return normalize(f[0] * x[0] + f[1] * x[1]), x[1]

    def comp(f, g):
        return normalize(f[0] * g[0]), normalize(f[0] * g[1] + f[1])

    return TupleLazySegtree(
        v=[(normalize(x), 1) for x in values],
        op=op,
        e=(0, 0),
        mp=mp,
        comp=comp,
        ide=(1, 0),
    )


class TupleLazySegtreeTests(unittest.TestCase):
    def test_random_affine_updates_sets_and_queries(self):
        rng = random.Random(20261020)
        for mod in [1, 97, 998244353]:
            for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33]:
                values = [rng.randrange(mod) for _ in range(n)]
                tree = affine_tree(values, mod)
                for _ in range(160):
                    kind = rng.randrange(5)
                    left = rng.randrange(n + 1)
                    right = rng.randrange(left, n + 1)
                    if kind == 0:
                        b, c = rng.randrange(-100, 101), rng.randrange(-100, 101)
                        tree.apply(left, right, (b, c))
                        for i in range(left, right):
                            values[i] = (b * values[i] + c) % mod
                    elif kind == 1 and n:
                        p = rng.randrange(n)
                        x = rng.randrange(-100, 101) % mod
                        tree.set(p, (x, 1))
                        values[p] = x
                    elif kind == 2 and n:
                        p = rng.randrange(n)
                        b, c = rng.randrange(-100, 101), rng.randrange(-100, 101)
                        tree.apply_point(p, (b, c))
                        values[p] = (b * values[p] + c) % mod
                    elif kind == 3 and n:
                        p = rng.randrange(n)
                        self.assertEqual(tree.get(p), (values[p], 1))
                    self.assertEqual(tree.all_prod(), (sum(values) % mod, n))
                    self.assertEqual(
                        tree.prod(left, right),
                        (sum(values[left:right]) % mod, right - left),
                    )
                self.assertEqual(str(tree), str([(x, 1) for x in values]))

    def test_composition_order_and_stale_tags(self):
        values = list(range(16))
        tree = affine_tree(values)
        for left, right, b, c in [
            (0, 16, 2, 1),
            (0, 16, 3, 4),
            (0, 8, 0, -7),
            (4, 12, -2, 5),
            (0, 16, 1, 0),
            (0, 16, 5, 2),
        ]:
            tree.apply(left, right, (b, c))
            for i in range(left, right):
                values[i] = b * values[i] + c
            for p in [0, 7, 8, 15]:
                self.assertEqual(tree.get(p), (values[p], 1))
        tree.set(3, (10**100, 1))
        values[3] = 10**100
        tree.apply(0, 16, (-1, 10**90))
        values = [-x + 10**90 for x in values]
        for left in range(17):
            for right in range(left, 17):
                self.assertEqual(
                    tree.prod(left, right),
                    (sum(values[left:right]), right - left),
                )

    def test_different_arities_and_float_components(self):
        rng = random.Random(317)
        for arity in [2]:
            n = 17
            values = [
                tuple(
                    rng.randrange(-20, 21) * (0.5 if j == 1 else 1)
                    for j in range(arity)
                )
                for _ in range(n)
            ]
            zero = tuple(0.0 if j == 1 else 0 for j in range(arity))

            def op(x, y):
                return tuple(a + b for a, b in zip(x, y))

            def mp(f, x):
                return tuple(x[j] + f[j] * x[-1] for j in range(arity)) + (x[-1],)

            tree = TupleLazySegtree(
                [x + (1,) for x in values], op, zero + (0,), mp, op, zero
            )
            for _ in range(100):
                left = rng.randrange(n + 1)
                right = rng.randrange(left, n + 1)
                tag = tuple(
                    rng.randrange(-5, 6) * (0.5 if j == 1 else 1) for j in range(arity)
                )
                tree.apply(left, right, tag)
                for i in range(left, right):
                    values[i] = tuple(values[i][j] + tag[j] for j in range(arity))
                left = rng.randrange(n + 1)
                right = rng.randrange(left, n + 1)
                expected = tuple(
                    sum(x[j] for x in values[left:right]) for j in range(arity)
                ) + (right - left,)
                self.assertEqual(tree.prod(left, right), expected)

    def test_noncommutative_products_and_searches(self):
        values = list("abcdefghi")

        def op(x, y):
            return x[0] + y[0], x[1] + y[1]

        def mp(f, x):
            return x if f[0] is None else (f[0] * x[1], x[1])

        tree = TupleLazySegtree(
            [(x, 1) for x in values],
            op,
            ("", 0),
            mp,
            lambda f, g: g if f[0] is None else f,
            (None, 0),
        )
        for left, right, letter in [(0, 7, "x"), (2, 5, "y"), (7, 9, "z")]:
            tree.apply(left, right, (letter, 0))
            values[left:right] = [letter] * (right - left)
        for left in range(10):
            for right in range(left, 10):
                text = "".join(values[left:right])
                self.assertEqual(tree.prod(left, right), (text, right - left))
                self.assertEqual(
                    tree.max_right(left, lambda x: text.startswith(x[0])), right
                )
                self.assertEqual(
                    tree.min_left(right, lambda x: text.endswith(x[0])), left
                )

    def test_sum_searches_with_pending_tags(self):
        rng = random.Random(184)
        for n in [0, 1, 2, 7, 8, 9, 31, 32, 33]:
            values = [rng.randrange(10) for _ in range(n)]
            tree = affine_tree(values)
            for _ in range(10):
                left = rng.randrange(n + 1)
                right = rng.randrange(left, n + 1)
                b, c = rng.randrange(3), rng.randrange(4)
                tree.apply(left, right, (b, c))
                for i in range(left, right):
                    values[i] = b * values[i] + c
                limit = rng.randrange(sum(values) + 2)
                for left in range(n + 1):
                    right = left
                    while right < n and sum(values[left : right + 1]) <= limit:
                        right += 1
                    self.assertEqual(
                        tree.max_right(left, lambda x: x[0] <= limit), right
                    )
                for right in range(n + 1):
                    left = right
                    while left and sum(values[left - 1 : right]) <= limit:
                        left -= 1
                    self.assertEqual(
                        tree.min_left(right, lambda x: x[0] <= limit), left
                    )

    def test_three_component_values_and_tags(self):
        rng = random.Random(47)
        values = [(rng.randrange(-10, 11), rng.randrange(-10, 11)) for _ in range(17)]

        def op(x, y):
            return x[0] + y[0], x[1] + y[1], x[2] + y[2]

        def mp(f, x):
            b, c, d = f
            return b * x[0] + c * x[2], b * x[1] + d * x[2], x[2]

        def comp(f, g):
            return f[0] * g[0], f[0] * g[1] + f[1], f[0] * g[2] + f[2]

        tree = TupleLazySegtree(
            [(a, b, 1) for a, b in values],
            op,
            (0, 0, 0),
            mp,
            comp,
            (1, 0, 0),
        )
        for _ in range(100):
            left = rng.randrange(18)
            right = rng.randrange(left, 18)
            b, c, d = (rng.randrange(-3, 4) for _ in range(3))
            tree.apply(left, right, (b, c, d))
            for i in range(left, right):
                a, aa = values[i]
                values[i] = b * a + c, b * aa + d
            left = rng.randrange(18)
            right = rng.randrange(left, 18)
            self.assertEqual(
                tree.prod(left, right),
                (
                    sum(x[0] for x in values[left:right]),
                    sum(x[1] for x in values[left:right]),
                    right - left,
                ),
            )

    def test_identity_action(self):
        tree = TupleLazySegtree(
            [(3, 1), (-2, 1), (5, 1)],
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            (0, 0),
            lambda f, x: x,
            lambda f, g: (0, 0),
            (0, 0),
        )
        tree.apply(0, 3, (0, 0))
        tree.apply_point(1, (0, 0))
        tree.set(0, (7, 1))
        self.assertEqual(tree.get(0), (7, 1))
        self.assertEqual(tree.prod(0, 3), (10, 3))

    def test_unregistered_arities(self):
        for e, identity in [
            ((), (0, 0)),
            ((0,), (0, 0)),
            ((0,) * 4, (0, 0)),
            ((0, 0), ()),
            ((0, 0), (0,)),
            ((0, 0), (0,) * 4),
        ]:
            with self.subTest(e=e, identity=identity):
                with self.assertRaises(AssertionError):
                    TupleLazySegtree(
                        [], lambda x, y: x, e, lambda f, x: x, lambda f, g: f, identity
                    )


if __name__ == "__main__":
    unittest.main()
