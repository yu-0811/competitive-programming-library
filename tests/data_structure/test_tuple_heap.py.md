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
    \ / \"algorithm_library/python/data-structure\"\n)\nTupleHeap = runpy.run_path(str(LIBRARY\
    \ / \"TupleHeap.py\"))[\"TupleHeap\"]\nPackedTupleHeap = runpy.run_path(str(LIBRARY\
    \ / \"PackedTupleHeap.py\"))[\"PackedTupleHeap\"]\n\n\nclass TupleHeapTests(unittest.TestCase):\n\
    \    def test_exhaustive_small_heaps(self):\n        for arity in [1, 2, 3]:\n\
    \            alphabet = [(0,) * arity, (0,) * (arity - 1) + (1,), (1,) * arity]\n\
    \            for cls in [TupleHeap, PackedTupleHeap]:\n                for n in\
    \ range(6):\n                    for values in itertools.product(alphabet, repeat=n):\n\
    \                        for build in [True, False]:\n                       \
    \     heap = cls(\n                                arity=arity, values=iter(values)\
    \ if build else ()\n                            )\n                          \
    \  if not build:\n                                for item in values:\n      \
    \                              heap.push(iter(item))\n                       \
    \     self.assertEqual(\n                                [heap.pop() for _ in\
    \ values], sorted(values)\n                            )\n\n    def test_random_operations_against_heapq(self):\n\
    \        rng = random.Random(20261025)\n        for cls in [TupleHeap, PackedTupleHeap]:\n\
    \            for arity in [1, 2, 3, 4, 8, 16, 17, 32]:\n\n                def\
    \ make_item():\n                    return (rng.randrange(-4, 5),) + tuple(\n\
    \                        rng.randrange(16) for _ in range(arity - 1)\n       \
    \             )\n\n                for n in [0, 1, 2, 3, 7, 8, 9, 31, 32, 33,\
    \ 127]:\n                    values = [make_item() for _ in range(n)]\n      \
    \              reference = values[:]\n                    heapq.heapify(reference)\n\
    \                    heap = cls(arity=arity, values=values)\n                \
    \    values.clear()\n                    for _ in range(250):\n              \
    \          if reference and rng.randrange(2):\n                            self.assertEqual(heap.top(),\
    \ reference[0])\n                            self.assertEqual(heap.pop(), heapq.heappop(reference))\n\
    \                        else:\n                            item = make_item()\n\
    \                            heap.push(item)\n                            heapq.heappush(reference,\
    \ item)\n                        self.assertEqual(len(heap), len(reference))\n\
    \                        self.assertEqual(bool(heap), bool(reference))\n     \
    \               self.assertEqual([heap.pop() for _ in reference], sorted(reference))\n\
    \n    def test_shared_prefix_and_empty_heaps(self):\n        rng = random.Random(90)\n\
    \        for arity in [*range(1, 20), 32, 1000]:\n            values = [(0,) *\
    \ (arity - 1) + (i,) for i in range(32)]\n            rng.shuffle(values)\n  \
    \          for cls in [TupleHeap, PackedTupleHeap]:\n                heap = cls(arity=arity,\
    \ values=values)\n                self.assertEqual([heap.pop() for _ in values],\
    \ sorted(values))\n                self.assertFalse(heap)\n                for\
    \ method in [heap.top, heap.pop]:\n                    with self.assertRaises(IndexError):\n\
    \                        method()\n                    self.assertEqual(len(heap),\
    \ 0)\n                heap.push((0,) * arity)\n                self.assertEqual(heap.pop(),\
    \ (0,) * arity)\n\n    def test_different_component_types(self):\n        cases\
    \ = [\n            [(10**100, -(10**90)), (-(10**100), 7), (10**100, -2)],\n \
    \           [(math.inf, 1.5), (-math.inf, 0.0), (2.5, -math.inf), (2.5, math.inf)],\n\
    \            [(2.5, \"b\", -7), (2.5, \"a\", 10**100), (2.5, \"a\", -3)],\n  \
    \      ]\n        for values in cases:\n            heap = TupleHeap(arity=len(values[0]),\
    \ values=values)\n            self.assertEqual([heap.pop() for _ in values], sorted(values))\n\
    \n    def test_packed_bit_boundaries(self):\n        for widths in [(), (0,),\
    \ (1,), (20,), (63,), (100,), (0, 1, 2, 5, 63, 100)]:\n            masks = tuple((1\
    \ << width) - 1 for width in widths)\n            values = [\n               \
    \ (key,) + suffix\n                for key in [-(10**100), -1, 0, 1, 10**100]\n\
    \                for suffix in itertools.product(*[(0, mask) for mask in masks])\n\
    \            ]\n            heap = PackedTupleHeap(arity=len(widths) + 1, bits=widths,\
    \ values=values)\n            self.assertEqual([heap.pop() for _ in values], sorted(values))\n\
    \n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_tuple_heap.py
  requiredBy: []
  timestamp: '2026-10-25 22:38:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_tuple_heap.py
layout: document
redirect_from:
- /library/tests/data_structure/test_tuple_heap.py
- /library/tests/data_structure/test_tuple_heap.py.html
title: tests/data_structure/test_tuple_heap.py
---
