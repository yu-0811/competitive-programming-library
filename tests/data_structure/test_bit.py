import itertools
import random
import runpy
import unittest
from bisect import bisect_left
from pathlib import Path


BIT = runpy.run_path(
    str(
        Path(__file__).resolve().parents[2]
        / "algorithm_library/python/data-structure/BIT.py"
    )
)["BIT"]


class BITSumTests(unittest.TestCase):
    def test_empty_array(self):
        bit = BIT(0)
        self.assertEqual(bit.SUM(0), 0)
        self.assertEqual(bit.range_sum(1, 1), 0)

    def test_random_signed_range_updates(self):
        rng = random.Random(518)
        for n in [1, 2, 3, 7, 8, 9, 31, 32, 33, 63, 64, 65]:
            bit = BIT(n)
            values = [0] * n
            for _ in range(80):
                left = rng.randrange(n + 1)
                right = rng.randrange(left, n + 1)
                delta = rng.randrange(-(10**10), 10**10)
                bit.add(left + 1, right + 1, delta)
                for i in range(left, right):
                    values[i] += delta
                prefixes = [0, *itertools.accumulate(values)]
                for i, expected in enumerate(prefixes):
                    self.assertEqual(bit.SUM(i), expected)
                for _ in range(5):
                    left = rng.randrange(n + 1)
                    right = rng.randrange(left, n + 1)
                    self.assertEqual(
                        bit.range_sum(left + 1, right + 1),
                        prefixes[right] - prefixes[left],
                    )


class BITLowerBoundTests(unittest.TestCase):
    def check_lower_bounds(self, bit, values):
        prefixes = list(itertools.accumulate(values))
        for target in [-10, 0, *range(1, sum(values) + 2)]:
            expected = 0 if target <= 0 else bisect_left(prefixes, target) + 1
            self.assertEqual(bit.lower_bound(target), expected, (values, target))

    def test_empty_zero_and_sparse_arrays(self):
        for values in [[], [0], [0, 0, 0], [3], [0, 3, 0, 0, 2, 0]]:
            with self.subTest(values=values):
                bit = BIT(len(values))
                for i, value in enumerate(values, 1):
                    bit.add(i, i + 1, value)
                self.check_lower_bounds(bit, values)

    def test_range_additions_and_subtractions(self):
        bit = BIT(8)
        values = [0] * 8
        for left, right, delta in [(2, 8, 3), (1, 9, 2), (3, 6, -4), (1, 9, -1)]:
            bit.add(left, right, delta)
            for i in range(left - 1, right - 1):
                values[i] += delta
            self.check_lower_bounds(bit, values)

    def test_random_range_updates_around_powers_of_two(self):
        rng = random.Random(20261020)
        for n in [1, 2, 3, 7, 8, 9, 15, 16, 17, 31, 32, 33]:
            bit = BIT(n)
            values = [0] * n
            for _ in range(40):
                left = rng.randrange(n)
                right = rng.randrange(left + 1, n + 1)
                delta = rng.randint(-min(values[left:right]), 5)
                bit.add(left + 1, right + 1, delta)
                for i in range(left, right):
                    values[i] += delta
                self.check_lower_bounds(bit, values)

    def test_large_integer_targets(self):
        big = 10**30
        bit = BIT(4)
        bit.add(2, 4, big)
        cases = [(1, 2), (big, 2), (big + 1, 3), (2 * big, 3), (2 * big + 1, 5)]
        for target, expected in cases:
            self.assertEqual(bit.lower_bound(target), expected)


if __name__ == "__main__":
    unittest.main()
