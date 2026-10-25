import random
import runpy
import unittest
from pathlib import Path


LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/data-structure"
)
TupleSegtree = runpy.run_path(str(LIBRARY / "TupleSegtree.py"))["TupleSegtree"]


class TupleSegtreeTests(unittest.TestCase):
    def test_random_updates_queries_and_searches(self):
        rng = random.Random(20261025)
        for arity in [2, 3]:
            e = (0,) * arity

            def op(x, y):
                return tuple(a + b for a, b in zip(x, y))

            for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33]:
                values = [tuple(rng.randrange(10) for _ in e) for _ in range(n)]
                tree = TupleSegtree(v=values, op=op, e=e)
                for _ in range(120):
                    if n:
                        p = rng.randrange(n)
                        x = tuple(rng.randrange(10) for _ in e)
                        if rng.randrange(2):
                            tree.set(p, x)
                            values[p] = x
                        else:
                            tree.add(p, x)
                            values[p] = op(values[p], x)
                        self.assertEqual(tree.get(p), values[p])
                    left = rng.randrange(n + 1)
                    right = rng.randrange(left, n + 1)
                    self.assertEqual(
                        tree.prod(left, right),
                        tuple(
                            sum(x[j] for x in values[left:right]) for j in range(arity)
                        ),
                    )
                    self.assertEqual(
                        tree.all_prod(),
                        tuple(sum(x[j] for x in values) for j in range(arity)),
                    )
                    limit = rng.randrange(sum(x[0] for x in values) + 2)
                    expected_right = left
                    total = 0
                    while (
                        expected_right < n
                        and total + values[expected_right][0] <= limit
                    ):
                        total += values[expected_right][0]
                        expected_right += 1
                    self.assertEqual(
                        tree.max_right(left, lambda x: x[0] <= limit), expected_right
                    )
                    expected_left = right
                    total = 0
                    while (
                        expected_left and total + values[expected_left - 1][0] <= limit
                    ):
                        expected_left -= 1
                        total += values[expected_left][0]
                    self.assertEqual(
                        tree.min_left(right, lambda x: x[0] <= limit), expected_left
                    )
                self.assertEqual(str(tree), str(values))

    def test_noncommutative_products_and_searches(self):
        values = list("abcdefghi")
        tree = TupleSegtree(
            [(x, 1) for x in values],
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            ("", 0),
        )
        for p, letter in [(0, "z"), (4, "x"), (8, "y")]:
            tree.set(p, (letter, 1))
            values[p] = letter
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

    def test_float_and_large_integer_components(self):
        values = [(10**100, 0.5, -3), (-(10**100), -1.5, 8), (7, 2.0, -5)]
        tree = TupleSegtree(
            values, lambda x, y: tuple(a + b for a, b in zip(x, y)), (0, 0.0, 0)
        )
        values[0] = (0, 0.0, 0)
        self.assertEqual(tree.get(0), (10**100, 0.5, -3))
        tree.add(1, (10**100, 0.5, -2))
        self.assertEqual(tree.get(1), (0, -1.0, 6))
        self.assertEqual(tree.all_prod(), (10**100 + 7, 1.5, -2))
        self.assertEqual(tree.prod(1, 3), (7, 1.0, 1))

    def test_unregistered_arities(self):
        for arity in [0, 1, 4]:
            with self.subTest(arity=arity):
                with self.assertRaises(AssertionError):
                    TupleSegtree([], lambda x, y: x, (0,) * arity)


if __name__ == "__main__":
    unittest.main()
