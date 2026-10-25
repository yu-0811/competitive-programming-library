---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.16/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\nimport itertools\nimport math\nimport random\nimport runpy\n\
    import unittest\nfrom pathlib import Path\n\n\nLIBRARY = (\n    Path(__file__).resolve().parents[2]\
    \ / \"algorithm_library/python/data-structure\"\n)\nMODULE = runpy.run_path(str(LIBRARY\
    \ / \"TupleHeap.py\"))\nTupleHeap = MODULE[\"TupleHeap\"]\nPackedTupleHeap = MODULE[\"\
    PackedTupleHeap\"]\n\n\nclass TupleHeapTests(unittest.TestCase):\n    def test_exhaustive_small_heaps(self):\n\
    \        alphabet = [(0, 0), (0, 1), (1, 0)]\n        for cls in [TupleHeap, PackedTupleHeap]:\n\
    \            for n in range(7):\n                for values in itertools.product(alphabet,\
    \ repeat=n):\n                    expected = sorted(values)\n                \
    \    for build in [True, False]:\n                        heap = cls(iter(values)\
    \ if build else ())\n                        if not build:\n                 \
    \           for value in values:\n                                heap.push(value)\n\
    \                        actual = []\n                        while heap:\n  \
    \                          self.assertEqual(heap.peek(), expected[len(actual)])\n\
    \                            actual.append(heap.pop())\n                     \
    \   self.assertEqual(actual, expected)\n\n    def test_random_operations_against_heapq(self):\n\
    \        rng = random.Random(20261025)\n        for cls in [TupleHeap, PackedTupleHeap]:\n\
    \            for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33, 127]:\n              \
    \  original = [(rng.randrange(-4, 5), rng.randrange(16)) for _ in range(n)]\n\
    \                reference = original[:]\n                heapq.heapify(reference)\n\
    \                heap = cls(original)\n                original.clear()\n    \
    \            for _ in range(1000):\n                    item = rng.randrange(-4,\
    \ 5), rng.randrange(16)\n                    operation = rng.randrange(4)\n  \
    \                  if operation == 0:\n                        heap.push(item)\n\
    \                        heapq.heappush(reference, item)\n                   \
    \ elif operation == 1 and reference:\n                        self.assertEqual(heap.pop(),\
    \ heapq.heappop(reference))\n                    elif operation == 2 and reference:\n\
    \                        self.assertEqual(\n                            heap.replace(item),\
    \ heapq.heapreplace(reference, item)\n                        )\n            \
    \        else:\n                        self.assertEqual(\n                  \
    \          heap.pushpop(item), heapq.heappushpop(reference, item)\n          \
    \              )\n                    self.assertEqual(len(heap), len(reference))\n\
    \                    self.assertEqual(bool(heap), bool(reference))\n         \
    \           if reference:\n                        self.assertEqual(heap.peek(),\
    \ reference[0])\n                self.assertEqual(\n                    [heap.pop()\
    \ for _ in range(len(heap))], sorted(reference)\n                )\n\n    def\
    \ test_empty_operations(self):\n        for cls in [TupleHeap, PackedTupleHeap]:\n\
    \            heap = cls()\n            for method, args in [\n               \
    \ (heap.pop, ()),\n                (heap.peek, ()),\n                (heap.replace,\
    \ ((0, 0),)),\n            ]:\n                with self.assertRaises(IndexError):\n\
    \                    method(*args)\n                self.assertEqual(len(heap),\
    \ 0)\n            self.assertEqual(heap.pushpop((3, 2)), (3, 2))\n           \
    \ self.assertFalse(heap)\n            heap.push((1, 2))\n            self.assertEqual(heap.pop(),\
    \ (1, 2))\n            self.assertFalse(heap)\n\n    def test_large_negative_and_noninteger_components(self):\n\
    \        cases = [\n            [(10**100, -(10**90)), (-(10**100), 7), (10**100,\
    \ -2), (0, 0)],\n            [(math.inf, 1.5), (-math.inf, 0.0), (2.5, -math.inf),\
    \ (2.5, math.inf)],\n            [(\"b\", \"a\"), (\"a\", \"z\"), (\"a\", \"a\"\
    )],\n        ]\n        for values in cases:\n            heap = TupleHeap(values)\n\
    \            self.assertEqual([heap.pop() for _ in values], sorted(values))\n\n\
    \    def test_packed_integer_boundaries(self):\n        for bits in [0, 1, 20,\
    \ 63, 100]:\n            mask = (1 << bits) - 1\n            values = [\n    \
    \            (key, value)\n                for key in [-(10**100), -2, -1, 0,\
    \ 1, 10**100]\n                for value in [0, mask]\n            ]\n       \
    \     heap = PackedTupleHeap(values, bits=bits)\n            self.assertEqual([heap.pop()\
    \ for _ in values], sorted(values))\n            for value in [-1, mask + 1]:\n\
    \                with self.assertRaises(ValueError):\n                    PackedTupleHeap([(0,\
    \ value)], bits=bits)\n                heap = PackedTupleHeap([(2, 0)], bits=bits)\n\
    \                for method in [heap.push, heap.replace, heap.pushpop]:\n    \
    \                with self.assertRaises(ValueError):\n                       \
    \ method((1, value))\n                    self.assertEqual(heap.peek(), (2, 0))\n\
    \                    self.assertEqual(len(heap), 1)\n        for bits in [-1,\
    \ 1.5, \"20\"]:\n            with self.assertRaises(ValueError):\n           \
    \     PackedTupleHeap(bits=bits)\n\n    def test_invalid_arity_does_not_mutate_heap(self):\n\
    \        for cls in [TupleHeap, PackedTupleHeap]:\n            for item in [(),\
    \ (0,), (0, 1, 2)]:\n                heap = cls([(2, 0)])\n                for\
    \ method in [heap.push, heap.replace, heap.pushpop]:\n                    with\
    \ self.assertRaises(ValueError):\n                        method(item)\n     \
    \               self.assertEqual(len(heap), 1)\n                    self.assertEqual(heap.peek(),\
    \ (2, 0))\n\n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_tuple_heap.py
  requiredBy: []
  timestamp: '2026-10-25 21:47:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_tuple_heap.py
layout: document
redirect_from:
- /library/tests/data_structure/test_tuple_heap.py
- /library/tests/data_structure/test_tuple_heap.py.html
title: tests/data_structure/test_tuple_heap.py
---
