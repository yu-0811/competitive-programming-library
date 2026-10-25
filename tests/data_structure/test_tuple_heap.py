import heapq
import itertools
import math
import random
import runpy
import unittest
from pathlib import Path


LIBRARY = (
    Path(__file__).resolve().parents[2] / "algorithm_library/python/data-structure"
)
MODULE = runpy.run_path(str(LIBRARY / "TupleHeap.py"))
TupleHeap = MODULE["TupleHeap"]
PackedTupleHeap = MODULE["PackedTupleHeap"]


class TupleHeapTests(unittest.TestCase):
    def test_exhaustive_small_heaps(self):
        alphabet = [(0, 0), (0, 1), (1, 0)]
        for cls in [TupleHeap, PackedTupleHeap]:
            for n in range(7):
                for values in itertools.product(alphabet, repeat=n):
                    expected = sorted(values)
                    for build in [True, False]:
                        heap = cls(iter(values) if build else ())
                        if not build:
                            for value in values:
                                heap.push(value)
                        actual = []
                        while heap:
                            self.assertEqual(heap.peek(), expected[len(actual)])
                            actual.append(heap.pop())
                        self.assertEqual(actual, expected)

    def test_random_operations_against_heapq(self):
        rng = random.Random(20261025)
        for cls in [TupleHeap, PackedTupleHeap]:
            for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33, 127]:
                original = [(rng.randrange(-4, 5), rng.randrange(16)) for _ in range(n)]
                reference = original[:]
                heapq.heapify(reference)
                heap = cls(original)
                original.clear()
                for _ in range(1000):
                    item = rng.randrange(-4, 5), rng.randrange(16)
                    operation = rng.randrange(4)
                    if operation == 0:
                        heap.push(item)
                        heapq.heappush(reference, item)
                    elif operation == 1 and reference:
                        self.assertEqual(heap.pop(), heapq.heappop(reference))
                    elif operation == 2 and reference:
                        self.assertEqual(
                            heap.replace(item), heapq.heapreplace(reference, item)
                        )
                    else:
                        self.assertEqual(
                            heap.pushpop(item), heapq.heappushpop(reference, item)
                        )
                    self.assertEqual(len(heap), len(reference))
                    self.assertEqual(bool(heap), bool(reference))
                    if reference:
                        self.assertEqual(heap.peek(), reference[0])
                self.assertEqual(
                    [heap.pop() for _ in range(len(heap))], sorted(reference)
                )

    def test_empty_operations(self):
        for cls in [TupleHeap, PackedTupleHeap]:
            heap = cls()
            for method, args in [
                (heap.pop, ()),
                (heap.peek, ()),
                (heap.replace, ((0, 0),)),
            ]:
                with self.assertRaises(IndexError):
                    method(*args)
                self.assertEqual(len(heap), 0)
            self.assertEqual(heap.pushpop((3, 2)), (3, 2))
            self.assertFalse(heap)
            heap.push((1, 2))
            self.assertEqual(heap.pop(), (1, 2))
            self.assertFalse(heap)

    def test_large_negative_and_noninteger_components(self):
        cases = [
            [(10**100, -(10**90)), (-(10**100), 7), (10**100, -2), (0, 0)],
            [(math.inf, 1.5), (-math.inf, 0.0), (2.5, -math.inf), (2.5, math.inf)],
            [("b", "a"), ("a", "z"), ("a", "a")],
        ]
        for values in cases:
            heap = TupleHeap(values)
            self.assertEqual([heap.pop() for _ in values], sorted(values))

    def test_packed_integer_boundaries(self):
        for bits in [0, 1, 20, 63, 100]:
            mask = (1 << bits) - 1
            values = [
                (key, value)
                for key in [-(10**100), -2, -1, 0, 1, 10**100]
                for value in [0, mask]
            ]
            heap = PackedTupleHeap(values, bits=bits)
            self.assertEqual([heap.pop() for _ in values], sorted(values))
            for value in [-1, mask + 1]:
                with self.assertRaises(ValueError):
                    PackedTupleHeap([(0, value)], bits=bits)
                heap = PackedTupleHeap([(2, 0)], bits=bits)
                for method in [heap.push, heap.replace, heap.pushpop]:
                    with self.assertRaises(ValueError):
                        method((1, value))
                    self.assertEqual(heap.peek(), (2, 0))
                    self.assertEqual(len(heap), 1)
        for bits in [-1, 1.5, "20"]:
            with self.assertRaises(ValueError):
                PackedTupleHeap(bits=bits)

    def test_invalid_arity_does_not_mutate_heap(self):
        for cls in [TupleHeap, PackedTupleHeap]:
            for item in [(), (0,), (0, 1, 2)]:
                heap = cls([(2, 0)])
                for method in [heap.push, heap.replace, heap.pushpop]:
                    with self.assertRaises(ValueError):
                        method(item)
                    self.assertEqual(len(heap), 1)
                    self.assertEqual(heap.peek(), (2, 0))


if __name__ == "__main__":
    unittest.main()
