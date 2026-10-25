import itertools
import random
import unittest
from functools import cmp_to_key

from algorithm_library.python.math.AngularSort import compare
from algorithm_library.python.techniques.CmpSort import cmp_sort


def integer_compare(a, b):
    return a - b


class CmpSortTests(unittest.TestCase):
    def check_sort(self, values, cmp):
        expected = sorted(values, key=cmp_to_key(cmp))
        actual = values[:]
        self.assertIs(cmp_sort(actual, cmp), actual)
        self.assertEqual(actual, expected)

    def test_exhaustive_short_lists(self):
        for n in range(8):
            for values in itertools.product(range(3), repeat=n):
                self.check_sort(list(values), integer_compare)

    def test_run_boundaries_and_input_orders(self):
        rng = random.Random(42)
        for n in [0, 1, 2, 15, 16, 17, 31, 32, 33, 63, 64, 65, 127, 257, 4097]:
            for values in [
                list(range(n)),
                list(range(n - 1, -1, -1)),
                [7] * n,
                [rng.randrange(-10, 11) for _ in range(n)],
                list(range(0, n, 2)) + list(range(1, n, 2)),
                [i % 17 for i in range(n)],
            ]:
                self.check_sort(values, integer_compare)
                self.check_sort(values, lambda a, b: b - a)

    def test_opaque_items_and_stability(self):
        rng = random.Random(314)
        # 辞書同士の順序比較はできない。同順位の元の順序も検証する。
        for keys in [
            [rng.randrange(10) for _ in range(2049)],
            [i // 3 for i in range(257, -1, -1)],
            [0] * 257,
        ]:
            values = [{"key": key, "index": i} for i, key in enumerate(keys)]
            self.check_sort(values, lambda a, b: a["key"] - b["key"])

    def test_angular_sort_and_collinear_stability(self):
        rng = random.Random(2718)
        values = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        values = [(x * k, y * k) for k in range(1, 41) for x, y in values]
        rng.shuffle(values)
        self.check_sort(values, compare)
        for limit in [10**9, 10**30]:
            values = [
                (rng.randrange(-limit, limit + 1), rng.randrange(-limit, limit + 1))
                for _ in range(2049)
            ]
            self.check_sort([p for p in values if p != (0, 0)], compare)

    def test_sorted_and_strictly_reversed_use_linear_comparisons(self):
        for values in [list(range(10000)), list(range(9999, -1, -1)), [1] * 10000]:
            calls = 0

            def counted(a, b):
                nonlocal calls
                calls += 1
                return a - b

            actual = values[:]
            cmp_sort(actual, counted)
            self.assertEqual(actual, sorted(values))
            self.assertEqual(calls, len(values) - 1)


if __name__ == "__main__":
    unittest.main()
