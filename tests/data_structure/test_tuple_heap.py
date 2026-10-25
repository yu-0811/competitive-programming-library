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
TupleHeap = runpy.run_path(str(LIBRARY / "TupleHeap.py"))["TupleHeap"]
PackedTupleHeap = runpy.run_path(str(LIBRARY / "PackedTupleHeap.py"))["PackedTupleHeap"]


class TupleHeapTests(unittest.TestCase):
    def test_exhaustive_small_heaps(self):
        for arity in [1, 2, 3]:
            alphabet = [(0,) * arity, (0,) * (arity - 1) + (1,), (1,) * arity]
            for cls in [TupleHeap, PackedTupleHeap]:
                for n in range(6):
                    for values in itertools.product(alphabet, repeat=n):
                        for build in [True, False]:
                            heap = cls(
                                arity=arity, values=iter(values) if build else ()
                            )
                            if not build:
                                for item in values:
                                    heap.push(iter(item))
                            self.assertEqual(
                                [heap.pop() for _ in values], sorted(values)
                            )

    def test_random_operations_against_heapq(self):
        rng = random.Random(20261025)
        for cls in [TupleHeap, PackedTupleHeap]:
            for arity in [1, 2, 3, 4, 8, 16, 17, 32]:

                def make_item():
                    return (rng.randrange(-4, 5),) + tuple(
                        rng.randrange(16) for _ in range(arity - 1)
                    )

                for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33, 127]:
                    values = [make_item() for _ in range(n)]
                    reference = values[:]
                    heapq.heapify(reference)
                    heap = cls(arity=arity, values=values)
                    values.clear()
                    for _ in range(250):
                        if reference and rng.randrange(2):
                            self.assertEqual(heap.top(), reference[0])
                            self.assertEqual(heap.pop(), heapq.heappop(reference))
                        else:
                            item = make_item()
                            heap.push(item)
                            heapq.heappush(reference, item)
                        self.assertEqual(len(heap), len(reference))
                        self.assertEqual(bool(heap), bool(reference))
                    self.assertEqual([heap.pop() for _ in reference], sorted(reference))

    def test_shared_prefix_and_empty_heaps(self):
        rng = random.Random(90)
        for arity in [*range(1, 20), 32, 1000]:
            values = [(0,) * (arity - 1) + (i,) for i in range(32)]
            rng.shuffle(values)
            for cls in [TupleHeap, PackedTupleHeap]:
                heap = cls(arity=arity, values=values)
                self.assertEqual([heap.pop() for _ in values], sorted(values))
                self.assertFalse(heap)
                for method in [heap.top, heap.pop]:
                    with self.assertRaises(IndexError):
                        method()
                    self.assertEqual(len(heap), 0)
                heap.push((0,) * arity)
                self.assertEqual(heap.pop(), (0,) * arity)

    def test_different_component_types(self):
        cases = [
            [(10**100, -(10**90)), (-(10**100), 7), (10**100, -2)],
            [(math.inf, 1.5), (-math.inf, 0.0), (2.5, -math.inf), (2.5, math.inf)],
            [(2.5, "b", -7), (2.5, "a", 10**100), (2.5, "a", -3)],
        ]
        for values in cases:
            heap = TupleHeap(arity=len(values[0]), values=values)
            self.assertEqual([heap.pop() for _ in values], sorted(values))

    def test_packed_bit_boundaries(self):
        for widths in [(), (0,), (1,), (20,), (63,), (100,), (0, 1, 2, 5, 63, 100)]:
            masks = tuple((1 << width) - 1 for width in widths)
            values = [
                (key,) + suffix
                for key in [-(10**100), -1, 0, 1, 10**100]
                for suffix in itertools.product(*[(0, mask) for mask in masks])
            ]
            heap = PackedTupleHeap(arity=len(widths) + 1, bits=widths, values=values)
            self.assertEqual([heap.pop() for _ in values], sorted(values))


if __name__ == "__main__":
    unittest.main()
