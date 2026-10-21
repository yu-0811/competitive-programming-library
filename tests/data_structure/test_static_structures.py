import math
import operator
import random
import runpy
import unittest
from functools import reduce
from pathlib import Path

LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/data-structure"
)
SparseTable = runpy.run_path(str(LIBRARY / "SparseTable.py"))["SparseTable"]
MergeSortTree = runpy.run_path(str(LIBRARY / "MargeSortTree.py"))["MergeSortTree"]


class SparseTableTests(unittest.TestCase):
    def test_all_ranges_with_idempotent_operations(self):
        rng = random.Random(123)
        operations = [min, max, math.gcd, operator.or_, lambda x, y: x]
        for n in [1, 2, 3, 7, 8, 9, 15, 16, 17, 31, 32, 33]:
            values = [rng.randrange(-100, 101) for _ in range(n)]
            for op in operations:
                data = [abs(x) for x in values] if op is math.gcd else values
                table = SparseTable(data, op)
                for left in range(n):
                    for right in range(left + 1, n + 1):
                        self.assertEqual(
                            table.query(left, right), reduce(op, data[left:right])
                        )

    def test_empty_array_and_input_copy(self):
        table = SparseTable([], min)
        with self.assertRaises(AssertionError):
            table.query(0, 0)
        values = [3, -1, 2]
        table = SparseTable(values, min)
        values[1] = -100
        self.assertEqual(table.query(1, 2), -1)
        self.assertEqual(table.query(0, 3), -1)


class MergeSortTreeTests(unittest.TestCase):
    def test_counts_against_direct_scan(self):
        rng = random.Random(819)
        for n in [0, 1, 2, 3, 7, 8, 9, 15, 16, 17, 31, 32, 33, 63, 64, 65]:
            values = [rng.randrange(-10, 11) for _ in range(n)]
            tree = MergeSortTree(values)
            for _ in range(200):
                left = rng.randrange(n + 1)
                right = rng.randrange(left, n + 1)
                a = rng.randrange(-12, 13)
                b = rng.randrange(a, 14)
                self.assertEqual(
                    tree.query_leq(left, right, a),
                    sum(x <= a for x in values[left:right]),
                )
                self.assertEqual(
                    tree.query_range(left, right, a, b),
                    sum(a <= x < b for x in values[left:right]),
                )

    def test_sparse_values_across_large_boundaries(self):
        rng = random.Random(1031)
        for n in [127, 128, 129, 511, 512, 513]:
            values = [rng.randrange(-(10**12), 10**12) for _ in range(n)]
            tree = MergeSortTree(values)
            for _ in range(500):
                left, right = sorted([rng.randrange(n + 1), rng.randrange(n + 1)])
                a, b = sorted(rng.choices(values, k=2))
                self.assertEqual(
                    tree.query_range(left, right, a, b),
                    sum(a <= x < b for x in values[left:right]),
                )
                self.assertEqual(
                    tree.query_range(left, right, a, a + 1),
                    sum(x == a for x in values[left:right]),
                )
                self.assertEqual(
                    tree.query_leq(left, right, a),
                    sum(x <= a for x in values[left:right]),
                )

    def test_values_with_only_less_than_comparison(self):
        class Value:
            def __init__(self, key):
                self.key = key

            def __lt__(self, other):
                return self.key < other.key

        keys = [2, 0, 2, 1, 0, 3, 2, 4, 1]
        tree = MergeSortTree([Value(key) for key in keys])
        for left in range(len(keys) + 1):
            for right in range(left, len(keys) + 1):
                for a in range(-1, 6):
                    self.assertEqual(
                        tree.query_leq(left, right, Value(a)),
                        sum(x <= a for x in keys[left:right]),
                    )
                    for b in range(a, 6):
                        self.assertEqual(
                            tree.query_range(left, right, Value(a), Value(b)),
                            sum(a <= x < b for x in keys[left:right]),
                        )

    def test_ordered_equal_and_large_values(self):
        for values in [list(range(64)), list(range(64))[::-1], [10**30] * 64]:
            tree = MergeSortTree(values)
            expected = values[:]
            values[0] = -(10**30)
            for left in range(64):
                for right in range(left, 65):
                    for x in [-1, 0, 32, 63, 10**30]:
                        self.assertEqual(
                            tree.query_leq(left, right, x),
                            sum(v <= x for v in expected[left:right]),
                        )


if __name__ == "__main__":
    unittest.main()
