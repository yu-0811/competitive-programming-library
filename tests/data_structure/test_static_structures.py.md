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
  code: "import math\nimport operator\nimport random\nimport runpy\nimport unittest\n\
    from functools import reduce\nfrom itertools import product\nfrom pathlib import\
    \ Path\n\nLIBRARY = (\n    Path(__file__).resolve().parents[2] / \"algorithm_library/python/data-structure\"\
    \n)\nSparseTable = runpy.run_path(str(LIBRARY / \"SparseTable.py\"))[\"SparseTable\"\
    ]\nMergeSortTree = runpy.run_path(str(LIBRARY / \"MargeSortTree.py\"))[\"MergeSortTree\"\
    ]\n\n\nclass SparseTableTests(unittest.TestCase):\n    def test_all_ranges_with_idempotent_operations(self):\n\
    \        rng = random.Random(123)\n        operations = [min, max, math.gcd, operator.or_,\
    \ lambda x, y: x]\n        for n in [1, 2, 3, 7, 8, 9, 15, 16, 17, 31, 32, 33]:\n\
    \            values = [rng.randrange(-100, 101) for _ in range(n)]\n         \
    \   for op in operations:\n                data = [abs(x) for x in values] if\
    \ op is math.gcd else values\n                table = SparseTable(data, op)\n\
    \                for left in range(n):\n                    for right in range(left\
    \ + 1, n + 1):\n                        self.assertEqual(\n                  \
    \          table.query(left, right), reduce(op, data[left:right])\n          \
    \              )\n\n    def test_empty_array_and_input_copy(self):\n        table\
    \ = SparseTable([], min)\n        with self.assertRaises(AssertionError):\n  \
    \          table.query(0, 0)\n        values = [3, -1, 2]\n        table = SparseTable(values,\
    \ min)\n        values[1] = -100\n        self.assertEqual(table.query(1, 2),\
    \ -1)\n        self.assertEqual(table.query(0, 3), -1)\n\n\nclass MergeSortTreeTests(unittest.TestCase):\n\
    \    def test_small_nodes_with_duplicates(self):\n        for n in [2, 4]:\n \
    \           for values in product(range(3), repeat=n):\n                tree =\
    \ MergeSortTree(values)\n                for left in range(n + 1):\n         \
    \           for right in range(left, n + 1):\n                        for a in\
    \ range(4):\n                            self.assertEqual(\n                 \
    \               tree.query_leq(left, right, a),\n                            \
    \    sum(x <= a for x in values[left:right]),\n                            )\n\
    \                            for b in range(a, 4):\n                         \
    \       self.assertEqual(\n                                    tree.query_range(left,\
    \ right, a, b),\n                                    sum(a <= x < b for x in values[left:right]),\n\
    \                                )\n\n    def test_counts_against_direct_scan(self):\n\
    \        rng = random.Random(819)\n        for n in [0, 1, 2, 3, 7, 8, 9, 15,\
    \ 16, 17, 31, 32, 33, 63, 64, 65]:\n            values = [rng.randrange(-10, 11)\
    \ for _ in range(n)]\n            tree = MergeSortTree(values)\n            for\
    \ _ in range(200):\n                left = rng.randrange(n + 1)\n            \
    \    right = rng.randrange(left, n + 1)\n                a = rng.randrange(-12,\
    \ 13)\n                b = rng.randrange(a, 14)\n                self.assertEqual(\n\
    \                    tree.query_leq(left, right, a),\n                    sum(x\
    \ <= a for x in values[left:right]),\n                )\n                self.assertEqual(\n\
    \                    tree.query_range(left, right, a, b),\n                  \
    \  sum(a <= x < b for x in values[left:right]),\n                )\n\n    def\
    \ test_sparse_values_across_large_boundaries(self):\n        rng = random.Random(1031)\n\
    \        for n in [127, 128, 129, 511, 512, 513]:\n            values = [rng.randrange(-(10**12),\
    \ 10**12) for _ in range(n)]\n            tree = MergeSortTree(values)\n     \
    \       for _ in range(500):\n                left, right = sorted([rng.randrange(n\
    \ + 1), rng.randrange(n + 1)])\n                a, b = sorted(rng.choices(values,\
    \ k=2))\n                self.assertEqual(\n                    tree.query_range(left,\
    \ right, a, b),\n                    sum(a <= x < b for x in values[left:right]),\n\
    \                )\n                self.assertEqual(\n                    tree.query_range(left,\
    \ right, a, a + 1),\n                    sum(x == a for x in values[left:right]),\n\
    \                )\n                self.assertEqual(\n                    tree.query_leq(left,\
    \ right, a),\n                    sum(x <= a for x in values[left:right]),\n \
    \               )\n\n    def test_values_with_only_less_than_comparison(self):\n\
    \        class Value:\n            def __init__(self, key):\n                self.key\
    \ = key\n\n            def __lt__(self, other):\n                return self.key\
    \ < other.key\n\n        keys = [2, 0, 2, 1, 0, 3, 2, 4, 1]\n        tree = MergeSortTree([Value(key)\
    \ for key in keys])\n        for left in range(len(keys) + 1):\n            for\
    \ right in range(left, len(keys) + 1):\n                for a in range(-1, 6):\n\
    \                    self.assertEqual(\n                        tree.query_leq(left,\
    \ right, Value(a)),\n                        sum(x <= a for x in keys[left:right]),\n\
    \                    )\n                    for b in range(a, 6):\n          \
    \              self.assertEqual(\n                            tree.query_range(left,\
    \ right, Value(a), Value(b)),\n                            sum(a <= x < b for\
    \ x in keys[left:right]),\n                        )\n\n    def test_ordered_equal_and_large_values(self):\n\
    \        for values in [list(range(64)), list(range(64))[::-1], [10**30] * 64]:\n\
    \            tree = MergeSortTree(values)\n            expected = values[:]\n\
    \            values[0] = -(10**30)\n            for left in range(64):\n     \
    \           for right in range(left, 65):\n                    for x in [-1, 0,\
    \ 32, 63, 10**30]:\n                        self.assertEqual(\n              \
    \              tree.query_leq(left, right, x),\n                            sum(v\
    \ <= x for v in expected[left:right]),\n                        )\n\n\nif __name__\
    \ == \"__main__\":\n    unittest.main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tests/data_structure/test_static_structures.py
  requiredBy: []
  timestamp: '2026-10-22 00:00:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tests/data_structure/test_static_structures.py
layout: document
redirect_from:
- /library/tests/data_structure/test_static_structures.py
- /library/tests/data_structure/test_static_structures.py.html
title: tests/data_structure/test_static_structures.py
---
